---
source: https://m3.material.io/components/toolbars/specs
title: "Toolbars"
captured: 2026-09-14
---

# Toolbars

> Toolbars display frequently used actions relevant to the current page

## Variants

![2 variants of toolbars.](../../_assets/j7SkkZwP6mNfPUFrpFyRIcGSsfI3_5Kv8VI0whqh3B1cGJq3v0lx_xaG3wOnjjjRl6GIEV4EZATztyOc-1205e9221c74c7276de9.png)

1.  Docked toolbar
2.  Floating toolbar

### Baseline variant

The baseline bottom app bar is no longer recommended. It should be replaced with the docked toolbar, which is very similar and more flexible.

![Baseline bottom app bar, which looks like the docked toolbar, but is not recommended.](../../_assets/tIdFhkPyYLLkFb4gUvrKPLzfIPcmAx4al6ORcGUGmS8oukJMF7ZzittOV7r-Nxwq0V63i9VTRfaVICzi-1e5270b9b1dbbcc7f7a0.png)

1.  Bottom app bar (not recommended)

| Variant | M3 | M3 Expressive |
| --- | --- | --- |
| Docked toolbar | \-- | Available |
| Floating toolbar | \-- | Available |
| Bottom app bar | Available | Not recommended.  Use **docked toolbar**. |

star

Note:

Implementation differs per platform. On Jetpack Compose, the floating toolbar is a separate component from the docked toolbar and bottom app bar.

## Configurations

![Color configuration of toolbars.](../../_assets/o4tXTZsCpct2GOpIk9NZcIqwhbbw1CLCMMGKI8rjcbmGoiECpJUHMaKtCGRJ_bL-ngPgBlo5zJAj0wdf-245f41f7b4c9fc7f94da.png)![Color configuration of toolbars.](../../_assets/o4tXTZsCpct2GOpIk9NZcIqwhbbw1CLCMMGKI8rjcbmGoiECpJUHMaKtCGRJ_bL-ngPgBlo5zJAj0wdf-141a195d79c42cb6bc4c.png)

1.  Standard and vibrant toolbars
2.  Vertical floating toolbar
3.  Floating toolbar with FAB

| Category | Configuration | M3 | M3 Expressive |
| --- | --- | --- | --- |
| Color | Standard (default) | Available as bottom app bar | Available |
| Vibrant | \-- | Available |
| Floating toolbar layout | Horizontal (default) | \-- | Available |
| Vertical | \-- | Available |
| Other elements | With FAB | Available as bottom app bar | Available\* |

star

Note:

\*Implementation differs per platform. On Jetpack Compose, floating toolbar with FAB is [fully supported](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#HorizontalFloatingToolbar\(kotlin.Boolean,androidx.compose.ui.Modifier,androidx.compose.material3.FloatingToolbarColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.material3.FloatingToolbarScrollBehavior,androidx.compose.ui.graphics.Shape,kotlin.Function1,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,kotlin.Function1\)). On other platforms, each component needs to be added separately. 

## Tokens & specs

Browse the component elements, attributes, tokens, and their values. [Jump to baseline bottom app bar specs](/m3/pages/toolbars/specs#ad142675-3e3b-43b8-ba53-12c1f0b7138d)

Token

Value

Close

## Anatomy

![2 elements of a toolbar.](../../_assets/q5KTYC5SjXAnSvSVvP72h2InKksCupfh4xqfQsa8eqO3ImcNxSiNEvyVzwrM54a_bgMyYUG2oOrljsqu-19997b1bfb1be14be67a.png)

1.  Container
2.  Placed components

### Flexibility & slots

When configuring a toolbar, think of it as a container with several slots. 

Each slot can be a different element. The most common elements are icon buttons When configuring a toolbar, think of it as a container with several slots. Each slot can be a different element. The most common elements are icon buttons, buttons, and text fields. [More on icon buttons](/m3/pages/icon-buttons/specs) , buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/specs) , and text fields Text fields let users enter text into a UI. [More on text fields](/m3/pages/text-fields/overview) .

![A toolbar with 5 slots, conceptual spaces for UI elements, next to each other.](../../_assets/U8tAffspM1NK0nWpYaxRxJHvPJOXWBX8GEuuEMeW6b-RjRo7OKtlMaYohHO-8Rn9QzwodfT_aJgLSocP-e7989b56723d91da44ac.png)

A toolbar is essentially a container with configurable slots

## Color

Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)

### Standard

![4 color roles in the standard color scheme  of the floating toolbar in light and dark scheme.](../../_assets/vnb-hvZkhHov6Q_xpnqsRpE-v1-ahJAuOOAS49Uw7K1JgYNot331UJ_viioRQnCmG5c_kqdBCgTXYkFk-0a7fb28fc93b4407bd65.png)

Standard color schemes and icon button types:

1.  Surface container
2.  Filled button (Primary, On primary)

3.  Toggle tonal button (Secondary container, On secondary container)
4.  Standard button (Primary)

### Vibrant

![4 color roles in the vibrant color scheme of the floating toolbar in light and dark scheme.](../../_assets/MSHjbfagavP64_aZ8he_iw3phiUh6IkZDUjRhPkoMvHcSGsAh-0j3khoUTMDeaPdCVcRwhCp9XyMVOQu-ab3dd715f015d1d84011.png)

Vibrant color scheme and icon button types:

1.  Primary container
2.  Filled button (Primary, On primary)
3.  Toggle tonal button: (Surface container, On surface)
4.  Standard button (On primary container)

## Measurements

By default all toolbars are 64dp high, center-aligned, have equal padding between items, and have a minimum outside padding of 16dp.

### Docked toolbar

![Default internal padding of a docked toolbar.](../../_assets/Eovie9hEPA5n7suVT8sw4C5TaWOwLmXIl0J3WBMBVOcBFDGyGqhwTTePHEyqXbPNsWb4kH1PH0QZ0llh-57126d8fcf07e7faa621.png)

1.  Default margins and padding
2.  Margins and padding with leading, middle, and trailing content

![2 docked toolbars with different margins and alignment.](../../_assets/Vsgw_yvIWA9pxAKEs4qmxtfhofUIoJnSXq6bO3_6v_OmMq4BZhQnS5FaT70GZEHJOzMm7DPuYd-ZUVsV-727e5585f8e707f98162.png)

Alignment and padding can be configured to create unique layouts:

1.  Left and right alignment
2.  Center-aligned, 8dp padding between items

### Floating toolbar

![Diagram noting margin around edge of floating toolbar.](../../_assets/BmOWzjQZ3a-oyRtJT94Nez52vT0DHXNgDWueCiIVnteA35K89UKvwAP_gs8fdqn450QEN9oEnw_yWK0o-65f9bfee49f1356c76d2.png)

Default padding of floating toolbar

![Diagram noting layout measurements.](../../_assets/OStcy-GlT-NRB63inDLnhvNm3czBqigQcIhixAV3N7fMvikSrBtiJtNJc_r0m8yP6nyxDkzhLQnsxBdp-ca096b59a5bc4cb15dfb.png)

Floating toolbar size and padding measurements

![Diagram noting layout margins.](../../_assets/l1zIH0wA5J3kRRwuwvmIpG4gmlFXXYK88L4lF0q5vQ0_ThjPiPwpPJk0mOT8zbMyO20rMum-TPkHfY65-f57b95c5f6ff6c6b99a6.png)

Floating toolbar margins

* * *

## Bottom app bar (baseline)

![Diagram of bottom app bar indicating the container.](../../_assets/XW6h1Afu7o0EPJEU5KC5OEODx1r67sQMqU9pUmqzyOAPy1b_y8-pMDrw-GqoWeSbEXhBR7cA_qDpTDdG-783a6c7eee3bd00bf9f9.png)

1.  Container

### Tokens & specs

Bottom app bar tokens are in one token set.

Token

Value

Enabled

Close

### Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)

![Diagram of bottom app bar indicating its color mappings.](../../_assets/RDMrnLfQpoptezvVbHosgCQV_qq-MEVY3hKWH4U1fo8wYZLg0Zv4Z1jqiQT1FxojqUYoCEZ8lekjZ3SY-e2718eb9a34a6c394e8c.png)

Bottom app bar color role used for light and dark themes:

1.  Surface container

### Measurements

![Diagram showing layout values and paddings for bottom app bar.](../../_assets/42HaRTtyV44uEgw2rZzgGwWNqlOy1g0mCiaUjMy7iuiG2lAJ4ACu5xe9PEJgOfE2PFIJ_8TjIRqrk75W-ba259f420520da101fad.png)

Bottom app bar padding and size measurements

### Common layouts

![Side by side view of bottom app bars in different configurations.](../../_assets/JvPTixMCyejczwwssuEezKtZO-2y_RmCjTIrMEpHFu5HOAApXlYpEt-Pq3GV4Bd1LJQlgRd4O3PPpK7Y-2884e37e8d4b17c5d1c9.png)

1.  Icon buttons and FAB
2.  Icon buttons and no FAB
