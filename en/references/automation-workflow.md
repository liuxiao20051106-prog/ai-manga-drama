# AI Manga Drama Automation

Load for batch shots, seasons, cross-session work, multiple contributors, or programmatic image/video/audio calls. Automation reduces repetition; it does not expand authority.

## State model

Use `unplanned → brief approved → anchors approved → candidate assets → quality review → author review → accepted → published`. Return to the latest recoverable state on failure.

## Minimal pipeline

1. Ingest the brief, source of truth, rights constraints, and input versions.
2. Validate files, fields, dependencies, and conflicts; stop on failure.
3. Plan assets, budget, limits, and completion criteria.
4. Obtain human approval for direction, real-person assets, bulk scope, and external changes.
5. Generate one reviewable unit, anchors before batches.
6. Check continuity, visual quality, motion, audio, rights, and specifications with evidence.
7. Accept, reject, discard, or request a bounded fix.
8. Commit only accepted results to records.
9. Require separate authorization for upload, public release, payment, contracts, or messages.

## Idempotency and retries

- Give every run a unique ID and record input versions, tools, outputs, validation, cost, and human decisions.
- A retry must not duplicate ledger rows, overwrite approved assets, charge twice, or publish twice.
- Write candidates first and promote only after validation.
- Cap attempts, time, and cost; stop after repeated same-class failures.
- When a service times out but may have completed or charged, query job status before resubmitting.

Use [the production run log](../templates/production-run-log.md). Keep secrets, contracts, identity records, and full voice samples out of ordinary logs. Lock batch scope so color work cannot change story, motion cannot redesign characters, and TTS cannot use an unapproved voice.
