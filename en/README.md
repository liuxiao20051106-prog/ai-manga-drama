# 🎬 AI Manga-Drama Studio - Build Your First AI Animated Short

> **In one sentence**: an "AI assistant director". You describe the story you want, and it turns the idea into an animated comic short you can publish on vertical video feeds. **No drawing, no editing software, no prior experience required.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)
[![Chinese](https://img.shields.io/badge/Lang-Chinese-red)](../README.md)
[![English](https://img.shields.io/badge/Lang-English-blue)](SKILL.md)
[![Validation](https://github.com/liuxiao20051106-prog/ai-manga-drama/actions/workflows/validate.yml/badge.svg)](../../actions/workflows/validate.yml)

---

## Contents

- [What is an AI manga drama?](#what-is-an-ai-manga-drama)
- [What does this project do for you?](#what-does-this-project-do-for-you)
- [Do I need experience?](#do-i-need-experience)
- [What do you need?](#what-do-you-need)
- [Five-minute start](#five-minute-start)
- [Eight steps to a finished piece](#eight-steps-to-a-finished-piece)
- [How to choose a tool route](#how-to-choose-a-tool-route)
- [What does it cost, and how do you work it out?](#what-does-it-cost-and-how-do-you-work-it-out)
- [Installation](#installation)
- [Bundled scripts](#bundled-scripts)
- [Repository layout](#repository-layout)
- [FAQ](#faq)
- [Maintenance and validation](#maintenance-and-validation)
- [Related projects](#related-projects)
- [Licence](#licence)

---

## What is an AI manga drama?

**AI manga drama = an AI-generated animated comic short.**

You have probably seen the format in a vertical feed:

> A 30-second to 3-minute anime-styled short with characters, dialogue, plot, and music. The art is comic-like but has small motion - wind in hair, a camera push, shifting light - so it reads as a comic that moves.

A 30-second episode might look like this:

```text
Shot 1 (4s) -> old apartment entrance, dusk light, slow downward camera move
Shot 2 (3s) -> a girl steps out, the breeze lifts her skirt
Shot 3 (3s) -> she turns to the mailbox, hopeful
Shot 4 (4s) -> close-up: the mailbox is empty, only a faded sticker
Shot 5 (4s) -> fingers brush the frame (voice-over: "forty-seven days now")
Shot 6 (5s) -> she walks out; the sunset stretches her shadow long
Shot 7 (5s) -> push in: a corner of white envelope in the door gap (hook)
```

No drawing is involved. The images come from AI tools; you make the judgement calls.

---

## What does this project do for you?

Think of yourself as the director and this Skill as your assistant director:

| It handles | You handle |
|-----------|------------|
| Expanding a one-line idea into a structured script and an episode brief | Saying what kind of story you want |
| Character design, look IDs, and a **reference library** (the foundation against face drift) | Approving the direction and picking the reference you like |
| Defining the six style dimensions, palette, and time-of-day temperature as a style anchor | Approving the look |
| Storyboarding (shot size, setup, action joints, continuity entry and exit) | Confirming or asking for changes |
| Writing precise image, image-to-video, and voice prompts | **Copy, paste into the tool, download the result** |
| Line-length budgets, lip-sync level, mix hierarchy, subtitle rules | Generating the audio with your voice tool |
| Editing steps and multi-platform delivery specs | Assembling and exporting in your editor |
| Mechanically checking the shot list, prompts, and budget with scripts | Reading the check and deciding what to change |

> The idea: the AI does the thinking work (script, shots, prompts, checks) and you do the doing work (pasting, generating, selecting). Together that is a finished episode.

---

## Do I need experience?

**No.** This project assumes you know nothing about AI tools.

| What you will use | Difficulty | Note |
|-------------------|------------|------|
| **Talking to an AI** | like chatting | say "I want to make a manga drama about X" |
| **Copying and pasting prompts** | none | the AI writes them, you paste them |
| **Pressing generate in an image or video tool** | one button | most have a usable UI |
| **Assembling clips in an editor** | drag and drop | closer to Lego than to film school |

**You do not need**: programming, drawing, animation, screenwriting, photography, or Premiere, After Effects, or Blender.

---

## What do you need?

### Minimum setup

| Item | What it is | Where |
|------|------------|-------|
| **A runtime** | an AI client that supports Skills (Claude Code, Codex, and similar) | see [Installation](#installation) |
| **An image generation account** | start with whatever is accessible in your region | entry points in [the tool catalog](references/tools-catalog.md) |
| **A video generation account** | image-to-video | same |
| **A free editor** | CapCut, DaVinci Resolve, and similar | vendor site |
| **Internet access** | - | - |

### Upgraded setup

Higher image quality and stronger character stability usually mean upgrading the image, video, or voice stage. **Prices, quotas, and availability change constantly, so always check each vendor's official page** (this project promises no price and no free tier).

> Reminder: free tiers, model names, regional availability, and commercial terms all change. Re-check official pages before committing to any long-term plan.

---

## Five-minute start

After installing, type:

```text
Help me make a manga drama.
```

It asks a few questions first rather than generating a whole season:

```text
AI: What kind of story?
You: A sweet romance - the heroine has a secret crush.

AI: How long should an episode be, and where will it be published?
You: 30 seconds to start, vertical feed.

AI: I suggest route A (accessible cloud tools) to validate the story first. Good?
You: Yes.

AI: Tell me about the heroine.
You: A university student, introverted but kind, reads in the library corner.
```

Then it walks you through brief, character and style anchors, storyboard, keyframes, motion clips, voice and subtitles, assembly, and final check.

**Keep the first episode to 15-30 seconds.** Once the pipeline works, later episodes speed up a lot, because the anchors (character, location, style) are built only once.

---

## Eight steps to a finished piece

Each step has a deeper guide; open it when you hit the specific problem.

| Step | What happens | Output | Deep guide |
|------|--------------|--------|------------|
| **0 Setup** | genre, length, platform, aspect, budget order of magnitude, rights boundaries | project overview | [Cost and scheduling](references/production-cost-and-schedule.md), [delivery specs](references/platform-specs-and-delivery.md) |
| **1 Script and brief** | logline, episode brief, shootable script | brief and script | [Short-form narrative](references/craft-short-form-narrative.md) |
| **2 Character, location, voice** | identity anchors, look IDs, reference library, style anchor, palette | character bible and style guide | [Character consistency](references/character-consistency.md), [visual style anchor](references/craft-visual-style.md) |
| **3 Storyboard** | per-shot breakdown with continuity entry and exit | shot list | [Shot language](references/craft-shot-language.md) |
| **4 Keyframes** | fixed identity, fixed style, shot variables | approved stills | [Prompt templates](references/prompt-templates.md) |
| **5 Motion** | choose the motion level, image-to-video, first/last-frame joins | shot clips | [Motion design](references/craft-motion-design.md) |
| **6 Voice and sound** | line sheet, lip level, music and effects, subtitles | audio and subtitles | [Dialogue, voice, and sound](references/craft-dialogue-voice-and-sound.md) |
| **7 Assembly and acceptance** | edit, quality scorecard, release package | candidate cut | [Quality evaluation](references/quality-evaluation-and-tests.md), [release checklist](templates/release-checklist.md) |

> Each phase's inputs, outputs, acceptance criteria, and the decisions that belong to you are written in [SKILL.md](SKILL.md).

---

## How to choose a tool route

| Route | Best for | Strength | Cost |
|-------|----------|----------|------|
| **A Accessible cloud** | no experience, fast validation | usable UI, quick start, no GPU | quality and consistency limited by the tool; quota, privacy, and commercial terms change with the service |
| **B High-quality cloud** | budget available, quality matters | more model choice, more consistency tools | higher spend; regional availability and terms must be checked item by item |
| **C Local and controllable** | GPU or technical skill, privacy and batch work | data stays local, scriptable, batchable | deployment and upkeep, model licences, hardware |
| **Hybrid** | balancing quality, cost, privacy | best tool per stage | you must manage colour, resolution, and asset handover |

**Recommended path**: validate the story on route A, then upgrade stage by stage.

Do not judge tools on unit price alone; judge them on six capability dimensions (reference input, first/last-frame control, per-generation length and multi-shot, native audio and lip sync, aspect, hit rate) - see [the tool catalog](references/tools-catalog.md).

---

## What does it cost, and how do you work it out?

**This project lists no prices.** Prices, free tiers, and model names change every few weeks, and hardcoding them would simply mislead you.

What actually matters:

```text
cost per publishable unit = (credits + subscriptions + power + labour + licences) / usable outputs
```

The denominator is the point: count the failures. If a shot needed four generations to yield one keeper, all four are charged to that keeper.

The repository ships an estimator so you can size it before committing:

```bash
python scripts/budget_estimate.py --shots 40 --seconds 5 --attempts 2.5 --unit-cost 0.6 --target-seconds 180
```

It reports cost per publishable unit and a cost-versus-attempts sensitivity table, which answers "spend on a better tool, or accept more retries". Method: [Cost, capacity, and scheduling](references/production-cost-and-schedule.md).

---

## Installation

### Prerequisite

An AI client that supports Skills (Claude Code, Codex, and similar).

### Option 1: clone into the skills directory

Claude Code:

```bash
git clone https://github.com/liuxiao20051106-prog/ai-manga-drama.git ~/.claude/skills/ai-manga-drama
```

Codex:

```bash
git clone https://github.com/liuxiao20051106-prog/ai-manga-drama.git ~/.codex/skills/ai-manga-drama
```

Windows PowerShell:

```powershell
git clone https://github.com/liuxiao20051106-prog/ai-manga-drama.git "$env:USERPROFILE\.claude\skills\ai-manga-drama"
```

### Option 2: as a system prompt

1. Open [SKILL.md](SKILL.md) and remove the opening front matter block.
2. Paste the body into your platform's system prompt or custom instructions.
3. Start chatting, and attach the relevant file from `references/` when a specialist topic comes up.

### Option 3: download the ZIP

Extract into the skills directory, keeping the folder name `ai-manga-drama`.

### If the target directory already exists

Do not overwrite it. Check for local changes first:

```powershell
git -C "$env:USERPROFILE\.claude\skills\ai-manga-drama" status --short
git -C "$env:USERPROFILE\.claude\skills\ai-manga-drama" pull --ff-only
```

Back up or merge when there are local changes; never force-pull, reset, or delete the directory.

### Chinese entry

The Chinese version uses the separate name `ai-manga-drama`, so both can coexist: [../SKILL.md](../SKILL.md)

---

## Bundled scripts

Four zero-dependency Python scripts (standard library only), runnable from a terminal:

```bash
# 1. Shot-list lint: ID format, required fields, per-shot cap, total duration, entry/exit continuity, framing monotony
python scripts/shotlist_lint.py shot-list.md --target-seconds 60

# 2. Prompt assembly and checks: identity, style, variables, negatives
#    It also flags two common mistakes - asking for a recognisable creator, and re-describing appearance in shot variables
python scripts/prompt_blocks.py --style-guide style-guide.md --identity identity.txt \
  --action "reaches for the mailbox" --shot-size "medium close" --camera "slow push in" \
  --negative "extra hands"

# 3. Budget and capacity: cost per publishable unit plus a sensitivity table
python scripts/budget_estimate.py --shots 40 --seconds 5 --attempts 2.5 --unit-cost 0.6

# 4. Repository self-check: front matter, links, bilingual mirror, Han characters in the English tree, unfinished markers, script syntax, reachability
python scripts/validate.py --warnings-as-errors

# Unit tests for the scripts
python -m unittest discover -s tests
```

Scripts give **leads, not verdicts**: read the context before changing anything.

---

## Repository layout

```text
ai-manga-drama/
├── SKILL.md                       <- Chinese entry, with the task routing table and eight phases
├── README.md                      <- Chinese README
├── CHANGELOG.md                   <- Change log
├── LICENSE                        <- MIT
│
├── references/                    <- 16 specialist guides, loaded on demand
│   ├── craft-short-form-narrative.md   episode rhythm, hooks, retention diagnosis
│   ├── craft-shot-language.md          shot sizes, axis, action joints, vertical storyboarding
│   ├── craft-motion-design.md          motion levels, micro-motion, parallax, camera moves
│   ├── craft-visual-style.md           six style dimensions, palette, cross-tool normalisation
│   ├── craft-dialogue-voice-and-sound.md  line budgets, four lip levels, mixing, subtitles
│   ├── character-consistency.md        reference-library workflow and drift diagnosis
│   ├── prompt-templates.md             prompt shapes for script, image, video, voice, music
│   ├── platform-specs-and-delivery.md  delivery specs, aspect conversion, distribution
│   ├── production-cost-and-schedule.md unit cost, capacity model, scheduling gates
│   ├── tools-catalog.md                capability dimensions and official entry points
│   ├── project-and-continuity.md       source of truth, naming, versions, handover
│   ├── workflow-examples.md            end-to-end examples for the three routes
│   ├── automation-workflow.md          batch, retries, idempotency, human gates
│   ├── rights-safety-and-platforms.md  copyright, likeness, voice, AI labelling
│   ├── commercialization-and-analytics.md  audience, serialisation, contracts, analytics
│   └── quality-evaluation-and-tests.md hard gates, scoring, behavioural tests
│
├── templates/                     <- 12 copy-ready templates
├── scripts/                       <- 4 zero-dependency scripts
├── tests/                         <- unit tests for the scripts
├── .github/workflows/validate.yml <- validation and tests on push and pull request
│
└── en/                            <- full English tree: 16 guides, 12 templates, SKILL.md, README.md
```

---

## FAQ

### Can I really do this without drawing?

Yes. Images come from AI tools; you supply text and references. The text is written for you as fixed identity, fixed style, shot variables, and negative constraints.

### My character keeps changing faces. What now?

That is the hardest technical problem in this format. **The answer is not a longer description - it is a reference library that every shot points back to**:

1. Build one clean frontal canonical image (even light, neutral expression, long edge at least 1024 px).
2. Generate five to eight angle, expression, and full-body references from it, and approve each one.
3. Reference two to four per shot and say which image governs the face and which governs the wardrobe.
4. **Never use a past output as the reference for the next shot** - chaining compounds drift.

See [Character consistency](references/character-consistency.md).

### How long does an episode take, and how often should I publish?

Derive the cadence from real capacity rather than declaring a schedule and absorbing the pain. The estimator gives unit cost, and [Cost, capacity, and scheduling](references/production-cost-and-schedule.md) describes the sample, small-batch, and volume gates plus scheduling buffers.

Roughly: the first three episodes are the most expensive because anchors must be built, and later episodes drop noticeably. **Never economise on the anchor stage** - saving an hour there costs two hours per episode afterwards.

### Can I publish it, or make money from it?

Yes, after three checks:

- **Rights**: original or licensed script; licences for music, fonts, voice, and likeness; no unlicensed material.
- **Labelling**: AI-generated content published in mainland China must carry explicit and implicit labels under the applicable measures and their supporting standard; overseas platforms differ, so re-check on release day. **Never delete labels or metadata written by a service.**
- **Truthfulness**: no impersonation of real people, and no deceptive content mistakable for real events.

Paths, metrics, and contract points: [Commercialization and analytics](references/commercialization-and-analytics.md). This project **promises no revenue**.

### Can I do it on a phone?

Most of route A works on mobile (image and video tools, editing apps), but a desktop is far more efficient for shot lists and asset management.

### Other languages?

Yes. Treat dubbing and subtitles as separate decisions - a common pattern is native-language dubbing with original or bilingual subtitles. Leave on-screen text sparse during generation so it can be laid out per language in post.

### How is this different from just asking an AI to make a manga drama?

Asking directly can help, but the key steps get skipped: reference libraries, shot continuity, motion-level choice, line-length budgets, lip-sync strategy, delivery specs, and AI labelling. This project turns those into a workflow with checklists and four mechanical checks.

### Do the scripts make creative decisions?

No. They only check mechanics - missing fields, mismatched durations, broken links, missing mirror files. **Creative calls, selection, style judgement, and release are yours.**

---

## Maintenance and validation

The repository ships a validator covering UTF-8, front matter, relative links, bilingual mirror completeness, Han characters in the English tree, unfinished markers, script syntax, and whether every guide is reachable from the entry file:

```bash
python -X utf8 scripts/validate.py --warnings-as-errors
```

GitHub Actions runs the same validation plus the unit tests on every push and pull request. Maintainers should still run the [behavioural tests](references/quality-evaluation-and-tests.md) by hand and re-open official documentation for tools and platform rules before release.

See [CHANGELOG.md](../CHANGELOG.md) for the change history.

---

## Related projects

- [UllrAI/CineGen-ShortDrama](https://github.com/UllrAI/CineGen-ShortDrama) - open-source AI director for comics, anime, and short drama
- [AniME (SIGGRAPH Asia 2025)](https://dl.acm.org/doi/10.1145/3757374.3771455) - multi-agent animation generation paper (seven-agent architecture)
- [BigBanana-AI-Director](https://github.com/shuyu-labs/BigBanana-AI-Director) - industrial project-season-episode pipeline
- [Yutarop/comic-generator](https://github.com/Yutarop/comic-generator) - one sentence to a full comic (MIT)
- [Ran-Chou/moyin-creator](https://github.com/Ran-Chou/moyin-creator) - six-layer identity anchoring system

---

## Licence

MIT Licence - see [LICENSE](../LICENSE).

This project provides a creative and production risk-checking framework. It does **not** replace legal advice for a specific region, contract, or release scenario.
