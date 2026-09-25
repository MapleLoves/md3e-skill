# 可选附录：Compose API 与迁移

仅在实际项目使用 Compose 或用户明确询问 Compose 时读取。本文是次要实现资料，
不决定 MD3E 的设计边界，也不要求其他技术栈引入 Compose。

原资料核对日期：**2026-09-14**；版本记录本次未重新核验，不代表当前最新版本。
原来源：Compose Material 3 版本说明与 Compose 开发指南。
依赖选择以项目实际版本和需求为准，不默认采用 alpha 或要求升级。
先阅读 [设计判断](design-system.md)；版本背景见 [历史版本快照](../version-baseline.md)。

## 一、版本门槛速查

| 能力 | 最低版本 | 稳定性 |
| --- | --- | --- |
| `MaterialTheme`（colorScheme / typography / shapes） | M3 早期 | ✅ 稳定 |
| 动态取色（`dynamicLightColorScheme` 等） | M3 早期，需 **API 31+** | ✅ 稳定 |
| 组件动画切换到 `MotionScheme` | **1.4.0** | ✅ 稳定 |
| `MotionScheme.standard()` / `expressive()` | 1.4.0-alpha02 起（由 `standardMotionScheme`/`expressiveMotionScheme` 重命名） | 随版本 |
| `MaterialExpressiveTheme`、`expressiveLightColorScheme` | 1.5.0-alpha18 | ⚠️ alpha |
| `ToggleButton` / FAB Menu | 1.4.0-alpha19 | ⚠️ alpha 线 |
| `ButtonGroup` | 1.4.0-alpha22 | ⚠️ alpha 线 |
| `SplitButton` | 1.4.0-alpha20 | ⚠️ alpha 线 |
| Flexible TopAppBar 系列 / `FlexibleBottomAppBar` | 1.5.0-alpha23 | ⚠️ alpha 线 |
| `FloatingToolbar` | 1.5.0-alpha22 | ⚠️ alpha 线 |
| `SearchBarState` + slot 版 `SearchBar` | 1.5.0-alpha24 | ⚠️ alpha 线 |
| `carouselParallaxScrollEffect` | 1.5.0-alpha28 | ⚠️ alpha 线 |
| `material3-ripple` | 1.5.0-alpha24 | ⚠️ alpha 线（独立库） |

**快照记录**：**在上述核对日期，所记录的完整 M3E 组件集仅在 alpha 线**。
稳定线（1.4.0）提供的是"M3 + MotionScheme + 部分 Expressive"，不包含全套 M3E 新组件。

---

## 二、稳定线（1.4.0）的破坏性变更

| 变更 | 影响与处理 |
| --- | --- |
| **移除 `material-icons-core` 传递依赖** | 用到图标必须**显式声明**依赖（I735ff, b/349894318） |
| **`androidx.compose.material.icons` 不再推荐** | 官方建议改用 fonts.google.com/icons 的 Material Symbols 矢量图 |
| `NavigationBarItem` / `NavigationRailItem` 选中标签色 | `onSurface` → **`secondary`**；恢复需手动设 `selectedTextColor = MaterialTheme.colorScheme.onSurface` |
| 组件动画机制 | 全部改用新的 **`MotionScheme`** |
| **1.4.0-beta01 移除了所有 `ExperimentalMaterial3ExpressiveApi` / `ExperimentalMaterial3ComponentOverrideApi` 的公共 API** | 想继续用必须切到 **1.5.0-alpha** |

---

## 三、项目内实现与迁移

- 先核对项目依赖与目标设计；仅对需要的功能查相应版本 API。
- 复用项目已有主题生成、颜色角色与配置，不要求复制主题骨架或重新生成主题文件。
- 根据设计目的选取可用组件，不为获得某个 API 名称而更换整个项目的技术方案。
- 自定义交互沿用项目动效与状态语言，具体方法签名按实际依赖查询。
- 迁移范围服从任务，保留适用的既有组件，并检查受影响的主题、尺寸和交互状态。

---

## 四、alpha 线的 API 变动频率（风险提示）

1.5.0-alpha 线在多个月内发生了**大量重命名与移除**，例如：

| 版本 | 变动 |
| --- | --- |
| alpha28 | `Slider`/`RangeSlider` 无状态重载弃用；`RangeSliderState` 字段重命名 |
| alpha27 | `TopAppBarDefaults` 旧 scrollBehavior 重载移除；`LocalMotionScheme` 移除；`RichTimePickerDialog` → `VibrantTimePickerDialog` |
| alpha26 | `ExposedDropdownMenu` 改为扩展函数（**需改 import**） |
| alpha25 | `TonalToggleButton` → `FilledTonalToggleButton`；ComponentOverride API 移除；`SplitButtonLayout` 弃用 |
| alpha24 | `SearchBarState` 稳定；`material3-ripple` 新库 |
| alpha23 | ComponentOverride API 移除；Expressive AppBar 毕业；`TextFieldLabelPosition.Attached` 弃用 |
| alpha20 | BottomSheet remember 系列统一 |
| alpha18 | `rememberWithGapSearchBarState` 重命名；`Material3ExpressiveApi` 提供免 OptIn 版本 |

**结论**：使用 alpha 组件时，**升级前必须读一遍该版本的 release notes**，
并保证组件调用点集中（包一层自己的封装），降低重命名带来的改动面。

---

## 五、实现时的设计检查

| 约束 | 说明 |
| --- | --- |
| 颜色成对使用 | `primary`+`onPrimary`、`primaryContainer`+`onPrimaryContainer`；官方反例：`tertiaryContainer` + `primaryContainer` 对比度不足 |
| 字号放大 | 系统字号放大后必须验证布局不溢出、不截断 |
| 减少动效 | 按平台设置提供适合的简化反馈，保留必要状态信息 |
| 语义 | 保留控件已有语义，按需补充标签、角色与状态，避免重复播报 |

---

## 六、按实际任务核对

设计规格优先查 [Material 设计快照](../m3-content/index.md)，其中保留来源和抓取日期。
API 完整签名查 [包文档快照](../compose-api-full.md)，并与项目实际依赖匹配。
如果项目版本不同，应核对相应发布说明；旧版本表不能证明新版本的可用性。
涉及形变、动效参数或组件状态等具体实现时，仅核对当前任务需要的部分。
