# Optional Compose Version Snapshot

Read only for an actual Compose implementation task. These are historical records from the
**2026-09-14** knowledge baseline, not current dependency recommendations or design requirements.
The version details have not been reverified during the design-focused revision of this skill.
Original sources: AndroidX release notes and the Compose developer guide. Match the actual
project dependencies before using these records; do not adopt alpha versions by default.

## 1. Version matrix (M3E-relevant)

| Component | Stable | Pre-release recorded in the snapshot | Notes |
| --- | --- | --- | --- |
| Compose Material 3 | **1.4.0** (2025-09-24) | **1.5.0-alpha28** (2026-09-09) | Full M3E components only on alpha line |
| Compose Material 3 Adaptive | **1.3.0** (2026-08-12) | **1.4.0-alpha02** | `NavigationSuiteScaffold`, pane scaffolds |
| Compose core (UI/Foundation/…) | 1.12 via BOM **2026.08.00** | **1.13.0-alpha03** via `compose-bom-alpha` | BOM also maps material3 + adaptive |
| Compose BOM | `2026.09.00` | `compose-bom-alpha:2026.09.00` | Explicit versions override BOM |
| `material-icons-core` | 1.7.8 (frozen in BOM) | — | **No longer transitive from material3 1.4.0+** |
| Navigation 3 | 1.1.7 | 1.2.0-rc01 | Outside Compose BOM |
| WindowManager | 1.5.1 | 1.6.0-alpha05 | Foldables |

### BOM coverage (verified via POM)

`compose-bom-alpha:2026.09.00` **does** manage:

- `androidx.compose.material3:material3` → 1.5.0-alpha28
- `androidx.compose.material3:material3-adaptive-navigation-suite` → 1.5.0-alpha28
- `androidx.compose.material3.adaptive:*` → 1.4.0-alpha02
- core UI/runtime/foundation/animation → 1.13.0-alpha03

**Not** in BOM (declare explicitly): `navigation3`, `window`, `lifecycle`, `activity`.

---

## 2. Hard compatibility constraints

### Material 3 / M3E

| Constraint | Detail |
| --- | --- |
| Icons | Since **1.4.0**, `material-icons-core` is **not** passed transitively — declare it explicitly, or use [Material Symbols](https://fonts.google.com/icons) (recommended; `androidx.compose.material.icons` is discouraged) |
| Nav label color | `NavigationBarItem` / `NavigationRailItem` selected label: `onSurface` → **`secondary`** (override with `selectedTextColor`) |
| Experimental split | **1.4.0-beta01 removed all public `ExperimentalMaterial3ExpressiveApi` APIs** from the stable line — full Expressive requires **1.5.0-alpha** |
| Motion | Component animations use **`MotionScheme`** since 1.4.0; get specs from `MaterialTheme.motionScheme` (not `LocalMotionScheme`, removed in alpha27) |
| ColorScheme | Immutable since 1.2.0-alpha08 — rebuild scheme, don't mutate fields |
| Surface containers | Since **1.3.0**, components default to `SurfaceContainer*` roles and are **not** affected by tonal elevation the old way |
| Focus overlay | 1.3.0: focus state overlay **0.1f**; light/dark surface & background micro-adjustments |

### Compose / toolchain (context)

| Constraint | Detail |
| --- | --- |
| Compose 1.12+ | AGP ≥ 9.1.2; compileSdk API 37+ |
| Compose 1.13-alpha | compileSdk ≥ 37.1 |
| Dynamic color | API **31+** (`Build.VERSION_CODES.S`); must fall back otherwise |
| Dynamic color pairing | Always pair `primary`+`onPrimary`, `primaryContainer`+`onPrimaryContainer`. Official anti-pattern: `tertiaryContainer` + `primaryContainer` (insufficient contrast) |

---

## 3. Feature gate map (which line has what)

| Capability | Minimum version | Channel |
| --- | --- | --- |
| `MaterialTheme` (color/typography/shapes) | early M3 | stable |
| Dynamic color | early M3, API 31+ | stable |
| `MotionScheme.standard()` / `.expressive()` | 1.4.0-alpha02 (renamed from `standardMotionScheme`/`expressiveMotionScheme`) | stable in 1.4.0 |
| `MaterialExpressiveTheme`, `expressiveLightColorScheme` | 1.5.0-alpha18 (API ref also shows alpha23 additions) | alpha |
| `ToggleButton` / FAB Menu | 1.4.0-alpha19 | alpha line |
| `ButtonGroup` | 1.4.0-alpha22 (promoted stable APIs in alpha22) | alpha line |
| `SplitButton` | 1.4.0-alpha20 | alpha line |
| Flexible TopAppBar series / `FlexibleBottomAppBar` | 1.5.0-alpha23 (graduated non-experimental) | alpha line |
| `FloatingToolbar` | 1.5.0-alpha22 | alpha line |
| `SearchBarState` + slot `SearchBar` | 1.5.0-alpha24 | alpha line |
| `carouselParallaxScrollEffect` | 1.5.0-alpha28 | alpha line |
| `material3-ripple` (inset focus ring) | 1.5.0-alpha24 | alpha, separate artifact |

---

## 4. Alpha line volatility (read release notes before upgrading)

| Version | Notable changes |
| --- | --- |
| alpha28 | Stateless `Slider`/`RangeSlider` overloads deprecated; `RangeSliderState` field renames (`activeRangeStart/End` → `startValue/endValue`); global `carouselParallaxScrollEffect` |
| alpha27 | Old `TopAppBarDefaults` scrollBehavior overloads removed; **`LocalMotionScheme` removed**; `RichTimePickerDialog` → `VibrantTimePickerDialog` (`richColors` → `vibrantColors`); `SelectableDropdownMenuItem` / `CheckableDropdownMenuItem` added |
| alpha26 | `ExposedDropdownMenu` → extension function on `ExposedDropdownMenuBoxScope` (**import change**) |
| alpha25 | `TonalToggleButton` → **`FilledTonalToggleButton`**; ComponentOverride API removed; **`SplitButtonLayout` deprecated** (use `SplitButton`); `ButtonGroupScope` sealed interface |
| alpha24 | `SearchBarState` stable; `material3-ripple` new library |
| alpha23 | Flexible AppBar family graduated non-experimental; ComponentOverride API removed; `TextFieldLabelPosition.Attached` deprecated |
| alpha20 | BottomSheet remember helpers unified → `rememberBottomSheetState` |
| alpha18 | `rememberWithGapSearchBarState` → `rememberSearchBarWithGapState`; MaterialExpressiveTheme opt-in helpers |

---

## 5. Historical dependency example (not a project default)

```kotlin
// gradle/libs.versions.toml (or module build.gradle.kts)
implementation(platform("androidx.compose:compose-bom-alpha:2026.09.00"))
implementation("androidx.compose.ui:ui")
implementation("androidx.compose.foundation:foundation")
implementation("androidx.compose.material3:material3") // → 1.5.0-alpha28 via alpha BOM
implementation("androidx.compose.material3:material3-adaptive-navigation-suite")
implementation("androidx.compose.material:material-icons-core") // explicit if you still use material icons

// Outside BOM — explicit versions required:
implementation("androidx.lifecycle:lifecycle-runtime-compose:2.12.0-alpha03")
implementation("androidx.activity:activity-compose:1.14.0-alpha02")
```

This historical example does not choose a dependency policy for the project. Inspect the actual
versions and relevant release notes before changing dependencies.

---

## 6. Related reading

- [Compose notes](m3e/compose-api.en.md) / [中文](m3e/compose-api.md): optional implementation context.
- [API snapshot](compose-api-full.md): historical signatures and release notes.
- [Design judgment](m3e/design-system.en.md) / [中文](m3e/design-system.md): the primary design perspective.
- [Component judgment](m3e/components.en.md) / [中文](m3e/components.md): kit fit and custom design.
- [Motion intent](m3e/motion-physics.en.md) / [中文](m3e/motion-physics.md): design meaning independent of APIs.
