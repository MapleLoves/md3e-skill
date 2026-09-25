---
source: https://m3.material.io/components/checkbox/accessibility
title: "Checkbox"
captured: 2026-09-14
---

# Checkbox

> Checkboxes let users select one or more items from a list, or turn an item on or off

## Use cases

People should be able to use assistive technology to:

-   Navigate to a checkbox   

-   Toggle the checkbox on and off

-   Get appropriate feedback based on input type documented under [Interaction & style](/m3/pages/checkbox/accessibility#6a2f55e5-2fa0-4204-b6d1-62362dda89c7)

## Interaction & style

Users should be able to select either the text label or the checkbox to select an option.

![In a list, checkboxes for 2 items are selected via their text labels.](../../_assets/mg0vkh7s-1-5dd9c8412960f2a1bb31.png)

A checkbox selected via the text label

The parent checkbox has three states: selected, unselected, and indeterminate. 

Checkboxes can be selected or unselected regardless of the state of the other checkboxes in a group. 

If some, but not all, child checkboxes are checked, the parent checkbox becomes indeterminate. Selecting an indeterminate parent checkbox will check all of its child checkboxes.

![In a list, a child checkbox for 1 item is selected and the parent checkbox is in indeterminate state.](../../_assets/mcyq4z51-2-b8f750f0d780fd2c164c.png)

An indeterminate selection indicating that at least one checkbox is selected within a group

## Avoid applying density by default

Don't apply density to checkboxes by default — this lowers their targets below our best practice of 48x48 CSS pixels. Instead, give people a way to choose a higher density, like selecting a denser layout or changing the theme.

To ensure that this density setting can be easily reverted when it's active, keep all the targets to change it at minimum 48x48 CSS pixels each.

## Keyboard navigation

| Keys | Actions |
| --- | --- |
| **Tab** | Moves focus to enabled An enabled state communicates an interactive component or element. [More on enabled state](/m3/pages/interaction-states/applying-states#39b2fc90-01db-41b5-b6f8-47be61ed1479) chip or chip group |
| **Space** or **Enter** | Activates, selects, or deselects the focused chip |
| **Backspace** or **Delete** | Removes currently  focused A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice. [More on focused state](/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f) input chip |
| **Arrows** | Moves focus between chips |

## Labeling elements

If the UI text is correctly linked to the checkbox, assistive tech (such as a screen reader) will read the UI text followed by the component’s role.

The accessibility Accessible design makes products usable for people with all kinds of abilities. [More on accessibility](/m3/pages/overview/principles) label for an individual checkbox is typically the same as its adjacent text label.

![Accessibility labels of a checkbox.](../../_assets/mg0vlqi0-3-c3c3f254950d3dd7dd20.png)

The accessibility label clearly states the text label of the checkbox
