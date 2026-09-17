# -*- coding: utf-8 -*-
"""Unit tests for scripts/shotlist_lint.py."""

import sys
import tempfile
import unittest
from io import StringIO
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import shotlist_lint as sl  # noqa: E402


HEADER = (
    "| 镜号 | 时间码/秒 | 场景 | 角色/造型 | 构图/景别 | 动作与情绪 | 运镜 | 台词/声音 | "
    "入镜连续性 | 出镜连续性 | 状态 |\n"
    "|------|-----------|------|-----------|-----------|------------|------|-----------|"
    "------------|------------|------|\n"
)


def table(*rows):
    return "# 分镜表\n\n" + HEADER + "".join(row + "\n" for row in rows)


ROW_OK = "| E01-S001 | 00:00/4 | LOC-01 | CHAR-01/LOOK-01 | 全景 | 走进画面 | 缓推 | 无 | 门关闭 | 手抬起 | 已批准 |"
ROW_OK2 = "| E01-S002 | 00:04/5 | LOC-01 | CHAR-01/LOOK-01 | 中景 | 抬手触碰 | 固定 | 旁白 | 手抬起 | 手放下 | 已批准 |"


def run(text, *args):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "shot-list.md"
        path.write_text(text, encoding="utf-8")
        return sl.main([str(path), *args])


def capture(text, *args):
    """Run main() and return (exit code, stdout, stderr)."""
    out, err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out, err
    try:
        code = run(text, *args)
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    return code, out.getvalue(), err.getvalue()


class ShotlistLintTests(unittest.TestCase):
    def test_valid_table_has_no_errors(self):
        code, output, err = capture(table(ROW_OK, ROW_OK2), "--target-seconds", "9")
        self.assertEqual(code, 0)
        self.assertIn("0 errors", output)
        self.assertEqual(err.strip(), "")

    def test_bad_shot_id_is_error(self):
        code, output, _ = capture(table(ROW_OK.replace("E01-S001", "shot1")))
        self.assertEqual(code, 1)
        self.assertIn("shot ID", output)

    def test_missing_required_field_is_error(self):
        code, output, _ = capture(table(ROW_OK.replace("| 全景 |", "|  |")))
        self.assertEqual(code, 1)
        self.assertIn("framing", output)

    def test_unparsable_duration_is_error(self):
        code, output, _ = capture(table(ROW_OK.replace("00:00/4", "晚些时候")))
        self.assertEqual(code, 1)
        self.assertIn("not parsable", output)

    def test_long_shot_is_warning(self):
        code, output, _ = capture(table(ROW_OK.replace("00:00/4", "00:00/22")))
        self.assertEqual(code, 0)
        self.assertIn("single-shot cap", output)

    def test_warnings_as_errors_fails(self):
        code, _, _ = capture(table(ROW_OK.replace("00:00/4", "00:00/22")), "--warnings-as-errors")
        self.assertEqual(code, 1)

    def test_total_duration_beyond_tolerance_is_error(self):
        code, output, _ = capture(table(ROW_OK, ROW_OK2), "--target-seconds", "60")
        self.assertEqual(code, 1)
        self.assertIn("differs by", output)

    def test_blank_exit_state_is_warning(self):
        code, output, _ = capture(table(ROW_OK, ROW_OK2.replace("| 手抬起 | 手放下 |", "|  | 手放下 |")))
        self.assertEqual(code, 0)
        self.assertIn("exit/entry state not written", output)

    def test_consecutive_identical_framing_is_warning(self):
        second = ROW_OK2.replace("00:04/5", "00:04/5")
        third = ROW_OK2.replace("E01-S002", "E01-S003")
        fourth = ROW_OK2.replace("E01-S002", "E01-S004")
        code, output, _ = capture(table(second, third, fourth))
        self.assertEqual(code, 0)
        self.assertIn("consecutive shots share framing", output)

    def test_csv_input_is_supported(self):
        csv_text = (
            "Shot,Timecode,Composition,Action,Entry,Exit,Status\n"
            "E01-S001,4,wide,walks in,none,hand raised,approved\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "shots.csv"
            path.write_text(csv_text, encoding="utf-8")
            self.assertEqual(sl.main([str(path)]), 0)

    def test_missing_shot_table_is_error(self):
        code, _, err = capture("# no table here\n\njust prose\n")
        self.assertEqual(code, 1)
        self.assertIn("no shot table found", err)

    def test_short_clock_duration_is_parsed(self):
        self.assertEqual(sl.parse_duration("00:06"), 6.0)
        self.assertEqual(sl.parse_duration("01:30/00:04"), 4.0)
        self.assertEqual(sl.parse_duration("4s"), 4.0)
        self.assertIsNone(sl.parse_duration("abc"))


if __name__ == "__main__":
    unittest.main()
