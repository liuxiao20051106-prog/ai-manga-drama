# Dialogue, Voice, and Sound Design

Load when writing lines, planning voice and lip sync, mixing audio, or diagnosing "it sounds off", "the audio does not match the picture", or "the lines do not fit". SKILL.md carries the baseline (clone only your own voice or one with written consent; proof subtitles against the actual audio; intelligibility of dialogue comes first); this is the full expansion.

> Related: sound cues inside shots in [Shot Language](craft-shot-language.md); motion and lip movement in [Motion Design](craft-motion-design.md); voice and music rights in [Rights, Safety, and Platforms](rights-safety-and-platforms.md).

## I. Five audio layers in a manga drama

| Layer | Job | Priority |
|-------|-----|----------|
| Narration | carries information and pacing (the workhorse of this format) | highest (intelligibility) |
| Dialogue | performance and relationships | highest |
| Effects | hits, space, weight | medium |
| Music | emotional bed and rhythm | medium-low |
| Ambience | location realism (wind, rain, street) | lowest |

**The key difference from live-action short drama**: manga-drama storytelling leans on **narration plus subtitles**, and audiences tolerate imperfect lip sync far better than in live action. The strategy is therefore "**plausible mouth movement + accurate subtitles + well-placed sound effects**", not spending the whole budget on frame-accurate mouths.

## II. Writing lines

- **Word budget**: Mandarin voice-over runs about 4-5 characters per second. 30 s is roughly 90-130 characters, 60 s roughly 180-250, including narration.
- **One idea per line**: split "because of what happened three years ago, I never dared come back" into two lines with an image between them.
- **Speakable first**: if it trips the tongue, rewrite it. Do not make the voice performer carry it.
- **No explanatory lines**: characters do not explain their own motives; let action and consequence do it.
- **Give information to the picture**: if an action, prop, or expression can carry it, keep it out of the script.
- **Leave breath**: half a beat between lines so music and effects have room.

## III. Voice

Annotate every line:

```
[AUD-ID / CHAR-ID]
Line: ...
Language and pronunciation: proper nouns, stress, how numbers are read
Emotional target: primary emotion + intensity (restrained 0.3 / normal 0.6 / explosive 1.0)
Pace and pauses: as the performance requires
Voice boundaries: age impression, range, voices that must not be imitated
Shot / timecode: E01-S003 00:02-00:05
```

- **One voice plan per character**: timbre, baseline pace, verbal tics, and pronunciation habits are fixed in the character bible and kept across tool changes.
- **Multilingual**: prioritise native naturalness in the target market; dubbing and subtitles need not match (dubbed audio with original-language subtitles is a common pattern).
- **Cloning boundary**: only your own voice or one with written consent, and never to impersonate a real person, client, or colleague. Even ordinary synthetic voices need commercial terms and platform disclosure checked.

## IV. Four lip-sync options

| Option | Method | Best for | Cost |
|--------|--------|----------|------|
| No lip requirement | profile, back of head, cut away, or move the line to narration | most narrative shots | lowest, and cannot look wrong |
| Prompted mouth | enable the model's dialogue or lip option and let it resolve | frontal medium and close shots | low; occasionally imprecise |
| Local driving | drive the mouth or the whole face from audio | close-ups where the mouth matters | medium; needs another tool and hardware |
| Frame-by-frame repair | fix mouths in post | a few key shots | highest; not viable across a full episode |

**Decision order**: first ask whether the shot can avoid showing the mouth; then check the model's native ability; only then bring in a dedicated driver. Spend the saved budget on performance, effects, and pacing — audiences notice those far more.

## V. Subtitle standards

- **12-18 characters per line** for Chinese; wrap rather than shrinking the type.
- Each subtitle stays at least 1 second and no more than the spoken length plus 0.5 s.
- Keep the position fixed and clear of platform UI (a common vertical convention is within the lower 15-20%).
- Proof against the actual audio, not the script — performers change lines in the booth.
- Mark the speaker when more than two are present, and add accessibility notes for meaningful non-speech sound (for example "(door)").
- Fix one spelling for proper nouns, numbers, and loanwords in the project glossary.

## VI. Mixing

- **Hierarchy**: voice > effects > music > ambience. Nothing may cover the voice.
- **Reference ranges** (always defer to the platform document, they change): dialogue −12 to −6 dB, music −24 to −18 dB, effects below the voice; programme loudness commonly around **−14 LUFS** (platforms range from about −13 to −16), true peak no higher than **−1 dBTP**.
- **Do not substitute fixed level offsets for listening**: check on headphones, a phone speaker, and laptop speakers.
- **Dialogue intelligibility is the single most important metric.** If lines cannot be heard, everything upstream was wasted.
- Music and effects need licence and commercial-scope records; see [Rights, Safety, and Platforms](rights-safety-and-platforms.md).

## VII. Sync checklist

- [ ] Does every line start and end with the speaker's action on screen?
- [ ] Do effect hits land on the action frame (door, dropped object, footstep)?
- [ ] Do music entries and exits land on cuts?
- [ ] Do transitions carry sound across, avoiding a sudden silence?
- [ ] Is loudness consistent across the whole piece?
- [ ] Have subtitles been checked line by line against the audio?
- [ ] Is dialogue still clear on a phone speaker?

## VIII. Common problems

| Symptom | Cause | Fix |
|---------|-------|-----|
| Lines do not fit | over the character budget | cut lines; never speed up delivery |
| Sounds fake | every line is a complete written sentence | make it colloquial, add pauses and particles |
| Mouths do not match | no lip handling, or shot length mis-estimated | measure the audio before setting shot length, or move the line to narration |
| Volume jumps | no loudness normalisation | normalise the whole piece |
| Music buries the voice | hierarchy not set | pull the music down; voice first |
| Subtitles unreadable | too many characters or hidden by UI | wrap, enlarge, move up |
