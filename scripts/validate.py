#!/usr/bin/env python3
"""Validate the repository without third-party dependencies.

The repository is both a Skill and a small open-source project, and it is
bilingual. The failure modes that matter are mechanical, so a script handles them:

  * front matter that no longer parses, or a Skill body that grew past the limit
  * a relative link that points at a file which moved
  * a Chinese reference or template without an English counterpart
  * Han characters left inside the English tree
  * an English file that is a stub rather than a translation
  * a reference or template that nothing links to (unreachable from the router)
  * unfinished markers such as TODO or PLACEHOLDER
  * a script with a syntax error

Mirror sets are discovered from the filesystem rather than hard-coded, so adding
a guide only requires adding its translation.

Usage:
    python -X utf8 scripts/validate.py
    python -X utf8 scripts/validate.py --root .
    python -X utf8 scripts/validate.py --warnings-as-errors

Exit code is 1 when errors are found (or when warnings are promoted), 0 otherwise.
"""

from __future__ import annotations

import argparse
import py_compile
import re
import sys
import tempfile
import unicodedata
from pathlib import Path
from urllib.parse import unquote

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
LOCAL_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b", re.IGNORECASE)
HEADING = re.compile(r"^#{1,6}\s+\S", re.MULTILINE)

SKILL_FILES = (("SKILL.md", "ai-manga-drama"), ("en/SKILL.md", "ai-manga-drama-en"))
MIRROR_DIRS = ("references", "templates")
MAX_SKILL_LINES = 500
MAX_DESCRIPTION_CHARS = 1024
MIN_MIRROR_RATIO = 0.4


def han_characters(text: str) -> list:
    """Return the Han characters present in text."""
    return [char for char in text if unicodedata.name(char, "").startswith("CJK UNIFIED")]


def markdown_files(root: Path) -> list:
    return sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)


def read_utf8(path: Path, root: Path, failures: list) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        failures.append(("error", f"{path.relative_to(root)} is not valid UTF-8: {error}"))
        return ""


def check_front_matter(root: Path, failures: list) -> None:
    for relative, expected_name in SKILL_FILES:
        path = root / relative
        if not path.is_file():
            failures.append(("error", f"{relative} is missing"))
            continue
        text = read_utf8(path, root, failures)
        match = FRONT_MATTER.match(text)
        if not match:
            failures.append(("error", f"{relative} has invalid front matter"))
            continue

        fields = {}
        for line in match.group(1).splitlines():
            key, separator, value = line.partition(":")
            if separator:
                fields[key.strip()] = value.strip()

        if fields.get("name") != expected_name:
            failures.append(("error", f"{relative} must use name: {expected_name}"))

        description = fields.get("description", "")
        if not description:
            failures.append(("error", f"{relative} has no description"))
        elif len(description) > MAX_DESCRIPTION_CHARS:
            failures.append(("error", f"{relative} description exceeds {MAX_DESCRIPTION_CHARS} characters"))
        elif "<" in description or ">" in description:
            failures.append(("error", f"{relative} description contains XML angle brackets"))

        body_lines = len(text[match.end():].splitlines())
        if body_lines > MAX_SKILL_LINES:
            failures.append(("error", f"{relative} body is {body_lines} lines, above the {MAX_SKILL_LINES} line limit"))


def check_links(root: Path, failures: list) -> None:
    for path in markdown_files(root):
        text = read_utf8(path, root, failures)
        for raw_target in LOCAL_LINK.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if target and not (path.parent / target).resolve().exists():
                failures.append(("error", f"{path.relative_to(root)} has a broken link: {raw_target}"))


def check_placeholders(root: Path, failures: list) -> None:
    for path in markdown_files(root):
        text = read_utf8(path, root, failures)
        if PLACEHOLDER.search(text):
            failures.append(("error", f"{path.relative_to(root)} contains an unfinished marker"))


def check_english_tree(root: Path, failures: list) -> None:
    en_root = root / "en"
    if not en_root.is_dir():
        failures.append(("error", "en/ mirror directory is missing"))
        return
    for path in sorted(en_root.rglob("*.md")):
        text = read_utf8(path, root, failures)
        leftover = han_characters(text)
        if leftover:
            sample = "".join(leftover[:8])
            failures.append(("error", f"{path.relative_to(root)} contains Han characters: {sample}"))
        if not HEADING.search(text):
            failures.append(("error", f"{path.relative_to(root)} has no headings"))


def check_mirrors(root: Path, failures: list) -> None:
    for directory in MIRROR_DIRS:
        chinese = root / directory
        english = root / "en" / directory
        if not chinese.is_dir():
            failures.append(("error", f"{directory}/ is missing"))
            continue
        if not english.is_dir():
            failures.append(("error", f"en/{directory}/ is missing"))
            continue

        zh_files = sorted(path.name for path in chinese.glob("*.md"))
        en_files = sorted(path.name for path in english.glob("*.md"))

        for name in zh_files:
            if name not in en_files:
                failures.append(("error", f"en/{directory}/{name} is missing (mirror incomplete)"))
                continue
            zh_lines = len((chinese / name).read_text(encoding="utf-8").splitlines())
            en_lines = len((english / name).read_text(encoding="utf-8").splitlines())
            if zh_lines and en_lines < zh_lines * MIN_MIRROR_RATIO:
                failures.append(
                    ("warning",
                     f"en/{directory}/{name} has {en_lines} lines against {zh_lines} in the Chinese file: "
                     "check that it is a translation rather than a stub")
                )

        for name in en_files:
            if name not in zh_files:
                failures.append(("warning", f"en/{directory}/{name} has no Chinese counterpart"))


def check_reachability(root: Path, failures: list) -> None:
    """Every guide and template should be reachable from the Skill router."""
    for relative in ("SKILL.md", "en/SKILL.md"):
        path = root / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        linked = set()
        for target in LOCAL_LINK.findall(text):
            cleaned = unquote(target.strip().strip("<>").split("#", 1)[0])
            if cleaned and not cleaned.startswith(("http://", "https://", "mailto:")):
                linked.add(cleaned.replace("\\", "/"))
        for directory in MIRROR_DIRS:
            for child in sorted((path.parent / directory).glob("*.md")):
                file_relative = f"{directory}/{child.name}"
                root_relative = child.relative_to(root).as_posix()
                if file_relative not in linked and root_relative not in linked:
                    failures.append(
                        ("warning",
                         f"{relative} does not link {root_relative}: the file is unreachable from the router")
                    )


def check_scripts(root: Path, failures: list) -> None:
    scripts = root / "scripts"
    if not scripts.is_dir():
        failures.append(("error", "scripts/ is missing"))
        return
    with tempfile.TemporaryDirectory() as tmp:
        for path in sorted(scripts.glob("*.py")):
            try:
                py_compile.compile(str(path), cfile=str(Path(tmp) / f"{path.stem}.pyc"), doraise=True)
            except py_compile.PyCompileError as error:
                failures.append(("error", f"{path.name} has a syntax error: {error}"))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Validate the ai-manga-drama skill repository")
    parser.add_argument("--root", type=Path, default=None, help="repository root (defaults to the parent of scripts/)")
    parser.add_argument("--warnings-as-errors", action="store_true", help="treat warnings as failures")
    args = parser.parse_args(argv)

    root = (args.root or Path(__file__).resolve().parents[1]).resolve()

    findings: list = []
    check_front_matter(root, findings)
    check_links(root, findings)
    check_placeholders(root, findings)
    check_english_tree(root, findings)
    check_mirrors(root, findings)
    check_reachability(root, findings)
    check_scripts(root, findings)

    errors = [message for level, message in findings if level == "error"]
    warnings = [message for level, message in findings if level == "warning"]

    print(f"Validated {len(markdown_files(root))} Markdown files under {root}")
    for message in errors:
        print(f"  [ERROR]   {message}")
    for message in warnings:
        print(f"  [WARNING] {message}")
    print(f"Result: {len(errors)} errors, {len(warnings)} warnings")

    if errors or (args.warnings_as_errors and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
