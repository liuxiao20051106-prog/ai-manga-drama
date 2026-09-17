# 🎬 AI漫剧工坊 — 从零创造你的第一部 AI 动漫短剧

> **一句话说清楚**：这是一个"AI 副导演"。你跟它聊天，它帮你把脑海里的故事，一步一步变成能在抖音/B站/小红书发布的动漫短视频。**不需要手绘、不需要学软件，零基础就能上手。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![中文](https://img.shields.io/badge/语言-中文-red)](SKILL.md)
[![English](https://img.shields.io/badge/Lang-English-blue)](en/README.md)
[![Validation](https://github.com/liuxiao20051106-prog/ai-manga-drama/actions/workflows/validate.yml/badge.svg)](../../actions/workflows/validate.yml)

---

## 📖 目录

- [什么是"AI漫剧"？](#什么是ai漫剧)
- [这个项目能帮你做什么？](#这个项目能帮你做什么)
- [我没有基础，真的能用吗？](#我没有基础真的能用吗)
- [你需要准备什么？](#你需要准备什么)
- [快速开始：5分钟体验](#快速开始5分钟体验)
- [八步出片](#八步出片)
- [三条工具路线怎么选？](#三条工具路线怎么选)
- [要花多少钱？怎么算？](#要花多少钱怎么算)
- [安装方法](#安装方法)
- [自带脚本](#自带脚本)
- [项目文件说明](#项目文件说明)
- [常见问题 FAQ](#常见问题-faq)
- [维护与验证](#维护与验证)
- [参考项目](#参考项目)
- [许可](#许可)

---

## 什么是"AI漫剧"？

**AI 漫剧 = AI 生成的动态漫画短视频**

你刷抖音/快手/B站时可能见过这类内容：

> 一段 30 秒到 3 分钟的动漫风格短视频，有角色、有对话、有剧情、有 BGM，画面是漫画风但带微小动态（风吹发丝、镜头推拉、光影变化），看起来像"动起来的漫画"。

一个 30 秒单集的样子：

```text
画面1（4秒）→ 老旧公寓门口，黄昏光线，镜头缓慢下移
画面2（3秒）→ 少女从门内走出，微风吹动裙摆
画面3（3秒）→ 她侧头看向墙上的信箱，眼神期待
画面4（4秒）→ 信箱特写——空的，只贴着一张褪色贴纸
画面5（4秒）→ 手指轻划过信箱边框（配音："已经第四十七天了"）
画面6（5秒）→ 她走出大门，夕阳把背影拉得很长
画面7（5秒）→ 镜头推近信箱——门缝里隐约有白色信封一角（钩子）
```

制作它不需要画一笔画——所有画面由 AI 工具生成，你负责判断和选择。

---

## 这个项目能帮你做什么？

把自己想象成"导演"，本 Skill 是你的"副导演"：

| 它帮你做的事 | 你只需要做的事 |
|-------------|--------------|
| 把一句话创意扩展成结构化剧本，并给出单集任务卡 | 告诉它你想拍什么类型的故事 |
| 设计角色外貌与造型编号，建立**参考图库**（防变脸的地基） | 确认角色方向，挑出满意的那张图 |
| 定义画风六维度、色板与时段色温，写成"风格锚" | 确认画风 |
| 规划分镜（景别/机位/动作接点/连续性出入口） | 确认或提出修改意见 |
| 写出精确的图生图、图生视频、配音提示词 | **复制提示词 → 粘贴到工具 → 下载结果** |
| 标注台词时长、口型档位、混音层级与字幕规范 | 用配音工具生成音频 |
| 给出剪辑合成步骤与多平台交付规格 | 在剪映里按步骤拼接导出 |
| 用脚本给分镜表、提示词、预算做机械体检 | 看体检结果决定改哪里 |

> 💡 **核心原理**：不是 AI 替你做完漫剧，而是 AI 承担"脑力劳动"（剧本、分镜、提示词、检查），你完成"体力劳动"（复制粘贴、点生成、挑片子），一部漫剧就出来了。

---

## 我没有基础，真的能用吗？

**真的能。** 本项目假设你对 AI 工具一无所知。

| 你会用到的东西 | 难不难 | 说明 |
|--------------|--------|------|
| **和 AI 对话** | 跟聊天一样 | 说"我想做一个关于 XX 的漫剧"就行 |
| **复制粘贴提示词** | 0 难度 | AI 写好，你 Ctrl+C / Ctrl+V |
| **在图像/视频工具里点"生成"** | 点一下按钮 | 多数有中文界面 |
| **在剪映里拼接片段** | 拖拖拽拽 | 跟拼乐高差不多 |

**你不需要**：编程、画图、做动画、写脚本、懂摄影、学 PR/AE/Blender。

---

## 你需要准备什么？

### 最低配置

| 需要 | 是什么 | 哪里获取 |
|------|--------|---------|
| **运行环境** | 支持 Skills 的 AI 客户端（如 Claude Code / Codex） | 见[安装方法](#安装方法) |
| **一个图像生成账号** | 中文工具为主，零门槛起步 | 入口见[工具目录](references/tools-catalog.md) |
| **一个视频生成账号** | 图生视频 | 同上 |
| **免费剪辑软件** | 剪映专业版（或 DaVinci Resolve） | 官网下载 |
| **网络** | 能上网就行 | — |

### 进阶配置

追求更高画质与角色稳定性时，通常需要升级图像、视频或配音环节的工具。**具体价格、额度与可用性随时变化，请以各工具官方页面为准**（本项目不承诺任何价格或免费额度）。

> ⚠️ 注意：免费额度、模型名称、地区可用性和商用条款都会变。任何长期计划都应在开工前重新核对官方页面。

---

## 快速开始：5分钟体验

安装完后，在客户端里输入：

```text
帮我做一部漫剧
```

它会先问你几个问题（不会一上来就生成一整季）：

```text
AI：想做什么类型的故事？
你：甜宠的，女主暗恋男主那种

AI：好的。单集想做多长、发哪个平台？
你：先来个 30 秒试试，抖音

AI：工具路线我推荐 A 路线（中文零门槛，先跑通）。可以吗？
你：可以

AI：好。你的女主角是什么样的人？
你：大学生，内向但善良，喜欢在图书馆角落看书
```

然后它会一步步带你走完：任务卡 → 角色与风格锚 → 分镜 → 关键帧 → 动态片段 → 配音字幕 → 合成 → 终检。

**建议第一集只做 15–30 秒**，把流程跑通。跑通后每集速度会明显提升——因为锚点（角色、场景、风格）只需要建一次。

---

## 八步出片

每一步都有对应的深度指南，遇到具体问题时再打开。

| 步骤 | 做什么 | 产出 | 深度指南 |
|------|--------|------|----------|
| **0 项目初始化** | 定类型、时长、平台、画幅、预算量级与权利边界 | 项目总览 | [成本与排期](references/production-cost-and-schedule.md)、[交付规格](references/platform-specs-and-delivery.md) |
| **1 剧本与任务卡** | 一句话梗概 → 单集任务卡 → 可拍摄剧本 | 任务卡 + 剧本 | [短格式叙事](references/craft-short-form-narrative.md) |
| **2 角色/场景/声音** | 身份锚点、造型编号、参考图库、风格锚、色板 | 角色 Bible + 风格指南 | [角色一致性](references/character-consistency.md)、[视觉风格锚](references/craft-visual-style.md) |
| **3 分镜** | 逐镜拆解（景别/机位/动作/连续性出入口） | 分镜表 | [镜头语言与分镜](references/craft-shot-language.md) |
| **4 关键帧出图** | 固定身份块 + 固定风格块 + 镜头变量 | 已批准关键帧 | [提示词模板](references/prompt-templates.md) |
| **5 动态化** | 选动态档位 → 图生视频 → 首尾帧衔接 | 镜头片段 | [动态化技法](references/craft-motion-design.md) |
| **6 配音与声音** | 台词表、口型档位、音乐音效、字幕 | 音频 + 字幕 | [台词、配音与声音](references/craft-dialogue-voice-and-sound.md) |
| **7 合成与验收** | 剪辑合成、质量评分、发布包 | 候选成片 | [质量评测](references/quality-evaluation-and-tests.md)、[发布终检](templates/release-checklist.md) |

> 每步的输入、输出、验收标准和"需要你决定什么"，都写在 [SKILL.md](SKILL.md) 里。

---

## 三条工具路线怎么选？

| 路线 | 适合谁 | 优势 | 代价 |
|------|--------|------|------|
| **A 易用云端** | 零基础、快速验证 | 中文界面、上手快、不必装显卡 | 画质与一致性受工具限制；额度/隐私/商用条款随服务变化 |
| **B 高质量云端** | 有预算、追求画质 | 模型选择多、角色一致性手段多 | 成本更高；地区可用性与条款需逐项核对 |
| **C 本地可控** | 有显卡、重视隐私与批量 | 数据不出本地、可批量可脚本化 | 部署维护成本、模型许可、硬件投入 |
| **混合路线** | 在质量/成本/隐私间平衡 | 按环节挑最合适的工具 | 必须管理色彩、分辨率与资产交接 |

**推荐路径**：先用 A 路线跑通第一集验证故事 → 故事成立后，再逐个环节升级到 B/C。

选工具别只看单价，看六个能力维度（参考输入、首尾帧控制、单次时长与多镜、原生音频与口型、画幅、命中率）——见[工具目录](references/tools-catalog.md)。

---

## 要花多少钱？怎么算？

**本项目不列具体价格**——价格、免费额度、模型名称每几周就会变，写死在文档里只会误导人。

真正该算的是这个：

```text
每支可用成片成本 =（生成额度 + 订阅 + 硬件电费 + 人工工时 + 授权费）÷ 可用成片数
```

关键在**分母**：把失败的尝试也算进去。一个镜头生成 4 次只留 1 次，那 4 次的钱都摊到那 1 次上。

仓库自带估算脚本，先看量级再决定投多少钱：

```bash
python scripts/budget_estimate.py --shots 40 --seconds 5 --attempts 2.5 --unit-cost 0.6 --target-seconds 180
```

它会给出每支可用成片成本，以及"尝试次数 → 成本"的敏感性表，帮你判断**该花钱买更好的工具，还是接受更多重试**。方法详见[成本、产能与排期](references/production-cost-and-schedule.md)。

---

## 安装方法

### 前置条件

装有支持 Skills 的 AI 客户端（Claude Code、Codex 等）。

### 方式一：克隆到 Skills 目录

Claude Code：

```bash
git clone https://github.com/liuxiao20051106-prog/ai-manga-drama.git ~/.claude/skills/ai-manga-drama
```

Codex：

```bash
git clone https://github.com/liuxiao20051106-prog/ai-manga-drama.git ~/.codex/skills/ai-manga-drama
```

Windows PowerShell：

```powershell
git clone https://github.com/liuxiao20051106-prog/ai-manga-drama.git "$env:USERPROFILE\.claude\skills\ai-manga-drama"
```

### 方式二：作为系统提示词

1. 打开 [SKILL.md](SKILL.md)，去掉开头的 `---` front matter 块；
2. 把正文粘贴到平台的"系统提示词 / 自定义指令"；
3. 开始对话。需要专项内容时，把 `references/` 下对应文件一并附上。

### 方式三：下载 ZIP

下载后解压到对应 skills 目录，目录名保持 `ai-manga-drama`。

### 目标目录已存在时

不要直接覆盖。先检查有没有本地修改：

```powershell
git -C "$env:USERPROFILE\.claude\skills\ai-manga-drama" status --short
git -C "$env:USERPROFILE\.claude\skills\ai-manga-drama" pull --ff-only
```

有本地修改时先备份或合并；不要强制拉取、重置或删除目录。

### 英文入口

英文版使用独立名称 `ai-manga-drama-en`，与中文入口 `ai-manga-drama` 不冲突：[en/SKILL.md](en/SKILL.md)

---

## 自带脚本

四个零依赖 Python 脚本（仅用标准库），可直接在终端运行：

```bash
# 1. 分镜表体检：镜号格式、必填字段、单镜时长上限、总时长偏差、入/出镜连续性、景别单调
python scripts/shotlist_lint.py 分镜表.md --target-seconds 60

# 2. 提示词拼装与机械检查：固定身份块/风格块/镜头变量/负面约束
#    并检出两类高频错误——要求复刻在世创作者、在镜头变量里重复描述外貌
python scripts/prompt_blocks.py --style-guide 风格指南.md --identity 身份.txt \
  --action "伸手触碰信箱" --shot-size 中景 --camera "缓慢推近" --negative 多手

# 3. 预算与产能：每支可用成片成本 + 尝试次数敏感性表
python scripts/budget_estimate.py --shots 40 --seconds 5 --attempts 2.5 --unit-cost 0.6

# 4. 仓库自检：front matter、链接、双语镜像、英文目录中文残留、未完成标记、脚本语法、可达性
python scripts/validate.py --warnings-as-errors

# 脚本自身的单元测试
python -m unittest discover -s tests
```

脚本给的是**线索不是判决**：指标异常先看上下文，改不改由你决定。

---

## 项目文件说明

```text
ai-manga-drama/
├── SKILL.md                       ← 主文件（中文），含任务路由表与八阶段工作流
├── README.md                      ← 你正在读的文件
├── CHANGELOG.md                   ← 更新日志
├── LICENSE                        ← MIT 许可
│
├── references/                    ← 16 份专项指南（按需加载）
│   ├── craft-short-form-narrative.md   单集节奏、钩子与留存诊断
│   ├── craft-shot-language.md          景别、轴线、动作接点、竖屏分镜
│   ├── craft-motion-design.md          动态档位、微动、视差、运镜
│   ├── craft-visual-style.md           画风六维度、色板、跨工具统一
│   ├── craft-dialogue-voice-and-sound.md 台词预算、口型四档、混音字幕
│   ├── character-consistency.md        参考库工作流与漂移诊断
│   ├── prompt-templates.md             剧本/图像/视频/声音提示结构
│   ├── platform-specs-and-delivery.md  交付规格、画幅转换、多平台分发
│   ├── production-cost-and-schedule.md 单位成本、产能模型、排期闸门
│   ├── tools-catalog.md                工具能力维度与官方入口
│   ├── project-and-continuity.md       事实源、命名、版本、交接
│   ├── workflow-examples.md            三条路线的端到端示例
│   ├── automation-workflow.md          批量、重试、幂等、人工闸门
│   ├── rights-safety-and-platforms.md  版权、肖像、声音、AI 标识
│   ├── commercialization-and-analytics.md 受众、连载、合同、数据复盘
│   └── quality-evaluation-and-tests.md 硬门禁、评分、行为测试
│
├── templates/                     ← 12 套可直接复制的模板
│   ├── manga-project.md  episode-brief.md  character-bible.md
│   ├── style-guide.md    shot-list.md      audio-sheet.md
│   ├── asset-ledger.md   rights-consent-log.md  production-run-log.md
│   ├── quality-scorecard.md  experiment-log.md  release-checklist.md
│
├── scripts/                       ← 4 个零依赖脚本
│   ├── shotlist_lint.py  prompt_blocks.py  budget_estimate.py  validate.py
├── tests/                         ← 脚本单元测试
├── .github/workflows/validate.yml ← push/PR 自动校验
│
└── en/                            ← 完整英文版（16 份指南 + 12 套模板 + SKILL.md + README.md）
```

---

## 常见问题 FAQ

### Q1：完全不会画画，也能做吗？

能。画面由 AI 图像工具生成，你只需要输入文字描述和参考图。描述也不用自己想——Skill 会按"固定身份块 + 固定风格块 + 镜头变量"的结构写给你。

### Q2：角色总是"变脸"怎么办？

这是 AI 漫剧最大的技术挑战。**正解不是把描述写得更详细，而是建立参考图库并每镜回指它**：

1. 先定一张干净的正脸标准图（均匀光、中性表情、短边 ≥1024）；
2. 以它为准生成 5–8 张角度/表情/全身参考，逐张人工批准；
3. 每镜从库里挑 2–4 张引用，并说明哪张图管脸、哪张管服装；
4. **绝不用"上一张满意的成品"当下一张的参考**——逐代传递会让偏差滚雪球。

详见 [角色一致性指南](references/character-consistency.md)。

### Q3：一集做多久？更新频率怎么定？

用真实产能倒推，不要先定"日更"再硬扛。仓库的预算脚本可以算单位成本，[成本、产能与排期](references/production-cost-and-schedule.md) 给了"样片 → 小批 → 量产"的三道闸门与排期缓冲建议。

经验上：前三集最贵（要建锚点），之后每集边际成本明显下降。**锚点阶段不要省**——省一小时，后面每集多花两小时修漂移。

### Q4：做出来能发布/赚钱吗？

可以，但要过三关：

- **权利关**：剧本原创或已授权；音乐、字体、声音、肖像各有许可；不能用无授权素材。
- **标识关**：中国境内发布的 AI 生成合成内容需要按规定添加显式/隐式标识（《人工智能生成合成内容标识办法》及配套标识方法标准）；海外平台的披露规则不同，发布当日按平台复核。**不得删除服务写入的标识或元数据**。
- **真实性关**：不冒充真人、不制作可能被误认为真实事件的欺骗性内容。

商业化路径、指标与合同注意项见[商业化与分析](references/commercialization-and-analytics.md)。本项目**不承诺任何收益**。

### Q5：可以用手机完成吗？

A 路线的大部分环节在手机端都能做（图像/视频工具、剪辑 App），但用电脑操作效率更高，尤其是分镜表和素材管理。

### Q6：能做其他语言的漫剧吗？

可以。配音与字幕分开决策：常见做法是配音用目标市场母语、字幕保留原文或双语。画面里的文字要在生成阶段留白，交给后期排版、便于多语言替换。

### Q7：这个 Skill 和直接问 AI "帮我做漫剧"有什么区别？

直接问也能得到帮助，但容易跳过关键步骤：角色参考库、分镜连续性、动态档位选择、台词时长预算、口型策略、多平台交付规格、AI 标识。本 Skill 把这些做成流程与检查清单，并有四个脚本做机械体检。

### Q8：脚本会替我做决定吗？

不会。脚本只做机械检查（字段缺失、时长对不上、链接失效、镜像缺文件）。**创意、选片、风格判断和是否发布永远由你决定。**

---

## 维护与验证

仓库自带校验脚本，检查 UTF-8、front matter、相对链接、双语镜像完整性、英文目录中文残留、未完成标记、脚本语法与"指南是否可从入口到达"：

```bash
python -X utf8 scripts/validate.py --warnings-as-errors
```

GitHub Actions 在推送与拉取请求时会跑同一套校验加单元测试。维护 Skill 时仍应人工执行[行为测试](references/quality-evaluation-and-tests.md)，并在发布前重新打开官方文档核对工具与平台规则。

变更记录见 [CHANGELOG.md](CHANGELOG.md)。

---

## 参考项目

以下开源项目为本 Skill 提供了思路参考：

- [UllrAI/CineGen-ShortDrama](https://github.com/UllrAI/CineGen-ShortDrama) — 开源 AI 导演系统，漫剧/动漫/短剧生成
- [AniME (SIGGRAPH Asia 2025)](https://dl.acm.org/doi/10.1145/3757374.3771455) — B站多 Agent 动画生成论文（7 Agent 架构）
- [BigBanana-AI-Director](https://github.com/shuyu-labs/BigBanana-AI-Director) — 工业级项目-季-集生产管线
- [Yutarop/comic-generator](https://github.com/Yutarop/comic-generator) — 一句话 → 完整漫画（MIT 开源）
- [Ran-Chou/moyin-creator](https://github.com/Ran-Chou/moyin-creator) — 魔因漫创，6 层身份锚定系统

---

## 许可

MIT License — 详见 [LICENSE](LICENSE)。使用、修改、分发均可，附上原作者署名即可。

本项目提供的是创作与制作的风险检查框架，**不替代**针对具体地区、合同或发布场景的法律意见。
