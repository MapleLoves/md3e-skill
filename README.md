# MD3E Skill

**[English](README.md)** | **[中文](README.zh-CN.md)**

An AI skill for **Material Design 3 Expressive (MD3E) UI design**, centered on design awareness,
visual language, and judgment. It works with the project's actual technology stack and does not
require Android or Jetpack Compose.

## What the skill contributes

- **Design philosophy and values:** connect product character and expressive intensity to user needs.
- **Design principles and logic:** establish hierarchy, grouping, interaction meaning, and clear feedback.
- **Visual language:** coordinate color, typography, shape, space, and motion with purposeful expression.
- **Ethics and inclusion:** preserve understandable choices, readability, operability, and user control.
- **UI Kit judgment:** use suitable components and styles, adapt partial matches, and design a grounded
  custom solution when no existing pattern fits.
- **Design references:** curated notes and source snapshots for component guidelines and exact specifications.

M3E builds on Material 3 foundations. The skill supports different expressive intensities within a
product and does not require every screen to use every expressive treatment. When implementation
is requested, design decisions are applied in the existing project stack.

## UI Kit and original design

A UI Kit means the resources actually provided or designated for the project. Inspect their
semantics, behavior, states, and presentation before selecting them.

1. Use a suitable kit component, style, or pattern where it fits the task.
2. Adapt or compose suitable resources when only part of the need is covered.
3. If no suitable match exists, design the missing composition or interaction from the task,
   Material principles, and project language, reusing useful primitives within it.

An unavailable kit is not proof that a component is absent. The skill distinguishes inspected
resources from assumptions and explains consequential reuse or custom-design choices briefly.

## Installation

Copy this repository's skill contents into a folder named md3e in your assistant's skill directory.
For example, a project using a .codebuddy/skills directory can place it at .codebuddy/skills/md3e/.
Use the location supported by your assistant; the entry point is [SKILL.md](SKILL.md).

The design skill requires no Python runtime, theme-generation script, or Kotlin templates.
Theme generation remains with the project's existing tools; this skill guides how the resulting
roles support hierarchy, contrast, and meaning.

When upgrading an existing installation, remove the retired generator and templates listed in
[the changelog](CHANGELOG.md). A file-copy update alone will not remove old files. Preserve any
project-specific content before cleaning an installation.

## Example requests

- “Give this web application's task page an MD3E visual direction using its current components.”
- “Review this screen's hierarchy and expressive intensity; explain the important tradeoffs.”
- “Use the project's UI Kit where appropriate, and design a custom comparison region if none fits.”
- “Make this settings page clear and expressive while keeping frequent actions efficient.”
- “Refine color, type, shape, and motion as one coherent language without changing the framework.”

A small edit should produce a focused result; it does not require a long design report. An
implementation request should produce implementation, with concise rationale where useful.

## Repository guide

| Resource | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Scope, design judgment, kit decisions, and reference routing |
| [Design awareness](references/m3e/design-system.en.md) / [中文](references/m3e/design-system.md) | Philosophy, values, principles, reasoning criteria, and ethics |
| [Component judgment](references/m3e/components.en.md) / [中文](references/m3e/components.md) | UI Kit fit and custom-design decisions |
| [Visual language](references/m3e/color-typography-shape.en.md) / [中文](references/m3e/color-typography-shape.md) | Color, typography, shape, space, and relationships |
| [Motion intent](references/m3e/motion-physics.en.md) / [中文](references/m3e/motion-physics.md) | Feedback, continuity, expressive intensity, and reduced motion |
| [Expressive tactics](references/expressive-design-tactics.md) | When and why to apply expressive treatments |
| [Pattern catalog](references/components-catalog.md) | Component selection by task and interaction meaning |
| [Token index](references/design-tokens.md) | Semantic roles and links to precise specifications |
| [M3 and M3E](references/m3-vs-m3e-diff.md) | Design continuity and expressive choices |
| [Design evidence](references/design-research.md) | Sources, hypotheses, and actual verification |
| [Official design snapshots](references/m3-content/index.md) | Component, style, and foundation reference pages |

### Optional Compose appendix

The [Compose notes](references/m3e/compose-api.en.md) / [中文](references/m3e/compose-api.md),
[version snapshot](references/version-baseline.md), and
[androidx.compose.material3 reference](references/compose-api-full.md) are secondary resources.
Read them only for an actual Compose project or an explicit API question. They do not choose the
project's framework or dependency versions and are not part of the default design workflow.

## Sources and scope

Material design guidance is the primary reference. Dated design-page snapshots retain their
source and capture date, **2026-09-14**. Older navigation pages retain inline source headers without
per-page dates. Curated notes distinguish editorial recommendations from source specifications. This revision reorganizes the skill; it does not claim a fresh verification
of every external page, research result, or Compose release.

See [contribution guidance](CONTRIBUTING.md) for maintenance and validation, and
[publishing guidance](PUBLISH.md) for release preparation. Repository validation is a maintainer
activity, not a prerequisite for using the design skill.

## License

[Apache License 2.0](LICENSE).
