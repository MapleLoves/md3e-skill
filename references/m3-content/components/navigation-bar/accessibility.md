---
source: https://m3.material.io/components/navigation-bar/accessibility
title: "Navigation bar"
captured: 2026-09-14
---

# Navigation bar

> Navigation bars let people switch between UI views on smaller devices

## Use cases

People should be able to do the following using the assistive technology:

-   Move between navigation destinations
-   Select a particular navigation destination from a set
-   Get appropriate feedback based on input type

## Interaction & style

**Touch**

-   When a navigation item is tapped, the active indicator appears in place, providing feedback that it’s selected

-   A touch ripple passes through the indicator

-   The icon switches from outlined to filled

-   The icon changes color

Touch: Tap

**Cursor**

-   When hovered, the active indicator appears in a reduced state providing a visual cue that the destination is interactive

-   When clicked (in both active and inactive states), a ripple passes through the indicator

-   The icon switches from outlined to filled

-   The icon changes color, becoming darker

Cursor: Hover, Click

### Text scaling and truncation

When someone sets their device to show a larger text size, the navigation bar should grow vertically to accommodate larger labels while retaining the default padding. It’s okay for scaled text to wrap in navigation items.

To remain accessible, ensure the full label is always visible on-screen at up to 2x text sizing. Beyond this size, text can truncate. 

![Nav bar with text scaled to 1.5x size. Some labels are on two lines, others are on one line.](../../_assets/m2kua3ge-03-e6bef93d4812a4133853.png)

Text scaled to 1.5 size

![Nav bar with text scaled to 2x size. Some labels wrap to two lines.](../../_assets/m2kuaeol-04-77b0296e075f1a4feabb.png)

Text scaled to 2x size

## Initial focus

Initial focus lands directly on the first navigation item, since that is the first interactive element of the component.

![Focus order and keyboard navigation of a nav bar.](../../_assets/m0fr7kb3-03-f0f21065f307c10787b5.png)

Focus lands on first navigation item

![Activating a nav item with space on a keyboard.](../../_assets/m0fr7nd7-04-e4f7a9d8dcd81f9ee8a9.png)

The navigation item is selected with Space/Enter

## Visual indicators

Use a filled icon with a bold label for selected destinations. For unselected destinations use an outlined icon with a medium label.

If an icon doesn’t have a filled style, use a thicker or heavier version of the icon instead.

![A nav bar with a filled icon for the selected nav item.](../../_assets/m0fr7qqu-05-acd7b47558372fb0c9f9.png)

check Do

Use a filled icon for the selected navigation destination to differentiate from the other destinations

![A nav bar with an outlined icon for the selected nav item.](../../_assets/m0fr7ugl-06-337eab98ae8bd7eae8ae.png)

close Don’t

Don’t use outlined icons on selected nav items

![2 nav items, one selected, one unselected.](../../_assets/m0fr7yfn-07-53e80b4ef7149e4524e4.png)

When selected, the icon fills, darkens, and is backed by an active indicator shape

## Keyboard navigation

<table style="width:100%"><tbody><tr><th>Keys</th><td>Actions</td></tr><tr><th>Tab</th><td><span style="white-space:pre-wrap" id="isPasted">Move between navigation items</span></td></tr><tr><th>Space / Enter</th><td><span style="white-space:pre-wrap" id="isPasted">Selects the focused navigation item</span></td></tr></tbody></table>

## Labeling elements

The accessibility label for a navigation item is typically the same as the destination name.

![Accessibility label and role defined for a Home icon on a navigation bar.](../../_assets/m0fr861i-08-5799596302682ca1c9cc.png)

A navigation bar’s accessibility label can incorporate its adjacent UI text

When the visible UI text is ambiguous, accessibility labels need to be more descriptive. For example, a navigation destination visibly labeled **Library** would benefit from additional information in its accessibility label to clarify the destination’s intent.

Note: On Android Views (MDC-Android), a more descriptive accessibility label is not available and the role is not announced.

![Accessibility labels of a navigation bar.](../../_assets/m0fr8a8y-09-9260ba8a83de62b263a9.png)

While the visible label text reads **Library**, the accessibility label for this destination clarifies its function: **Music library**
