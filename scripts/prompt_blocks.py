#!/usr/bin/env python3
"""Assemble structured generation prompts and lint the most common prompt mistakes.

The default prompt shape has four parts, in this order:

    FIXED IDENTITY   - who the character is; pasted verbatim in every shot
    FIXED STYLE      - the look; pasted verbatim in every shot
    SHOT VARIABLES   - what changes in this shot: action, framing, camera, light
    NEGATIVE         - what must not appear

Two failure modes account for most wasted generations, and both are mechanical:

  * identity or style wording drifts between shots, so the model re-interprets it;
  * the shot variables re-describe appearance that the reference image already
    fixed, which makes the model reinterpret the face.

The script assembles the prompt and flags both, plus prompts that ask for a
living creator's style, which is a rights risk rather than a craft choice.

Usage:
    python scripts/prompt_blocks.py --style-guide templates/style-guide.md \\
        --identity-text "CHAR-01 / LOOK-01: ..." --action "reaches for the mailbox" \\
        --shot-size "medium close" --camera "slow push in"

    python scripts/prompt_blocks.py --lang zh --style-block "..." --subject "小满" \\
        --action "伸手触碰信箱" --shot-size 中景 --out prompt.txt

Exit code is 1 when errors are found, 0 otherwise. Warnings alone do not fail the
run unless --warnings-as-errors is passed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.DOTALL)
STYLE_HEADING_KEYS = ("风格块", "style block", "风格文本")

IMITATION_PATTERNS = (
    r"in the style of",
    r"styled after",
    r"fan ?art",
    r"风格像",
    r"模仿",
    r"仿照",
    r"照搬",
    r"复刻",
    r"致敬",
    r"同人",
)

APPEARANCE_WORDS = (
    "发型",
    "发色",
    "头发",
    "短发",
    "长发",
    "刘海",
    "马尾",
    "辫",
    "服装",
    "穿着",
    "衣服",
    "眼睛",
    "瞳孔",
    "脸型",
    "五官",
    "耳环",
    "hair",
    "hairstyle",
    "short hair",
    "long hair",
    "bangs",
    "ponytail",
    "wardrobe",
    "outfit",
    "clothing",
    "eyes",
    "eye colour",
    "eye color",
    "face shape",
    "features",
)

MAX_IDENTITY_CHARS = 400

LABELS = {
    "zh": {
        "identity": "固定身份块",
        "style": "固定风格块",
        "variables": "镜头变量",
        "negative": "负面约束",
        "subject": "主体",
        "action": "动作",
        "shot_size": "景别/构图",
        "camera": "镜头运动",
        "setting": "场景与位置",
        "light": "光线与氛围",
        "entry": "入镜连续性",
        "exit": "出镜连续性",
    },
    "en": {
        "identity": "FIXED IDENTITY",
        "style": "FIXED STYLE",
        "variables": "SHOT VARIABLES",
        "negative": "NEGATIVE CONSTRAINTS",
        "subject": "subject",
        "action": "action",
        "shot_size": "shot size / composition",
        "camera": "camera movement",
        "setting": "setting and position",
        "light": "light and atmosphere",
        "entry": "entry continuity",
        "exit": "exit continuity",
    },
}


def extract_style_block(text: str) -> str:
    """Pull the first fenced block that follows a style-block heading."""
    lowered = text.lower()
    for key in STYLE_HEADING_KEYS:
        position = lowered.find(key.lower())
        if position == -1:
            continue
        match = FENCE_RE.search(text, position)
        if match:
            return match.group(1).strip()
    match = FENCE_RE.search(text)
    return match.group(1).strip() if match else ""


def load_text(path: Path, label: str, issues: list) -> str:
    try:
        return path.read_text(encoding="utf-8").strip()
    except OSError as error:
        issues.append(("error", f"{label}: cannot read {path} ({error})"))
        return ""


def build_variables(args, labels: dict) -> list:
    pairs = (
        (labels["subject"], args.subject),
        (labels["action"], args.action),
        (labels["shot_size"], args.shot_size),
        (labels["camera"], args.camera),
        (labels["setting"], args.setting),
        (labels["light"], args.light),
        (labels["entry"], args.entry),
        (labels["exit"], args.exit),
    )
    return [(name, value.strip()) for name, value in pairs if value and value.strip()]


def lint(identity: str, style: str, variables: list, negatives: list, issues: list) -> None:
    if not identity:
        issues.append(("error", "identity block is empty: consistency starts from a fixed identity text"))
    if not style:
        issues.append(("error", "style block is empty: without a fixed style text the look drifts"))
    if not variables:
        issues.append(("warning", "no shot variables given: nothing changes between this and the previous frame"))
    if not negatives:
        issues.append(("warning", "no negative constraints given: extra limbs, text and watermarks are easier to prevent than to fix"))

    combined = " ".join([identity, style] + [f"{name} {value}" for name, value in variables])
    lowered = combined.lower()
    for pattern in IMITATION_PATTERNS:
        if re.search(pattern, lowered):
            issues.append(
                ("error",
                 f"prompt asks for a recognisable creator or work ('{pattern}'): translate it into "
                 "line, colour, material, lighting and framing traits instead")
            )

    if identity and len(identity) > MAX_IDENTITY_CHARS:
        issues.append(
            ("warning",
             f"identity block is {len(identity)} characters, above {MAX_IDENTITY_CHARS}: "
             "long blocks dilute the parts that matter")
        )

    variable_text = " ".join(value for _, value in variables).lower()
    leaked = [word for word in APPEARANCE_WORDS if word in variable_text]
    if leaked:
        issues.append(
            ("warning",
             "shot variables re-describe appearance "
             f"({', '.join(sorted(set(leaked)))}): the reference image already fixes identity, "
             "repeating it makes the model reinterpret the face")
        )


def render(args, labels: dict, identity: str, style: str, variables: list, negatives: list) -> str:
    lines = []
    lines.append(f"[{labels['identity']}]")
    lines.append(identity or "-")
    lines.append("")
    lines.append(f"[{labels['style']}]")
    lines.append(style or "-")
    lines.append("")
    lines.append(f"[{labels['variables']}]")
    for name, value in variables:
        lines.append(f"- {name}: {value}")
    lines.append("")
    lines.append(f"[{labels['negative']}]")
    if negatives:
        for item in negatives:
            lines.append(f"- {item}")
    else:
        lines.append("- (none)")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Assemble a structured generation prompt")
    parser.add_argument("--lang", choices=("zh", "en"), default="zh")
    parser.add_argument("--style-guide", type=Path, default=None, help="style guide file to read the style block from")
    parser.add_argument("--style-block", default="", help="style block text given directly")
    parser.add_argument("--identity", type=Path, default=None, help="file holding the fixed identity text")
    parser.add_argument("--identity-text", default="", help="fixed identity text given directly")
    parser.add_argument("--subject", default="")
    parser.add_argument("--action", default="")
    parser.add_argument("--shot-size", default="")
    parser.add_argument("--camera", default="")
    parser.add_argument("--setting", default="")
    parser.add_argument("--light", default="")
    parser.add_argument("--entry", default="")
    parser.add_argument("--exit", default="")
    parser.add_argument("--negative", action="append", default=[], help="repeatable")
    parser.add_argument("--out", type=Path, default=None, help="write the prompt to this file")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--warnings-as-errors", action="store_true")
    args = parser.parse_args(argv)

    labels = LABELS[args.lang]
    issues = []

    style = args.style_block.strip()
    if not style and args.style_guide:
        if not args.style_guide.is_file():
            issues.append(("error", f"style guide not found: {args.style_guide}"))
        else:
            style = extract_style_block(load_text(args.style_guide, "style guide", issues))

    identity = args.identity_text.strip()
    if not identity and args.identity:
        if not args.identity.is_file():
            issues.append(("error", f"identity file not found: {args.identity}"))
        else:
            identity = load_text(args.identity, "identity", issues)

    variables = build_variables(args, labels)
    negatives = [item.strip() for item in args.negative if item.strip()]
    lint(identity, style, variables, negatives, issues)

    prompt = render(args, labels, identity, style, variables, negatives)
    if args.out:
        try:
            args.out.write_text(prompt + "\n", encoding="utf-8")
        except OSError as error:
            issues.append(("error", f"cannot write {args.out} ({error})"))

    errors = [message for level, message in issues if level == "error"]
    warnings = [message for level, message in issues if level == "warning"]

    if args.json:
        print(json.dumps(
            {
                "prompt": prompt,
                "identity_chars": len(identity),
                "style_chars": len(style),
                "variables": [name for name, _ in variables],
                "errors": errors,
                "warnings": warnings,
                "written_to": str(args.out) if args.out else None,
            },
            ensure_ascii=False,
            indent=2,
        ))
    else:
        print(prompt)
        print()
        if args.out:
            print(f"Written to {args.out}")
        for message in errors:
            print(f"  [ERROR]   {message}", file=sys.stderr)
        for message in warnings:
            print(f"  [WARNING] {message}", file=sys.stderr)
        if errors or warnings:
            print(f"Result: {len(errors)} errors, {len(warnings)} warnings", file=sys.stderr)

    if errors or (args.warnings_as_errors and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
