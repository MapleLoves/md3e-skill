---
name: md3e
description: "Material Design 3 Expressive (MD3E) design system skill for Android Jetpack Compose. This skill should be used when building Android UI with Material 3 / Material 3 Expressive design language, including theming (color schemes, typography, shapes, motion), component implementation (buttons, cards, navigation, FAB, floating toolbar, button group, etc.), and design guidance (when to use which component, M3 vs M3E differences, expressive design principles). Covers both MD3E (the evolution released 2025, targeting Android 16) and baseline M3 (many components only have M3 specs). Triggers on requests like Material 3 Expressive, MD3E, Material Design 3, M3 theme, MaterialExpressiveTheme, Compose Material 3 component, or when designing/building Android UI that should follow Google Material design guidelines."
---

# Material Design 3 Expressive (MD3E) Skill

## Overview

This skill provides comprehensive knowledge of Google's Material Design 3 Expressive (MD3E)
design system and its implementation in Android Jetpack Compose (`androidx.compose.material3`).
MD3E is the evolution of Material Design 3, released in 2025, with research-backed updates to
theming, components, motion, typography, and shapes. It targets Android 16 but is available via
the Compose Material 3 library (1.5.0-alpha+) for lower API levels.

**Design philosophy:** MD3E emphasizes "expressive UX" — using bolder colors, varied shapes,
spring-based physics motion, and variable typography to create engaging, emotionally connected,
and personalized user experiences. It moves beyond M3's uniform, restrained aesthetic toward
designs that guide user attention through visual hierarchy.

**M3 vs M3E:** MD3E is an *expansion* of M3, not a replacement. Many components still only have
M3 specs. This skill covers both: prefer MD3E APIs and principles where available, fall back to
M3 for components not yet updated.

## When to Use This Skill

- Building any Android UI with Jetpack Compose that should follow Material design guidelines
- Setting up Material theming (color scheme, typography, shapes, motion scheme)
- Implementing or customizing Material components (buttons, cards, navigation, FAB, etc.)
- Migrating from M2 to M3, or from M3 to M3E (MaterialExpressiveTheme)
- Answering questions about Material 3 / M3E design specs (color roles, type scale, shape scale)
- Designing expressive UI with new MD3E components (FloatingToolbar, ButtonGroup, SplitButton,
  WideNavigationRail, ToggleFloatingActionButton, FlexibleBottomAppBar, etc.)
- Reviewing UI for Material design compliance

## Quick Reference: Key MD3E APIs

| Category | M3 (baseline) | MD3E (expressive) |
|----------|---------------|-------------------|
| Theme | `MaterialTheme` | `MaterialExpressiveTheme` |
| Color scheme | `lightColorScheme()` / `darkColorScheme()` | `expressiveLightColorScheme()` |
| Motion | (easing + duration tokens) | `MotionScheme.standard()` / `MotionScheme.expressive()` |
| Shapes | `Shapes(extraSmall, small, medium, large, extraLarge)` | (same, with more varied usage) |
| Experimental opt-in | `@ExperimentalMaterial3Api` | `@ExperimentalMaterial3ExpressiveApi` |

### MD3E-Only Components (require `@ExperimentalMaterial3ExpressiveApi` unless graduated)

- `HorizontalFloatingToolbar` / `VerticalFloatingToolbar` — floating contextual toolbars
- `ButtonGroup` — connected button row with overflow menu
- `SplitButtonLayout` — split button with primary + overflow actions
- `WideNavigationRail` / `ModalWideNavigationRail` — expanded navigation rail for large screens
- `ToggleFloatingActionButton` — FAB that toggles between two states with morph animation
- `FloatingActionButtonMenu` — FAB that expands into a menu
- `FlexibleBottomAppBar` — bottom app bar with flexible arrangement
- `MediumFlexibleTopAppBar` / `LargeFlexibleTopAppBar` — flexible top app bars
- Expressive list items (non-interactive variants)
- Expressive TimePicker

## Workflow

### 1. Setting Up Theming

To create an MD3E-themed app, use `MaterialExpressiveTheme` instead of `MaterialTheme`:

```kotlin
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialExpressiveTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.expressiveLightColorScheme
import androidx.compose.material3.MotionScheme
import androidx.compose.material3.Typography
import androidx.compose.material3.Shapes
import androidx.compose.runtime.Composable

@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    MaterialExpressiveTheme(
        colorScheme = if (darkTheme) darkColorScheme() else expressiveLightColorScheme(),
        motionScheme = MotionScheme.expressive(),  // or MotionScheme.standard()
        typography = AppTypography,
        shapes = AppShapes,
        content = content
    )
}
```

For custom brand colors, define a `lightColorScheme()` / `darkColorScheme()` with all color roles.
See `references/design-tokens.md` for the complete color role list and `assets/templates/` for
ready-to-use template files.

### 2. Choosing Components

Consult `references/components-catalog.md` for the full component list organized by category,
with M3/MD3E tags, key parameters, and usage guidance.

### 3. Applying Design Tokens

All token values (color roles, type scale, shape scale, motion) are documented in
`references/design-tokens.md`. Use `MaterialTheme.colorScheme.*`, `MaterialTheme.typography.*`,
`MaterialTheme.shapes.*`, and `MaterialTheme.motionScheme.*` to access them.

### 4. Detailed API Lookup

For full API signatures of any component or function, search the complete API reference:
`references/compose-api-full.md` (10000+ lines, the official `androidx.compose.material3`
package documentation). Use grep patterns like:
- `### ComponentName` to find a specific composable's definition
- `fun lightColorScheme` / `fun darkColorScheme` for color scheme builders
- `MaterialExpressiveTheme` for the expressive theme
- `MotionScheme` for motion scheme details
- `class ButtonColors` / `class CardColors` for color/elevation classes

### 5. Official Design Specs Lookup

For detailed design specifications (variants, anatomy, color roles, states, measurements,
baseline tokens), search the official m3.material.io content mirrored in
`references/m3-content/`. Structure:

```
m3-content/
├── components/          # 37 component dirs, each with overview/specs/guidelines/accessibility
│   ├── buttons/         # overview.md, specs.md, guidelines.md, accessibility.md
│   ├── toolbars/        # (M3E new component)
│   ├── button-groups/   # (M3E new component)
│   ├── split-button/    # (M3E new component)
│   ├── fab-menu/        # (M3E new component)
│   ├── loading-indicator/ # (M3E new component)
│   └── ...              # all other components
├── styles/              # color, motion, shape, typography, elevation, spacing, icons
│   ├── color/           # 14 docs: system overview, roles, dynamic color, custom colors, etc.
│   ├── motion/          # motion overview, patterns, spring physics, transitions
│   ├── shape/           # shape overview, principles, 35 shape library
│   ├── typography/      # type scale, emphasized styles, variable fonts
│   └── spacing/         # 8dp spacing system (IO 2026)
├── foundations/         # layout, design tokens, accessibility, watches, XR, customization
│   ├── layout/          # 21 docs: scaffold, grids, breakpoints, canonical examples, RTL
│   ├── design-tokens/   # token system overview
│   ├── watches/         # Wear OS design guidance
│   └── xr/              # immersive XR design guidance
└── develop/             # developer guidance
```

To find a component's spec, read `references/m3-content/components/{component-name}/specs.md`.
To find color/shape/motion/typography guidance, read the corresponding file under
`references/m3-content/styles/`.

## Resources

### references/

- **`compose-api-full.md`** — Complete official `androidx.compose.material3` package API
  reference (10000+ lines). Contains every composable, class, interface, function, property,
  and the full Compose Material 3 guide + changelog. Search with grep for specific APIs.

- **`design-tokens.md`** — Extracted design token values: all color roles (M3 + M3E fixed
  variants + surface containers), type scale (15 styles with sizes/weights/line heights),
  shape scale (5 sizes with dp values), motion system (spring physics, MotionScheme presets,
  easing/duration tokens), and elevation guidelines.

- **`components-catalog.md`** — Organized component catalog by category (buttons, cards,
  navigation, input, feedback, etc.) with M3/MD3E tags, key composables, color roles, shapes,
  and usage notes.

- **`m3-vs-m3e-diff.md`** — Side-by-side comparison of M3 and M3E: what changed, what's new,
  what stayed the same, migration guidance, and Google I/O 2026 updates (Expressive layout
  system, spacing system, Compose-first direction, 14 component list, 7 design tactics).

- **`expressive-design-tactics.md`** — The 7 official M3E design tactics (shape variety, rich
  color, typography emphasis, container grouping, fluid motion, component flexibility, hero
  moments) with principles, do/caution guidance, code examples, and research backing.

- **`design-research.md`** — Research-backed foundations from Google's blog: HCT color science,
  dynamic color harmony algorithm, tone-based surface colors, Roboto Flex variable fonts (12 axes),
  readability research (grade for light/dark mode), 4 motion transition patterns, accessibility
  foundations, large screen design, and Figma design kit reference.

- **`m3-content/`** — Complete mirror of m3.material.io official design guidelines (260 files).
  Contains detailed specs for every component (overview/specs/guidelines/accessibility), all style
  systems (color/motion/shape/typography/elevation/spacing), and foundations (layout/tokens/
  accessibility/watches/XR). This is the authoritative source for design questions. Search by
  reading `m3-content/components/{name}/specs.md` for component specs or
  `m3-content/styles/{category}/` for style system details.

### assets/templates/

Ready-to-use Kotlin template files for Compose theming:

- **`MD3ETheme.kt`** — Complete `MaterialExpressiveTheme` setup with dynamic color support,
  custom typography, shapes, and motion scheme.
- **`Color.kt`** — Color definitions and `lightColorScheme()` / `darkColorScheme()` builders
  with all M3E color roles including fixed variants.
- **`Type.kt`** — `Typography` definition with all 15 type scale styles.

Copy these into an Android project's `ui/theme/` package and customize.

### scripts/

- **`generate_theme.py`** — Generates a complete Compose color scheme (Color.kt + Theme.kt)
  from a single seed color. Uses the Material Color Utilities algorithm (HCT color space) to
  derive all color roles. Outputs both light and dark schemes.

  Usage: `python generate_theme.py --seed #6750A4 --package com.example.app --output ./theme/`

## Design Principles (MD3E)

1. **Color as hierarchy** — Use color roles (primary/secondary/tertiary + containers + surface
   tones) to create visual layers, not just decoration. MD3E adds `*Fixed` color roles that
   don't change between light/dark modes.

2. **Shape variety** — Break from uniform corners. Mix shapes (rounded, pill, angular) to
   create visual tension and guide attention. MD3E introduces shape morph animations.

3. **Spring-based motion** — Replace easing curves with spring physics (stiffness/damping).
   Use `MotionScheme.expressive()` for bouncy, lively animations; `MotionScheme.standard()`
   for subtle, professional motion.

4. **Variable typography** — Use font weight, size, color, and spacing to create editorial-style
   hierarchy. Emphasize key actions and information with bolder type.

5. **Container grouping** — Group related content in containers with surface tones and spacing
   to reduce cognitive load and guide attention.

6. **Adaptive components** — Components should adapt to screen size (foldables, tablets).
   Use `WideNavigationRail` on larger screens, `NavigationBar` on compact screens.

7. **Highlight moments** — Create 1-2 memorable, delightful interaction moments per product
   (e.g., celebration animations, morphing shapes) that connect emotionally with users.
