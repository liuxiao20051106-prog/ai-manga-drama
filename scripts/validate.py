#!/usr/bin/env python3
"""Validate the repository without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_REFERENCES = {
    "automation-workflow.md",
    "character-consistency.md",
    "commercialization-and-analytics.md",
    "project-and-continuity.md",
    "prompt-templates.md",
    "quality-evaluation-and-tests.md",
    "rights-safety-and-platforms.md",
    "tools-catalog.md",
    "workflow-examples.md",
}
EXPECTED_TEMPLATES = {
    "asset-ledger.md",
    "character-bible.md",
    "episode-brief.md",
    "manga-project.md",
    "production-run-log.md",
    "quality-scorecard.md",
    "release-checklist.md",
    "rights-consent-log.md",
    "shot-list.md",
}
LOCAL_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b", re.IGNORECASE)
HAN = re.compile(r"[\u3400-\u9fff]")


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def read_utf8(path: Path, failures: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        failures.append(f"{path.relative_to(ROOT)} is not UTF-8: {error}")
        return ""


def validate_skill(path: Path, expected_name: str, failures: list[str]) -> None:
    text = read_utf8(path, failures)
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        failures.append(f"{path.relative_to(ROOT)} has invalid front matter")
        return

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if separator:
            fields[key.strip()] = value.strip()

    if fields.get("name") != expected_name:
        failures.append(f"{path.relative_to(ROOT)} must use name: {expected_name}")
    description = fields.get("description", "")
    if not description or len(description) > 1024 or "<" in description or ">" in description:
        failures.append(f"{path.relative_to(ROOT)} has an invalid description")
    if len(text.splitlines()) > 500:
        failures.append(f"{path.relative_to(ROOT)} exceeds 500 lines")


def validate_links(path: Path, text: str, failures: list[str]) -> None:
    for raw_target in LOCAL_LINK.findall(text):
        target = raw_target.strip().strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if target and not (path.parent / target).resolve().exists():
            failures.append(f"{path.relative_to(ROOT)} has broken link: {raw_target}")


def filenames(directory: Path) -> set[str]:
    return {path.name for path in directory.glob("*.md")}


def main() -> int:
    failures: list[str] = []
    validate_skill(ROOT / "SKILL.md", "ai-manga-drama", failures)
    validate_skill(ROOT / "en" / "SKILL.md", "ai-manga-drama-en", failures)

    mirrors = (
        (ROOT / "references", ROOT / "en" / "references", EXPECTED_REFERENCES),
        (ROOT / "templates", ROOT / "en" / "templates", EXPECTED_TEMPLATES),
    )
    for chinese, english, expected in mirrors:
        if filenames(chinese) != expected:
            failures.append(f"{chinese.relative_to(ROOT)} does not match the expected file set")
        if filenames(english) != expected:
            failures.append(f"{english.relative_to(ROOT)} does not mirror the expected file set")

    for path in markdown_files():
        text = read_utf8(path, failures)
        validate_links(path, text, failures)
        if PLACEHOLDER.search(text):
            failures.append(f"{path.relative_to(ROOT)} contains an unfinished marker")
        if "en" in path.relative_to(ROOT).parts and HAN.search(text):
            failures.append(f"{path.relative_to(ROOT)} contains Han characters")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1

    print(f"Validated {len(markdown_files())} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
