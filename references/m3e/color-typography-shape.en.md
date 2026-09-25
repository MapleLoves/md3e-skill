# Color, Typography, Shape, and Space as Design Language

[中文](color-typography-shape.md)

These are design judgment notes. Linked official snapshots support the roles and specifications;
contextual recommendations are this skill's synthesis. Consult [tokens](../design-tokens.md) for
precise specifications when needed, without assuming an implementation framework.

## Establish relationships first

Color, type, shape, and space should jointly explain importance, belonging, and state. Identify
the important content and actions, then choose which dimensions carry emphasis. Placement or
space may make an action clear before stronger color or shape is needed. Avoid competing signals.

## Color: roles before values

- Use accent/content pairs for significant actions and container, surface, and secondary content
  roles for supporting relationships. Avoid filling every region with high-emphasis color or
  treating color names as fixed business priority levels.
- Distinguish brand, interaction, state, and grouping. Avoid conflicting nearby meanings for the
  same color. Errors and success need understandable text, icons, or another supporting cue.
- Preserve meaning and readability across light and dark themes, not identical values everywhere.
  Consider fixed roles when a stable tone across modes is useful, and inspect surrounding contrast;
  fixed roles do not mean a brand color is locked.
- Use roles from the project's existing generator and theme configuration. Evaluate actual
  foreground/background combinations, transparency, and states. Do not recreate theme generation
  code in this skill.

For example, a primary submit action should be easy to locate while secondary help remains
discoverable. Making help illegible is not a useful way to establish hierarchy.

Sources: [Color roles](../m3-content/styles/color/roles.md) and
[choosing a scheme](../m3-content/styles/color/choosing-a-scheme.md).

## Typography: make content structure readable

Use semantic display, headline, title, body, and label roles rather than a new style for every
paragraph. Emphasis should reflect actual importance: a key number may warrant stronger treatment,
while sustained reading needs a stable rhythm.

Consider weight, size, width, and line height together. Variable fonts offer expressive range but
are not a prerequisite for M3E. Confirm language coverage before choosing a font treatment. Chinese,
long labels, and mixed-language content require their own density and wrapping decisions.

Inspect real content, enlarged text, and constrained widths. Display treatments suit short focal
content; they should not turn an entire page of body text into a promotional headline.

Sources: [Applying type](../m3-content/styles/typography/applying-type.md),
[editorial treatments](../m3-content/styles/typography/editorial-treatments.md), and
[fonts](../m3-content/styles/typography/fonts.md).

## Shape: make differences meaningful

Let repeated shapes establish a family, reserving purposeful differences for emphasis or
distinction. Rounded, angular, and abstract silhouettes can work together when they help identify
hierarchy, categories, or interaction rather than randomly changing corner radii.

Distinguish image masks, containers, and interaction targets. A decorative crop is not necessarily
a suitable button shape. When a morph communicates state or object relationships, keep labels and
operable regions clear and stable.

Sources: [Shape principles](../m3-content/styles/shape/overview-principles.md) and
[shape morph](../m3-content/styles/shape/shape-morph.md).

## Space and containers: organize reading rhythm

Space, alignment, and proximity can group content by themselves. Add surface treatments, containers,
or dividers when a clearer boundary helps; do not place every sentence in a card. Contents within
a container should have a meaningful relationship.

Density follows the task: comparison needs simultaneous visibility, while browsing may allow a
more spacious rhythm. At different widths, preserve reading and task order by reorganizing content
relationships rather than only stretching elements.

Sources: [Spacing](../m3-content/foundations/layout/grids-spacing/spacing.md),
[density](../m3-content/foundations/layout/grids-spacing/density.md), and
[adaptive design](../m3-content/foundations/layout/layout-overview/adaptive-design.md).

## Working with the UI Kit

Use suitable kit styles and semantic tokens. For new compositions, preserve shared roles and
rhythm and explain the purpose of departures from defaults. Exact values depend on the selected
specification, font, component, and platform units. Library defaults are not the complete set of
cross-platform design rules.
