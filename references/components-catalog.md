# Material Component and Pattern Catalog

Select components by the problem they solve. Names below describe design patterns, not required
functions or framework dependencies. The linked guidelines retain their official source and
capture date. Exact anatomy, measurements, states, and accessibility guidance are in the sibling
specs.md and accessibility.md files for each component.

For UI Kit reuse, adaptation, and original design decisions, read
[Component judgment](m3e/components.en.md) / [中文](m3e/components.md).
Use an expressive variant only when its treatment helps the task and fits the project; a library
release label is not a design-selection criterion.

## Actions

| Pattern | Appropriate purpose | Important distinction |
| --- | --- | --- |
| [Buttons](m3-content/components/buttons/guidelines.md) | A clearly named action | Match emphasis to importance; a filled treatment is not required for every action |
| [Icon buttons](m3-content/components/icon-buttons/guidelines.md) | A compact, recognizable action or toggle | Ambiguous meaning needs a label or other clear explanation |
| [Floating action button](m3-content/components/floating-action-button/guidelines.md) | A significant, readily available action | It must relate clearly to the current task and avoid covering content |
| [Extended FAB](m3-content/components/extended-fab/guidelines.md) | A prominent action that benefits from visible wording | Its size and persistence should be justified by the context |
| [FAB menu](m3-content/components/fab-menu/guidelines.md) | Related actions revealed from a focal control | Discovery, focus, and dismissal must remain understandable |
| [Button group](m3-content/components/button-groups/guidelines.md) | A related set of controls | Grouping does not by itself define exclusive or multiple selection |
| [Split button](m3-content/components/split-button/guidelines.md) | A default action plus related alternatives | Distinguish performing the action from opening alternatives |
| [Toolbars](m3-content/components/toolbars/guidelines.md) | Actions associated with content or the current context | Placement should preserve the relationship to the affected content |

## Navigation and discovery

| Pattern | Appropriate purpose | Important distinction |
| --- | --- | --- |
| [App bars](m3-content/components/app-bars/guidelines.md) | Page context and related navigation or actions | Avoid overcrowding the title and key controls |
| [Navigation bar](m3-content/components/navigation-bar/guidelines.md) | Persistent access to primary destinations | Navigation changes location; it is not a generic action row |
| [Navigation rail](m3-content/components/navigation-rail/guidelines.md) | Persistent destinations with room for a side structure | Choose form by space and task, retaining clear destination identity |
| [Navigation drawer](m3-content/components/navigation-drawer/guidelines.md) | A destination structure suited to a larger or revealed panel | Decide whether hiding the structure impairs frequent navigation |
| [Tabs](m3-content/components/tabs/guidelines.md) | Related peer content views | Preserve scope and selected state; do not use as arbitrary button styling |
| [Search](m3-content/components/search/guidelines.md) | Finding content within a defined scope | Query, results, empty results, and return behavior belong to the design |

## Input and selection

| Pattern | Appropriate purpose | Important distinction |
| --- | --- | --- |
| [Text fields](m3-content/components/text-fields/guidelines.md) | Entering or editing text | Labels, format expectations, errors, and existing values must remain clear |
| [Checkbox](m3-content/components/checkbox/guidelines.md) | Independent or multiple selections | Do not imply mutually exclusive choice |
| [Radio button](m3-content/components/radio-button/guidelines.md) | One choice among alternatives | Make the group relationship understandable |
| [Switch](m3-content/components/switch/guidelines.md) | An on/off setting | Make the effect and state clear, including when it takes effect |
| [Segmented buttons](m3-content/components/segmented-buttons/guidelines.md) | A compact related selection set | Define single or multiple choice; the shape alone does not define it |
| [Chips](m3-content/components/chips/guidelines.md) | Contextual actions, filters, suggestions, or input items | Use the subtype whose behavior matches the meaning |
| [Sliders](m3-content/components/sliders/guidelines.md) | A value or range along a meaningful continuum | Consider precision, labels, and an alternative input when needed |
| [Date pickers](m3-content/components/date-pickers/guidelines.md) | Choosing dates | Support the task's range, locale, and error conditions |
| [Time pickers](m3-content/components/time-pickers/guidelines.md) | Choosing a time | Clarify format and meaningful constraints |
| [Menus](m3-content/components/menus/guidelines.md) | A contextual set of choices or actions | Keep the trigger, scope, and selected or unavailable options clear |

## Content and grouping

| Pattern | Appropriate purpose | Important distinction |
| --- | --- | --- |
| [Cards](m3-content/components/cards/guidelines.md) | A coherent content unit, sometimes with related actions | Not every group needs a card; avoid confusing nested interaction targets |
| [Lists](m3-content/components/lists/guidelines.md) | Scannable, comparable items | Maintain consistent item hierarchy and state; density follows the task |
| [Carousel](m3-content/components/carousel/guidelines.md) | Browsing a sequence of content | Hidden items may make simultaneous comparison difficult |
| [Divider](m3-content/components/divider/guidelines.md) | A useful boundary between regions | Space or headings may already communicate the relationship |
| [Badges](m3-content/components/badges/guidelines.md) | A compact status or count attached to another element | Make meaning discoverable without relying only on color |

## Feedback and temporary surfaces

| Pattern | Appropriate purpose | Important distinction |
| --- | --- | --- |
| [Dialogs](m3-content/components/dialogs/guidelines.md) | A focused decision or task that warrants interruption | Use only the necessary interruption and provide clear resolution |
| [Bottom sheets](m3-content/components/bottom-sheets/guidelines.md) | Supporting content or actions connected to the current context | Modal and persistent behavior have different focus and dismissal needs |
| [Side sheets](m3-content/components/side-sheets/guidelines.md) | Supporting content alongside or over the main region | Preserve the relationship and usable space for the primary task |
| [Snackbar](m3-content/components/snackbar/guidelines.md) | Brief feedback, sometimes with a related action | Essential information or decisions may need a more persistent treatment |
| [Tooltips](m3-content/components/tooltips/guidelines.md) | Supplementary explanation of a control | Essential action meaning should not depend on hover alone |
| [Progress indicators](m3-content/components/progress-indicators/guidelines.md) | Ongoing work or measurable progress | Use known progress when available; do not imply false precision |
| [Loading indicator](m3-content/components/loading-indicator/guidelines.md) | An expressive waiting state | Keep the context understandable and consider reduced-motion needs |

## Compositions and patterns without a direct match

A task may need a [list-detail layout](m3-content/foundations/layout/canonical-examples/list-detail.md),
[supporting pane](m3-content/foundations/layout/canonical-examples/supporting-pane.md), or
[feed](m3-content/foundations/layout/canonical-examples/feed.md), rather than another standalone
component. Use [layout guidance](m3-content/foundations/layout/layout-overview/adaptive-design.md)
to preserve task relationships as space changes.

For gestures such as swipe-to-dismiss, pair the intended action with clear feedback and a suitable
alternative where needed; see [gestures](m3-content/foundations/interaction/gestures.md). A drag
handle or decorative shape is not, by itself, a complete interaction design. Choose
[icons](m3-content/styles/icons/applying-icons.md) for meaning and consistency with the actual kit.

If neither a kit pattern nor a suitable composition meets the need, create a design grounded in
the task and Material principles. Specify relevant behavior, states, and shared visual roles.
Explain the meaningful departure briefly; do not falsely label a custom pattern as an official
component or claim kit availability without checking it.
