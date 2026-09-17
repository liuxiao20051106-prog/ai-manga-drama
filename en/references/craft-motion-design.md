# Motion Design

Load when deciding how a still should move, diagnosing "this looks like a slideshow" or "it breaks the moment I generate", or planning an image-to-video strategy. SKILL.md carries the baseline (one primary action per shot; check flicker, face drift, anatomy, penetration, direction; do not retry endlessly); this is the full expansion.

> Related: how shots are split in [Shot Language](craft-shot-language.md); image-to-video prompt structure in [Prompt Templates](prompt-templates.md); look continuity in [Visual Style Anchor](craft-visual-style.md).

## I. Four levels of motion intensity: pick the level before the tool

Not every shot needs generated animation. Choose the level from the shot's job and you save both failures and money:

| Level | Method | Best for | Cost and risk |
|-------|--------|----------|---------------|
| **1 Static with micro-motion** | original still plus slight scale/offset/parallax, light effects, particles | emotional holds, narration, atmosphere | lowest; almost never breaks |
| **2 2.5D layering** | split foreground/midground/background and move layers at different speeds | depth, camera moves, comic feel | low; needs layer separation |
| **3 Local driving** | animate only part of the image (blink, mouth, hair, hem) | dialogue shots, close-ups | medium; needs masks or drivers |
| **4 Full generated animation** | image-to-video redraws the frame | action shots, transitions, key scenes | highest; face and anatomy risk concentrate here |

**Working ratio**: levels 1 and 2 should cover more than half of an episode, level 3 handles lines that need mouths, and level 4 is reserved for the few shots that genuinely need action. Running level 4 everywhere is expensive and fragile.

## II. Micro-motion list (the cheapest way to wake a still)

Add any two or three of these and the image stops reading as a picture:

- **Breathing**: a 1-2% rise and fall in chest or shoulders
- **Blink**: every 2-4 seconds, irregular
- **Hair and hem**: a slight sway, one consistent direction
- **Light drift**: cloud shadows passing, curtain light shifting, candle flicker
- **Atmosphere**: floating dust, snow, rain, steam, falling leaves
- **Camera breath**: a very slow push or pull, 3-8% across the shot
- **Water and reflection**: ripples, shifting glints

All of these can be done in an editor with keyframes and a few overlay assets, with no generation model involved.

## III. 2.5D layered parallax

Split one image into 3-5 layers (background / midground / character / foreground occluder / light effects) and move each at a different speed:

1. Separate the layers (select in an image editor, or generate a "foreground-only" layer).
2. Export each as a transparent PNG.
3. In the editor, move the background least and the foreground most to create depth.
4. Apply easing (fast then slow) so it does not feel mechanical.

**Typical uses**: a lateral move through the location, a character held centre while the background flows, the comic-style push-in.

## IV. Camera moves: how to describe them so they work

In an image-to-video prompt, describe **direction + speed + start and end**, not "cinematic camera":

| Move | What to specify | Watch out |
|------|-----------------|-----------|
| Push in | wide to close, slow, constant | keep the range small or the character distorts |
| Pull out | close to wide, decelerating | good for endings and reveals |
| Pan | left to right, following the eyeline | must respect the axis |
| Track | parallel move, subject held in place | keep the range small in vertical |
| Follow | follows action, slight lag | match the character's direction |
| Handheld | small irregular sway | overusing it looks cheap |

**Principle**: one camera move per shot. Define the start and end states so the model knows where to travel.

## V. Working with the generation pipeline

1. **Lock the keyframes first**: generate and approve the entry and exit frames, then generate the motion between them.
2. **First/last-frame chaining**: the previous shot's final frame becomes the next shot's first frame; the most reliable cross-shot join.
3. **One action per shot**: see [Shot Language](craft-shot-language.md).
4. **Split complex action**: fights, runs, and turns split into 2-3 short shots, with a far better success rate than one long take.
5. **Do not re-describe appearance**: the source image already fixed identity; repeating face and wardrobe in the motion prompt makes the model reinterpret and drift. Describe only action, environmental motion, camera, and time.
6. **Do not retry endlessly**: set attempts and cost caps; three similar failures means change the approach (shot, level, or tool).

## VI. Failure modes and repairs

| Symptom | Common cause | Smallest fix |
|---------|--------------|--------------|
| Flicker or unstable frames | weak temporal consistency; too much detail | reduce motion range, simplify detail, drop to level 1 or 2 |
| Face drift | appearance re-described in the prompt; references missing or weak | keep only the action, re-attach the reference library |
| Anatomy failure | too much action or occlusion in one shot | split the shot, add an intermediate keyframe, use explicit pose reference |
| Object penetration | the model does not understand spatial relations | go back to static micro-motion, or mask it in post |
| Wrong direction | no direction given, or it conflicts with the axis | state the direction; verify against the previous shot |
| The frame "melts" | motion amplitude too large | cut amplitude to 30-50% and retry |
| Clip too short | model's per-generation limit | chain a second segment by first/last frame, or extend at level 1 or 2 |

## VII. Where sound meets motion

Motion must be planned together with sound, or the action finishes before the line does:

- Mark a **sound cue** for every shot in the shot list (dialogue span, effect hit, music entry and exit).
- Align **effect hits** with picture action (the door slam lands on the frame the door closes).
- Dialogue length decides shot length: measure the line first, then set the shot, never the reverse.
- For shots that need lip movement see [Dialogue, Voice, and Sound](craft-dialogue-voice-and-sound.md).

## VIII. Checklist

- [ ] Was this shot's motion level chosen deliberately rather than defaulting to full generation?
- [ ] Have all shots that could use static micro-motion or parallax been converted?
- [ ] Does the prompt describe only action, environmental motion, camera, and time — with no re-described appearance?
- [ ] One primary action per shot?
- [ ] Does it connect to the previous shot by frame or by screen direction?
- [ ] Are sound cues marked, with effects aligned to action?
- [ ] Are attempt and cost caps set?
