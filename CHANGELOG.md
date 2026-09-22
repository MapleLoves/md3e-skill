# Changelog

All notable changes to this skill are documented here. The format is based on
[Semantic Versioning](https://semver.org/lang/zh-CN/) and the skill follows the
`MAJOR.MINOR.PATCH` scheme described in `PUBLISH.md`.

## [1.2.0] - 2026-09-22

Latest-content refresh from the verified knowledge base (baseline **2026-09-14**).

### Added
- `references/version-baseline.md` — version matrix, feature gates, BOM coverage, alpha-line
  churn log (`material3` 1.5.0-alpha28 / stable 1.4.0; icons, MotionScheme, ColorScheme rules).
- `references/m3e/` — five curated M3E notes (核对 2026-09-14): `design-system.md`,
  `color-typography-shape.md`, `motion-physics.md`, `components.md`, `compose-api.md`,
  plus English mirrors (`*.en.md`) for open-source accessibility.
- SKILL.md workflow step for version pinning; icon guidance (Material Symbols / explicit
  `material-icons-core`).

### Changed
- **`references/m3-content/` fully re-synced**: 249 pages replaced with clean browser-rendered
  Markdown from m3.material.io (front matter `source` / `captured: 2026-09-14`); removed old
  encoding artifacts and TOC noise. Navigation hub pages (`index`, `components`, `styles`, …) kept.
- `m3-vs-m3e-diff.md` — baseline banner; SplitButton / FilledTonalToggleButton / slot SearchBar /
  AppBarWithSearch; experimental-API removal on stable 1.4.0-beta01; alpha churn notes.
- `components-catalog.md` — version-line header; ButtonGroup/SplitButton/SearchBar updates.
- SKILL.md → **1.2.0**; README / README.zh-CN structure and feature lists updated.

### Fixed
- `m3e/compose-api.md` migration note: alpha line **is** covered by `compose-bom-alpha`
  (material3 / adaptive included in BOM POM — was incorrectly marked "not via BOM").

### Notes
- Full M3E still requires the **1.5.0-alpha** line; official warning: alpha/beta BOMs are not
  for production.

## [1.1.0] - 2026-08-03

Maintenance and quality pass to prepare the skill for public release.

### Changed
- **SKILL.md refined** for the official `skill-creator` "Concise is Key" principle: dropped the
  ~23-line `m3-content/` directory tree and ~55 lines of redundant resource summaries from the
  always-loaded context; reduced SKILL.md from 232 to 133 lines (~43% less trigger context).
- **Structured Workflow**: reorganized into a clear 6-step sequence with explicit script invocation
  (Step 2 + "Theme generator" block) and a standard `MaterialExpressiveTheme` scaffold.
- **Unified doc numbers**: `compose-api-full.md` cited as ~8,000 lines (measured 7,949) and
  `m3-content/` as 256 files across README / SKILL.md / PUBLISH.md (previously contradictory).
- **Fixed `assets/templates/` listing**: now correctly lists all 4 files (MD3ETheme / Color / Type /
  Shape) — `Shape.kt` was previously missing.

### Added
- `version: 1.1.0` field in SKILL.md frontmatter.
- `CONTRIBUTING.md`, `CHANGELOG.md`.
- `.gitignore` entries for `dist/`, `*.zip`, `output/`.

## [1.0.0] - 2026-08-03

First public release — Material Design 3 Expressive (MD3E) AI skill for Android
Jetpack Compose. Compatible with CodeBuddy, Cursor, Windsurf, and other assistants
that support the agent skill format.

### Added
- `SKILL.md` entry point: triggers, workflow, quick reference, and design principles.
- `references/compose-api-full.md` — full `androidx.compose.material3` API reference
  (~8,000 lines).
- `references/design-tokens.md` — color roles, type scale, shape scale, motion system.
- `references/components-catalog.md` — every M3/M3E component organized by category.
- `references/m3-vs-m3e-diff.md` — differences, migration guide, I/O 2026 updates.
- `references/expressive-design-tactics.md` — the 7 official M3E design tactics.
- `references/design-research.md` — color science, readability, motion, accessibility.
- `references/m3-content/` — mirror of m3.material.io (256 files).
- `assets/templates/` — ready-to-use `MD3ETheme.kt`, `Color.kt`, `Type.kt`, `Shape.kt`.
- `scripts/generate_theme.py` — seed color → complete Compose theme (HCT, with fallback).
- Bilingual README (`README.md` / `README.zh-CN.md`).
- Apache License 2.0.

[1.0.0]: https://github.com/mfskys/md3e-skill/releases/tag/v1.0.0
