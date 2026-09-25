---
source: https://m3.material.io/foundations/xr/components/toolbars
title: "XR components"
captured: 2026-09-14
---

# XR components

> Learn how Material 3 Expressive components adapt to extended reality devices

star

Note:

XR guidelines are primarily intended for designers. Find what’s implemented in code in the [design kit](https://www.figma.com/community/file/1035203688168086460).

Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has an XR toolbar with custom specs and guidance. Read [XR developer documentation](https://developer.android.com/design/ui/xr/guides/foundations) for more details.

## Variants

There is one toolbar orbiter Orbiters are floating elements that control the content within spatial panels. [More on orbiters](https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters) . It closely aligns with the floating toolbar Floating toolbars float on top of page content and can provide contextual, dynamic actions. [More on toolbars](/m3/pages/toolbars/overview) . It can be configured to be horizontal or vertical. [Go to XR toolbar API reference](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/package-summary#HorizontalFloatingToolbar\(kotlin.Boolean,androidx.compose.ui.Modifier,androidx.compose.material3.FloatingToolbarColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.material3.FloatingToolbarScrollBehavior,kotlin.Function1,kotlin.Function1,kotlin.Function1\))

![Horizontal and vertical toolbar orbiters.](../../../_assets/ds2nZJkQR-ChJVdNLWz0le3T0Qrn7_7xC3m88jQKzP0vtewiS711HSyShuX5Z7CS9izVcwCl3jqtb723-65676ff8a543f3083bbf.png)

1.  Horizontal floating toolbar
2.  Vertical floating toolbar

## Anatomy

![2 elements of a toolbar orbiter: container and placed components. ](../../../_assets/wPnd0meDx_6WgA0RcmAh3jBLHG0iuYG-GonjBTpRZXx8jbGK2mhttARyxdipcS3kS2iSHJFhSFb3eXw_-f8258a42412001c1084f.png)

1.  Container
2.  Placed components

## Color & elevation

XR uses color to communicate the elevation of UI elements and orbiters. With [spatial elevation](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation), the toolbar displays above the spatial panel In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content. [More on spatial panels](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels) on the Z-axis. Elevated toolbars can use any of these color options:

![4 versions of toolbar elevation color strategy.](../../../_assets/w6VacobEqegZ2sNrmTh9bvGoH7GlIqFV0rkepmfEObuvNceGyegLbNeOQKw6DnY0PBwm-knNvVozQEha-47db2d3b7abe9ea720cd.png)![4 versions of toolbar elevation color strategy.](../../../_assets/w6VacobEqegZ2sNrmTh9bvGoH7GlIqFV0rkepmfEObuvNceGyegLbNeOQKw6DnY0PBwm-knNvVozQEha-22a81a1c679a6c2e168d.png)

1.  Surface container
2.  Surface container high
3.  Surface container highest
4.  Tertiary container

## Measurements

![Diagram with measurements for toolbar orbiters.](../../../_assets/QKzN5tAxYlmJ3FQZI3BGI6GDG249mlMDhzYL0PQBj2ABlwwZ25a465b1e7KuZujPAXcSFIpWEZA0_wvh-9fdaaea695162ee126a1.png)

Measurements for toolbar orbiters

![Diagram with 12dp padding for toolbar orbiters.](../../../_assets/mrquic0M5r5AkyYCEdVNfNfr6sTJwfTLOOO6y0-G4bIIMOKCoqXOt15g5aJHGa8OCeh6ubTElhCaN1nn-d174b7eb8e31589181c2.png)

Padding for toolbar orbiters

## Usage

A toolbar can appear in an orbiter Orbiters are floating elements that control the content within spatial panels. [More on orbiters](https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters) for a more immersive experience. Currently, this spatial capability is only available in full space Full space is Android XR’s immersive mode and supports spatial components. [More on full space](https://developer.android.com/design/ui/xr/guides/foundations#modes) . In home space Home space is compatible with mobile and large screen apps, but doesn’t support spatial components. [More on home space](https://developer.android.com/design/ui/xr/guides/foundations#modes) , use a regular toolbar on the same plane as the body content to mimic a 2D experience.

A toolbar’s behavior and placement changes from a 2D to a 3D experience

## Behavior

### Local context (recommended)

When placed in local context, the toolbar orbiter is centered at the bottom of the spatial panel it controls. 

It repositions in response to layout or content changes.

In most cases, toolbars should be placed in local context. The orbiter is centered and anchored to the bottom of the panel it controls.

### Global context

When placed in global context, the toolbar orbiter is centered at the bottom of the app. 

It stays anchored to the app during layout or content changes. 

exclamation Caution

In global context, toolbar orbiters are centered and anchored to the bottom of the app. This use case is less common, as toolbars usually contain actions that control a specific panel.

### Expand & collapse

Toolbar orbiters with more than five items can expand and collapse to reveal or hide additional content.

When a toolbar orbiter expands, it stays within the bounds of the adjacent spatial panel.

Alternatively, more complex toolbars can be split into multiple toolbars.

Toolbar orbiters can expand to reveal additional content, but should stay within the bounds of the adjacent spatial panel

### Additional toolbars

In some cases, full space apps can have more than one toolbar orbiter, placed in either global or local context. 

exclamation Caution

Limit the use of multiple toolbars to rare cases when additional spatialization improves usability

## Placement

### Offset & inset positioning

In full space, a toolbar orbiter can be positioned adjacent to or overlap a spatial panel. 

![Toolbar orbiter with offset positioning.](../../../_assets/moxer5rt-11-do-279e697bcf32eb4fcc24.png)

check Do

The recommended toolbar orbiter position from the spatial panel is: 

-   Offset by 20dp or 
-   Inset by 12dp

![Toolbar orbiter with inset positioning above 12dp that obstructs content on the spatial panel. ](../../../_assets/moxetpx5-12-don-t-346a56ff90a09f25f203.png)

close Don’t

To prevent content obstruction, don’t overlap the toolbar orbiter and spatial panel above 12dp

### Horizontal alignment

![A horizontal toolbar orbiter placed within the bounds of its spatial panel.](../../../_assets/moxewjln-13-do-9d00652200bde9cc34a5.png)

check Do

Always align the toolbar orbiter within the horizontal bounds of nearby spatial panels

![A horizontal toolbar orbiter that extends beyond the width of its spatial panel.](../../../_assets/moxeyben-14-don-t-4dda7b35f34d1d7d3139.png)

close Don’t

The toolbar orbiter shouldn’t exceed the width of adjacent spatial panels

### Vertical alignment

![A vertical toolbar orbiter placed within the bounds of its spatial panel.](../../../_assets/moxf0mbw-15-do-5a26b390a5a76700a6f6.png)

check Do

Always align the toolbar orbiter within the vertical bounds of nearby spatial panels

![A vertical toolbar orbiter that extends beyond the height of its spatial panel.](../../../_assets/memfyo8f-16-don-t-524eb42b00e844ba382d.png)

close Don’t

The toolbar orbiter shouldn’t exceed the height of adjacent spatial panels

### Spatial panel alignment

By default, toolbar orbiters are center-aligned to the spatial panel. Their placement can be adjusted to accommodate specific user needs, such as improved ergonomics or [right-to-left (RTL) languages](/m3/pages/bidirectionality-rtl).

![Toolbar orbiter alignment options in relation to spatial panels.](../../../_assets/memfvpq3-17-1945362a818c564bb964.png)

Depending on the configuration (horizontal or vertical) of the toolbar orbiter, it can align to the center, left, right, top, or bottom of a spatial panel

Avoid placing a vertical toolbar orbiter between spatial panels. 

This negatively affects the interface structure and can make it difficult to find.

![A vertical toolbar orbiter is placed between 2 spatial panels.](../../../_assets/memfx943-18-don-t-e662900d9eb2c99f653d.png)

close Don’t

Don't place a vertical toolbar orbiter between spatial panels

## Accessibility considerations

[XR accessibility](/m3/pages/xr-design/accessibility) guidelines are still evolving. XR toolbars should follow applicable Material [toolbar accessibility standards](/m3/pages/toolbars/accessibility).
