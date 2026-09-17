# -*- coding: utf-8 -*-
"""Unit tests for scripts/budget_estimate.py."""

import csv
import sys
import tempfile
import unittest
from io import StringIO
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import budget_estimate as be  # noqa: E402


def capture(args):
    out, err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out, err
    try:
        code = be.main(args)
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    return code, out.getvalue(), err.getvalue()


class BudgetEstimateTests(unittest.TestCase):
    def test_cost_arithmetic(self):
        result = be.estimate(shots=40, seconds=5, attempts=2, unit_cost=1.0, target_seconds=180)
        self.assertEqual(result["kept_seconds"], 200)
        self.assertEqual(result["generated_seconds"], 400)
        self.assertEqual(result["cost"], 400)
        self.assertAlmostEqual(result["cost_per_publishable_minute"], 120.0)
        self.assertAlmostEqual(result["episodes"], 200 / 180)

    def test_discarded_attempts_are_charged_to_keepers(self):
        cheap_but_lossy = be.estimate(10, 5, 4, 1.0, 0)
        dear_but_reliable = be.estimate(10, 5, 1.5, 2.0, 0)
        self.assertGreater(cheap_but_lossy["cost"], dear_but_reliable["cost"],
                           "the lossy route should cost more once failures are counted")

    def test_sensitivity_is_monotonic_in_attempts(self):
        rows = be.sensitivity(shots=10, seconds=6, unit_cost=1.0)
        costs = [row["cost"] for row in rows]
        self.assertEqual(costs, sorted(costs))
        self.assertEqual(len(rows), len(be.ATTEMPT_STEPS))

    def test_break_even_attempts(self):
        self.assertAlmostEqual(be.break_even_attempts(200, 10, 5, 1.0), 4.0)
        self.assertIsNone(be.break_even_attempts(0, 10, 5, 1.0))

    def test_text_output_reports_key_metrics(self):
        code, output, _ = capture(["--shots", "42", "--seconds", "6", "--attempts", "2.5",
                                   "--unit-cost", "0.6", "--target-seconds", "180"])
        self.assertEqual(code, 0)
        self.assertIn("Cost / pub. minute", output)
        self.assertIn("Sensitivity to attempts", output)

    def test_budget_exceeded_warns(self):
        code, _, err = capture(["--shots", "42", "--seconds", "6", "--attempts", "3",
                                "--unit-cost", "2", "--budget", "10"])
        self.assertEqual(code, 0)
        self.assertIn("exceed the stated budget", err)

    def test_json_output_is_parseable(self):
        import json
        code, output, _ = capture(["--shots", "5", "--seconds", "4", "--json"])
        self.assertEqual(code, 0)
        payload = json.loads(output)
        self.assertEqual(payload["result"]["kept_seconds"], 20)
        self.assertIn("sensitivity", payload)

    def test_csv_export(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "budget.csv"
            code, _, _ = capture(["--shots", "5", "--seconds", "4", "--csv", str(target)])
            self.assertEqual(code, 0)
            rows = list(csv.reader(target.read_text(encoding="utf-8").splitlines()))
            self.assertEqual(rows[0][0], "attempts_per_kept_shot")
            self.assertEqual(len(rows), len(be.ATTEMPT_STEPS) + 1)

    def test_invalid_input_is_rejected(self):
        code, _, err = capture(["--shots", "0"])
        self.assertEqual(code, 1)
        self.assertIn("must be positive", err)


if __name__ == "__main__":
    unittest.main()
