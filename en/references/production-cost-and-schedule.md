# Cost, Capacity, and Scheduling

Load when estimating a budget, deciding an update cadence, diagnosing "we keep working but nothing ships", or planning the ramp from sample to volume. The goal is **accountable and reproducible**, not a revenue forecast.

> Related: retry and idempotency rules in [Automation Workflow](automation-workflow.md); records and write-back in [Project and Continuity](project-and-continuity.md); platform revenue structures in [Commercialization and Analytics](commercialization-and-analytics.md).

## I. The only meaningful cost metric: cost per publishable minute

Cost per generated shot is a false metric. What matters is:

```
cost per publishable unit = (generation credits + subscriptions + hardware power + labour + licences) / number of usable outputs
```

The denominator is the point: include failures and rework. If a shot needed four generations to yield one keeper, all four attempts are charged to that keeper.

**Compare hit rate, not unit price.** A cheap tool that keeps one in four is usually more expensive than one at double the price that keeps three in four.

Size the budget first with the script:

```bash
python scripts/budget_estimate.py --shots 42 --seconds 6 --attempts 2.5 --unit-cost 0.6 --target-seconds 180
```

Fill in the unit cost for the tools you actually use; those numbers change constantly, so always verify against the current official page.

## II. The per-episode effort model

```
episode effort ~= shots x attempts per shot x (generation wait + review and selection + rework)
                + script and storyboard (one-off, improves fastest with practice)
                + voice, music, subtitles
                + assembly and final check
```

**Rules of thumb**:

- The first three episodes are the most expensive. Once anchors (character, location, style) are approved, each later episode's marginal cost drops noticeably.
- **Never economise on the anchor stage.** Saving an hour there costs two hours of drift repair on every subsequent episode.
- Use the waiting: while generations queue, write the next script or finish the previous episode's post. This is the single most direct capacity gain available.

## III. Failure rate and retry budget

Every stage needs a hard cap, or the budget disappears:

| Stage | Suggested cap (scale to project size) | Action on trigger |
|-------|----------------------------------------|-------------------|
| Attempts per shot | 3-5 | stop: change the shot, the motion level, or the tool |
| Same failure repeated | 3 | treat the method as wrong; stop pulling the lever |
| Rework share per episode | 20-30% | above that, re-audit anchors and the style block |
| Spend per episode | hard budget cap | ship the best usable version first, then decide whether to invest more |

**"One more try" is the biggest capacity killer.** Caps exist so failures surface early instead of compounding across a season.

## IV. Three gates: sample, small batch, volume

**Do not start with a full season.** Ramp in stages, each with explicit pass conditions:

| Stage | What you make | Pass condition |
|-------|---------------|----------------|
| **1 Sample** | one 15-30 second piece, or one minimal episode | no character drift, consistent style, usable sound, author approves the direction |
| **2 Small batch** | 3-5 episodes | cost per publishable unit stable, failure rate converging, cadence sustainable |
| **3 Volume** | full season or serial | earlier parameters frozen into templates and checklists that another person can execute |

Treat each gate as a real decision point rather than a default continuation.

## V. Scheduling

A schedule needs at least four columns: **episode / target delivery date / current state / blocker**. Add three kinds of buffer:

- **Review buffer**: platform and author review take time and can bounce work back.
- **Failure buffer**: sized from your measured failure rate (commonly 20-40%).
- **Rest buffer**: essential for daily updates; sustained intensity shows up directly in quality and judgement.

**Derive the cadence from real capacity** rather than declaring a schedule and absorbing the pain. Steady updates beat a burst followed by silence.

## VI. Cost items people forget

- Generation credits and subscriptions (image, video, voice, music)
- Hardware and power (local routes: card depreciation, electricity, maintenance time)
- Labour (writing, storyboarding, selection, post, review)
- **Licences**: music, effects, fonts, reference material, real-person likeness and voice
- Storage and transfer (multi-version assets grow fast)
- Rework, derived from your failure rate

Local routes look free but card depreciation and power belong in the model; paid routes look expensive but the time they save is also a cost. Compare both on **cost per publishable unit**.

## VII. Records and review

- Log attempts, hit rate, and spend per shot in [the production run log](../templates/production-run-log.md).
- After each episode record: actual hours, actual spend, rework share, and the stage that failed most.
- **How to find the bottleneck**: rank stages by share of time or spend consumed. If 70% goes into one thing (usually character drift or broken action), change the process for that thing instead of working longer overall.

## VIII. Checklist

- [ ] Is cost per publishable unit calculated, including failures and licences?
- [ ] Are the per-shot attempt cap, repeated-failure cap, and per-episode budget cap set?
- [ ] Did you go sample, then small batch, then volume?
- [ ] Was the anchor stage given enough time?
- [ ] Is the cadence derived from real capacity rather than guessed?
- [ ] Does the schedule carry review, failure, and rest buffers?
- [ ] Is each episode's actual spend and failure stage recorded?
