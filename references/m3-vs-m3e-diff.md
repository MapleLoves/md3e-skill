# M3 and M3E: Design Continuity and Expressive Choices

This is a design comparison, not a dependency migration guide. M3E extends Material 3 foundations;
existing roles, interaction meanings, and suitable patterns remain useful. Do not assume that
baseline M3 is uniformly plain or that an expressive interface must replace every component.

The interpretation below draws on the bundled
[applying M3 Expressive](m3-content/foundations/usability/applying-m3-expressive.md) guidance.
Examples and adoption advice are this skill's editorial recommendations.

## What to carry forward and where to extend expression

| Dimension | Foundation to preserve | Expressive opportunity | Design question |
| --- | --- | --- | --- |
| Hierarchy | Clear relationships between content and actions | Stronger contrasts in scale, placement, color, or grouping | What deserves attention in this situation? |
| Color | Semantic roles and readable foreground/background relationships | Richer accent and surface relationships | Does contrast clarify purpose or create competition? |
| Typography | Understandable display, headline, title, body, and label roles | More distinctive emphasis and editorial composition | Is important content easier to find and read? |
| Shape | Consistent meaning and recognizable interaction targets | Purposeful variation, masks, and state-related morphing | Does the variation communicate a relationship? |
| Motion | Feedback, continuity, and user control | Fluid spatial transitions and selective expressive response | What does movement explain, and can it be reduced? |
| Components | Appropriate semantics, states, and usability | More flexible configurations or a custom composition | Does the pattern fit the task and the available kit? |
| Layout | Grouping, reading order, and useful adaptation | Deliberate contrast between focal and supporting regions | What should remain related or simultaneously visible? |

Color roles, type roles, or a framework feature may have histories distinct from the M3E design
update. Consult the relevant source before labeling a capability as M3E-only. A library version
is evidence about that implementation, not about every possible expression of the design.

## Adopting an expressive direction

Start with the actual problem: weak hierarchy, unclear feedback, undifferentiated content, or a
product character that is not coming through. Keep existing choices that already serve the task.

Use one or more expressive tactics where they address the problem. For example, strengthen the
primary action through its relationship to surrounding content, rather than enlarging every
button. If a form needs clarity, grouping and text hierarchy may matter more than decorative motion.

Reuse suitable kit patterns. Where no pattern fits, design the missing relationship or interaction
and reuse appropriate primitives. Implementation belongs to the project's chosen stack. There is
no requirement to switch frameworks, pin a Compose version, or reproduce Kotlin theme scaffolding.

## Different intensities within one product

A frequently used work surface may need restrained rhythm and stable positions; an important
summary can support stronger type and selective shape contrast. They can share the same semantic
roles and feedback language. Avoid prescribing all professional products as restrained or all
consumer products as playful: the immediate task and audience matter.

Review the result with realistic content, relevant input methods, and accessibility needs.
Stronger style alone is not evidence of better usability. Keep observed outcomes separate from
the intended design effect.

## Further reading

- [Design judgment](m3e/design-system.en.md) / [中文](m3e/design-system.md)
- [Expressive tactics](expressive-design-tactics.md)
- [Pattern selection](components-catalog.md)
- [Design token roles](design-tokens.md)
- [Official usability guidance](m3-content/foundations/usability/applying-m3-expressive.md)

For an actual Compose migration only, use the optional
[implementation notes](m3e/compose-api.en.md) / [中文](m3e/compose-api.md) and
[version snapshot](version-baseline.md). Those historical implementation details are not the
default path for applying this design language.
