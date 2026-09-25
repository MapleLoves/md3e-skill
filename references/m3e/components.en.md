# Component Selection, UI Kits, and Custom Design

[中文](components.md)

This is the skill's design judgment guide. Component names describe patterns, not required API
identifiers. See the [pattern catalog](../components-catalog.md) for component specifications.

## Understand the resources before judging fit

A UI Kit comprises the components, styles, assets, and patterns actually provided or designated
for the project. Inspect existing interfaces and resources to understand purpose, states,
composition, and customization boundaries. Identify real resource names; unseen resources are
not evidence that a capability exists or is absent.

| Dimension | Fit question |
| --- | --- |
| Semantics | Does this represent an action, navigation, selection, input, or status, as required? |
| Behavior | Is the effect immediate or submitted later, single or multiple choice, interrupting or persistent? |
| Information | Can it accommodate real wording, density, language length, and simultaneous comparison? |
| States | Are the relevant selected, focus, loading, empty, error, or recovery states understandable? |
| Visual language | Does its emphasis, shape, and color fit the roles and rhythm of the surrounding interface? |
| Context | Does it suit the screen, input methods, assistive technology, and responsive needs? |

Use the consequential criteria; do not output this entire table for every simple control.

## Four situations

| Situation | Action | Useful rationale |
| --- | --- | --- |
| Suitable resource | Use the matching kit component, style, or pattern | What significant element was reused and why it fits |
| Partial fit | Customize within its supported contract or compose suitable primitives | Which mismatch the change resolves and which semantics remain intact |
| No suitable resource | Design from the task, specifications, and project language | What existing patterns fail to support, the new design's purpose, and important states |
| Kit unavailable or unspecified | Separate missing evidence from missing capability; inspect conventions or proceed with a stated assumption | Do not invent resource names; ask for kit details only when consequential |

A missing complete component does not require rebuilding every part. An original composition
can reuse suitable buttons, type styles, icons, and feedback. Do not distort the task to fit a kit.

## What makes custom design justified

Identify the actual unmet need: simultaneous comparison, continuous editing, multiple state
dimensions, or keeping an action associated with its target. Derive layout and interaction
relationships from that need before choosing the visual treatment.

Preserve shared color roles, text hierarchy, spacing rhythm, and state language. For new
interactions, specify the relevant inputs, outcomes, feedback, and exit or recovery behavior.
Cover states the task needs, without requiring irrelevant ones. Use applicable Material
specifications to support decisions; identify original work as a project proposal, not an
official component or an already validated pattern.

## Examples

- **Reuse:** a setting controls an immediately applied on/off state. Use the kit's suitable
  switch and label, preserving clear meaning and state feedback.
- **Adapt and compose:** a filtering area needs multiple choices and selected states. Compose
  suitable filter chips with grouping and a clear action. Do not choose an exclusive-selection
  pattern simply because its appearance is similar.
- **Design:** a scheduling view must compare several people's time intervals simultaneously,
  but the kit provides only lists and cards. Design a scheduling region with a clear time axis,
  selection, and conflict feedback; reuse suitable text, buttons, and overlays and consider
  keyboard or equivalent operation. Do not force comparison into serial card browsing.

These examples demonstrate criteria, not required solutions for every project.

## Delivery and review

Deliver the requested design or implementation. Explain consequential choices briefly; when
code is requested, implement in the project's actual stack. Check that a new composition
remains understandable and operable rather than hiding missing behavior behind a static visual.
Report checks actually performed; do not claim interaction or user testing that did not occur.

Sources: [Customization](../m3-content/foundations/customization.md),
[states](../m3-content/foundations/interaction/states/overview.md),
[interface structure](../m3-content/foundations/designing/structure.md), and
[accessibility principles](../m3-content/foundations/overview/principles.md).
