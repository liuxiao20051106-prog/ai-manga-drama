#!/usr/bin/env python3
"""Lint a manga-drama shot list without third-party dependencies.

The shot list is the contract between the script, the image generation stage, and
the video generation stage. When a field is missing or a duration does not add up,
the cost surfaces later as rework. This script checks the mechanical parts so the
human review can spend its attention on story and continuity.

Supported input:
  * Markdown tables (the shape used by templates/shot-list.md, Chinese or English)
  * CSV files

Checks performed:
  * shot ID format (E01-S001 and similar)
  * missing required fields
  * unparsable or zero duration
  * shots longer than the per-shot cap
  * total duration vs the target duration
  * entry/exit continuity left blank between adjacent shots
  * three or more consecutive shots with identical framing
  * unknown status values

Usage:
    python scripts/shotlist_lint.py templates/shot-list.md --target-seconds 60
    python scripts/shotlist_lint.py shots.csv --max-shot-seconds 12 --json
    python scripts/shotlist_lint.py shots.md --target-seconds 90 --tolerance 0.2

Exit code is 1 when errors are found, 0 otherwise. Warnings alone do not fail
the run unless --warnings-as-errors is passed.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

SHOT_ID_RE = re.compile(r"^[A-Za-z]+\d{1,3}-S\d{1,4}$")
DURATION_RE = re.compile(r"^\d+(?:\.\d+)?$")
CLOCK_RE = re.compile(r"^(\d{1,2}):(\d{2})(?::(\d{2}))?$")
PLACEHOLDERS = {"", "-", "--", "...", "…", "n/a", "na", "待填", "待定", "无"}

# Header keyword -> canonical field. Longer keys are matched first so that
# "entry continuity" wins over "continuity".
HEADER_KEYS = (
    ("entry", ("入镜", "entry")),
    ("exit", ("出镜", "exit")),
    ("id", ("镜号", "shot id", "shot")),
    ("time", ("时间码", "timecode", "time")),
    ("location", ("场景", "location", "set")),
    ("cast", ("角色", "cast", "character")),
    ("framing", ("构图", "composition", "framing", "shot size")),
    ("action", ("动作", "action")),
    ("camera", ("运镜", "camera", "movement")),
    ("sound", ("台词", "声音", "dialogue", "sound", "audio")),
    ("status", ("状态", "status")),
)

REQUIRED_FIELDS = ("id", "time", "framing", "action")

DEFAULT_STATUSES = {
    "待办",
    "制作中",
    "已批准",
    "退回",
    "废弃",
    "planned",
    "in progress",
    "approved",
    "rejected",
    "superseded",
}


def split_row(line: str) -> list:
    """Split a Markdown table row into stripped cells."""
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator_row(cells: list) -> bool:
    return bool(cells) and all(set(cell) <= set("-: ") and cell for cell in cells)


def find_table(text: str):
    """Return (header, rows) for the first Markdown table row that looks like a shot list."""
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if "|" not in line:
            continue
        header = split_row(line)
        mapped = map_columns(header)
        if "id" in mapped and "time" in mapped:
            rows = []
            for follow in lines[index + 1:]:
                if "|" not in follow:
                    break
                cells = split_row(follow)
                if is_separator_row(cells):
                    continue
                rows.append(cells)
            return header, rows
    return None, []


def map_columns(header: list) -> dict:
    """Map header labels onto canonical field names."""
    mapping = {}
    for position, label in enumerate(header):
        lowered = label.strip().lower()
        for field, keys in HEADER_KEYS:
            if field in mapping:
                continue
            if any(key in lowered for key in keys):
                mapping[field] = position
                break
    # "time" must not win over "timecode-like" fields already claimed by entry/exit.
    return mapping


def parse_duration(raw: str):
    """Parse '00:00/4', '4', '4s', '00:04' or '00:00:04' into seconds."""
    if raw is None:
        return None
    value = raw.strip().rstrip("s秒")
    if not value:
        return None
    if "/" in value:
        value = value.split("/")[-1].strip()
    if DURATION_RE.match(value):
        return float(value)
    match = CLOCK_RE.match(value)
    if match:
        first, second, third = match.groups()
        if third is None:
            return int(first) * 60 + int(second)
        return int(first) * 3600 + int(second) * 60 + int(third)
    return None


def cell(row: list, mapping: dict, field: str) -> str:
    position = mapping.get(field)
    if position is None or position >= len(row):
        return ""
    return row[position].strip()


def blank(value: str) -> bool:
    return value.strip().lower() in PLACEHOLDERS or value.strip() in PLACEHOLDERS


def read_rows(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".csv":
        rows = [row for row in csv.reader(text.splitlines()) if any(cell.strip() for cell in row)]
        if not rows:
            return {}, []
        return map_columns(rows[0]), rows[1:]
    header, rows = find_table(text)
    if not header:
        return None, []
    return map_columns(header), rows


def lint(path: Path, mapping: dict, rows: list, args) -> list:
    issues = []
    durations = []
    shots = []

    for line_number, row in enumerate(rows, start=2):
        shot_id = cell(row, mapping, "id")
        if blank(shot_id):
            continue
        label = f"{path.name}:{line_number} {shot_id}"

        if not SHOT_ID_RE.match(shot_id):
            issues.append(("error", f"{label}: shot ID should look like E01-S001"))

        for field in REQUIRED_FIELDS:
            if blank(cell(row, mapping, field)):
                issues.append(("error", f"{label}: field '{field}' is empty"))

        for field in ("entry", "exit", "sound"):
            if field in mapping and blank(cell(row, mapping, field)):
                issues.append(("warning", f"{label}: '{field}' is empty"))

        seconds = parse_duration(cell(row, mapping, "time"))
        if seconds is None:
            issues.append(("error", f"{label}: duration '{cell(row, mapping, 'time')}' is not parsable"))
        elif seconds <= 0:
            issues.append(("error", f"{label}: duration must be greater than zero"))
        else:
            durations.append(seconds)
            if seconds > args.max_shot_seconds:
                issues.append(
                    ("warning",
                     f"{label}: {seconds:g}s exceeds the {args.max_shot_seconds:g}s single-shot cap")
                )

        status = cell(row, mapping, "status")
        if status and status not in DEFAULT_STATUSES:
            issues.append(("warning", f"{label}: unknown status '{status}'"))

        shots.append(
            {
                "id": shot_id,
                "seconds": seconds,
                "framing": cell(row, mapping, "framing"),
                "entry": cell(row, mapping, "entry"),
                "exit": cell(row, mapping, "exit"),
            }
        )

    if not shots:
        issues.append(("error", f"{path.name}: no shot rows found"))
        return issues, shots, durations


    for previous, current in zip(shots, shots[1:]):
        if blank(previous["exit"]) or blank(current["entry"]):
            issues.append(
                ("warning",
                 f"{previous['id']} -> {current['id']}: exit/entry state not written, the join is unverified")
            )

    run = 1
    for previous, current in zip(shots, shots[1:]):
        if previous["framing"] and previous["framing"] == current["framing"]:
            run += 1
            if run == 3:
                issues.append(
                    ("warning",
                     f"{current['id']}: three or more consecutive shots share framing "
                     f"'{current['framing']}'")
                )
        else:
            run = 1

    total = sum(durations)
    if args.target_seconds:
        difference = abs(total - args.target_seconds) / args.target_seconds
        level = "warning" if difference <= args.tolerance else "error"
        if difference > args.tolerance:
            issues.append(
                (level,
                 f"total duration {total:g}s vs target {args.target_seconds:g}s "
                 f"differs by {difference * 100:.1f}% (tolerance {args.tolerance * 100:.0f}%)")
            )
        else:
            issues.append(("info", f"total duration {total:g}s within tolerance of target {args.target_seconds:g}s"))

    return issues, shots, durations


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Lint a manga-drama shot list")
    parser.add_argument("path", type=Path, help="Markdown or CSV shot list")
    parser.add_argument("--target-seconds", type=float, default=None, help="expected episode duration")
    parser.add_argument("--tolerance", type=float, default=0.15, help="allowed relative deviation from target")
    parser.add_argument("--max-shot-seconds", type=float, default=15.0, help="cap for a single shot")
    parser.add_argument("--min-shots", type=int, default=1, help="minimum number of shots expected")
    parser.add_argument("--json", action="store_true", help="emit machine-readable output")
    parser.add_argument("--warnings-as-errors", action="store_true", help="fail on warnings too")
    args = parser.parse_args(argv)

    if not args.path.is_file():
        print(f"ERROR: {args.path} not found", file=sys.stderr)
        return 1

    mapping, rows = read_rows(args.path)
    if mapping is None:
        print(f"ERROR: {args.path.name}: no shot table found (need a header with a shot id column)",
              file=sys.stderr)
        return 1

    issues, shots, durations = lint(args.path, mapping, rows, args)
    if len(shots) < args.min_shots:
        issues.append(("error", f"only {len(shots)} shots found, expected at least {args.min_shots}"))

    errors = [message for level, message in issues if level == "error"]
    warnings = [message for level, message in issues if level == "warning"]
    notes = [message for level, message in issues if level == "info"]
    total = sum(durations)

    if args.json:
        print(json.dumps(
            {
                "path": str(args.path),
                "shots": len(shots),
                "total_seconds": total,
                "errors": errors,
                "warnings": warnings,
                "info": notes,
            },
            ensure_ascii=False,
            indent=2,
        ))
    else:
        print(f"Checked {args.path} - {len(shots)} shots, total {total:g}s")
        for message in errors:
            print(f"  [ERROR]   {message}")
        for message in warnings:
            print(f"  [WARNING] {message}")
        for message in notes:
            print(f"  [INFO]    {message}")
        print(f"Result: {len(errors)} errors, {len(warnings)} warnings")

    if errors or (args.warnings_as_errors and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
