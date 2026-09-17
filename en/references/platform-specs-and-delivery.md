# Delivery Specs and Multi-Platform Distribution

Load when fixing delivery specs, deriving one master for several platforms, or preparing a release package. **Every number on this page is a reference range, not a promise.** Platform documents, encoding guidance, and content policies change; re-open the official pages on the day you publish.

> Related: labelling and rights in [Rights, Safety, and Platforms](rights-safety-and-platforms.md); titles, covers, and audience strategy in [Commercialization and Analytics](commercialization-and-analytics.md); the final check is [the release checklist](../templates/release-checklist.md).

## I. Fix the master first, then derive

**Master specs** (as high quality as practical; the single source of truth):

- Resolution set by the highest requirement among your platforms (commonly 1080×1920 vertical, or 1920×1080 horizontal)
- Frame rate matching the source material (commonly 30 fps; 60 fps when there is real motion)
- Codec: H.264 / MP4 for the widest compatibility; H.265 is smaller but less compatible
- Audio: 48 kHz stereo, loudness-normalised before export
- Keep a **clean master with no subtitles, no labels, no watermark** for later revisions and localisation

Derive everything from the master. **Do not re-edit per platform** — many versions means changing one thing in ten places.

## II. Technical reference ranges

| Item | Vertical (TikTok-like, Douyin-like, Reels-like feeds) | Horizontal (Bilibili-like, YouTube-like) |
|------|--------------------------------------------------------|------------------------------------------|
| Aspect | 9:16 | 16:9 |
| Resolution | 1080×1920 or higher | 1920×1080 or higher |
| Frame rate | 30 / 60 fps | 24 / 30 / 60 fps |
| Video bitrate | roughly 8-16 Mbps | roughly 8-20 Mbps |
| Audio bitrate | 128-192 kbps | 192-320 kbps |
| Loudness | around −14 LUFS (platforms range from about −13 to −16) | same |
| True peak | ≤ −1 dBTP | same |
| Codec | H.264 / MP4 | H.264 / MP4 |
| Safe area | keep about 15% clear top and bottom (text in the centre column) | keep about 10% clear at the bottom |

**Always defer to the platform's own publishing documentation**: the same platform can publish different recommendations for app, web, and open API.

## III. Safe areas and subtitle placement

- The top and bottom edges of a vertical frame are covered by titles, buttons, comments, and progress bars. Put **faces, props, and title cards in the centre column**.
- Fix subtitles at one height; do not let them jump within a piece.
- Opening title cards and closing call-to-action cards also need safe-area layout.
- Check the final on a real phone, not only on a desktop monitor.

## IV. Aspect conversion means re-planning, not cropping

Vertical to horizontal (or the reverse):

1. **Re-frame**: some shots may need regenerating (wider sizes, more environment).
2. **Fill the sides**: add artwork or a blurred or solid treatment — never stretch.
3. **Rebuild title cards**: vertical cards look sparse in horizontal and need re-layout.
4. **Repeat the safe-area check.**
5. **Record the derivation**: master and derived versions with IDs and dates in [the asset ledger](../templates/asset-ledger.md).

What gets "cut away" changes how a piece reads, so never treat aspect conversion as a one-click operation.

## V. Covers, titles, and first frames

- **First frame**: vertical feeds often show the first frame or a cover by default; put the most arresting image here, never an empty establishing shot.
- **Cover**: character occupying a large share of the frame, exaggerated expression, 3-8 large title characters, high contrast.
- **Title**: state "who + what happens + which way it leans" without misleading clickbait. Keep the structure consistent across a series so viewers can follow it.
- **Description and tags**: genre, relationships, update cadence — for search and recommendation.

## VI. Platform differences (structure level; verify specifics on the day)

These vary most between platforms and **must be checked individually — one rule set does not travel**:

| Dimension | What to confirm |
|-----------|-----------------|
| Content positioning | vertical fast-paced vs horizontal serial vs female-skewed vs mystery — preferences differ |
| Length and episode count | per-episode range, total season length, whether serial status is supported |
| Access and eligibility | open to individuals, or needs an agency, rights proof, or content rating |
| Rights and IP | whether an open IP library is offered, and whether adaptation subsidies require full rights |
| AI labelling | explicit label placement and form; whether implicit metadata labels must be preserved |
| Traffic rules | whether off-platform links or promotion are allowed |
| Monetisation | revenue share, guarantees, paid episodes, brand deals, subscriptions — and their thresholds |
| Analytics | how each backend defines retention, completion, and follow-through |

**Caution**: guarantee amounts, revenue splits, and programme names that circulate in self-published media change extremely fast and are frequently exaggerated. Any figure, percentage, or subsidy term must come from an official page or the signed contract.

## VII. Multilingual and international release

- **Subtitles and dubbing are separate decisions**: a common pattern is native-language dubbing with either original or bilingual subtitles.
- Translate by rewriting, not word-for-word: idiom, slang, forms of address, and units all need localisation.
- On-screen text (signage, phone screens, title cards) **should be left sparse during generation** and laid out in post so languages can be swapped.
- Overseas platforms may have different AI disclosure requirements; verify each one.
- Cultural fit: gestures, colours, festivals, and religious or political sensitivities need checking per market.

## VIII. Release package contents

Every delivery should include:

- [ ] The finished piece (master plus per-platform derivations, named with episode and version)
- [ ] Cover and first frame at required sizes
- [ ] Title, description, tags, topics
- [ ] Subtitle files including accessibility notes
- [ ] Asset ledger and rights records (music, fonts, voice, likeness)
- [ ] AI labelling implementation notes
- [ ] Quality scorecard and open risk list
- [ ] Release checklist with verification date and links

## IX. Publish-day checklist

- [ ] Did you re-open the target platform's current spec document (resolution, bitrate, length, loudness)?
- [ ] Did you confirm AI labelling rules and the labelling feature in the backend?
- [ ] Are content policy and rating requirements checked?
- [ ] Are title, cover, and description free of misleading or false claims?
- [ ] Is upload permission and public release separately authorised by the author?
- [ ] After upload, did you play it back on a real device for safe area, subtitles, and sync?
