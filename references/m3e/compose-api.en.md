# Optional Appendix: Compose API and Migration

Read only when the actual project uses Compose or the user explicitly asks about it. This is
secondary implementation context, not the boundary of MD3E design or a dependency requirement
for another stack.

Original verification date: **2026-09-14**. Version records were not reverified in this revision
and are not a claim about current releases. Original sources: Compose Material 3 release notes
and the Compose developer guide. Choose dependencies for the actual project; do not default to
alpha or require an upgrade. Start with [design judgment](design-system.en.md); see the
[historical version snapshot](../version-baseline.md) for implementation context.

## 1. Version gates quick reference

| Capability | Minimum version | Stability |
| --- | --- | --- |
| `MaterialTheme` (colorScheme / typography / shapes) | Early M3 | ✅ Stable |
| Dynamic color (`dynamicLightColorScheme` etc.) | Early M3, needs **API 31+** | ✅ Stable |
| Component animations switch to `MotionScheme` | **1.4.0** | ✅ Stable |
| `MotionScheme.standard()` / `expressive()` | Since 1.4.0-alpha02 (renamed from `standardMotionScheme`/`expressiveMotionScheme`) | Version-dependent |
| `MaterialExpressiveTheme`, `expressiveLightColorScheme` | 1.5.0-alpha18 | ⚠️ alpha |
| `ToggleButton` / FAB Menu | 1.4.0-alpha19 | ⚠️ alpha line |
| `ButtonGroup` | 1.4.0-alpha22 | ⚠️ alpha line |
| `SplitButton` | 1.4.0-alpha20 | ⚠️ alpha line |
| Flexible TopAppBar family / `FlexibleBottomAppBar` | 1.5.0-alpha23 | ⚠️ alpha line |
| `FloatingToolbar` | 1.5.0-alpha22 | ⚠️ alpha line |
| `SearchBarState` + slot `SearchBar` | 1.5.0-alpha24 | ⚠️ alpha line |
| `carouselParallaxScrollEffect` | 1.5.0-alpha28 | ⚠️ alpha line |
| `material3-ripple` | 1.5.0-alpha24 | ⚠️ alpha line (separate library) |

**Snapshot record**: **at the recorded date, the full M3E component set was on the alpha line**.
The stable line (1.4.0) ships "M3 + MotionScheme + partial Expressive" without the full M3E new components.

---

## 2. Breaking changes on the stable line (1.4.0)

| Change | Impact / handling |
| --- | --- |
| **`material-icons-core` transitive dependency removed** | Declare icon dependencies **explicitly** (I735ff, b/349894318) |
| **`androidx.compose.material.icons` discouraged** | Officially recommend Material Symbols vectors from fonts.google.com/icons |
| `NavigationBarItem` / `NavigationRailItem` selected label color | `onSurface` → **`secondary`**; to restore set `selectedTextColor = MaterialTheme.colorScheme.onSurface` manually |
| Component animation mechanism | All moved to **`MotionScheme`** |
| **1.4.0-beta01 removed all public APIs under `ExperimentalMaterial3ExpressiveApi` / `ExperimentalMaterial3ComponentOverrideApi`** | To keep using them, switch to **1.5.0-alpha** |

---

## 3. Implementation and migration within the project

- Inspect project dependencies and intended design; consult versioned APIs only for needed features.
- Reuse existing theme generation, color roles, and configuration. Do not require a theme scaffold or regenerate theme files.
- Select available components for their design purpose rather than changing the entire stack to obtain an API name.
- Custom interactions should share project motion and state language; verify signatures against actual dependencies.
- Keep migration within scope, retain suitable components, and check affected themes, sizes, and states.

---

## 4. Alpha-line API churn (risk notice)

The 1.5.0-alpha line saw **many renames and removals** over months, e.g.:

| Version | Change |
| --- | --- |
| alpha28 | Stateless `Slider`/`RangeSlider` overloads deprecated; `RangeSliderState` field renames |
| alpha27 | Old `TopAppBarDefaults` scrollBehavior overloads removed; `LocalMotionScheme` removed; `RichTimePickerDialog` → `VibrantTimePickerDialog` |
| alpha26 | `ExposedDropdownMenu` becomes an extension function (**update imports**) |
| alpha25 | `TonalToggleButton` → `FilledTonalToggleButton`; ComponentOverride API removed; `SplitButtonLayout` deprecated |
| alpha24 | `SearchBarState` stable; `material3-ripple` new library |
| alpha23 | ComponentOverride API removed; Expressive AppBar graduated; `TextFieldLabelPosition.Attached` deprecated |
| alpha20 | BottomSheet remember APIs unified |
| alpha18 | `rememberWithGapSearchBarState` renamed; opt-in-free `Material3ExpressiveApi` provided |

**Conclusion**: when using alpha components, **read that version's release notes before upgrading**,
and keep call sites centralized (wrap in your own facade) to limit rename fallout.

---

## 5. Design checks during implementation

| Constraint | Notes |
| --- | --- |
| Color pairs | `primary`+`onPrimary`, `primaryContainer`+`onPrimaryContainer`; official counter-example: `tertiaryContainer` + `primaryContainer` insufficient contrast |
| Font scale | After system font scaling, verify no overflow/clipping |
| Reduced motion | Provide suitable simplified feedback for platform preferences while preserving essential state information |
| Semantics | Preserve built-in semantics; add labels, roles, and states where needed without duplicate announcements |

---

## 6. Verify for the actual task

Consult [Material design snapshots](../m3-content/index.md) for design specifications and their
source/capture dates. Use the [API snapshot](../compose-api-full.md) for signatures, matching them
to the project dependency. If versions differ, consult the relevant release notes; an old table
cannot establish availability in a newer release. Verify shape, motion, or component-state
implementation details only when the current task needs them.
