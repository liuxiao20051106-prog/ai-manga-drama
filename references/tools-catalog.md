# 工具选择与官方入口

在选择或更换工具、估算预算、确认版本和可用性时读取。以下入口核对日期为 **2026-08-21**；价格、额度、地区、模型状态、许可和功能变化频繁，使用前必须重新打开官方页面。

## 先按约束选择

| 约束 | 优先考虑 | 必须核对 |
|------|----------|----------|
| 零基础/中文界面 | 即梦、可灵、Vidu、剪映等云端工具 | 地区、免费额度、隐私、商用和水印 |
| 画面/运动质量 | 当前高质量云端图像和视频模型 | 输入权利、价格、排队、分辨率、时长 |
| 角色稳定 | 多参考、角色功能、LoRA/IP-Adapter、首尾帧 | 参考图权利、跨镜头限制、可复现性 |
| 隐私/批量 | ComfyUI、开源模型、本地 TTS、FFmpeg | 模型许可证、硬件、依赖维护、安全 |
| 多语言配音 | 授权演员、合成音或经同意的声音克隆 | 肖像/声音权、语言质量、披露和撤回 |

## 易用云端入口

- 即梦：<https://dreamina.jianying.com>
- 可灵：<https://klingai.kuaishou.com>
- Vidu：<https://www.vidu.com>
- 剪映：<https://www.jianying.com>

这些服务可用于图片、视频、音频或剪辑的不同环节，但功能和计划因地区/账号而异。本目录不承诺免费额度或固定价格。

## 国际云端入口

- **Midjourney**：当前官方参数页显示 V7 相关功能，并说明角色引用方式随版本变化；不要在长期模板中固定旧 `--v 6.1`：<https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List>
- **Runway**：官方 Gen-4.5 指南覆盖文生视频和图生视频；图生视频提示应主要描述运动和镜头：<https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5>
- **Google Veo**：Gemini API 官方指南当前提供 Veo 3.1 入口；可用模型代码和预览状态应现场核对：<https://ai.google.dev/gemini-api/docs/veo>
- **OpenAI Sora**：OpenAI 官方模型页列出 Sora 2 的视频/同步音频能力和模型状态；不要把 Character、API、时长或价格当永久接口：<https://developers.openai.com/api/docs/models/sora-2>
- **ElevenLabs**：语音合成/克隆前先查看安全和声音验证要求：<https://elevenlabs.io/safety>
- DaVinci Resolve：<https://www.blackmagicdesign.com/products/davinciresolve>
- Adobe Premiere：<https://www.adobe.com/products/premiere.html>

## 本地与开源入口

- ComfyUI：<https://github.com/Comfy-Org/ComfyUI>
- Stable Diffusion WebUI：<https://github.com/AUTOMATIC1111/stable-diffusion-webui>
- IP-Adapter：<https://github.com/tencent-ailab/IP-Adapter>
- ControlNet：<https://github.com/lllyasviel/ControlNet>
- GPT-SoVITS：<https://github.com/RVC-Boss/GPT-SoVITS>
- FFmpeg：<https://ffmpeg.org>
- MoviePy：<https://zulko.github.io/moviepy/>

本地模型“可下载”不等于可商用。分别核对底模、LoRA、节点、训练集、声音和输出的许可。

MoviePy v2 有破坏性变更，旧示例中的 `moviepy.editor`、`.set_*`、`.subclip` 等写法可能失效；按官方迁移指南更新：<https://zulko.github.io/moviepy/getting_started/updating_to_v2.html>

## 推荐流程

先选一个能完成最小样片的组合，记录实际生成质量、失败率、单位时长成本、等待时间、隐私和权利。只有数据表明瓶颈存在时才替换某一环节，一次不要同时更换图片、视频和声音工具。
