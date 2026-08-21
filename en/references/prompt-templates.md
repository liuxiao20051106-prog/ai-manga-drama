# Manga Drama Prompt Structures

Load when converting a brief into script, image, video, voice, or music prompts. Start model-neutral and add parameters only after reading the current tool documentation.

## Script

```text
Task: create a filmable [duration] manga-drama script for [project/episode].
Source of truth: [characters, world, previous episode state]
Episode goal: [goal, resistance, change, emotional movement]
Must preserve: [content]
Must not add/change: [content]
Deliver: scenes, action, dialogue/narration, sound, visual point, estimated duration.
Check: timing, causality, visualizability, continuity, and new facts requiring approval.
```

Do not impose a universal word count or three-second hook. Use actual delivery, pauses, caption readability, and platform experience.

## Character sheet

```text
[CHAR-ID / LOOK-ID]
Identity lock: [face, features, core hair, body, signature item]
Look lock: [wardrobe, colors, materials, shoes, props]
Variables: [expression, pose, angle]
Views: [front, sides, back, proportions, expressions]
Visual language: [line, palette, texture, light, detail]
Neutral review background.
Negative constraints: [identity drift, text, watermark, anatomy issues]
```

Replace a living-artist name with high-level visual traits.

## Location anchor

```text
[LOC-ID]
Layout: [entrance, windows, furniture, roads, landmarks and positions]
Time/weather: [content]
Key light and color temperature: [content]
Props and positions: [content]
Blocking zones: [establishing/dialogue/action]
Empty location; no characters; reusable structure.
```

## Shot keyframe

```text
[E01-S001]
References: [CHAR/LOOK, LOC, PROP IDs]
Positions and eyelines: [content]
Frozen action beat: [one clear moment]
Composition: [shot size, angle, lens feel, layers]
Light/atmosphere: [only changes from anchor]
Entry continuity: [prior exit]
Exit continuity: [next requirement]
Negative constraints: [identity, wardrobe, props, text, anatomy]
```

## Image to video

```text
Based on approved [shot keyframe].
Subject motion: [who moves from what state to what state]
Environmental motion: [only necessary motion]
Camera: [direction, speed, start/end]
Temporal progression: [rhythm, pauses, light changes]
Keep fixed: [identity, wardrobe, props, layout, style]
End frame: [state required by the next shot]
```

Prefer one main action per shot. Do not restate the source image’s identity in ways that invite reinterpretation.

## Voice and music

```text
[AUD-ID / CHAR-ID]
Line: [text]
Language/pronunciation: [names, stress, numbers]
Performance: [primary emotion, restraint/intensity, pace, pauses]
Voice boundary: [age impression, range, prohibited imitation]
Shot/timecode: [content]
```

```text
Use: [episode/time range/emotional function]
Music: [tempo range, rhythmic density, instruments, harmony, arc]
Make room for: [dialogue and key effects]
Structure: [in, development, peak, out, loop]
Prohibit: [recognizable song/melody or unauthorized samples]
```

Generation still requires listening, editing, licensing, and provenance records.
