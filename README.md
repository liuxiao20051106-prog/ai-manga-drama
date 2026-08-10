# AI漫剧工坊 (AI Manga Drama Studio)

> 一个 Claude Code Skill，从零创造 AI 漫剧（AI 动态漫画短剧）的全流程制作助手。

## 这是什么？

AI漫剧工坊是一个 Claude Code 的 Skill 文件，让你能够通过自然语言对话，完成从剧本创作到成片输出的完整 AI 漫剧制作流程。

你不需要手绘能力，不需要学专业动画软件——你只需要和 Claude 对话，它会逐步引导你产出每个环节的 AI 提示词，你拿着提示词去对应的 AI 工具生成素材，最后组装成片。

## 支持的制作路线

| 路线 | 工具链 | 费用 | 适合 |
|------|--------|------|------|
| **A路线（国产零门槛）** | DeepSeek + 即梦 + 可灵 + 剪映 | ¥0 | 零基础新手 |
| **B路线（国际高品质）** | ChatGPT/Claude + Midjourney + Veo3/Runway + ElevenLabs | ~$30-50/月 | 追求品质 |
| **C路线（技术开源）** | SD + ComfyUI + AnimateDiff + Ollama | 硬件一次性投入 | 技术型创作者 |

三路线可灵活混合搭配。

## 工作流程（8个阶段）

```
阶段零: 项目初始化（路线选择 + 项目文件创建）
    ↓
阶段一: 剧本工坊（选题 → 梗概 → 完整剧本）
    ↓
阶段二: 角色与场景设计（人设卡 + 场景图提示词 + 角色一致性方案）
    ↓
阶段三: 分镜脚本（剧本 → 分镜序列，含景别/运镜/台词/时长）
    ↓
阶段四: 分镜图生成（逐镜文生图提示词）
    ↓
阶段五: 动画生成（图生视频提示词 + 首尾帧转场）
    ↓
阶段六: 配音与配乐（TTS 脚本 + BGM 设计 + 音效清单）
    ↓
阶段七: 合成与发布（剪辑指南 + 字幕 + 导出 + 平台适配）
```

## 安装

将整个 `ai-manga-drama` 文件夹放入你的 Claude Code skills 目录：

```bash
# 如果使用 Claude Code CLI
cp -r ai-manga-drama ~/.claude/skills/

# 如果使用 VSCode 扩展
# 放入对应工作区的 .claude/skills/ 目录
```

安装后，Claude Code 会自动识别并注册 Skill。之后用中文说以下触发词即可：

- "帮我做一部漫剧"
- "我想做 AI 动态漫画"
- "AI漫剧制作"
- "帮我做动漫短剧"
- "短剧生成"

## 文件结构

```
ai-manga-drama/
├── SKILL.md                          # 主 Skill 文件（618行）
├── README.md                         # 本文件
└── references/
    ├── tools-catalog.md              # 全工具速查表（三路线对比）
    ├── prompt-templates.md           # 提示词模板库（所有环节）
    ├── character-consistency.md      # 角色一致性技术详解（7种方案）
    └── workflow-examples.md          # 完整工作流示例（3个实例）
```

## 角色一致性：7 种方案

AI 漫剧最大的技术难题——角色在不同分镜中"变脸"。Skill 覆盖全部解决方案：

1. ⭐ 参考图法（新手首选）
2. ⭐ 统一关键词法
3. ⭐ 即梦智能画布（A路线专属）
4. ⭐⭐ 角色ID/种子固定
5. ⭐⭐⭐ LoRA 微调（效果最佳）
6. ⭐⭐⭐ IP-Adapter（ComfyUI）
7. ⭐⭐ Character Cameo（Sora2专属）

## 收录工具（30+）

国产：DeepSeek、即梦、可灵、Vidu、海螺AI、剪映、Mureka、必剪
国际：ChatGPT、Claude、Midjourney、Veo3、Sora2、Runway、Pika、ElevenLabs、Suno
开源：ComfyUI、SDXL、Flux、AnimateDiff、GPT-SoVITS、Ollama、Kohya_ss、MusicGen

## 相关项目参考

- [UllrAI/CineGen-ShortDrama](https://github.com/UllrAI/CineGen-ShortDrama) — 开源AI漫剧生成系统
- [AniME (SIGGRAPH 2025)](https://dl.acm.org/doi/10.1145/3757374.3771455) — B站多Agent动画生成论文
- [BigBanana-AI-Director](https://github.com/shuyu-labs/BigBanana-AI-Director) — 工业级项目-季-集工作流

## 许可

MIT License
