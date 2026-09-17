# 工具选择与官方入口

在选择或更换工具、估算预算、确认版本和可用性时读取。以下入口核对日期为 **2026-09-17**；价格、额度、地区、模型状态、许可和功能变化频繁，使用前必须重新打开官方页面。

> 本页只写**结构性事实**（有哪些能力维度、怎么选），不写具体价格、额度与版本号——这些数字的半衰期通常只有几周。

## 先按约束选择

| 约束 | 优先考虑 | 必须核对 |
|------|----------|----------|
| 零基础/中文界面 | 中文云端工具（图像、视频、剪辑） | 地区、免费额度、隐私、商用和水印 |
| 画面/运动质量 | 当前高质量云端图像和视频模型 | 输入权利、价格、排队、分辨率、时长 |
| 角色稳定 | 支持多图参考、首尾帧、区域编辑的工具 | 参考图数量上限、权重、商用条款 |
| 隐私/批量 | ComfyUI、开源模型、本地 TTS、FFmpeg | 模型许可证、硬件、依赖维护、安全 |
| 多语言配音 | 授权演员、合成音或经同意的声音克隆 | 肖像/声音权、语言质量、披露和撤回 |

## 选工具看六个能力维度（比看榜单有用）

漫剧的实际瓶颈不在"画面够不够漂亮"，而在下面这六项能不能满足你的流程：

| 维度 | 为什么重要 | 怎么问 |
|------|------------|--------|
| **参考输入** | 决定角色一致性上限 | 能挂几张参考图？参考视频？参考音频？能否指定每张图管什么？ |
| **首尾帧控制** | 决定镜头能不能"缝"起来 | 能否指定起始帧与结束帧？结束帧精度如何？ |
| **单次时长与多镜** | 决定一集要拼多少段 | 单次最长几秒？能否一次生成多镜？超过时长后靠什么延长？ |
| **原生音频/口型** | 决定声音环节的工作量 | 是否带同步语音？支持哪些语言？口型质量如何？ |
| **画幅与分辨率** | 决定能否直出竖屏 | 支持 9:16 吗？原生分辨率多少？（注意区分"原生生成"与"后期放大"） |
| **命中率与可复现性** | 决定真实成本 | 同一输入重跑是否稳定？失败后能否定位原因？ |

**成本要按"每支可用成片"算**，见[成本、产能与排期](production-cost-and-schedule.md)。单价低但命中率差的工具通常更贵。

## 易用云端入口

- 即梦：<https://dreamina.jianying.com>
- 可灵：<https://klingai.kuaishou.com>
- Vidu：<https://www.vidu.com>
- 剪映：<https://www.jianying.com>

这些服务覆盖图片、视频、音频或剪辑的不同环节，但功能和计划因地区/账号而异。本目录不承诺免费额度或固定价格。

## 国际云端入口

- **Midjourney**：参数与角色引用方式随版本变化，不要长期模板化写死版本参数：<https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List>
- **Runway**：官方指南覆盖文生视频与图生视频；图生视频提示应主要描述运动和镜头：<https://help.runwayml.com/>
- **Google Veo / Gemini**：模型代码、预览状态与配额应现场核对：<https://ai.google.dev/gemini-api/docs/veo>
- **OpenAI 视频能力**：产品与 API 的可用状态在 2026 年内有过调整，**任何长期管线都不要绑定单一模型**；接入前先看当前官方模型页：<https://platform.openai.com/docs/models>
- **ElevenLabs**：语音合成/克隆前先查看安全和声音验证要求：<https://elevenlabs.io/safety>
- DaVinci Resolve：<https://www.blackmagicdesign.com/products/davinciresolve>
- Adobe Premiere：<https://www.adobe.com/products/premiere.html>

> **纪律**：不要因为某篇测评说"某模型第一"就换工具。榜单与版本每周都变；只有在你自己的任务卡上跑过 A/B、且失败率或成本确实更好时，才替换某一环节。

## 本地与开源入口

- ComfyUI：<https://github.com/Comfy-Org/ComfyUI>
- Stable Diffusion WebUI：<https://github.com/AUTOMATIC1111/stable-diffusion-webui>
- IP-Adapter：<https://github.com/tencent-ailab/IP-Adapter>
- ControlNet：<https://github.com/lllyasviel/ControlNet>
- GPT-SoVITS：<https://github.com/RVC-Boss/GPT-SoVITS>
- 口型同步类开源工具（按需核对协议与显存要求）：<https://github.com/bytedance/LatentSync>、<https://github.com/Rudrabha/Wav2Lip>、<https://github.com/DanielSWolf/rhubarb-lip-sync>
- FFmpeg：<https://ffmpeg.org>
- MoviePy：<https://zulko.github.io/moviepy/>

本地模型"可下载"不等于可商用。分别核对底模、LoRA、节点、训练集、声音和输出的许可。

MoviePy v2 有破坏性变更，旧示例中的 `moviepy.editor`、`.set_*`、`.subclip` 等写法可能失效；按官方迁移指南更新：<https://zulko.github.io/moviepy/getting_started/updating_to_v2.html>

## 推荐流程

先选一个能完成最小样片的组合，记录实际生成质量、失败率、单位时长成本、等待时间、隐私和权利。只有数据表明瓶颈存在时才替换某一环节，一次不要同时更换图片、视频和声音工具。

**注意区分"原生能力"与"后期修补"**：原生支持 4K 与"生成 720p 再放大到 4K"是两回事，后者的细节不会凭空出现；把放大放在已经满意的成片上，而不是用来救崩坏的画面。
