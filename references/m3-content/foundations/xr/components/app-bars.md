---
source: https://m3.material.io/foundations/xr/components/app-bars
title: "XR components"
captured: 2026-09-14
---

# XR components

> Learn how Material 3 Expressive components adapt to extended reality devices

star

Note:

XR guidelines are primarily intended for designers. Find what’s implemented in code in the [design kit](https://www.figma.com/community/file/1035203688168086460).

Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has an XR app bar with custom specs and guidance. See [XR developer documentation](https://developer.android.com/design/ui/xr/guides/foundations) for more details.

## Variants & configurations

There is one app bar orbiter Orbiters are floating elements that control the content within spatial panels. [More on orbiters](https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters) . It closely aligns with the small app bar Small app bars display information and actions in compact layouts. They're often used for scrolled views on subpages that require back navigation and multiple actions. [More on small app bars](/m3/pages/app-bars/overview) . It can be configured to be center-aligned or left-aligned.

![Center and left-aligned app bar orbiters.](../../../_assets/4Vdn-iH-z3fko57KiqLULyRWIN845IFV7T3yC7smqZ9bVb5vXsO3s_-BaAojJNwXIcW6uorvb3qjbFxv-9d265fea602f21f18725.png)![Center and left-aligned app bar orbiters.](../../../_assets/4Vdn-iH-z3fko57KiqLULyRWIN845IFV7T3yC7smqZ9bVb5vXsO3s_-BaAojJNwXIcW6uorvb3qjbFxv-ea4adbcef52ed7482d1d.png)

1.  Center-aligned app bar
2.  Left-aligned app bar

## Anatomy

![Diagrams of app bar orbiters identifying 4 internal elements.](../../../_assets/u2YwIRPzgQXNG2dOG6VjZ42_rl1vEV32kphFtG-in9JaGpdtAMOnMZTtyE49JpCTqNB4ZyTFyytePqLO-226ef6c674a838c0a146.png)![Diagrams of app bar orbiters identifying 4 internal elements.](../../../_assets/u2YwIRPzgQXNG2dOG6VjZ42_rl1vEV32kphFtG-in9JaGpdtAMOnMZTtyE49JpCTqNB4ZyTFyytePqLO-8c9239cb9edbbeb3dd8c.png)

1.  Container
2.  Headline
3.  Trailing icons
4.  Leading icon

## Color & elevation

XR uses color to communicate the elevation of UI elements and orbiters. With [spatial elevation](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation), the app bar displays above the spatial panel In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content. [More on spatial panels](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels) on the Z-axis. Elevated app bars can use any of these color options:

![3 versions of app bar elevation color strategy.](../../../_assets/0hgrQRQF5mEFNy0s_RbxRDEV7fJYHsWUq0adzDor4Ogpq5nNCNmQrrJA-2hJgwv315HAyAMpxpVwDQe7-640c98e5a918b3b3c4c3.png)

1.  Surface container
2.  Surface container high
3.  Surface container highest

## Measurements

![Diagrams with measurements and padding for app bar orbiters.](../../../_assets/IzfAl6XWiO_JPWqGVK4P-7us8V9d_iehPeqgzzROuGZhbpvUMolBMBa9x9BMbL5iNZTTwEHNJsxIA28W-b2b8330d2ed6a7b00e0f.png)

Measurements and padding for app bar orbiters

## Usage

An app bar can appear in an orbiter Orbiters are floating elements that control the content within spatial panels. [More on orbiters](https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters) for a more immersive experience. Currently, this spatial capability is only available in full space Full space is Android XR’s immersive mode and supports spatial components. [More on full space](https://developer.android.com/design/ui/xr/guides/foundations#modes) . In home space Home space is compatible with mobile and large screen apps, but doesn’t support spatial components. [More on home space](https://developer.android.com/design/ui/xr/guides/foundations#modes) , use a regular app bar on the same plane as the body content to mimic a 2D experience.

An app bar’s behavior and placement changes from a 2D to a 3D experience

## Behavior

### Global context

When placed in global context, the orbiter is centered at the top of the app it controls. 

It stays anchored to the app during layout or content changes. 

This ensures navigation elements are always easy to find and use.

Global app bar orbiters should be centered and anchored to the top of the app

### Local context

When placed in local context, the orbiter is centered at the top of the spatial panel it controls. 

It repositions in response to layout or content changes.

exclamation Caution

Local app bar orbiters should be centered and anchored to the top of the panel. However, this is less common, so make sure that it contains actions that only affect its anchored panel.

### Additional app bars

In most cases, apps should only have one app bar orbiter, placed in global context.

exclamation Caution

Limit the use of multiple app bars to rare cases when additional spatialization improves usability

## Placement

### Offset & inset positioning

In full space, an app bar orbiter can be positioned:

-   Offset 20dp from the spatial panel

-   Inset 12dp, overlapping spatial panel without obstructing content

![App bar orbiter with offset positioning.](../../../_assets/mowwbs16-09-c9bdff6bea911f2e5934.png)

check Do

An app bar orbiter with a 20dp offset creates visual separation from the spatial panel

![App bar orbiter with inset positioning that obstructs content..](../../../_assets/mowwe02f-10-1e08c68997244b3475ea.png)

close Don’t

Don’t overlap the app bar orbiter and spatial panel more than 12dp

### Horizontal alignment

![An app bar orbiter placed within the bounds of its spatial panel.](../../../_assets/mowwevxe-11-68bf136938e334764fbb.png)

check Do

Always align the app bar orbiter within the bounds of nearby spatial panels

![An app bar orbiter that extends beyond the width of its spatial panel.](../../../_assets/mowwgpq6-12-3ba2ff466f485cb8fd94.png)

close Don’t

The app bar orbiter shouldn’t exceed the width of adjacent spatial panels

### Spatial panel alignment

By default, app bar orbiters are center-aligned to the spatial panel. Their width and placement can be adjusted to accommodate specific user needs, such as improved ergonomics or [right-to-left (RTL) languages](/m3/pages/bidirectionality-rtl).

App bar orbiters can align to the center, left, or right of the spatial panel

### Width boundaries

An app bar orbiter’s width should adjust to stay in a person’s [field of view](https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place). 

This makes crucial navigation elements easy to find.

![An app bar orbiter with a width that fits in a person’s field of view.](../../../_assets/mowy6885-14-d7e1ab16bcadfd22b59e.png)

check Do

Adjust the width of the app bar orbiter to fit in a person’s field of view

It’s not recommended to increase the width of an app bar orbiter beyond a person’s natural [field of view](https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place). 

This creates a visual imbalance and makes it difficult to find navigation elements.

![An app bar orbiter that exceeds the panel’s width and a person’s field of view.](../../../_assets/mowy73ja-15-8be47781a17a0733043a.png)

close Don’t

Avoid expanding the app bar orbiter beyond the adjacent panel’s width and a person’s field of view

### Adaptable width

When placed in a local context, an app bar orbiter can expand to the width of its adjacent spatial panel.   

Be sure the orbiter stays in a person’s field of view, and test for usability.

exclamation Caution

Use caution before expanding the app bar’s width to match its spatial panel. The orbiter may not fit in a person’s primary field of view.

## Accessibility considerations

[XR accessibility](/m3/pages/xr-design/accessibility) guidelines are still evolving. XR app bars should follow applicable Material [app bar accessibility standards](/m3/pages/app-bars/accessibility).
