# 🎬 AI Manga Drama — AI 漫剧全流程 Skill

面向 Codex 与 Claude Code 的动态漫画/漫剧制作助手：从创意、剧本、角色 Bible 和分镜，到静态图、动态片段、配音、剪辑、质量验收、发布准备与连载复盘。

[中文 Skill](SKILL.md) · [English Skill](en/SKILL.md) · [MIT License](LICENSE)

## 能做什么

- 把一句话创意转成可拍摄的单集任务卡、剧本和分镜表
- 建立角色、造型、场景、道具、声音和镜头连续性
- 为图像、视频、配音、音乐和字幕生成模型无关提示结构
- 根据预算、设备、隐私、地区和质量选择云端、本地或混合路线
- 管理素材来源、版本、依赖、权利、重试和人工审批
- 检查故事、画面、运动、音频、字幕、交付规格与 AI 标识
- 规划连载、指标实验、合同权利和商业化路径，但不承诺播放量或收入

当当前环境提供媒体生成工具且用户授权时，Skill 可以直接协助生成资产；否则输出可交给外部工具执行的提示词和操作清单。

## 快速开始

安装后输入：

```text
帮我做一部 45 秒竖屏治愈漫剧，先完成第一集任务卡和角色方向，不要直接生成整季。
```

Skill 会逐步确认受众、平台、时长、语言、已有素材、权利、预算和工具，再进入制作。已有项目会先读取文件并增量更新，不直接覆盖。

## 安装

### Codex

```bash
git clone https://github.com/liuxiao20051106-prog/ai-manga-drama.git ~/.codex/skills/ai-manga-drama
```

Windows PowerShell：

```powershell
git clone https://github.com/liuxiao20051106-prog/ai-manga-drama.git "$env:USERPROFILE\.codex\skills\ai-manga-drama"
```

### Claude Code

```bash
git clone https://github.com/liuxiao20051106-prog/ai-manga-drama.git ~/.claude/skills/ai-manga-drama
```

如果目标目录已有同名 Skill，先检查差异并备份或合并，不要直接覆盖。

## 八阶段流程

```text
0 项目初始化
  → 1 剧本与单集任务卡
  → 2 角色/场景/声音 Bible
  → 3 分镜与时间轴
  → 4 静态资产
  → 5 动态片段
  → 6 配音/音乐/字幕
  → 7 合成/质量验收/发布准备
```

每阶段都有输入、输出、验收和人工决定。建议状态：

```text
待规划 → 任务卡已批准 → 锚点已批准 → 候选资产 → 质量检查 → 作者审阅 → 已接受 → 已发布
```

## 制作路线

| 路线 | 适合 | 主要取舍 |
|------|------|----------|
| 易用云端 | 零基础、中文界面、快速样片 | 功能、额度、隐私和商用条款会变化 |
| 高质量云端 | 有预算、追求画面或声音 | 需核对地区、成本、输入权利和模型状态 |
| 本地可控 | 有技术能力、隐私或批量需求 | 部署维护、硬件和模型许可成本更高 |
| 混合 | 按环节平衡质量与成本 | 需要更严格的颜色、尺寸和资产交接 |

工具目录不写死价格和免费额度。使用前从[官方入口表](references/tools-catalog.md)重新核对。

## 项目结构

```text
ai-manga-drama/
├── SKILL.md                         # 中文核心入口
├── README.md                        # 项目说明
├── LICENSE                          # MIT
├── references/                      # 中文专项指南（按需读取）
│   ├── tools-catalog.md
│   ├── character-consistency.md
│   ├── prompt-templates.md
│   ├── workflow-examples.md
│   ├── project-and-continuity.md
│   ├── rights-safety-and-platforms.md
│   ├── automation-workflow.md
│   ├── commercialization-and-analytics.md
│   └── quality-evaluation-and-tests.md
├── templates/                       # 9 套中文项目模板
│   ├── manga-project.md
│   ├── episode-brief.md
│   ├── character-bible.md
│   ├── shot-list.md
│   ├── asset-ledger.md
│   ├── rights-consent-log.md
│   ├── production-run-log.md
│   ├── quality-scorecard.md
│   └── release-checklist.md
└── en/
    ├── SKILL.md                     # English core skill
    ├── references/                  # 9 English specialist guides
    └── templates/                   # 9 English templates
```

## 关键改进

### 可验证的角色一致性

用身份锚点、造型编号、参考资产、镜头入口/出口和素材版本管理一致性，不用“成功率百分比”作保证。详见[角色连续性指南](references/character-consistency.md)。

### 不依赖旧模型参数

提示词先采用模型无关结构，再按当前官方文档添加参数。工具版本、价格、额度和地区可用性都在使用时复核。

### 权利与透明度

- 不复刻受保护作品或在世创作者的可识别风格
- 真人肖像和声音克隆需要与用途匹配的授权
- 未成年人素材采用更严格的同意和隐私检查
- 保留来源、许可、AI 工具和人工修改记录
- 发布前复核中国境内、YouTube、TikTok 等适用的 AI 标识规则

详见[权利、安全与平台规则](references/rights-safety-and-platforms.md)。

### 可控自动化

批量生产包含任务 ID、输入版本、候选目录、幂等重试、成本/次数上限和人工闸门。质量通过不代表授权自动发布。

## 验证

维护者提交前应至少检查：

```bash
python -X utf8 scripts/validate.py
python -X utf8 /path/to/skill-creator/scripts/quick_validate.py .
python -X utf8 /path/to/skill-creator/scripts/quick_validate.py en
git diff --check
```

仓库自带的验证脚本会检查 UTF-8、核心 front matter、Markdown 相对链接、双语文件镜像、英文目录中文残留和未完成标记；GitHub Actions 会在推送和拉取请求时运行同一检查。仍需人工复核当前官方链接和[行为测试](references/quality-evaluation-and-tests.md)。

## 费用说明

本项目不提供固定价格表或“零成本保证”。云端计划、免费额度、税费、地区与商用条款经常变化；本地方案也包含硬件、电力、存储、维护和人工成本。先跑通最小样片，再根据真实质量、失败率和单位成片成本升级工具。

## License

MIT License。使用第三方工具、模型、字体、音乐、声音和参考素材时，仍需分别遵守其许可证、服务条款和适用法律。
