# Tool Selection and Official Entry Points

Load to select tools, estimate budget, or verify versions and availability. Entry points checked **2026-08-21**; prices, quotas, regions, model status, licensing, and features change. Reopen official pages before use.

| Constraint | Consider | Verify |
|------------|----------|--------|
| Beginner/Chinese UI | Dreamina, Kling, Vidu, CapCut/Jianying | Region, quotas, privacy, commercial use, watermark |
| Visual/motion quality | Current premium image/video services | Input rights, price, queue, resolution, duration |
| Stable characters | Multi-reference, character tools, LoRA/IP-Adapter, first/last frame | Reference rights, limits, reproducibility |
| Privacy/batch | ComfyUI, local models/TTS, FFmpeg | Model licenses, hardware, maintenance, security |
| Multilingual voice | Authorized actors, synthetic voices, consented clones | Voice rights, quality, disclosure, withdrawal |

## Accessible cloud

- Dreamina: <https://dreamina.jianying.com>
- Kling: <https://klingai.kuaishou.com>
- Vidu: <https://www.vidu.com>
- Jianying/CapCut China: <https://www.jianying.com>

This catalog does not promise free credits or fixed pricing.

## International cloud

- **Midjourney:** the official parameter page currently documents V7-era features and version-dependent character references; do not hard-code old `--v 6.1`: <https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List>
- **Runway:** official Gen-4.5 guidance covers text- and image-to-video; image-to-video prompts should focus on motion and camera: <https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5>
- **Google Veo:** the Gemini API guide currently exposes Veo 3.1; verify model code and preview status: <https://ai.google.dev/gemini-api/docs/veo>
- **OpenAI Sora:** the official model page lists Sora 2 video and synced-audio capabilities and current status; character, API, duration, and pricing are not durable interfaces: <https://developers.openai.com/api/docs/models/sora-2>
- **ElevenLabs:** review current safety and voice-verification requirements: <https://elevenlabs.io/safety>
- DaVinci Resolve: <https://www.blackmagicdesign.com/products/davinciresolve>
- Adobe Premiere: <https://www.adobe.com/products/premiere.html>

## Local/open source

- ComfyUI: <https://github.com/Comfy-Org/ComfyUI>
- Stable Diffusion WebUI: <https://github.com/AUTOMATIC1111/stable-diffusion-webui>
- IP-Adapter: <https://github.com/tencent-ailab/IP-Adapter>
- ControlNet: <https://github.com/lllyasviel/ControlNet>
- GPT-SoVITS: <https://github.com/RVC-Boss/GPT-SoVITS>
- FFmpeg: <https://ffmpeg.org>
- MoviePy: <https://zulko.github.io/moviepy/>

Downloadability does not establish commercial rights. Check every base model, LoRA, node, training set, voice, and output license.

MoviePy v2 introduced breaking changes; old `moviepy.editor`, `.set_*`, and `.subclip` examples may fail. Use the official migration guide: <https://zulko.github.io/moviepy/getting_started/updating_to_v2.html>

Prove one minimal toolchain and record quality, failure rate, cost per delivered second, waiting time, privacy, and rights. Replace one bottleneck at a time.
