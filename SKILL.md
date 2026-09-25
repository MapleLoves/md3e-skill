---
name: md3e
description: "Design and review UI using the Material Design 3 Expressive (MD3E) design language, independent of implementation framework. Use for Material 3 / M3E visual direction, design philosophy, information hierarchy, expressive styling, component and UI Kit selection, custom interface design, and design critique. Apply design principles to the project's actual platform and UI Kit; implementation API documentation is optional context."
metadata:
  version: "2.0.0"
---

# Material Design 3 Expressive (MD3E)

Use this skill to make intentional UI design decisions: what users need to understand, what
should draw attention, and how visual and interaction choices support that purpose. The focus
is design awareness, judgment, and a coherent Material expressive language across frameworks.

M3E builds on Material 3 foundations. An interface can combine expressive treatments with
quieter patterns. A component's availability in a particular library does not define the
limits of the design language.

## Scope

- Establish or refine an MD3E visual direction, product character, or interaction language.
- Design or review hierarchy, grouping, navigation, color, typography, shape, and motion.
- Select suitable elements from the project's UI Kit and design missing patterns thoughtfully.
- Apply this direction while implementing UI in the project's existing technology stack.

Keep the user's scope and existing product conventions. A local UI improvement does not imply
a full redesign. This skill supplies neither a theme generator nor starter code templates.
Use the project's existing theme generation and token infrastructure when present.

## Design judgment

For substantial design work, read [Design awareness and judgment](references/m3e/design-system.en.md)
([中文](references/m3e/design-system.md)). For a small change, use the relevant criteria directly:

- **Purpose and values:** relate the design to the user's task, context, and desired product
  character. Make expression useful for comprehension, confidence, or an appropriate emotion.
- **Hierarchy and logic:** establish what matters first, what belongs together, and which
  action follows. Spend visual emphasis where it improves those relationships.
- **Language and strategy:** coordinate type, color, shape, space, and motion. Choose expressive
  intensity for this situation; a dense work surface and a milestone can need different treatment.
- **Ethics and inclusion:** keep choices understandable and usable. Avoid misleading emphasis,
  hidden alternatives, and decorative effects that undermine legibility or user control.

Treat these as decision criteria, not a mandatory questionnaire. A brief rationale for a
consequential choice is useful; a design essay for every edit is not.

## Working approach

Understand the relevant task and inspect the current screen, content, theme roles, and available
UI Kit before choosing a treatment. Use reasonable assumptions for small gaps and identify them
when they affect the result. Ask only when an unresolved choice materially changes the design.

Develop hierarchy and interaction meaning before choosing decorative treatments. Use
[Expressive design tactics](references/expressive-design-tactics.md) to connect a treatment to a
specific purpose, rather than applying every tactic to every screen.

### UI Kit and custom design

A UI Kit here means the components, styles, assets, and patterns actually provided or designated
for the project, not a particular platform library. Consult
[Component judgment](references/m3e/components.en.md) ([中文](references/m3e/components.md)) when fit
or customization is consequential.

- **Suitable:** use the matching kit element when its meaning, behavior, states, and presentation
  fit the task. Identify real available items; do not invent kit names or claim unseen assets exist.
- **Partly suitable:** compose or adapt existing elements where that preserves semantics and
  resolves the mismatch. Respect their interaction and accessibility contracts.
- **No suitable match:** develop a custom solution grounded in Material principles, the user's
  task, and the project's design language. Define the needed behavior and states as well as its
  appearance. A kit gap is a reason to design, not to force an unrelated component into the task.
- **Kit unavailable:** distinguish unavailable evidence from a confirmed missing component.
  Inspect project conventions or continue with a stated assumption; request a kit reference only
  when it materially affects the work. Do not introduce a new kit or framework by default.

Reuse meaningful subcomponents inside a custom composition where they still fit. Custom design
must solve a real mismatch, not merely seek novelty.

When implementation is requested, deliver it in the actual project stack. Map design roles and
behaviors to existing project tokens and components. Do not introduce Compose dependencies or
recreate a theme generator as a prerequisite to using this skill.

## Review and output

Deliver the artifact the user asked for. Where useful, briefly explain the intended hierarchy,
the significant kit reuse/customization decisions, and the tradeoff behind an unusual treatment.
Scale explanation to the task. Do not turn implementation requests into design advice alone.

Review whether emphasis supports the main task, secondary choices remain discoverable, related
elements feel coherent, and relevant states are understandable. Check the actual presentation
for readability, input/focus behavior, responsive needs, and reduced motion where applicable.
A token name or kit label alone does not establish usability. Distinguish what was inspected or
tested from what remains an assumption; do not claim user testing without conducting it.

## References: choose by design question

Read only what the current task needs. Prefer design meaning and applicable design specifications
over implementation API availability.

| Question | Reference |
| --- | --- |
| What should guide the design? | [Design awareness and judgment](references/m3e/design-system.en.md) / [中文](references/m3e/design-system.md) |
| How much expression, and where? | [Expressive tactics](references/expressive-design-tactics.md), [M3 and M3E](references/m3-vs-m3e-diff.md) |
| Does a kit element fit, or is custom design needed? | [Component judgment](references/m3e/components.en.md) / [中文](references/m3e/components.md), [Pattern catalog](references/components-catalog.md) |
| What should color, type, and shape communicate? | [Visual language](references/m3e/color-typography-shape.en.md) / [中文](references/m3e/color-typography-shape.md) |
| What should movement explain? | [Motion intent](references/m3e/motion-physics.en.md) / [中文](references/m3e/motion-physics.md) |
| Which roles or precise specifications apply? | [Design tokens](references/design-tokens.md), relevant pages under [design specifications](references/m3-content/index.md) |
| What evidence supports the decision? | [Research and verification](references/design-research.md) |

Curated notes are editorial guidance, with links to supporting sources. Dated design-page
snapshots retain their source and capture date (2026-09-14); older navigation pages retain inline
source headers without per-page dates. Editing this skill does not newly verify those sources.
Separate source requirements, this skill's recommendations, and project-specific decisions.

### Optional implementation appendix: Compose only

Only read these when the actual project uses Compose or the user explicitly asks about it:
[Compose notes](references/m3e/compose-api.en.md) / [中文](references/m3e/compose-api.md),
[version snapshot](references/version-baseline.md), and the
[androidx.compose.material3 API snapshot](references/compose-api-full.md).
They are secondary implementation references, not design requirements or dependency choices for
other platforms. Check the project's versions before applying historical API examples.
