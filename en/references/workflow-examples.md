# End-to-End Workflow Examples

These examples show decision and handoff structure, not guaranteed time, price, or service availability.

## Accessible-cloud 30-second healing short

Project: *Waiting for a Letter*. Vertical. The promise is a small sign of hope after a long wait.

- Xiaoman has ear-length black hair, cream sweater, gray skirt, and red wrist cord in every shot.
- Shots: apartment entrance; approach mailbox; right hand touches empty box with narration; she leaves as short hair moves in the breeze; envelope appears in the gap.
- Approve character and apartment anchors before five keyframes, then animate each shot and complete voice, captions, mix, and review.

If a generation changes ear-length hair to long hair, reject it as continuity failure rather than calling it wind motion.

## Premium-cloud 60-second mystery

Project: *Life-Swap Game*. The phone’s rules and a rider’s reaction create the reversal.

1. Lock the rules, protagonist knowledge, and final reveal in the brief.
2. Approve protagonist and rider separately before group work.
3. Typeset long phone messages in post instead of relying on image-model text.
4. Separate phone, reaction, run-to-window, rider lookup, and message reveal shots.
5. Do not use a real delivery worker, company marks, or real-person voice; recheck platform disclosure on release.

## Local batch pipeline

```text
approved brief
  → structured shot list
  → human-approved character/location anchors
  → candidate keyframes
  → continuity and rights review
  → candidate motion clips
  → voice/music/captions
  → editor or FFmpeg assembly
  → quality score and author review
  → separately authorized release
```

Write every shot to a candidate directory. Record run ID, input versions, seed, model, license, attempts, and cost in [the run log](../templates/production-run-log.md). If using MoviePy, test against current v2 documentation rather than copying old `moviepy.editor` code.

## Acceptance

- Facts, looks, and shot entry/exit agree.
- Rejected candidates are not mixed into approved directories.
- Voice, captions, and picture timecodes align.
- Every asset has provenance, rights, version, and review state.
- A passing master is a release candidate, not permission to publish.
