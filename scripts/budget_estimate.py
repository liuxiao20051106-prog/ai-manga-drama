#!/usr/bin/env python3
"""Estimate generation volume, spend, and the sensitivity of cost to hit rate.

Cost per generated second is a misleading number on its own, because the shots you
throw away are paid for by the shots you keep. The metric that decides whether a
route is affordable is the cost of one publishable minute:

    cost per publishable minute = total spend / kept seconds * 60

This script takes the four numbers you actually know at planning time - how many
shots, how long each shot is, how many attempts a kept shot really takes, and what
one generated second costs - and reports the result plus a sensitivity table, so
the decision "spend on a better tool or accept more retries" becomes arithmetic.

Usage:
    python scripts/budget_estimate.py --shots 42 --seconds 6 --attempts 2.5 --unit-cost 0.6
    python scripts/budget_estimate.py --shots 42 --seconds 6 --attempts 2.5 --unit-cost 0.6 \\
        --target-seconds 180 --episodes 12 --budget 900 --csv budget.csv

Unit cost is deliberately abstract: pass the cost of one generated second in
whatever currency you pay in. Prices and quotas change constantly, so verify them
against the current official page before committing a budget.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ATTEMPT_STEPS = (1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0)


def estimate(shots: int, seconds: float, attempts: float, unit_cost: float, target_seconds: float):
    kept_seconds = shots * seconds
    generated_seconds = kept_seconds * attempts
    cost = generated_seconds * unit_cost
    per_kept_second = cost / kept_seconds if kept_seconds else 0.0
    per_minute = per_kept_second * 60
    episodes = kept_seconds / target_seconds if target_seconds else None
    cost_per_episode = cost / episodes if episodes else None
    return {
        "kept_seconds": kept_seconds,
        "generated_seconds": generated_seconds,
        "cost": cost,
        "cost_per_kept_second": per_kept_second,
        "cost_per_publishable_minute": per_minute,
        "episodes": episodes,
        "cost_per_episode": cost_per_episode,
    }


def sensitivity(shots: int, seconds: float, unit_cost: float):
    kept_seconds = shots * seconds
    rows = []
    for attempts in ATTEMPT_STEPS:
        cost = kept_seconds * attempts * unit_cost
        rows.append(
            {
                "attempts": attempts,
                "generated_seconds": kept_seconds * attempts,
                "cost": cost,
                "cost_per_publishable_minute": (cost / kept_seconds * 60) if kept_seconds else 0.0,
            }
        )
    return rows


def break_even_attempts(budget: float, shots: int, seconds: float, unit_cost: float):
    kept_seconds = shots * seconds
    if not budget or not kept_seconds or not unit_cost:
        return None
    return budget / (kept_seconds * unit_cost)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Estimate manga-drama generation budget")
    parser.add_argument("--shots", type=int, required=True, help="shots per episode")
    parser.add_argument("--seconds", type=float, default=5.0, help="average kept seconds per shot")
    parser.add_argument("--attempts", type=float, default=2.0, help="average attempts per kept shot")
    parser.add_argument("--unit-cost", type=float, default=1.0, help="cost of one generated second")
    parser.add_argument("--target-seconds", type=float, default=None, help="episode target duration")
    parser.add_argument("--episodes", type=int, default=None, help="plan for this many episodes")
    parser.add_argument("--budget", type=float, default=None, help="available budget for the episode")
    parser.add_argument("--currency", default="", help="currency symbol or code, for display only")
    parser.add_argument("--csv", type=Path, default=None, help="write the sensitivity table to CSV")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if args.shots <= 0 or args.seconds <= 0:
        print("ERROR: --shots and --seconds must be positive", file=sys.stderr)
        return 1
    if args.attempts <= 0 or args.unit_cost < 0:
        print("ERROR: --attempts must be positive and --unit-cost cannot be negative", file=sys.stderr)
        return 1

    result = estimate(args.shots, args.seconds, args.attempts, args.unit_cost, args.target_seconds or 0)
    rows = sensitivity(args.shots, args.seconds, args.unit_cost)
    max_attempts = break_even_attempts(args.budget, args.shots, args.seconds, args.unit_cost)
    total_cost = result["cost"] * args.episodes if args.episodes else None

    symbol = f"{args.currency}" if args.currency else ""
    warnings = []
    if result["episodes"] is None:
        warnings.append("no --target-seconds given: episode count could not be derived")
    if args.budget is not None and result["cost"] > args.budget:
        warnings.append("current assumptions exceed the stated budget")
    if args.attempts > 3:
        warnings.append("more than three attempts per kept shot usually means the method, not the luck, is the problem")

    if args.csv:
        try:
            with args.csv.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.writer(handle)
                writer.writerow(["attempts_per_kept_shot", "generated_seconds", "cost",
                                 "cost_per_publishable_minute"])
                for row in rows:
                    writer.writerow([row["attempts"], f"{row['generated_seconds']:.1f}",
                                     f"{row['cost']:.2f}", f"{row['cost_per_publishable_minute']:.2f}"])
        except OSError as error:
            print(f"ERROR: cannot write {args.csv} ({error})", file=sys.stderr)
            return 1

    if args.json:
        print(json.dumps(
            {
                "inputs": {
                    "shots": args.shots,
                    "seconds": args.seconds,
                    "attempts": args.attempts,
                    "unit_cost": args.unit_cost,
                    "target_seconds": args.target_seconds,
                    "episodes": args.episodes,
                    "budget": args.budget,
                },
                "result": result,
                "total_cost": total_cost,
                "max_affordable_attempts": max_attempts,
                "sensitivity": rows,
                "warnings": warnings,
            },
            ensure_ascii=False,
            indent=2,
        ))
        return 0

    print(f"Shots per episode : {args.shots}")
    print(f"Kept seconds      : {result['kept_seconds']:.1f}s")
    print(f"Attempts per shot : {args.attempts:g}")
    print(f"Generated seconds : {result['generated_seconds']:.1f}s")
    print(f"Cost              : {symbol}{result['cost']:.2f}")
    print(f"Cost / kept second: {symbol}{result['cost_per_kept_second']:.3f}")
    print(f"Cost / pub. minute: {symbol}{result['cost_per_publishable_minute']:.2f}")
    if result["episodes"] is not None:
        print(f"Episodes covered  : {result['episodes']:.2f}")
        print(f"Cost per episode  : {symbol}{result['cost_per_episode']:.2f}")
    if total_cost is not None:
        print(f"Cost for {args.episodes} episodes: {symbol}{total_cost:.2f}")

    if max_attempts is not None:
        print(f"Budget {symbol}{args.budget:.2f} allows about {max_attempts:.2f} attempts per kept shot")

    print()
    print("Sensitivity to attempts per kept shot")
    print("  attempts   generated seconds        cost   cost / pub. minute")
    for row in rows:
        print(f"  {row['attempts']:>8.2f}   {row['generated_seconds']:>17.1f}   "
              f"{symbol}{row['cost']:>9.2f}   {symbol}{row['cost_per_publishable_minute']:>16.2f}")

    for message in warnings:
        print(f"  [WARNING] {message}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
