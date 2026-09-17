# Shot Language and Storyboarding

Load when converting a script into shots, diagnosing "the image is flat", "the axis jumped", or "shots do not connect", or when deciding vertical-framing strategy. SKILL.md carries the baseline (adjacent shots check axis, eyeline, action joints, screen direction, wardrobe, props, light); this is the full expansion.

> Related: what each shot should move in [Motion Design](craft-motion-design.md); look and palette in [Visual Style Anchor](craft-visual-style.md); the shot-list fields are machine-checkable with `scripts/shotlist_lint.py`.

## I. Five shot sizes and their jobs

| Size | Holds | Typical use | Vertical adjustment |
|------|-------|-------------|---------------------|
| Extreme wide | environment, scale, isolation | opening, ending, time passage | reads empty in vertical; prefer a high angle instead |
| Wide | full body plus spatial relations | establishing, action | characters must fill more of the frame |
| Medium | waist up | the dialogue workhorse | the "standard shot" of vertical |
| Medium close | chest up | emotion, key lines | highest frequency in vertical |
| Close-up | face, hands, props | emotional peaks, information beats | vertical's advantage — use it |

**Principle**: the stronger the emotion, the tighter the shot. Every episode should include at least one shot tighter than the norm to deliver its emotional peak.

## II. Camera position and angle

- **Eye level**: neutral, objective; the dialogue default.
- **High angle**: shrinks the character; weakness, being watched, loneliness.
- **Low angle**: enlarges pressure; dominance, threat.
- **Over the shoulder**: puts the viewer inside the conversation.
- **Point of view**: the viewer enters the character's eyes; you lose that character's own face — most effective for a key reveal.

**Change setups to serve emotion, not for energy.** Three setups inside one calm conversation reads as unease. If you want calm, do not cut.

## III. The axis and screen direction (the most fatal rule)

- **180-degree axis**: keep every setup on the same side of two speakers. Crossing it makes the viewer think they swapped places.
- **Eyeline match**: if A looks screen-right, B looks screen-left. Reversed, the viewer reads them as not looking at each other.
- **Screen direction**: someone moving left continues left in the next shot; a sudden reversal reads as "they turned back".
- **When you must cross the axis**: do it through a neutral shot or a visible camera move so the viewer sees the space change.
- **Establishing shot**: open a new location with a shot that explains the space (wide or high angle), so later close-ups do not lose the viewer.

## IV. Action joints (match on action)

Carrying an action across the cut is the cheapest way to stitch two generated clips together:

- The first half of opening a door in shot A, stepping through in shot B.
- Half of raising a hand in shot A, landing it on a shoulder in shot B.

**With generation tools**: use shot A's **ending frame** as shot B's **starting frame** (first/last-frame chaining), and record "entry state" and "exit state" for every shot in the shot list, so the join is invisible.

## V. One action per shot

Generative video fails most when one shot tries to hold two actions (face drift, extra hands, object penetration). Split at the storyboard stage:

- One shot expresses one **freezable action node** ("turns her head" is one; "turns her head and stands up to grab the bag" is two).
- Split complex action into 2-3 shots, or add an intermediate keyframe.
- Avoid putting numbers, text, or intricate hand gestures into generation prompts — lay them out in post.

## VI. Building a scene in three steps

Inside one location, guide the viewer with shot size:

```
establishing (who is where) -> medium (what happens) -> close (what it feels like)
                                  \-> reverse (the other person reacts) -> back to close
```

Any dialogue passage needs **speaker -> listener reaction** at least once. Shooting only the speaker makes it look like a meeting recording.

## VII. Omission and transitions

- **Jump cut**: same setup, skip the middle; expresses time passing or repetition. Fast; suits comedy and anxiety.
- **Action-joint transition**: the smoothest; see section IV.
- **Wipe by occlusion**: cut while a character or object fills the frame; hides discontinuity. **The most practical transition for generated clips.**
- **Sound first**: the next scene's audio enters before its picture; the join feels tighter.
- **Dissolve or fade**: expresses time jumps or emotional closure; use sparingly in short form.
- **Graphic match**: round moon -> round lamp; shape carries the cut.

Principle: if an action can carry the join, do not use an effect. Fewer transitions make a piece feel more solid.

## VIII. Vertical versus horizontal storyboarding

| Dimension | Vertical 9:16 | Horizontal 16:9 |
|-----------|---------------|-----------------|
| Dominant sizes | medium, medium close, close | wide and medium |
| Side-by-side people | at most 2, staggered in depth | 3 can sit side by side |
| Spatial exposition | vertical layering (foreground/mid/background) | horizontal spread |
| Movement | push in, follow, slight handheld | lateral moves, pans, crane |
| Subtitle space | reserve roughly the lower 20% | reserve roughly the lower 10% |

For multiple platforms **do not crop**: converting vertical to horizontal means re-planning composition (add environment, rebuild title cards, re-frame characters), or faces get cut in half.

## IX. What makes a shot list shootable

Every shot must answer:

1. **Who is where in frame** (left/right, front/back, facing, eyeline)
2. **The one action of this shot** (a single freezable instant)
3. **Shot size and setup** (medium close / eye level / over the shoulder)
4. **Entry state** (what it carries from the previous shot)
5. **Exit state** (what the next shot must connect to)
6. **Duration** and **sound cue** (dialogue, effect, music entry)

Shots with missing fields always come back as rework. Fill [the shot list](../templates/shot-list.md) and check it mechanically:

```bash
python scripts/shotlist_lint.py shot-list.md --target-seconds 60
```

## X. Storyboard checklist

- [ ] Axis and eyeline consistent across adjacent shots?
- [ ] Screen direction continuous when a character enters or exits frame?
- [ ] Every new location opens with an establishing shot?
- [ ] One primary action per shot?
- [ ] Do adjacent entry/exit states connect (ideally by first/last frame)?
- [ ] At least one tighter shot delivering the episode's emotional peak?
- [ ] Dialogue has listener-reaction shots?
- [ ] Are transitions few and natural?
- [ ] In vertical framing, are characters close enough and is information stacked vertically?
