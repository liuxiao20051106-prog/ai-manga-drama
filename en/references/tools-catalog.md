# Tool Selection and Official Entry Points

Load when choosing or replacing tools, estimating budget, or confirming availability. Entry points below were verified on **2026-09-17**. Prices, quotas, regions, model status, licences, and features change frequently, so re-open the official page before use.

> This page records **structural facts** (which capability dimensions exist, how to choose) rather than prices, quotas, or version numbers — those have a half-life of weeks.

## Choose by constraint first

| Constraint | Prefer | Must verify |
|------------|--------|-------------|
| No experience / non-English UI | Chinese-language cloud tools (image, video, editing) | region, free quota, privacy, commercial use, watermark |
| Image and motion quality | Current high-quality cloud image and video models | input rights, price, queue, resolution, duration |
| Character stability | Tools with multi-reference, first/last frame, region editing | reference count limits, weights, commercial terms |
| Privacy and batch work | ComfyUI, open models, local TTS, FFmpeg | model licences, hardware, dependency upkeep, security |
| Multilingual voice | Licensed performers, synthetic voices, consented cloning | likeness and voice rights, language quality, disclosure and revocation |

## Six capability dimensions matter more than leaderboards

The real bottleneck in manga-drama production is not "how pretty the picture is" but whether these six fit your pipeline:

| Dimension | Why it matters | What to ask |
|-----------|----------------|-------------|
| **Reference input** | Sets the ceiling on character consistency | How many image references? Reference video? Reference audio? Can you say which image governs what? |
| **First/last frame control** | Decides whether shots can be joined | Can you set the start and end frames? How precise is the end frame? |
| **Per-generation length and multi-shot** | Decides how many segments an episode needs | Longest single generation? Multiple shots in one call? How do you extend beyond it? |
| **Native audio and lip sync** | Decides how much sound work remains | Synchronised speech? Which languages? How good is the mouth? |
| **Aspect and resolution** | Decides whether vertical is native | Does it support 9:16? Native resolution? (Distinguish native generation from upscaling.) |
| **Hit rate and reproducibility** | Decides the real cost | Is the same input stable across runs? Can you attribute a failure? |

**Cost is measured per publishable unit** — see [Cost, Capacity, and Scheduling](production-cost-and-schedule.md). A cheap tool with a poor hit rate is usually the expensive one.

## Accessible cloud entry points

- Jimeng (Dreamina): <https://dreamina.jianying.com>
- Kling: <https://klingai.kuaishou.com>
- Vidu: <https://www.vidu.com>
- CapCut / Jianying: <https://www.jianying.com>

These cover different stages of image, video, audio, or editing work, but features and plans differ by region and account. This catalog promises no free quota and no fixed price.

## International cloud entry points

- **Midjourney**: parameters and character reference change between versions; never hardcode version flags in long-lived templates — <https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List>
- **Runway**: official guides cover text-to-video and image-to-video; image-to-video prompts should describe motion and camera — <https://help.runwayml.com/>
- **Google Veo / Gemini**: verify model codes, preview status, and quotas on the day — <https://ai.google.dev/gemini-api/docs/veo>
- **OpenAI video capabilities**: product and API availability changed during 2026, so **no long-lived pipeline should bind to a single model**; check the current model page — <https://platform.openai.com/docs/models>
- **ElevenLabs**: read the safety and voice verification requirements before synthesis or cloning — <https://elevenlabs.io/safety>
- DaVinci Resolve: <https://www.blackmagicdesign.com/products/davinciresolve>
- Adobe Premiere: <https://www.adobe.com/products/premiere.html>

> **Discipline**: do not switch tools because one review claims a model is "number one". Leaderboards and versions change weekly. Replace a stage only after an A/B on your own brief shows a real gain in failure rate or cost.

## Local and open-source entry points

- ComfyUI: <https://github.com/Comfy-Org/ComfyUI>
- Stable Diffusion WebUI: <https://github.com/AUTOMATIC1111/stable-diffusion-webui>
- IP-Adapter: <https://github.com/tencent-ailab/IP-Adapter>
- ControlNet: <https://github.com/lllyasviel/ControlNet>
- GPT-SoVITS: <https://github.com/RVC-Boss/GPT-SoVITS>
- Open lip-sync tools (verify licence and VRAM requirements): <https://github.com/bytedance/LatentSync>, <https://github.com/Rudrabha/Wav2Lip>, <https://github.com/DanielSWolf/rhubarb-lip-sync>
- FFmpeg: <https://ffmpeg.org>
- MoviePy: <https://zulko.github.io/moviepy/>

"Downloadable" is not "commercially usable". Check the base model, LoRAs, nodes, training data, voice, and output licences separately.

MoviePy v2 introduced breaking changes; older examples using `moviepy.editor`, `.set_*`, or `.subclip` may fail. Follow the official migration guide: <https://zulko.github.io/moviepy/getting_started/updating_to_v2.html>

## Recommended process

Pick one combination that can finish a minimum sample, then record its real quality, failure rate, cost per second, wait time, privacy, and rights. Replace a stage only when the data shows a bottleneck, and never change image, video, and audio tools at the same time.

**Distinguish native capability from post-hoc repair**: native 4K is not the same as generating at 720p and upscaling — the detail does not appear from nowhere. Upscale an already-satisfying take, rather than using upscaling to rescue a broken frame.
