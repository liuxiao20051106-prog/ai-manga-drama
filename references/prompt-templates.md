# 提示词模板库

## 一、剧本生成模板

### 1.1 通用剧本模板

```
请帮我写一个[题材]短剧本。

## 基本信息
- 类型：[言情/悬疑/热血/治愈/搞笑/古风/科幻]
- 主角1：[姓名]，[年龄]岁[性别]，[身份]，[核心性格关键词]
- 主角2：[姓名]，[年龄]岁[性别]，[身份]，[核心性格关键词]
- 故事背景：[时间/地点/世界观]
- 单集时长：[30秒/60秒/90秒]
- 目标平台：[抖音/B站/小红书]
- 情感基调：[甜宠/虐心/燃向/治愈/惊悚]

## 剧本要求
1. 开场3秒有钩子（冲突/悬念/冲击画面）
2. 对话简短，每句不超过15字
3. 每集结尾留悬念/反转/情绪余韵
4. 输出包含：集标题、分场景描述、角色对话、视觉要点、结尾钩子
```

### 1.2 不同题材的专用提示词片段

**言情/甜宠**：
```
画面感强，多用特写镜头展示眼神和微表情。关键情感节点：初遇→心动→误会→和解。台词甜而不腻。
```

**悬疑**：
```
信息量精准控制，每次只揭露一部分真相。色调偏暗、阴冷。关键节奏：铺垫→线索→反转→更大谜团。结尾必须让观众"啊？"一声。
```

**热血战斗**：
```
节奏快，每10秒一个小爆点。打斗描述要有画面感（pose、光影、冲击力）。台词简短有力，BGM踩点。
```

**治愈日常**：
```
节奏舒缓，画面温暖明亮。重点刻画生活中的小而美：一杯热茶、夕阳下的影子、一朵野花。台词温柔克制。
```

**搞笑沙雕**：
```
节奏快，梗要密。人物表情夸张，动作幅度大。可在画面中加一些文字特效（震惊、裂开等）。2-3秒一个笑点。
```

---

## 二、角色人设卡提示词模板

### 2.1 中文提示词（A路线 - 即梦/可灵/海螺）

#### 基础模板
```
一位[年龄]岁的[性别]，[发型+发色]，[脸型]，[眼睛形状+颜色]，[鼻子特征]，[嘴型]，[肤色]，[身材体型]。

穿着[上装+下装+鞋子，颜色和款式都要写清楚]，[标志性配饰]。

[表情描述]，[姿势]，[构图要求]。

[画风描述]，[光线]，[背景要求]，高画质，细节丰富，角色设定图。
```

#### 日系少年漫男主示例
```
一位18岁的少年，黑色刺猬头短发，瘦削脸型，剑眉星目，黑色瞳孔锐利有神，小麦色皮肤，身材修长精瘦。

穿着红色连帽卫衣，外搭深蓝色校服外套敞开穿，黑色长裤，白色运动鞋，左手腕戴一块简约电子表。

嘴角微微上扬带点不羁的笑，双手插兜，正面站立姿势，微微仰视。

日系少年漫画风格，轮廓线条利落有力，高明暗对比，纯白背景，角色设定图，三视图（正面+侧面+背面），高画质，细节丰富。
```

#### 日系少女女主示例
```
一位16岁的少女，深棕色长直发及腰，齐刘海，鹅蛋脸，圆润的大眼睛琥珀色瞳孔，小巧的鼻子，微笑的嘴唇，肤色白皙透亮，身材娇小纤细。

穿着白色衬衫配浅蓝色百褶裙，领口系深蓝色蝴蝶结，黑色过膝袜，棕色圆头皮鞋，右手腕戴一条银色细链手镯。

温柔的微笑，双手交叠放在身前，正面站立，微微歪头。

日系清新动漫风格，新海诚式柔光，暖色调，淡蓝色渐变背景，角色设定图，三视图，高画质，细节丰富。
```

#### 古风角色示例
```
一位25岁的男性侠客，墨色长发束成高马尾，剑眉入鬓，丹凤眼狭长冷淡，高挺鼻梁，薄唇，肤白，身形颀长挺拔。

穿着月白色长袍，腰间束玄色腰带，外罩青灰色纱质外衫，随风微扬，腰间挂一柄青色剑鞘的长剑，足蹬黑色云纹靴。

面容冷淡沉静，目光遥望远方，一手自然垂落一手扶剑柄，站姿挺拔如松。

中国水墨古风，工笔人物风格，淡雅色调，远处山峦虚化背景，角色设定图，全身像，高画质，细节丰富。
```

### 2.2 英文提示词（B路线 - Midjourney）

#### 基础模板
```
character design sheet, [age] year old [gender], [hair description], [face shape], [eye color and shape], [body type].
Wearing [full outfit description with colors], [signature accessory].
[Expression], [pose], front view + side view + 3/4 view.
[Art style keywords], clean background, high quality, detailed face, detailed clothing --ar 3:4 --style raw --v 6.1
```

#### MJ 日系动漫男主
```
character design sheet, 18 year old male, spiky black short hair, sharp angular face, piercing black eyes, lean athletic build, tan skin.
Wearing red hoodie under an unbuttoned dark blue school blazer, black pants, white sneakers, simple digital watch on left wrist.
Confident smirk, hands in pockets, front view + side view + 3/4 view.
Shonen manga style, bold linework, high contrast, clean white background, high quality character reference --ar 3:4 --style raw --v 6.1
```

### 2.3 Stable Diffusion 提示词（C路线）

#### 基础模板
```
(masterpiece, best quality:1.2), [character description], character sheet, front view, side view, back view, standing pose, simple background, [art style trigger], (detailed face:1.1), (detailed eyes:1.1), (sharp focus:1.1)
Negative: nsfw, lowres, (worst quality:1.4), bad anatomy, bad hands, missing fingers, extra fingers, blurry, deformed, disfigured, (watermark:1.3), text, signature
```

#### SD 常用画风 trigger 词
```
日系动漫: anime style, anime screencap, makoto shinkai style
少年漫: shonen manga, black and white manga, screentone
韩漫风格: manhwa style, webtoon style, semi-realistic
写实: photorealistic, realistic, 8k, raw photo
古风: chinese ink painting, traditional chinese art style
```

---

## 三、分镜脚本模板

### 3.1 分镜表模板

```
## 第X集分镜表：【集标题】

**本集时长**：约XX秒 | **分镜数**：X个
**情感曲线**：[起始情绪] → [中间变化] → [结尾情绪]

| 镜号 | 画面描述 | 角色 | 景别 | 运镜 | 台词/旁白 | 秒 |
|------|---------|------|------|------|----------|----|
| S01 | 空旷的走廊，夕阳从窗户斜射进来，光斑落在地板上 | 无 | 全景 | 缓慢推镜至窗边 | — | 4 |
| S02 | 少女背靠墙壁，低头看着手机，屏幕的光映在她脸上 | 女主 | 近景 | 从侧面缓慢推近 | "还是没有回复……" | 3 |
| ... | ... | ... | ... | ... | ... | ... |
```

### 3.2 分镜画面描述的精确写法

好的分镜画面描述 = 空间锚定 + 角色动作 + 情感信息 + 视觉风格

| 差的写法 | 好的写法 |
|---------|---------|
| 女主在教室 | 空旷的教室里只有女主一人，她坐在靠窗的最后一排，窗外的夕阳把她的侧脸染成金色 |
| 男主走进来 | 门被推开，男主的身影出现在门口，走廊的灯光从他背后打过来形成剪影 |
| 两人对视 | 特写，两人目光交汇的瞬间——女主的瞳孔微微放大，男主的喉结滚动了一下 |
```

### 3.3 景别选择决策表

| 你想让观众感受到…… | 用这个景别 |
|------------------|-----------|
| 角色的内心情感 | 面部特写/眼睛特写 |
| 角色的肢体语言 | 中景（半身） |
| 角色之间的关系 | 双人中景/过肩镜头 |
| 角色所处的环境 | 全景/远景 |
| 环境中的关键物品 | 物品特写 |
| 气氛和空间感 | 远景/大远景 |
| 紧张对抗 | 快速切近景+特写 |
| 抒情慢节奏 | 缓慢全景/慢摇 |

---

## 四、文生图提示词模板

### 4.1 提示词公式

```
[主体描述] + [场景/环境] + [动作/姿态] + [镜头/构图] + [光线/氛围] + [画风/风格] + [质量词]
```

### 4.2 各路线提示词模板

**A路线（即梦/可灵）**：
```
（参考角色X人设卡）[角色名]站在[场景描述]，[动作/姿态]，[镜头景别]，[光线描述]，[画风关键词]，高清画质，细节清晰
```

**B路线（Midjourney）**：
```
[Subject], [scene], [action/pose], [camera angle], [lighting], [art style], [quality keywords] --ar 16:9 --style raw --v 6.1
```

**C路线（Stable Diffusion）**：
```
(masterpiece, best quality:1.2), [subject], [scene], [action], [camera], [lighting], [art style], (highly detailed:1.1)
Negative: nsfw, lowres, bad anatomy, bad hands, blurry, deformed, watermark
```

### 4.3 光线描述词库

| 光线类型 | 中文描述词 | English Keywords |
|---------|-----------|-----------------|
| 黄金时刻 | 夕阳逆光，金色光线，长阴影 | golden hour, backlight, warm glow, long shadows |
| 柔和散射 | 阴天柔光，窗边自然光，温柔光线 | overcast, soft diffused light, window light |
| 戏剧性 | 侧面强光，明暗分明，高对比 | dramatic side lighting, chiaroscuro, high contrast |
| 夜景 | 月光，路灯，霓虹灯反射 | moonlight, street lamp, neon reflection |
| 清晨 | 晨曦薄雾，淡蓝色冷光 | early morning mist, cool blue light, dawn |
| 室内暖 | 暖黄灯光，台灯暖光，火炉光 | warm indoor lighting, desk lamp glow, fireplace |

---

## 五、图生视频提示词模板

### 5.1 提示词公式（中文）

```
[运镜方式] + [画面中的动态元素（什么在动）] + [动态的幅度和速度] + [氛围/光线变化（如有）] + [保持不变的要素]
```

### 5.2 各工具模板

**可灵/即梦（A路线）**：
```
[运镜描述]，[角色动作]，[环境动态（风吹/落叶/光影变化）]，画面流畅，动作自然，保持角色形象一致，高画质
```

**Runway Gen-3（B路线）**：
```
[Camera movement], [subject action], [environmental dynamics], cinematic, smooth motion, [mood/atmosphere], maintaining visual consistency, high quality
```

**Vidu（A/B均可）**：
```
[运镜]，画面中[谁]在做[什么动作]，[环境动态]，保持角色一致，画面稳定流畅
```

### 5.3 动态描述词库

#### 角色动作
```
微动类（适合静止画面增加生气）：
- 轻微呼吸起伏、发丝被风微微吹动、睫毛轻颤
- 手指轻敲桌面、脚尖轻点地面
- 眼神流转、嘴角微动

中幅动作（适合对话和日常）：
- 转身、回头、起身、坐下
- 伸手、拿起物品、放下杯子
- 点头、摇头、挥手、捂嘴笑

大幅度（适合高潮/战斗）：
- 奔跑、跳跃、飞踢
- 挥剑、格挡、闪避
- 拥抱、推开、追赶
```

#### 环境动态
```
- 窗帘被风吹起、花瓣缓缓飘落、树叶沙沙摇动
- 烛光摇曳、水面波光粼粼、烟雾缓缓升腾
- 雨滴滑落窗户、雪花飘落、阳光中漂浮的灰尘
- 云层缓缓流动（时间流逝感）、街灯渐次亮起
```

#### 运镜动态（按情绪分类）
```
平静/抒情：
- 缓慢推镜（slow push-in）
- 轻微呼吸感（gentle breathing motion）
- 从右至左平移（slow pan right to left）
- 画面上摇（tilt up）

紧张/冲突：
- 快速推镜（quick zoom-in）
- 镜头晃动（camera shake）
- 突然拉远（rapid pull-back）
- 快速切换焦点（rack focus）

震撼/高潮：
- 希区柯克变焦（dolly zoom - 推镜+变焦）
- 环绕拍摄（orbit around subject）
- 极速推进→骤停（crash zoom）

第一人称：
- 行走时的镜头晃动（walking camera）
- 转头视角（pan as character turns head）
```

---

## 六、配音情绪标注格式

### 6.1 情绪标签词库

```
正向情绪：
开心、愉悦、兴奋、激动、惊喜、欣慰、温暖、甜蜜、温柔、宠溺、自豪

负向情绪：
悲伤、难过、委屈、愤怒、害怕、紧张、绝望、失落、愧疚、压抑、痛苦

中性/复杂：
平静、冷淡、克制、隐忍、犹豫、困惑、若有所思、言不由衷、强颜欢笑

特殊效果：
耳语、喊叫、哽咽、颤抖、嘶哑、有气无力、一字一顿
```

### 6.2 配音配置模板

```
角色：[角色名]
台词：[台词内容]
情绪：[主情绪] + [辅情绪（如有）]
语速：[0.8x-1.2x，0.85x=缓慢深情，1.0x=正常，1.1x=稍快（短视频推荐），1.2x=激动]
音调：[正常/偏高/偏低]
停顿：[在XX词后停顿0.3秒]
强度：[轻声/正常/有力/爆发]
```

### 6.3 TTS 工具配置速查

| 工具 | 情绪控制方式 | 示例 |
|------|------------|------|
| 剪映AI配音 | 选择对应情绪的预设音色 | "伤感女声"、"活泼少年"、"沉稳男声" |
| 微软Azure TTS | SSML标签 | `<mstts:express-as style="sad">台词</mstts:express-as>` |
| ElevenLabs | 提示词+设置 | 在生成时用 `[sad, trembling voice]` 前缀 |
| GPT-SoVITS | 参考音频 | 提供目标情绪的参考音频片段 |

---

## 七、场景图提示词模板

### 7.1 场景图提示词公式

```
[场景名称]，[空间描述]，[关键物品/元素]，[时间/光线]，[氛围]，[画风]，空镜（无人物），[质量词]
```

### 7.2 场景提示词示例

```
# 日系校园教室（黄昏）
空旷的教室，整齐排列的课桌椅，靠窗最后一排，窗外夕阳金色光芒射入，窗帘被风吹起一角，黑板上有模糊的粉笔字迹，暖黄色调，安静放学后的氛围，日系动漫风格，空镜，高画质

# 古风庭院（月夜）
中式庭院，青石板地面，石灯笼发出暖黄微光，一株老梅树影子投在白墙上，远处有假山和竹子剪影，明月当空，清冷银蓝色月光，宁静深夜氛围，中国水墨古风，空镜，高画质

# 现代都市天台（夜晚）
高楼天台，城市天际线为背景，万家灯火星星点点，近处有空调外机和通风管道，地面有水渍反光，远处霓虹灯红蓝交错，冷色调，孤独城市氛围，新海诚风格，空镜，高画质
```

---

## 八、BGM 生成提示词（Suno/Mureka）

### 8.1 BGM 风格提示词框架

```
[情绪形容词] + [乐器配置] + [节奏(BPM)] + [风格/流派] + [用途描述]
```

### 8.2 BGM 提示词示例

```
# 甜蜜爱情场景
warm gentle love theme, solo piano with soft strings, 70bpm, lofi romance, soft emotional atmosphere

# 悬疑铺垫
dark ambient tension, low cello drone with subtle percussion, 60bpm, cinematic suspense, slow building unease

# 热血战斗高潮
epic battle climax, full orchestra with heavy taiko drums and electric guitar, 160bpm, anime battle theme, intense and powerful

# 治愈日常
light heartwarming, acoustic guitar and kalimba, 90bpm, cozy lo-fi, gentle and peaceful

# 悲伤分别
melancholic farewell, solo violin with distant piano, 60bpm, emotional cinematic, tearful and bittersweet
```
