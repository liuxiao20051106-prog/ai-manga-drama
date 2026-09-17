# Visual Style Anchor

Load when setting a look, holding it across shots and tools, or diagnosing "the style splits" or "one episode looks like two different shows". SKILL.md carries the baseline (never imitate a living creator or a specific work; translate the request into high-level visual traits); this file makes that practical.

> Related: character and wardrobe continuity in [Character Consistency](character-consistency.md); scene-anchor prompt structure in [Prompt Templates](prompt-templates.md); the fill-in template is [the style guide](../templates/style-guide.md).

## I. A style must be defined before it can be reproduced

"Anime style" or "ink-wash-ish" tells a model nothing. Break the look into six observable dimensions and give each an explicit value:

| Dimension | Example values |
|-----------|----------------|
| **Line** | weight (fine line / heavy outline) / colour (black / dark brown / coloured) / broken strokes |
| **Colour rendering** | flat / cel / painterly / watercolour bleed / screentone; hard or soft shadow edges |
| **Palette** | saturation (muted grey / bright saturated) / dominant cast (warm orange / cool blue / ink green) |
| **Lighting** | number and direction of sources (single backlight / rim light) / bloom, volumetric shafts, rim glow |
| **Detail density** | background information (minimal white space / dense) / materials (cloth folds, metal specular) |
| **Proportion and camera feel** | head-to-body ratio (3-head / 7-head) / perspective strength / framing habits |

Write that table into [the style guide](../templates/style-guide.md) and reference the same values in every prompt. **Style drift usually starts when the description quietly changes wording between shots.**

## II. The three-piece style anchor

Carrying a look across shots, tools, and sessions needs only three things:

1. **Style block text** (60-120 words): the six dimensions above compressed into one fixed paragraph, pasted verbatim every generation.
2. **Palette**: one or two dominant colours, two or three secondary, one accent, written as hex or exact colour names; plus a **time-of-day temperature table** (dawn / noon / dusk / night / rain) so the same location keeps a consistent cast across shots.
3. **Reference image library**: two to four approved images that represent the overall look (not character sheets — **scene plates**).

**Rule**: the style block is fixed like the identity block; only the shot-variable section may change. To adjust the style, version it (`STYLE-v01 -> v02`) and update every unmade shot — never patch a single shot in isolation.

## III. How to choose reference images

Reference quality sets output quality:

- **Clean**: simple background, no harsh shadows, no clutter, no text or watermark.
- **Evenly lit**: frontal or soft side light; avoid crushed blacks and blown highlights.
- **Sharp**: long edge at least 1024 px, higher is more stable; never frame-grab from a compressed final video.
- **Neutral pose**: front-facing, natural expression, no extreme angles.
- **Consistent**: references must not contradict each other (three images, three hairstyles, equals a drift generator).

**Never use "the last output I liked" as the reference for the next shot** — errors compound down the chain. Always point back to the **original reference library**.

## IV. Unifying across tools and stages

The more tools, the more you need a normalisation step:

| Stage | Normalisation |
|-------|---------------|
| Image generation | same style block and reference library; keep one episode inside one model where possible |
| Mixed models | convert to one colour space and resolution before post; record each shot's source model |
| Grading | apply one master LUT or filter; write per-location temperature, contrast, and sharpness into the spec |
| Resolution and sharpness | pick one delivery master resolution; scale and sharpen everything to it so nothing looks soft next to something crisp |
| Denoise and compression | use one encode setting; avoid stacking multiple lossy passes from different tools |

**Change one variable at a time.** If the model, prompt, references, and seed all change at once, you cannot attribute the result.

## V. Style-drift diagnosis

| Symptom | Check first | Smallest fix |
|---------|-------------|--------------|
| One shot looks different | was the style block reworded | restore the original style block verbatim |
| Everything gets softer over time | using outputs as references (chain drift) | point back to the original library |
| Two episodes look like two shows | model or tool was switched | rerun the affected shots with the same anchor, or normalise in grading |
| Colour suddenly warmer or cooler | inconsistent reference or time-of-day temperature | check each shot against the temperature table |
| Line weight varies | the line dimension was missing from the style block | state it explicitly |
| Detail density swings | shot variables are overloaded | move detail into the style block and leave only action and framing as variables |

## VI. Boundary: high-level traits yes, replication no

**Allowed**: describing a medium (cel animation, watercolour, woodblock, ink wash), compositional rules, colour relationships, lighting logic, material rendering, proportion, narrative distance.

**Not allowed**: naming a living creator's signature style or a specific work's recognisable character design or imagery. That is both a rights risk and the fastest way to make the work undistinctive.

When you want to move toward a direction, translate the reference into the six dimensions above — **the translation is the creative work.**

## VII. Checklist

- [ ] All six dimensions have explicit values, written into the style guide?
- [ ] Every generation used the same style block text?
- [ ] Palette and time-of-day temperature table defined and checked shot to shot?
- [ ] Is the reference library clean, sharp, mutually consistent, and never replaced by past outputs?
- [ ] When mixing tools, were colour, resolution, and sharpness normalised?
- [ ] Was any style change made as a version bump rather than a one-shot patch?
