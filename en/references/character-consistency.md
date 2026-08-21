# Character and Visual Continuity

Load when characters cross shots, episodes, wardrobe states, group scenes, or multiple generation tools. The goal is verifiable continuity, not a promised percentage.

## Identity anchors

Use [the character bible](../templates/character-bible.md) to separate:

1. **Immutable identity:** face structure, feature proportions, core hair silhouette, body, signature item, and base palette.
2. **State:** wardrobe, hair variation, injury, dirt, props, and age phase, identified by `LOOK-01` and similar IDs.
3. **Shot variables:** expression, pose, composition, light, and action; these must not rewrite the first two layers.

Approve a reference pack before batch work: front, sides, back, full-body proportion, key expressions, wardrobe details, and palette.

## Strategy matrix

| Strategy | Best for | Check |
|----------|----------|-------|
| Fixed description + reference | Baseline for all routes | Same identity block and approved reference in every shot |
| Multi-reference/character feature | Supporting cloud tools | Current feature, weight, privacy, and commercial terms |
| Fixed seed | Reproduction and diagnosis in one model | No guarantee across models or complex poses |
| Image adapter/pose control | Local node workflows | Control identity, pose, and depth separately |
| Character LoRA/fine-tune | Long serials | Training rights, diversity, base-model license, overfitting |
| Keyframe + first/last frame | Motion shots | Lock entry and exit poses before intermediate motion |

Do not treat marketing feature names as stable interfaces. Read [the tool catalog](tools-catalog.md) and current documentation.

## Order of operations

Approve single-character identity; test angles, expressions, and framing; test wardrobe and location light; then attempt groups, occlusion, and complex action; animate only approved stills.

Change one variable at a time and record failures. Check character, space, action, camera, and voice continuity between every adjacent shot.

| Symptom | First check | Smallest fix |
|---------|-------------|--------------|
| Face drift | Reference approval and identity-block changes | Reduce variables; add side/expression references |
| Wardrobe color drift | Look ID and palette binding | Write explicit `LOOK-ID` and color definition |
| Two people merge | Distinct descriptions and positions | Lock separately; specify left/right and spacing |
| Anatomy failure | Too much motion or occlusion | Split the shot or add an intermediate pose |
| Cross-tool mismatch | Color, size, sharpness, denoise | Normalize masters and minimize tool switching |

For real people, voices, or protected characters, also read [rights and safety](rights-safety-and-platforms.md).
