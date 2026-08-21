---
name: ai-manga-drama-en
description: End-to-end AI motion-comic and manga-drama production for scripting, storyboards, character and asset continuity, image/video/audio prompts, review, release preparation, automation, and commercialization. Trigger for requests to create or improve an AI motion comic, animated comic short, manga video, or episodic AI drama.
---

# AI Manga Drama Production

Turn a creative concept into a reviewable, producible, and maintainable motion-comic project. Depending on available tools and authorization, generate media directly or deliver prompts and operating instructions for external services. Never describe a prompt package as a finished asset.

## Core principles

1. **Story and performance precede tools.** Model names do not replace narrative decisions.
2. **The author owns key choices.** Theme, character outcomes, visual direction, accepted versions, and release require human approval.
3. **Continuity is a source-of-truth problem.** Track identity, wardrobe, props, space, lighting, eyelines, voices, and chronology.
4. **Deliver in reviewable units.** Prove one short episode or sample before scaling a season.
5. **Choose tools dynamically.** Consider territory, budget, hardware, privacy, rights, and quality; prices, quotas, and versions are not durable facts.
6. **Protect source material.** Read before editing and do not overwrite, delete, bulk-rewrite, or upload unpublished assets without authorization.
7. **Handle rights and transparency early.** Verify originality, likeness, voice, music, fonts, asset licenses, and AI-label requirements.
8. **Authorize external actions separately.** Uploading, publishing, purchasing, subscribing, signing, contacting third parties, or training on a real person requires explicit approval.

## Establish the brief

Ask one to three high-impact questions at a time until the production brief is actionable:

- format, audience, duration, episode count, language, and story promise;
- release territory, platform, aspect ratio, rating, and content boundaries;
- existing scripts, character art, voices, music, marks, and their rights status;
- available tools, budget ceiling, hardware, skill level, privacy needs, and deadline;
- whether the user wants planning/prompts only or authorizes direct use of available media tools.

For an existing project, load the project record and latest accepted version first. For a new project, create [the project overview](templates/manga-project.md) only with permission and leave unknown fields blank.

## Production routes

| Route | Best for | Tradeoff |
|------|----------|----------|
| **A: accessible cloud** | Beginners and fast validation | Easy access; quotas, privacy, commercial rights, and features change |
| **B: premium cloud** | Higher visual or audio quality | More options; cost, region availability, and terms require current checks |
| **C: local control** | Technical users, privacy, and batch control | Local data; greater setup, maintenance, hardware, and model-license burden |
| **Hybrid** | Balancing quality, cost, and privacy | Best tool per stage; requires careful color, resolution, and asset handoff |

Read [the tool catalog](references/tools-catalog.md) and verify current official pages before recommending a service.

## Eight-stage workflow

For each stage, state inputs, outputs, acceptance criteria, and human decisions. A failed review must not be marked accepted.

### 0. Initialize

Deliver a project overview, production route, delivery specification, rights boundaries, and first-episode goal. Define aspect ratio, resolution, frame rate, subtitle safe area, audio deliverables, asset IDs, ownership, and status.

### 1. Script and episode brief

Deliver a logline, [episode brief](templates/episode-brief.md), and filmable script. Establish character, change, or tension early without imposing a universal three-second hook. Each scene has a goal, resistance, change, and consequence. For serials, balance immediate reward, episode turn, and long promise.

Use [prompt templates](references/prompt-templates.md) when detailed structures are needed.

### 2. Character, location, and voice bibles

Deliver identity anchors, wardrobe rules, expression/pose references, location anchors, and voice direction. Separate immutable identity from scene-dependent states. Record voice source, permission, language, pronunciation, and performance boundaries.

Read [character consistency](references/character-consistency.md); use [the character bible](templates/character-bible.md) and [rights/consent log](templates/rights-consent-log.md).

### 3. Storyboard and timeline

Deliver a shot list with shot ID, location, characters, composition, action, camera movement, dialogue/sound, duration, and continuity entry/exit. Check screen direction, eyelines, action matches, wardrobe, props, and lighting between shots.

Use [the shot-list template](templates/shot-list.md).

### 4. Still assets

Approve character and location anchors before batch generation. Split prompts into identity lock, style lock, and shot variables. Record tool/model, check date or version, parameters, seed, references, and selection reason. Translate named living-artist imitation into high-level composition, line, color, light, texture, and narrative traits.

### 5. Motion clips

Image-to-video prompts primarily describe motion, camera, and temporal change. Prefer one main action per shot and split complex movement. Review flicker, identity drift, anatomy, lip sync, collisions, movement direction, and camera stability. Stop after the agreed retry, time, or cost limit.

### 6. Voice, music, sound, and captions

Use cloned speech only for the user’s own voice or a voice backed by written authorization. Record licenses for music, sound effects, and fonts. Caption the actual audio and include speakers and useful accessibility cues. Mix for intelligible dialogue; do not replace listening and loudness checks with a universal decibel offset.

### 7. Edit, quality review, and release preparation

Deliver a candidate master, quality scorecard, release package, and unresolved risks. Validate duration, aspect ratio, frame rate, codec, subtitle safe area, sync, and playback. A passing review does not authorize upload. Use [the release checklist](templates/release-checklist.md) and reopen current platform rules immediately before release.

## State and handoff

Recommended states: `unplanned → brief approved → asset production → rough cut → quality review → author review → accepted → published`.

- Commit only accepted story, design, voice, and shot facts to the source of truth.
- Update assets, continuity, versions, cost, and open decisions after each run.
- Surface conflicting sources and impact; do not silently choose one.
- For batch or multi-contributor work, read [the automation workflow](references/automation-workflow.md).

## Rights, safety, and platform boundaries

- Do not reproduce protected works, recognizable living-creator styles, unauthorized characters, or trade dress.
- Do not use a real person’s likeness, voice, private material, or an identifiable minor without appropriate permission.
- Do not create deceptive media likely to be mistaken for a real event or operational instructions for harm.
- Preserve source, license, generation-tool, and human-edit records; do not strip required provenance or AI metadata.
- AI labeling and monetization rules vary by territory and platform. Read [rights, safety, and platform rules](references/rights-safety-and-platforms.md) and recheck them on the release date.

## Load references as needed

- Tool capabilities and official entry points: [Tool Catalog](references/tools-catalog.md)
- Identity and shot continuity: [Character Consistency](references/character-consistency.md)
- Script, image, video, voice, and music prompt structures: [Prompt Templates](references/prompt-templates.md)
- End-to-end examples: [Workflow Examples](references/workflow-examples.md)
- Source of truth, naming, versions, and handoff: [Project and Continuity](references/project-and-continuity.md)
- Copyright, likeness, voice, minors, and AI labels: [Rights, Safety, and Platforms](references/rights-safety-and-platforms.md)
- Batch production, retries, idempotency, and human gates: [Automation Workflow](references/automation-workflow.md)
- Audience, serialization, revenue, contracts, and metrics: [Commercialization and Analytics](references/commercialization-and-analytics.md)
- Hard gates, evidence scoring, and behavioral tests: [Quality Evaluation and Tests](references/quality-evaluation-and-tests.md)

## Templates

- [Project Overview](templates/manga-project.md)
- [Episode Brief](templates/episode-brief.md)
- [Character Bible](templates/character-bible.md)
- [Shot List](templates/shot-list.md)
- [Asset Ledger](templates/asset-ledger.md)
- [Rights and Consent Log](templates/rights-consent-log.md)
- [Production Run Log](templates/production-run-log.md)
- [Quality Scorecard](templates/quality-scorecard.md)
- [Release Checklist](templates/release-checklist.md)

## Output conventions

- Episode: `E01`; shot: `E01-S001`; character: `CHAR-01`; location: `LOC-01`; audio: `AUD-001`.
- Put prompts in code blocks and separate fixed identity/style blocks from shot variables and negative constraints.
- Every handoff states what is complete, unverified, user-operated, risky, and next.
- Update only project fields affected by the task; never invent values to fill a template.
