# Design Tokens: Meaning, Selection, and Specification Lookup

This is a framework-independent role index. Use tokens to preserve design meaning and coherent
relationships, not as a checklist of values to apply everywhere. Detailed numeric tables remain
in the linked official snapshots; this note does not duplicate them as universal defaults.

Read [visual language](m3e/color-typography-shape.en.md) or [中文](m3e/color-typography-shape.md)
when the question is what a treatment should communicate rather than which value to retrieve.

## Color roles

Choose a role for its purpose, then use the actual project's theme values. Naming varies between
kits; map by semantics instead of assuming a particular property name exists.

| Role family | Design use | Relationship to preserve |
| --- | --- | --- |
| primary / onPrimary | A prominent accent and content on that accent | Legible foreground/background pairing and purposeful emphasis |
| primaryContainer / onPrimaryContainer | A related container and its content | Distinction from both the accent and surrounding surfaces |
| secondary and corresponding on/container roles | Supporting accents and related content | A coherent relationship to primary emphasis, not a fixed business priority |
| tertiary and corresponding on/container roles | Complementary expression or a distinct accent | Meaningful distinction without competing with every primary action |
| error and corresponding on/container roles | Error information and related surfaces | Clear wording or another cue in addition to color |
| surface / onSurface / onSurfaceVariant | Base regions and readable content | Content hierarchy across real light and dark appearances |
| surfaceContainerLowest through surfaceContainerHighest | Tonal grouping and containment | A consistent surface system rather than a universal task-priority ranking |
| surfaceBright / surfaceDim | Surfaces with particular relative brightness needs | Readability and separation in each theme |
| outline / outlineVariant | Boundaries and supporting separation | Adequate distinction for the actual interactive or structural purpose |
| inverseSurface / inverseOnSurface / inversePrimary | Content presented against an inverse surface | A deliberate local relationship, not arbitrary inversion |
| fixed / fixedDim / onFixed / onFixedVariant families | Accent relationships with stable tone across light/dark modes | Correct paired content and contrast with surrounding surfaces |
| scrim | Separation behind an overlay | Clear foreground focus without losing necessary context |

Fixed roles do not promise an unchanged brand hue across every generated palette. Likewise,
choosing a role name does not prove that custom opacity, imagery, or state combinations are
readable. Inspect actual combinations. Use the project's existing theme generator when available;
this skill does not supply or recreate one.

Sources: [Color roles](m3-content/styles/color/roles.md),
[color system](m3-content/styles/color/system/how-the-system-works.md),
[choosing a scheme](m3-content/styles/color/choosing-a-scheme.md), and
[adjusting existing colors](m3-content/styles/color/advanced/adjust-existing-colors.md).

## Typography roles

| Role | Typical communication need | Judgment |
| --- | --- | --- |
| Display | Short focal text or a significant number | Use where prominence is deserved and space supports it |
| Headline | Section or page-level emphasis | Establish hierarchy without overpowering the task |
| Title | A named region, item, or content group | Keep comparable items at comparable levels |
| Body | Sustained reading or explanation | Prioritize reading rhythm, language coverage, and scale behavior |
| Label | A control, caption, or compact annotation | Keep action meaning and state legible |

Select size and emphasis in context. The actual font, language, line length, and component affect
fit. A type scale is a shared vocabulary, not a requirement to use every style on each screen.
Use target-platform text units and scaling behavior; do not blindly substitute pixels for the
units in a reference table.

Precise values: [Type scale tokens](m3-content/styles/typography/type-scale-tokens.md).
Application: [Applying type](m3-content/styles/typography/applying-type.md),
[editorial treatments](m3-content/styles/typography/editorial-treatments.md), and
[text resizing](m3-content/foundations/writing/text-resizing.md).

## Shape, space, and elevation

Choose a shape family to express relatedness; use a contrast in shape for a reason. The shape
scale, component-specific shapes, and decorative masks serve different purposes. Do not infer a
component's radius from a generic library theme slot.

Use spacing to establish proximity, rhythm, and density. Choose containers or elevation where
separation or depth is useful. A darker surface, a larger radius, or a stronger shadow does not
by itself define higher task importance.

| Need | Specification | Design context |
| --- | --- | --- |
| Corner sizes | [Corner radius scale](m3-content/styles/shape/corner-radius-scale.md) | [Shape principles](m3-content/styles/shape/overview-principles.md) |
| Spacing values | [Spacing tokens](m3-content/styles/spacing/tokens.md) | [Applying spacing](m3-content/styles/spacing/applying-spacing.md) |
| Layout density | [Density guidance](m3-content/foundations/layout/grids-spacing/density.md) | [Grids and spacing](m3-content/foundations/layout/grids-spacing/overview.md) |
| Elevation values | [Elevation tokens](m3-content/styles/elevation/tokens.md) | [Applying elevation](m3-content/styles/elevation/applying-elevation.md) |

## Motion roles

First identify what moves and why: object position, size, and shape communicate spatial
relationships; color and opacity communicate appearance and state. Share rhythm across related
interactions while accounting for scope and purpose. Use project motion tokens rather than
copying unverified spring parameters.

Guidance: [Motion intent](m3e/motion-physics.en.md) / [中文](m3e/motion-physics.md).
Exact specifications: [Motion](m3-content/styles/motion/overview/specs.md) and
[easing and duration](m3-content/styles/motion/easing-and-duration/tokens-specs.md).

## Adaptive layout

Viewport width is one input to design, alongside content, input method, text size, and task
relationships. Use the relevant [breakpoint guidance](m3-content/foundations/layout/breakpoints/overview.md)
and [canonical layouts](m3-content/foundations/layout/canonical-examples/overview.md).
Map their intent to the actual platform rather than requiring a library's navigation scaffold.

## Working with specifications

Consult the selected component's specification for measurements and state behavior. Preserve the
source's units and scope when citing values. If the kit or project differs, make the difference
explicit and resolve it against the task instead of silently treating either as a universal rule.
The [token foundations](m3-content/foundations/design-tokens/overview.md) explain the underlying
concept; [token use](m3-content/foundations/design-tokens/how-to-use-tokens.md) gives further context.
