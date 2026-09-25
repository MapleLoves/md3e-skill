---
source: https://m3.material.io/components/segmented-buttons/overview
title: "Segmented buttons"
captured: 2026-09-14
---

# Segmented buttons

> Segmented buttons help people select options, switch views, or sort elements

star

Note:

Segmented buttons are no longer recommended in the Material 3 expressive update. For those who have updated, use the [connected button group](/m3/pages/button-groups/overview/) instead, which has mostly the same functionality but with an updated visual design.

-   Segmented buttons can contain icons, label text, or both

-   Two variants: single-select and multi-select

-   Use for simple choices between two to five items (for more items or complex choices, use chips Chips help people enter information, make selections, filter content, or trigger actions. [More on chips](/m3/pages/chips/overview) )

![Two variants of segmented buttons.](../../_assets/lw7qvais-1-dfcf8e5e672c5d87fbc7.png)

1.  Single-select segmented button
2.  Multi-select segmented button

## Availability & resources

| Type | Resource | Status |
| --- | --- | --- |
| Design |
| [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) | Available |
| Implementation |
| [Flutter](https://api.flutter.dev/flutter/material/SegmentedButton-class.html) | Available |
| [Jetpack Compose](https://developer.android.com/develop/ui/compose/components/segmented-button) | Available |
| [Android Views (MDC-Android)](https://github.com/material-components/material-components-android/blob/master/docs/components/Button.md#toggle-button) | Available |
|
Web

 | Unavailable |

Close

## M3 Expressive update

**May 2025**

The segmented button is no longer recommended. Use the [connected button group](/m3/pages/button-groups/overview/) instead. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive)

## Differences from M2

-   **Color:** New color mappings and compatibility with dynamic color Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI. [More on dynamic color](/m3/pages/dynamic/choosing-a-source)

-   **Icons:** Optional check icon to indicate selected state States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview)

-   **Layout:** Taller container height of 40dp

-   **Name and variants:** Segmented buttons were previously known as toggle buttons. They now have two official variants: single-select and multi-select.

-   **Shape:** Fully rounded corners

-   **Typography:** Labels use sentence case instead of all caps

![Diagram indicating the fully rounded corner radius of a segmented button.](../../_assets/lwhr0fyz-2-3e75542db38cd02d03fa.png)

Segmented buttons now have a container height of 40dp

![Segmented buttons with M2 color mappings, all caps text labels, boxy shape, and shorter height.](../../_assets/l20oj7ju-example-4d97025b17092d3a3f08.png)

M2: Segmented buttons had a small corner radius and label text in all caps

![Segmented buttons with M3 color mappings, sentence case text labels, fully round shape, and taller height.](../../_assets/lw7ruslm-4-a937b91816116527f259.png)

M3: Segmented buttons have fully rounded corners, sentence-case text, different height, and new color mappings
