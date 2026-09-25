# MD3E Design Awareness and Judgment

[中文](design-system.md)

This is an editorial synthesis of Material design resources, not an official taxonomy of
philosophy or a verbatim specification. Sources retain their capture dates in this repository.
The decision framework and examples below are this skill's recommendations.

## Design position

Use expression to help people understand, act, and connect emotionally. Understand the task,
content relationships, and product character before choosing visual intensity. Both bold and
restrained treatments can be intentional choices.

Applying M3E does not depend on a UI framework. Material foundations, project conventions, and
applicable platform behavior set the design context. A missing library implementation does not
make the corresponding design impossible.

## From ideas to decisions

| Dimension | Question | Design consequence |
| --- | --- | --- |
| Philosophy and conception | How does this interface help people understand and control their task? | Organize around task relationships before assembling components |
| Values | Does this situation need efficiency, confidence, exploration, or celebration? | Choose where and how strongly to express character; context can vary within a product |
| Principles | What should be noticed first, and what belongs together? | Coordinate emphasis, grouping, feedback, and consistency |
| Design thinking | Is the problem visual, or is it in the content or flow? | Address structure instead of decorating around the problem |
| Logic | Does visual importance match task importance? | Align reading order, action hierarchy, and state changes |
| Strategy | Which change improves the experience most, and at what cost? | Resolve important friction without turning every region into a focal point |
| Language | Do color, type, shape, space, and motion communicate the same relationship? | Establish recognizable roles and rhythms across screens |
| Ethics | Does emphasis respect informed choice? | Make alternatives, consequences, and exit paths understandable |

Use these questions to guide judgment, not as a questionnaire or required output structure.

## Hierarchy and expression

Identify the primary task, necessary information, and secondary choices in this situation.
Establish their relationships with scale, placement, space, type, and contrast before deciding
whether stronger shape or motion adds value. Keep equally important choices comparable; a
business preference does not justify making other choices difficult to discover.

Expression can concentrate on an action, a piece of content, or a state change. Stronger
expression does not mean increasing every color, corner radius, or bounce. Do not require a
fixed number of hero moments per product: purpose, frequency, and context determine the need.

Lists, forms, and dense work surfaces can express character through grouping, rhythm, and
clear states. At a meaningful success or progress moment, a visual change may reinforce the
meaning without hiding what the user can do next.

## Consistency through relationships

Consistency means related meanings receive related treatment; it does not require identical
appearance everywhere. Coordinate semantic colors, text roles, spacing relationships, and
interaction feedback. Give a purposeful reason for a local departure.

Respect the user's brand and the project's design system. Explain a conflict's concrete effect
and propose a tradeoff within scope rather than replacing the kit or product style unasked.
Use the project's theme infrastructure; this skill guides how its output supports hierarchy,
contrast, semantics, and context.

## UI Kit and original design

Use kit resources whose semantics and behavior fit. Superficial resemblance is insufficient.
When no pattern fits, design a composition or component from the task and design principles,
reusing suitable text styles, buttons, and state treatments within it.

See [Component selection and custom design](components.en.md). Kit use does not replace design
judgment, and original design still belongs to the project's design system.

## Inclusion and ethics

Make readability, comprehension, and operability part of the design. Consider text enlargement,
keyboard and touch input, assistive technology, language, and reduced motion as relevant to the
actual context. A specification label alone does not establish accessibility.

Do not distinguish essential states through color alone or let decoration overpower content.
For choices with consequences, align wording, emphasis, and feedback with their real meaning.
An exploratory surprise is inappropriate where the user needs certainty.

## Example of a decision

A habit tracker's daily entry screen needs scanning and repeated actions, while its weekly
summary may emphasize progress. The former can use rhythmic grouping and clear completion
states; the latter may give meaningful progress stronger type and a selective shape treatment.
They share semantic color and interaction feedback while varying expressive intensity.

If the kit lacks a suitable summary composition, design one around the content and reuse its
text styles and buttons. Do not force comparable information into separate, mutually hidden
carousel cards merely because a carousel exists. This illustrates contextual judgment, not a
required summary layout.

## Supporting sources

- [Applying M3 Expressive for usability](../m3-content/foundations/usability/applying-m3-expressive.md)
- [Accessibility principles](../m3-content/foundations/overview/principles.md)
- [User needs](../m3-content/foundations/building-for-all/user-needs.md)
- [Co-design](../m3-content/foundations/building-for-all/co-design.md)
- [Customization](../m3-content/foundations/customization.md)
- [Expressive design tactics](../expressive-design-tactics.md)

Consult the appropriate source before citing exact values, research findings, or platform
behavior. A recommendation is not a user-tested result, and static inspection does not establish
that an interaction works.
