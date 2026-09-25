---
source: https://m3.material.io/foundations/layout/breakpoints/large-extra-large
title: "Breakpoints"
captured: 2026-09-14
---

# Breakpoints

> Breakpoints ensure layouts work across a wide range of devices

These breakpoints are most useful for creating web experiences tailored to laptop and desktop devices. Some products may not need large and extra-large breakpoints. Consider your platform’s conventions and users when making decisions on which breakpoints to design for.

-   Layouts for large breakpoints Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes). [More on breakpoints](/m3/pages/breakpoints) are for screen widths **from 1200dp to 1599dp**

-   Layouts for extra-large breakpoints are for screen widths of **1600dp and larger**

![Large window with a video app in 2 pane layout.](../../../_assets/mp41v09e-01-36eaa77af6ee25a8e37b.png)

A two-pane layout is recommended for large and extra-large breakpoints

## Navigation

Use a navigation rail Navigation rails let people switch between UI views on mid-sized devices. [More on navigation rails](/m3/pages/navigation-rail/overview) , either collapsed or expanded, depending on the amount of content.  

For sorting, filtering, or secondary navigation, use tabs or other components directly in the pane.

![Large web browser with a small navigation area on the leading edge with 1 pane filling the rest of the window.](../../../_assets/mp41w5ix-02-4afab7896a7a2d82ae4d.png)

1.  Collapsed navigation area

2.  Single-pane layout

An expanded navigation rail is best suited for extra-large windows, where there's still plenty of room for content. Consider collapsing the navigation rail when space is needed, or when on pages deeper in the page hierarchy.

![Extra-large web browser with an expanded navigation area and 1 pane filling the rest of the window.](../../../_assets/mp41xhwl-03-cc27d1688668efe7dbcf.png)

1.  Expanded navigation area

2.  Single-pane layout

## Panes

A two-pane layout is often best for large and extra-large breakpoints.   

However, a single-pane layout can work when displaying visually- or information-dense content, such as videos.

![The single pane covers most of a large screen except for the navigation area and margins.](../../../_assets/mp41y2za-04-b4d0673b5ff507980ad5.png)

Only use a single-pane layout for dense content or media

When using a [fixed-and-flexible](/m3/pages/scaffold/panes#92371c3b-587d-4c6f-8105-05b69dcec81a) layout, the fixed pane should have a width of 412dp by default. 

![A 2-pane layout with 1 pane fixed at 412dp.](../../../_assets/mp41yyza-05-bbccaf2d2569d809b26c.png)

Fixed panes should be 412dp in large and extra-large layouts

When using a [split-pane layout](/m3/pages/scaffold/panes#dc7982b7-754c-410a-9e88-18a54557c87b), the spacer should be visually centered by default, even when using an expanded navigation rail. 

![An expanded nav rail and the first pane take up 50% of the window, and the second pane takes up 50%. ](../../../_assets/mp41zo3h-06-266dad975934cc3b5c8e.png)

In split-pane layouts, navigation components shrink the leading pane, so the spacer remains centered

## Additional panes

The extra-large breakpoint supports using a standard side sheet Standard side sheets display content without blocking access to the screen’s primary content, such as an audio player at the side of a music app. They're often used in medium and expanded window sizes like tablet or desktop. [More on side sheets](/m3/pages/side-sheets/overview) as a third pane. When the side sheet is present, the navigation rail can remain visible, collapse, or hide completely. Don't use more than three panes.   

Note: Fixed panes in this window size are recommended to be 412dp, but side sheets have a default maximum width of 400dp. 

![Extra-large window with 2 panes and a side sheet acting as a third pane.](../../../_assets/mp420iqc-07-db4f7e257d100da0d988.png)

1.  Standard side sheet (third pane)

## Spacing

Large and extra-large layouts have a leading and trailing margin of 24dp.

The spacer A spacer is the space between two panes. If panes can be resized, the spacer contains a drag handle. between panes is 24dp.

![2 pane layout with 24dp margins and 24dp space between panes.](../../../_assets/mp5lfdh0-08-a812b2a4909195e591d0.png)

Use 24dp for margins and spacers in large and extra-large layouts

## Special considerations

Large and extra-large layouts will need to transition dynamically to a smaller layout when:

-   The app goes from full-screen to split-screen

-   Multi-window mode is initiated

-   A free-form window is resized

Pay attention to typographic elements such as line length to ensure readability on large and extra-large layouts.

![An email app with 2 panes in a large layout.](../../../_assets/mp42206a-09-d0630620c84c9107472e.png)

Consider how a large layout should change at smaller breakpoints
