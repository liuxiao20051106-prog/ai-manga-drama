# -*- coding: utf-8 -*-
"""Unit tests for scripts/prompt_blocks.py."""

import sys
import tempfile
import unittest
from io import StringIO
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import prompt_blocks as pb  # noqa: E402


STYLE_GUIDE = """# 风格指南

## 1. 风格块（固定文本）

```text
细勾线，赛璐璐平涂，低饱和暖色调，单侧逆光，背景极简。
```

## 2. 六个维度取值
"""

IDENTITY = "CHAR-01 / LOOK-01：齐耳黑色短发，米白毛衣，灰色长裙，右手腕红色手绳。"


def capture(args):
    out, err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out, err
    try:
        code = pb.main(args)
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    return code, out.getvalue(), err.getvalue()


def base_args(tmp, *extra):
    guide = Path(tmp) / "style-guide.md"
    guide.write_text(STYLE_GUIDE, encoding="utf-8")
    return [
        "--style-guide", str(guide),
        "--identity-text", IDENTITY,
        "--action", "伸手触碰信箱",
        "--shot-size", "中景",
        "--camera", "缓慢推近",
        *extra,
    ]


class PromptBlocksTests(unittest.TestCase):
    def test_style_block_is_extracted_from_guide(self):
        with tempfile.TemporaryDirectory() as tmp:
            guide = Path(tmp) / "style-guide.md"
            guide.write_text(STYLE_GUIDE, encoding="utf-8")
            self.assertIn("赛璐璐", pb.extract_style_block(guide.read_text(encoding="utf-8")))

    def test_assembled_prompt_contains_all_four_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, output, _ = capture(base_args(tmp, "--negative", "多手", "--negative", "文字水印"))
            self.assertEqual(code, 0)
            for label in ("固定身份块", "固定风格块", "镜头变量", "负面约束"):
                self.assertIn(label, output)
            self.assertIn("伸手触碰信箱", output)

    def test_imitation_request_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, _, err = capture(base_args(tmp, "--shot-size", "参考某导演 in the style of 某某"))
            self.assertEqual(code, 1)
            self.assertIn("recognisable creator", err)

    def test_missing_style_block_is_error(self):
        code, _, err = capture(["--identity-text", IDENTITY, "--action", "走路"])
        self.assertEqual(code, 1)
        self.assertIn("style block is empty", err)

    def test_appearance_repeat_in_variables_is_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, _, err = capture(base_args(tmp, "--action", "整理黑色短发"))
            self.assertEqual(code, 0)
            self.assertIn("re-describe appearance", err)

    def test_missing_negatives_is_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, _, err = capture(base_args(tmp))
            self.assertEqual(code, 0)
            self.assertIn("no negative constraints", err)

    def test_writes_prompt_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            out_file = Path(tmp) / "prompt.txt"
            code, _, _ = capture(base_args(tmp, "--out", str(out_file), "--negative", "水印"))
            self.assertEqual(code, 0)
            self.assertIn("固定身份块", out_file.read_text(encoding="utf-8"))

    def test_language_switch_uses_english_labels(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, output, _ = capture(["--lang", "en", "--style-block", "fine line, cel shading",
                                       "--identity-text", "CHAR-01: short black hair",
                                       "--action", "reaches for the mailbox"])
            self.assertEqual(code, 0)
            self.assertIn("FIXED IDENTITY", output)
            self.assertIn("NEGATIVE CONSTRAINTS", output)


if __name__ == "__main__":
    unittest.main()
