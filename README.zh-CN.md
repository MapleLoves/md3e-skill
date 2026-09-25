# MD3E Skill

**[English](README.md)** | **[中文](README.zh-CN.md)**

一个以 **Material Design 3 Expressive（MD3E）UI 设计**为核心的 AI 技能包，重点在于
设计意识、设计语言与设计判断。面向项目实际采用的技术栈，不要求使用 Android 或 Jetpack Compose。

## 这个 Skill 提供什么

- **设计哲学与价值观：** 根据用户需要决定产品气质和表现力的强度。
- **设计原则与逻辑：** 建立信息层级、内容分组、交互含义和清楚的反馈。
- **设计语言：** 协调色彩、排版、形状、空间和动效，使表现力具有明确目的。
- **设计伦理与包容性：** 保持选择可理解、内容可读、界面可操作，并尊重用户控制权。
- **UI Kit 判断：** 采用合适的组件与样式，调整部分匹配的内容，在没有合适模式时自主设计。
- **设计参考资料：** 提供经过整理的设计笔记，以及供组件指南和精确规格查阅的来源快照。

M3E 建立在 Material 3 基础之上。同一产品可以根据情境采用不同表现强度，不要求每个
页面用齐所有表现手法。用户要求实现时，设计决策应在项目已有技术栈中落地。

## UI Kit 与自主设计

UI Kit 指项目实际提供或指定的资源。选用前先判断其语义、行为、状态和表现是否适合。

1. 有合适内容时，采用对应组件、样式或模式。
2. 只有部分匹配时，调整或组合合适的资源。
3. 没有合适内容时，根据任务、Material 设计原则和项目语言，设计缺失的组合或交互，
   同时复用其中仍然适合的基础内容。

资源不可见不等于组件不存在。Skill 会区分已经检查的资源与假设，并简要解释重要的
复用或自主设计选择。

## 安装

将仓库中的技能内容放入 AI 助手技能目录下名为 md3e 的文件夹。例如，使用
.codebuddy/skills 目录的项目可放在 .codebuddy/skills/md3e/。具体位置以助手支持的
目录为准；技能入口是 [SKILL.md](SKILL.md)。

使用设计技能不需要 Python 运行环境、主题生成脚本或 Kotlin 模板。主题生成交由项目
已有工具处理，Skill 指导生成结果怎样用于层级、对比和语义。

升级已有安装时，清理 [变更记录](CHANGELOG.md) 列出的旧生成器与模板。单纯复制新文件
不会删除旧文件；清理安装目录前应保留项目自定义内容。

## 使用示例

- “为这个 Web 应用的任务页面建立 MD3E 视觉方向，沿用项目已有组件。”
- “审视这个界面的信息层级与表现力强度，解释重要取舍。”
- “合适的地方使用项目 UI Kit；如果没有合适的比较区域，请自行设计。”
- “让这个设置页面清楚且有表现力，同时保持高频操作的效率。”
- “统一色彩、排版、形状与动效的设计语言，沿用当前技术栈。”

小修改应交付聚焦的结果，无需长篇设计报告。实现请求应交付实际实现，并在必要时
附上简短的设计依据。

## 资料结构

| 资料 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 定位、设计判断、Kit 决策和参考资料入口 |
| [设计意识](references/m3e/design-system.md) / [English](references/m3e/design-system.en.md) | 哲学、价值观、原则、思维、逻辑与伦理 |
| [组件判断](references/m3e/components.md) / [English](references/m3e/components.en.md) | UI Kit 适配与自主设计 |
| [视觉语言](references/m3e/color-typography-shape.md) / [English](references/m3e/color-typography-shape.en.md) | 色彩、排版、形状、空间及其关系 |
| [动效意图](references/m3e/motion-physics.md) / [English](references/m3e/motion-physics.en.md) | 反馈、连续性、表现强度和减少动效 |
| [表现力策略](references/expressive-design-tactics.md) | 何时、为何采用不同表现手法 |
| [组件目录](references/components-catalog.md) | 按任务与交互含义选型 |
| [Token 索引](references/design-tokens.md) | 语义角色与精确规格的查阅入口 |
| [M3 与 M3E](references/m3-vs-m3e-diff.md) | 设计延续与表现力选择 |
| [设计依据](references/design-research.md) | 区分来源、假设与实际验证 |
| [官方设计快照](references/m3-content/index.md) | 组件、样式和设计基础的参考页面 |

### 可选 Compose 附录

[Compose 笔记](references/m3e/compose-api.md) / [English](references/m3e/compose-api.en.md)、
[版本快照](references/version-baseline.md) 和
[androidx.compose.material3 包文档](references/compose-api-full.md) 是次要资料。
仅在实际项目使用 Compose 或明确查询 API 时读取，不替项目决定框架或依赖版本，也不
属于默认设计流程。

## 来源与边界

Material 设计资料是主要参考。带日期的设计页面保留来源与抓取日期：**2026-09-14**；
较早的导航页保留行内来源说明，没有逐页抓取日期。整理后的笔记区分本 Skill 的设计建议与来源规范。本次调整重组技能内容，不代表重新
核验了所有外部页面、研究结果或 Compose 版本。

仓库维护和校验见 [贡献指南](CONTRIBUTING.md)，发布准备见 [发布说明](PUBLISH.md)。
仓库校验属于维护工作，不是使用设计技能的前置条件。

## 许可

[Apache License 2.0](LICENSE)。
