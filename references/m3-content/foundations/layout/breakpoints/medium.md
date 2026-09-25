---
source: https://m3.material.io/foundations/layout/breakpoints/medium
title: "Breakpoints"
captured: 2026-09-14
---

# Breakpoints

> Breakpoints ensure layouts work across a wide range of devices

Layouts for medium breakpoints Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes). [More on breakpoints](/m3/pages/breakpoints) are for **screen widths from 600dp to 839dp.**

![A medium breakpoint with a video call app in full-screen mode.](../../../_assets/mp413hn4-01-f4f512d8e41db22fe10a.png)

Single-pane layouts can focus attention on one action or view, such as a video call

## Navigation

Place navigation components close to edges of the window where they’re easier to reach:

-   Single-pane layouts: Navigation rail Navigation rails let people switch between UI views on mid-sized devices. [More on navigation rails](/m3/pages/navigation-rail/overview)

-   Two-pane layouts: Navigation bar Navigation bars let people switch between UI views on smaller devices. [More on navigation bars](/m3/pages/navigation-bar/overview)

The navigation rail can be hidden in secondary destinations as long as the primary destination can still be accessed using a back button.

![The navigation area of a medium breakpoint is a vertical bar at the leading edge, beside a single pane.](../../../_assets/mp414ag3-02-0410ec91f9032059374a.png)

1.  Navigation area

2.  Single pane

## Panes

### Single-pane layout  

In a medium layout, a single pane is recommended because of limited screen width.

![A single pane uses most of the space in a medium window.](../../../_assets/mp417y7j-03-3e40329434663727c49c.png)

1.  A single-pane layout is recommended for medium breakpoints

### Two-pane layout

Limit use of two panes for content with lower information density, such as a settings screen.

Each pane in a two-pane layout should take up 50% of the window width. Avoid setting custom widths. A drag handle can be used to expand or collapse panes to be 100% of the window width.

![2-pane layout in a medium window. Both panes fit 50% of the window width by default.](../../../_assets/mp418umv-04-a0653b7a62ea16ccab8f.png)

Two-pane layouts should use 50% widths for each pane by default

When adding navigation to a two-pane layout, use a navigation bar. This allows the panes to fully use the available window width.

![A navigation bar extends over 2 panes at the bottom of a medium window.](../../../_assets/mp419dq9-05-4698c38e898ebf9c908c.png)

Two-pane layout with:

1.  Navigation bar

## Spacing

Medium layouts have margins of 24dp.

The spacer A spacer is the space between two panes. If panes can be resized, the spacer contains a drag handle. between panes is also 24dp.

![2 pane layout with 24dp margins and 24dp space between panes.](../../../_assets/mp41ahko-06-e914da8027b7e114ef25.png)

Use 24dp for margins and spacer in a medium layout

## Special considerations

A medium layout will need to transition dynamically to a compact or expanded layout when:

-   A foldable device is folded

-   A tablet is rotated from portrait to landscape

-   A product goes from full-screen to split-screen

-   Multi-window mode is initiated

-   A free-form window is resized

![Email app with 2 panes at  a medium breakpoint.](../../../_assets/mp5kr0vt-07-f7b7bc5b3853235c1e76.png)

Think of how a medium layout should change to a compact or expanded layout

### Reachability

For horizontal tablets and unfolded foldables, the top 25% of the screen is likely out of reach, unless the grip is adjusted. To accommodate device and hand sizes, limit the amount of interactions that are placed in the upper 25% of the screen.

![The hard-to-reach top quarter of a medium breakpoint in landscape mode.](../../../_assets/mp41cohr-08-8dd6d599ee93b96f7d70.png)

1.  Limit interactions in the upper quarter of a screen, as they can be hard to reach

Avoid placing essential interactive elements too close to the bottom edge of the screen. Some users, particularly those with larger hands, might struggle to reach this area.

Specify interactions in a layout with these ergonomic regions in mind:

1.  Users can reach this area by extending their fingers, which makes it inconvenient

2.  Users can reach this area comfortably

3.  Reaching this area is challenging when holding the device

![The 3 ergonomic regions of a medium breakpoint.](../../../_assets/mp41dv1l-09-fbb506656f4e0d0eead0.png)

Medium breakpoint ergonomic regions: 

1.  Inconvenient

2.  Comfortable

3.  Challenging
