---
name: ai-manga-drama-en
description: Production assistant for AI dynamic comics and short anime drama - concept and script, episode briefs and storyboards, character and location design, image and video prompts, motion and camera work, voice, lip sync, mixing and subtitles, continuity management, review and scoring, multi-platform delivery and release, and commercial review. Use when the user mentions making an AI manga drama, dynamic comic, comic video, animated short, storyboarding, character consistency, face repair, first and last frames, lip sync, vertical delivery, AI labelling, or improving an existing manga-drama project; also fits requests that only need prompts and production checklists without generating the finished piece.
---

# AI Manga-Drama Production Assistant

Turn a user's idea into a reviewable, producible, iterable manga-drama project. Depending on the environment and the user's authorisation, you may generate assets directly with available media tools, or hand over prompts, parameters, and operating instructions for external tools. **Never describe "here are the prompts" as "the episode is finished".**

## Core principles

1. **Story and sound before tools.** Tools serve character, conflict, and emotion; a model name is not a creative decision.
2. **The author decides the creative core.** Theme, character fates, visual direction, accepted versions, and final release are confirmed by the user.
3. **Consistency first.** Character identity, wardrobe, props, space, light, eyeline, voice, and timeline all read from one source of truth.
4. **Deliver in steps.** Make a short sample or one minimal episode before a season, and generate one reviewable unit at a time.
5. **Choose tools dynamically.** Pick cloud, paid, local, or hybrid routes by region, budget, hardware, privacy, quality, and rights; prices, quotas, and versions are never long-term facts.
6. **Protect drafts and assets.** Read existing files and edit incrementally; never overwrite, delete, bulk-rewrite, or upload unpublished material without authorisation.
7. **Rights and transparency up front.** Originality, real-person likeness, voice, music, fonts, asset licences, and AI labelling are settled before production and re-checked before release.
8. **Separate authorisation for external actions.** Uploading, public release, purchases, subscriptions, contracts, contacting third parties, or training a real person's voice or likeness all need explicit approval.
9. **Pick the motion level before the tool.** Decide static micro-motion, layered parallax, local driving, or full generation per shot; running everything at maximum is both expensive and fragile.
10. **Accountable and reproducible.** Every asset traces back to approved facts and input versions; cost is measured per publishable unit, never per generation.

## Task routing

Decide what the user needs, then enter the matching flow. When scope is unclear and a broad rewrite is possible, confirm the goal, what must be preserved, and what is off limits.

| User intent | Route | Load |
|---|---|---|
| Only a vague idea | Phase 0-1: specs, logline, episode brief | [Short-Form Narrative](references/craft-short-form-narrative.md) |
| Write a script or restructure an episode | Phase 1, brief first | [Short-Form Narrative](references/craft-short-form-narrative.md), [episode brief](templates/episode-brief.md) |
| Convert to shots, or shots do not connect | Phase 3 | [Shot Language](references/craft-shot-language.md), `scripts/shotlist_lint.py` |
| Faces drift or characters change across episodes | Phases 2 and 4 | [Character Consistency](references/character-consistency.md) |
| Style splits, or two episodes look like two shows | Phase 2 | [Visual Style Anchor](references/craft-visual-style.md), [style guide](templates/style-guide.md) |
| It looks like a slideshow, or breaks on generation | Phase 5 | [Motion Design](references/craft-motion-design.md) |
| Lines do not fit, mouths do not match, audio sounds wrong | Phase 6 | [Dialogue, Voice, and Sound](references/craft-dialogue-voice-and-sound.md), [audio sheet](templates/audio-sheet.md) |
| Writing prompts (text-to-image, image-to-video, voice) | Any phase | [Prompt Templates](references/prompt-templates.md), `scripts/prompt_blocks.py` |
| Estimate budget or set a cadence | Phases 0 and 7 | [Cost, Capacity, and Scheduling](references/production-cost-and-schedule.md), `scripts/budget_estimate.py` |
| Delivery, multi-platform distribution, aspect conversion | Phase 7 | [Delivery Specs](references/platform-specs-and-delivery.md) |
| Review, score, find problems | Phase 7 | [Quality Evaluation](references/quality-evaluation-and-tests.md), [scorecard](templates/quality-scorecard.md) |
| Continue an existing project across sessions | Any phase | [Project and Continuity](references/project-and-continuity.md) |
| Batch production or automation | Phases 3-6 | [Automation Workflow](references/automation-workflow.md) |
| Copyright, likeness, voice, AI labelling | Throughout, and before release | [Rights, Safety, and Platforms](references/rights-safety-and-platforms.md) |
| Monetisation, analytics, contracts | After release | [Commercialization and Analytics](references/commercialization-and-analytics.md), [experiment log](templates/experiment-log.md) |
| Walk through complete examples | Reference | [Workflow Examples](references/workflow-examples.md), [Tool Catalog](references/tools-catalog.md) |

## Confirm before starting

Ask one to three questions at a time until an actionable brief is possible:

- genre, core audience, per-episode length, episode count, language;
- release region, platform, aspect, rating, content boundaries;
- existing script, character art, voice, music, trademarks, or other assets and their rights status;
- available tools, budget cap, hardware, skill level, privacy requirements, delivery deadline;
- whether this round only needs planning and prompts, or whether the current environment may generate assets directly.

With an existing project, read the project files and the most recent accepted version first. Without one, create [the project overview](templates/manga-project.md) after the user agrees, and never invent unknown fields.

## Route selection

| Route | Best for | Main trade-off |
|-------|----------|----------------|
| **A: accessible cloud** | no experience, non-English UI, fast validation | quick start; quota, privacy, commercial rights, and features change with the service |
| **B: high-quality cloud** | budget available, image or sound quality matters | more model choice; cost, regional availability, and terms must be checked item by item |
| **C: local and controllable** | GPU or technical skill, privacy and batch control | data stays local; deployment, upkeep, model licences, and hardware cost more |
| **Hybrid** | balancing quality, cost, privacy | pick per stage; must manage colour, resolution, and asset handover |

Judge tools on six capability dimensions (reference input, first/last-frame control, per-generation length and multi-shot, native audio and lip sync, aspect and resolution, hit rate and reproducibility), not on unit price alone — see [the tool catalog](references/tools-catalog.md) and the current official pages.

## The eight-phase workflow

Each phase states inputs, outputs, acceptance criteria, and the decisions the user must make. A phase that has not passed does not mark its output as accepted.

### 0. Project setup

Outputs: project overview, route, delivery specs, rights boundaries, episode-one target, and an order-of-magnitude budget.

- Confirm aspect, resolution, frame rate, subtitle safe area, and audio delivery requirements.
- Define an ID, source, version, holder, and status for every asset.
- Size it before starting: `python scripts/budget_estimate.py --shots 40 --seconds 5 --attempts 2.5 --unit-cost 0.6`.
- For long or serial work, start the character, location, prop, story, and voice continuity records.

### 1. Script and episode brief

Outputs: logline, episode brief, and a shootable script.

- Give conflict or strong emotion in the first three seconds; settle character, goal, and resistance within fifteen.
- Every scene has goal, resistance, change, and consequence. One episode delivers one clear change (A to B).
- Write lines to the speech-rate budget (about 4-5 characters per second in Mandarin) and cut them rather than speeding up.
- End on one of four hook types (suspense, reversal, emotion, choice) that the plot produces naturally.
- For serials, keep episode closure, short-term payoff, and long-term promises running together.

Use [the episode brief](templates/episode-brief.md); the criteria live in [Short-Form Narrative](references/craft-short-form-narrative.md).

### 2. Character, location, and voice bible

Outputs: identity anchors, wardrobe rules, expression and pose sheets, location anchors, a style anchor, and voice notes.

- Define characters by observable traits, not abstract adjectives.
- Separate immutable identity, per-scene looks (`LOOK-01`), and shot variables; the last must not rewrite the first two.
- Build a **reference library** (one canonical image plus five to eight angle, expression, and full-body references), reference two to four per shot, say explicitly which image governs what, and **always point back to the library instead of using the last output**.
- Fix the six style dimensions (line, colour rendering, palette, lighting, detail density, proportion and camera feel) in the style guide; only shot variables may change afterwards.
- Record voice source, licence, language, pronunciation, and performance boundaries.

Use [the character bible](templates/character-bible.md), [the style guide](templates/style-guide.md), and [the rights consent log](templates/rights-consent-log.md); method and diagnosis in [Character Consistency](references/character-consistency.md) and [Visual Style Anchor](references/craft-visual-style.md).

### 3. Storyboard and timeline

Outputs: a per-shot list and a total-duration check.

Every shot records at least: shot ID, timecode and duration, location, cast and look, composition and shot size, action and emotion, camera movement, dialogue and sound, entry continuity, exit continuity, status. Adjacent shots are checked for axis, eyeline, action joints, screen direction, wardrobe, props, and light.

- One shot expresses one freezable action node; split complex action or add an intermediate keyframe.
- Build scenes as establishing shot, then medium, then close; dialogue needs listener-reaction shots.
- In vertical framing keep characters closer, stack information vertically, and reserve top and bottom space for UI and subtitles.

Fill in [the shot list](templates/shot-list.md) and then check it mechanically:

```bash
python scripts/shotlist_lint.py shot-list.md --target-seconds 60
```

Criteria live in [Shot Language](references/craft-shot-language.md).

### 4. Static asset generation

Outputs: selected character, location, and keyframe stills, plus a record of failure reasons.

- Generate and approve character and location anchors before batch-generating shots.
- Split prompts into fixed identity, fixed style, shot variables, and negative constraints, and assemble them with the script:

```bash
python scripts/prompt_blocks.py --style-guide style-guide.md --identity identity.txt \
  --action "reaches for the mailbox" --shot-size "medium close" --camera "slow push in" \
  --negative "extra hands" --negative "text, watermark"
```

- Record model or tool, version or date, parameters, seed, reference assets, and selection reason.
- Use **region editing** for wardrobe changes and facial fixes instead of regenerating the frame.
- Never ask for a living creator's style; translate it into composition, line, colour, lighting, material, and narrative distance.

### 5. Motion clips

Outputs: shot clips, first and last frame states, and motion quality records.

- **Choose the motion level first**: static micro-motion, 2.5D layering, local driving, or full generation; only a minority of shots justify the expensive level.
- Image-to-video prompts describe action, environmental motion, camera, and time only; do not re-describe identity the source image already fixed.
- Prefer one primary action per shot, and join adjacent shots by first and last frames.
- Check flicker, face drift, anatomy, lip sync, object penetration, screen direction, and camera stability.
- Do not retry endlessly: stop at the attempt, budget, or repeated-failure cap and ask for a decision.

Criteria, the micro-motion list, parallax method, and the repair table live in [Motion Design](references/craft-motion-design.md); prompt shapes in [Prompt Templates](references/prompt-templates.md).

### 6. Voice, music, sound effects, and subtitles

Outputs: a line sheet, audio assets, subtitles, and a mixing note.

- Measure each line before setting shot length, never the other way round.
- Decide lip treatment on four levels: no requirement, prompted, local driving, repair. Anything handleable in profile or from behind does not need lip sync at all.
- Clone only your own voice or one with written consent, and never impersonate a real person.
- Music, effects, and fonts must record licence and commercial scope.
- Proof subtitles against the actual audio, including speaker, tone, and necessary accessibility notes.
- Mix for dialogue intelligibility first: voice above effects above music above ambience; normalise loudness across the piece (around -14 LUFS with true peak at or below -1 dBTP, per the platform document).

Use [the audio sheet](templates/audio-sheet.md); rules in [Dialogue, Voice, and Sound](references/craft-dialogue-voice-and-sound.md).

### 7. Assembly, quality acceptance, and release preparation

Outputs: a candidate cut, a quality scorecard, a release package, and open risks.

- Verify duration, aspect, frame rate, codec, subtitle safe area, audio-picture sync, and playback across devices.
- Check story, character, continuity, image, motion, sound, originality, rights, and AI labelling.
- Fix the master and derive platform versions; aspect conversion is re-planning, not cropping.
- A pass is not a release authorisation. Use [the release checklist](templates/release-checklist.md) and re-open the target platform's current rules before uploading.

Specs and distribution in [Delivery Specs](references/platform-specs-and-delivery.md); scoring and hard gates in [Quality Evaluation](references/quality-evaluation-and-tests.md).

## Craft baselines

These are always in force. Load the matching guide from the routing table when you need detail, examples, or a diagnosis table.

| Technique | Baseline | Deep guide |
|---|---|---|
| Episode rhythm | conflict in the first three seconds; one change per episode; a hook at every ending | [Short-Form Narrative](references/craft-short-form-narrative.md) |
| Shot language | respect the axis and eyeline; one action per shot; establish a new location first | [Shot Language](references/craft-shot-language.md) |
| Motion design | level before tool; describe action, never re-describe appearance; cap retries | [Motion Design](references/craft-motion-design.md) |
| Character consistency | one reference library as the source of truth; point back every shot; region-edit wardrobe | [Character Consistency](references/character-consistency.md) |
| Visual style | six fixed dimensions; one variable at a time; never replicate a living creator | [Visual Style Anchor](references/craft-visual-style.md) |
| Dialogue and sound | write to the speech budget; four lip levels; voice first; cloning needs consent | [Dialogue, Voice, and Sound](references/craft-dialogue-voice-and-sound.md) |
| Cost and schedule | measure per publishable unit; cap attempts, repeated failures, and spend; sample first | [Cost, Capacity, and Scheduling](references/production-cost-and-schedule.md) |
| Delivery | master first; re-plan on aspect change; re-check specs and labelling on release day | [Delivery Specs](references/platform-specs-and-delivery.md) |
| Continuity | layered source of truth; write back accepted results only; propagate every change | [Project and Continuity](references/project-and-continuity.md) |
| Rights and safety | clear likeness, voice, music, and font licences first; keep AI labels; never impersonate | [Rights, Safety, and Platforms](references/rights-safety-and-platforms.md) |

## Project state and write-back

Recommended states: `planned -> brief approved -> anchors approved -> assets in progress -> rough cut -> quality check -> author review -> accepted -> released`.

- Write only author-accepted story, look, voice, and shots into the source of truth.
- After every session update the asset ledger, continuity, versions, cost, and open questions.
- On conflict, list sources and impact rather than silently choosing one version.
- For automation or multi-person work read [Automation Workflow](references/automation-workflow.md); log runs in [the production run log](templates/production-run-log.md).

## Rights, safety, and platform boundaries

- Do not replicate protected works, a living creator's recognisable style, unlicensed characters, or trademarked packaging.
- Do not use a real person's likeness, voice, private material, or an identifiable minor without consent.
- Do not make deceptive content that could be mistaken for real events, and do not write dangerous acts as actionable instructions.
- Keep records of sources, licences, generating tools, and human edits. **Do not delete source or AI metadata written by a service.**
- AI labelling rules differ between mainland China (the labelling measures and their supporting standard), YouTube, TikTok, and others. Read [Rights, Safety, and Platforms](references/rights-safety-and-platforms.md) and re-check on the day of release.

## Scripts

Four zero-dependency Python scripts ship with the repository (standard library only), producing readable text or JSON:

```bash
# Shot-list lint: ID format, required fields, per-shot cap, total duration, entry/exit continuity, framing monotony
python scripts/shotlist_lint.py shot-list.md --target-seconds 60

# Prompt assembly and mechanical checks: identity, style, variables, negatives; flags replication requests and repeated appearance
python scripts/prompt_blocks.py --style-guide style-guide.md --identity identity.txt \
  --action "..." --shot-size "medium close" --camera "slow push in" --negative "watermark"

# Budget and capacity: cost per publishable unit plus a cost-versus-attempts sensitivity table
python scripts/budget_estimate.py --shots 40 --seconds 5 --attempts 2.5 --unit-cost 0.6 --target-seconds 180

# Repository self-check: front matter, links, bilingual mirror, Han characters in the English tree, unfinished markers, script syntax, reachability
python scripts/validate.py --warnings-as-errors
```

Scripts give **leads, not verdicts**: read the context before changing anything, and let the author decide.

## On-demand references

- Tool capabilities, six selection dimensions, official entry points: [Tool Catalog](references/tools-catalog.md)
- Episode rhythm, hooks, retention diagnosis: [Short-Form Narrative](references/craft-short-form-narrative.md)
- Shot sizes, axis, action joints, vertical storyboarding: [Shot Language](references/craft-shot-language.md)
- Motion levels, micro-motion, parallax, camera moves: [Motion Design](references/craft-motion-design.md)
- Identity anchors, reference library, drift diagnosis: [Character Consistency](references/character-consistency.md)
- Look definition, palette, cross-tool normalisation: [Visual Style Anchor](references/craft-visual-style.md)
- Line budgets, four lip levels, mixing, subtitles: [Dialogue, Voice, and Sound](references/craft-dialogue-voice-and-sound.md)
- Prompt structures for script, image, video, voice, and music: [Prompt Templates](references/prompt-templates.md)
- Delivery specs, aspect conversion, multi-platform distribution: [Delivery Specs](references/platform-specs-and-delivery.md)
- Unit cost, capacity model, scheduling gates: [Cost, Capacity, and Scheduling](references/production-cost-and-schedule.md)
- Source of truth, asset naming, versions, handover: [Project and Continuity](references/project-and-continuity.md)
- Copyright, likeness, voice, minors, AI labelling: [Rights, Safety, and Platforms](references/rights-safety-and-platforms.md)
- Batch production, retries, idempotency, human gates: [Automation Workflow](references/automation-workflow.md)
- Audience, serialisation, revenue, contracts, analytics: [Commercialization and Analytics](references/commercialization-and-analytics.md)
- Hard gates, scoring, behavioural tests: [Quality Evaluation](references/quality-evaluation-and-tests.md)
- End-to-end examples for the three routes: [Workflow Examples](references/workflow-examples.md)

## Project templates

- [Project overview](templates/manga-project.md)
- [Episode brief](templates/episode-brief.md)
- [Character bible](templates/character-bible.md)
- [Style guide](templates/style-guide.md)
- [Shot list](templates/shot-list.md)
- [Audio sheet](templates/audio-sheet.md)
- [Asset ledger](templates/asset-ledger.md)
- [Rights consent log](templates/rights-consent-log.md)
- [Production run log](templates/production-run-log.md)
- [Quality scorecard](templates/quality-scorecard.md)
- [Experiment log](templates/experiment-log.md)
- [Release checklist](templates/release-checklist.md)

## Output conventions

- Episode `E01`; shot `E01-S001`; character `CHAR-01`; look `LOOK-01`; location `LOC-01`; prop `PROP-01`; audio `AUD-001`.
- Keep prompts in code blocks, with fixed identity, fixed style, shot variables, and negative constraints labelled separately.
- Every delivery states: done, unverified, needs user action, risks, next step.
- Update only the project fields this session affected; never invent values to fill a template.
