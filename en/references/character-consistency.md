# Character and Visual Continuity

Load when characters cross shots, episodes, wardrobe states, group scenes, or multiple generation tools. The goal is verifiable continuity, not a promised percentage.

> Related: overall look and palette in [Visual Style Anchor](craft-visual-style.md); shot-to-shot joins in [Shot Language](craft-shot-language.md); rights boundaries in [Rights, Safety, and Platforms](rights-safety-and-platforms.md).

## Identity anchors

Use [the character bible](../templates/character-bible.md) to separate three layers:

1. **Immutable identity:** face structure, feature proportions, core hair silhouette, body, signature item, and base palette.
2. **State:** wardrobe, hair variation, injury, dirt, props, and age phase, identified by `LOOK-01` and similar IDs.
3. **Shot variables:** expression, pose, composition, light, and action; these must not rewrite the first two layers.

Approve a reference pack before batch work: front, sides, back, full-body proportion, key expressions, wardrobe details, and palette.

## The reference-library workflow (the most reliable default)

Current models accept **multiple image references**, so the answer to drift is not a longer description — it is **a reference library that every shot points back to**:

1. **Build one canonical image**: frontal, evenly lit, neutral expression, clean background, long edge at least 1024 px. This is the single source of identity.
2. **Expand into a sheet**: using the canonical image as reference, generate front, three-quarter left and right, profile, smiling close-up, and full-body proportion — 5 to 8 images, each approved by a human.
3. **Change wardrobe by editing, not regenerating**: for clothing or prop changes use **region editing** (only the target area changes; face and hair stay), not a fresh roll.
4. **Reference 2-4 images per shot**: pick the angles and expressions the shot needs, and state **explicitly which image governs what** ("image 1 for face and hair, image 4 for body proportion and wardrobe").
5. **Always point back to the library**: never use "the last output I liked" to generate the next shot.

**The rule most often missed**: chaining compounds error. If shot one is 95% on model, shot two is 95% of shot one, and so on, the character stops looking like the character quickly. **Reference the original library every time** and drift stays bounded.

## Strategy matrix

| Strategy | Best for | Check |
|----------|----------|-------|
| Fixed description + reference | Baseline for all routes | Same identity block and approved reference in every shot |
| Multi-reference/character feature | Cloud tools that accept multiple references | How many references, at what weight, and the commercial terms |
| Region editing (local change only) | Wardrobe swaps, facial fixes, prop replacement | Edit mask precision, then verify the face is unchanged |
| Fixed seed | Reproduction and diagnosis in one model | No guarantee across models or complex poses |
| Image adapter/pose control | Local node workflows | Control identity, pose, and depth separately and ablate |
| Character LoRA/fine-tune | Very long serials, very high volume | Training rights, diversity, base-model licence |
| Reference-to-video | Moving from approved stills into motion | Attach the same references into the video node |

Do not treat marketing feature names as stable interfaces. Read [the tool catalog](tools-catalog.md) and current documentation.

## Order of operations

1. Lock single-character identity and base styling.
2. Verify angles, expressions, and shot sizes.
3. Verify location light and wardrobe states.
4. Only then test two people in frame, occlusion, and complex action.
5. Animate only after the still keyframes pass.

Change one variable at a time and record failure types and effective parameters.

## Four causes of drift (ordered by frequency)

| Cause | Symptom | Handling |
|-------|---------|----------|
| **The description quietly changed wording between shots** | early shots fine, later ones drift | extract identity and style into fixed text blocks and paste verbatim |
| **Wrong or dirty reference image** | one shot is clearly off; age or features shift | use the matching angle from the library; drop low-quality or noisy references |
| **Chain drift (using outputs as references)** | everything softens; faces converge on an average | point back to the original library |
| **Model, tool, or parameters switched mid-project** | one episode looks like two shows | keep one model per episode; if you must switch, rerun affected shots and normalise colour |

Diagnostic order: **wording first, then references, then the chain, and only last the model.**

## Continuity checks

- **People**: face, hair, body, age, wardrobe ID, injuries, signature items.
- **Space**: blocking, screen direction, eyeline, doors, windows, key object layout.
- **Action**: does the hand, foot, prop, and direction carry into the next shot?
- **Camera**: light direction, colour temperature, lens impression, depth of field, aspect.
- **Voice**: timbre, accent, pronunciation, emotional intensity, position in the mix.

## How to verify (not "it looks about right")

1. **Same-angle comparison**: pull 3-5 frontal frames of the same character from one episode and view them side by side. Check face silhouette, eye spacing, hairline, and signature items.
2. **Cross-episode comparison**: one frame from the previous episode against one from this one, same angle.
3. **Signature items get their own column**: earrings, scars, rings, hair ornaments — these vanish fastest when wardrobe changes.
4. **Record evidence**: mark failing shots `rejected` in [the asset ledger](../templates/asset-ledger.md) with the reason (face drift, wardrobe error, missing prop) so you can see which failure class dominates.
5. **Do not let an average hide it**: character breakage is a hard gate and does not pass because other dimensions scored well. See [Quality Evaluation and Tests](quality-evaluation-and-tests.md).

## Failure diagnosis

| Symptom | First check | Smallest fix |
|---------|-------------|--------------|
| Face drift | reference approval, identity-block changes, chain drift | reduce shot variables, add side/expression references, point back to the library |
| Wardrobe colour drift | look ID and palette binding | write explicit `LOOK-ID` and colour definition |
| Two people merge | distinct descriptions and positions | lock separately; specify left/right and spacing; split the shot if needed |
| Anatomy failure | too much motion or occlusion | split the shot, add an intermediate keyframe, or use pose control |
| Cross-tool mismatch | colour, size, sharpness, denoise chain | normalise master and post settings; switch tools less |
| Profile or back view breaks | the library lacks that angle | generate and approve that angle first |
| Signature item lost after a costume change | the change used full-frame regeneration | switch to region editing and change only the clothing |

For real people, voices, or protected characters, also read [Rights, Safety, and Platforms](rights-safety-and-platforms.md).
