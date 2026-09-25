---
source: https://m3.material.io/foundations/layout/breakpoints/compact
title: "Breakpoints"
captured: 2026-09-14
---

# Breakpoints

> Breakpoints ensure layouts work across a wide range of devices

Layouts for compact breakpoints Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes). [More on breakpoints](/m3/pages/breakpoints) are for **screen widths smaller than 600dp.**

![Messaging app at a compact breakpoint.](../../../_assets/mp40sit1-01-d94825af14c9a24c1f48.png)

A compact breakpoint focuses on a single view

## Navigation

Use a navigation bar or modal expanded navigation rail.

Place navigation components close to the edge of the screen where they’re easier to reach.

![Navigation bar and FAB are close to the bottom of a mobile app in a compact window.](../../../_assets/mp40u2kw-02-fc0a9576ba85bcc3f9a6.png)

Place navigation elements near the bottom of a compact window so they’re easy to reach

## Panes

Use a single pane in compact layouts.

![The single pane consumes most of the area in a compact window.](../../../_assets/mp40uzbp-03-5f60d0fd686c9d689e20.png)

1.  Single-pane layouts work best for compact breakpoints

## Spacing

Margins are 16dp from the leading and trailing edge of the window.

![The left and right margins of a compact window pane are 16dp.](../../../_assets/mp40vzj4-04-4a688a71dca83fc5c1b2.png)

In compact layouts, use 16dp margins

## Special considerations

A compact layout will need to transition dynamically to a medium or expanded layout when:

-   A foldable device is unfolded

-   A mobile device is rotated from portrait to landscape

-   A tablet exits split-screen mode

-   A product is resized to be larger in multi-window mode

-   A free-form window is resized

![2 mobile layouts showing a messaging app with a 1-pane list and an expanded navigation rail.](../../../_assets/mp40wssg-05-5db8272143c39be1997e.png)

Compact layouts should dynamically transition to larger layouts when a device is unfolded or rotated
