# Expressive Design Tactics

Use expressive treatments to make meaningful relationships noticeable. This note interprets the
seven tactics discussed in Material's [M3E introduction](https://m3.material.io/blog/building-with-m3-expressive)
through the bundled [usability guidance](m3-content/foundations/usability/applying-m3-expressive.md).
The contextual examples and tradeoffs below are editorial recommendations, not mandatory recipes.

## Select tactics for a purpose

| Tactic | Design purpose | Useful application | When to restrain it |
| --- | --- | --- | --- |
| Vary shapes | Distinguish a focal object or establish a recognizable family | Give a meaningful action a silhouette distinct from supporting containers | Arbitrary variation makes related controls look unrelated |
| Use rich, nuanced color | Express emphasis, grouping, and state through role relationships | Pair a prominent action with supporting surface tones and readable content colors | Every saturated region competes with the main task |
| Guide attention with typography | Make importance and reading order visible | Emphasize a key result or headline while keeping supporting text steady | Long text, dense comparison, or narrow widths need sustained readability |
| Contain related content | Make belonging and boundaries understandable | Group information and its action with space, alignment, and a suitable surface | Repeated nested cards can fragment one continuous task |
| Add fluid motion | Explain feedback, continuity, or a meaningful state change | Connect an expanded object to its origin or acknowledge completion | Frequent input, reduced-motion preferences, or unrelated destinations need simpler treatment |
| Use component flexibility | Fit the task to space, input, and context | Reorganize navigation or related panes while preserving meaning | A larger viewport alone is not a reason to add panels or complexity |
| Combine tactics at meaningful moments | Concentrate expression on something the user values | Give an important achievement a clear focal composition | Do not make every interaction a celebration or impose a fixed number of hero moments |

A useful treatment has an identifiable job. Choose only the tactics that contribute to it;
there is no requirement to use all seven.

## Shape and color carry relationships

Start from a coherent family and use contrast deliberately. A distinctive shape can signal an
action or frame imagery; it should not make a decorative object look accidentally interactive.
Use semantic color pairs and actual contrast, rather than choosing a color merely because it is
vibrant. Fixed accent roles and surface roles are part of the color vocabulary; do not infer their
history or availability from a library release label.

Sources: [Shape principles](m3-content/styles/shape/overview-principles.md),
[shape morph](m3-content/styles/shape/shape-morph.md), and [color roles](m3-content/styles/color/roles.md).

## Typography and containment create an editorial hierarchy

Give the main information enough space and a suitable text role. Let supporting information form
readable groups. A content-led composition can be expressive without extra ornament: for example,
a clear numerical result, a short interpretation, and a well-associated next action.

Do not confuse every larger container with higher task priority. Surface tones, whitespace,
placement, and type work together; actual light/dark appearance must be inspected.

Sources: [Editorial typography](m3-content/styles/typography/editorial-treatments.md) and
[spacing](m3-content/foundations/layout/grids-spacing/spacing.md).

## Motion and adaptation preserve meaning

Movement can make a relationship clear, but it must not delay an action or become the only state
cue. Adapt layout by the content that needs to remain related or comparable, preserving focus and
task position when relevant. Reuse suitable kit patterns; create a new composition when none fits.

Sources: [Motion intent](m3e/motion-physics.en.md),
[adaptive design](m3-content/foundations/layout/layout-overview/adaptive-design.md), and
[kit fit](m3e/components.en.md).

## Example: a progress summary

Suppose a learning product needs a weekly summary. A strong number and headline can establish the
main outcome; a shared container can relate it to supporting detail; selective shape and color can
express the product's character. A small transition may reinforce completion if it suits the use
context. Comparable results should remain visible together.

Use the kit's suitable type and action styles. If no summary pattern fits, design the composition
from these relationships. Do not insert an unrelated carousel, giant button, or animation simply
because the kit provides it. This is a contextual proposal, not a required layout.

## Evaluate the result

Ask whether users can identify the important information and next action, whether secondary
choices remain understandable, and whether the design still works with real content and relevant
accessibility settings. Research about expressive treatments does not guarantee the same outcome
for a new screen; distinguish a design hypothesis from actual user evidence.
