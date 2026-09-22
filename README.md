# MD3E Skill

**[English](./README.md)** | **[中文](./README.zh-CN.md)**

A universal AI skill for building Android UI with **Material Design 3 Expressive (MD3E)** using **Jetpack Compose**. Works with any AI coding assistant that supports the skill format (CodeBuddy, Cursor, Windsurf, etc.).

## What is MD3E?

Material 3 Expressive is Google's 2025 evolution of Material Design 3, featuring:
- **Spring-based motion** (MotionScheme) replacing easing curves
- **Expanded color system** with 18 new Fixed color roles + 7 surface container roles
- **New components**: FloatingToolbar, ButtonGroup, SplitButton, WideNavigationRail, ToggleFloatingActionButton, FlexibleBottomAppBar, and more
- **Expressive design principles**: bolder colors, varied shapes, variable typography, container grouping

This skill covers **both MD3E and baseline M3** — many components only have M3 specs, so the skill uses MD3E where available and falls back to M3 otherwise.

**Knowledge baseline: 2026-09-14.** Full M3E component set requires `material3` **1.5.0-alpha28**;
stable **1.4.0** ships M3 + MotionScheme + partial Expressive only.

## Features

- **Complete API reference**: Full `androidx.compose.material3` package documentation (~8,000 lines)
- **Design tokens**: All color roles, type scale, shape scale, motion system values
- **Component catalog**: Every M3/M3E component organized by category with usage guidance
- **Version baseline**: Feature gates, alpha-line churn, BOM coverage (2026-09-14)
- **Curated M3E notes**: Design system, color/type/shape, motion physics, components, Compose API
- **M3 vs M3E diff**: Clear comparison and migration guide
- **Official spec mirror**: 249 clean Markdown pages from m3.material.io (captured 2026-09-14)
- **Code templates**: Ready-to-use `MD3ETheme.kt`, `Color.kt`, `Type.kt`, `Shape.kt`
- **Theme generator**: Python script to generate a complete color scheme from a single seed color

### Installation

Copy the `md3e/` directory to your AI assistant's skill folder. For example:

- **CodeBuddy**: `.codebuddy/skills/md3e/` (project-level) or `~/.codebuddy/skills/md3e/` (user-level)
- **Other AI assistants**: place in the corresponding skills/plugins directory

```
md3e/
├── SKILL.md
├── references/
├── assets/
└── scripts/
```

### Using the Theme Generator

```bash
python scripts/generate_theme.py --seed #6750A4 --package com.example.app --output ./theme/
```

Install `material-color-utilities` for accurate HCT-based color generation:

```bash
pip install material-color-utilities
```

## Skill Structure

```
md3e/
├── SKILL.md                          # Entry point: triggers, workflow, quick reference
├── references/
│   ├── version-baseline.md           # Version matrix, feature gates, alpha churn (2026-09-14)
│   ├── m3e/                          # Curated M3E notes (5 zh + 5 en mirrors, verified 2026-09-14)
│   │   ├── design-system.md          # Theming, dynamic color, system UI (+ design-system.en.md)
│   │   ├── color-typography-shape.md # Color / type / shape (+ color-typography-shape.en.md)
│   │   ├── motion-physics.md         # MotionScheme spring physics (+ motion-physics.en.md)
│   │   ├── components.md             # Component inventory by version line (+ components.en.md)
│   │   └── compose-api.md            # API gates, migration, alpha churn (+ compose-api.en.md)
│   ├── compose-api-full.md           # Complete official API reference (10K+ lines)
│   ├── design-tokens.md              # Color/typography/shape/motion/elevation tokens
│   ├── components-catalog.md         # All components by category with M3/M3E tags
│   ├── m3-vs-m3e-diff.md             # Differences + migration guide + IO2026 updates
│   ├── expressive-design-tactics.md  # 7 expressive design tactics with guidance
│   ├── design-research.md            # Color science, readability, motion patterns, a11y
│   └── m3-content/                   # Mirror of m3.material.io (249 pages, 2026-09-14)
│       ├── components/               # 37 components × overview/specs/guidelines/a11y
│       ├── styles/                   # color, motion, shape, typography, spacing...
│       └── foundations/              # layout, design tokens, watches, XR, a11y
├── assets/
│   └── templates/
│       ├── MD3ETheme.kt              # MaterialExpressiveTheme setup template
│       ├── Color.kt                  # Full 48-role color scheme template
│       ├── Type.kt                   # 15-style typography template
│       └── Shape.kt                  # 5-size shape scale template
└── scripts/
    └── generate_theme.py             # Seed color -> complete Compose theme
```

## Key APIs

| Category | M3 | MD3E |
|----------|----|------|
| Theme | `MaterialTheme` | `MaterialExpressiveTheme` |
| Color | `lightColorScheme()` / `darkColorScheme()` | + `expressiveLightColorScheme()` |
| Motion | Easing + duration tokens | `MotionScheme.standard()` / `.expressive()` |
| Opt-in | `@ExperimentalMaterial3Api` | + `@ExperimentalMaterial3ExpressiveApi` |

## Usage Examples

After installing the skill, just ask your AI assistant naturally. The skill auto-triggers on relevant requests:

**Theming setup:**
> "Set up Material 3 Expressive theming for my Compose app with dynamic color support"

**Component creation:**
> "Create a Material 3 Expressive floating toolbar with 3 action buttons"
> "Build a button group with overflow menu using MD3E"
> "Make a Material 3 card list following the design spec"

**Design guidance:**
> "What are the MD3E color roles and when to use each?"
> "What's the difference between M3 and M3E motion system?"
> "Which shape should I use for a FAB?"

**Migration:**
> "Migrate my app from MaterialTheme to MaterialExpressiveTheme"
> "Update my color scheme to include the new M3E fixed color roles"

**Theme generation:**
> "Generate a Compose color scheme from the seed color #6750A4"

## Sources

- [m3.material.io](https://m3.material.io/) — Official Material Design 3 Expressive guidelines
- [androidx.compose.material3](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary) — Official Compose Material 3 API reference
- [Compose Material 3 guide](https://developer.android.com/develop/ui/compose/designsystems/material3) — Official developer guide

## Disclaimer

This skill is for reference and educational purposes. The actual behavior of Material 3 Expressive components may vary depending on the Compose Material 3 library version. Always test in your own environment before relying on it for production.

## License

[Apache License 2.0](./LICENSE) — same as the Material Design components and AndroidX libraries.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to report issues, propose changes,
and submit pull requests.

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for the version history (SemVer).

