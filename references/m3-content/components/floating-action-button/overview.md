---
source: https://m3.material.io/components/floating-action-button/overview
title: "Floating action buttons (FABs)"
captured: 2026-09-14
---

# Floating action buttons (FABs)

> Floating action buttons (FABs) help people take primary actions

-   Use a FAB for the most common or important action on a screen

-   Make sure the icon in a FAB is clear and understandable

-   FABs persist on the screen when content is scrolling

-   Three variants: FAB, medium FAB, large FAB

![The 3 sizes of floating action buttons.](../../_assets/mkap9gay-01-e1f1bece813d0566f00f.png)

1.  FAB

2.  Medium FAB

3.  Large FAB

## Availability & resources

| Type | Resource | Status |
| --- | --- | --- |
| Design |
| [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) | Available |
| Implementation |
| [Flutter](https://api.flutter.dev/flutter/material/FloatingActionButton-class.html) | Available |
| [Jetpack Compose](https://developer.android.com/develop/ui/compose/components/fab) | Available |
| [Jetpack Compose: Expressive](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#FloatingActionButton\(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0\)) | Available |
| [Android Views (MDC-Android)](https://github.com/material-components/material-components-android/blob/master/docs/components/FloatingActionButton.md) | Available |
| [Android Views (MDC-Android): Expressive](https://github.com/material-components/material-components-android/blob/master/docs/components/FloatingActionButton.md) | Available |
| [Web](https://github.com/material-components/material-web/blob/main/docs/components/fab.md) | Available |
|
Web: Expressive

 | Unavailable |

Close

## M3 Expressive update

**May 2025**

The FAB has new sizes to match the extended FAB and more color options. The small FAB is no longer recommended. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive)

Variants and naming:

-   Added **medium** FAB size

-   **Small** FAB size is no longer recommended

-   FAB and large FAB sizes are unchanged

-   FAB variants are based on size, not color

Color:

-   Added tone color styles: 

    -   Primary

    -   Secondary

    -   Tertiary

-   Renamed existing tonal color styles to match their token names: 

    -   **Primary** to **Primary container**

    -   **Secondary** to **Secondary container**

    -   **Tertiary** to **Tertiary container**

    -   The values haven't changed

-   Surface color FABs are no longer recommended

![4 FABs showing the colors available after the expressive update.](../../_assets/Kyq0kFrZiQkyIGco9EHQ5yzaPCDzbUydpq5bcHqcin1vLOhBpnqAeAW6D86dFvHrexhyJvo5jK0Brc4P-596125baf66b951bc0a7.png)![4 FABs showing the colors available after the expressive update.](../../_assets/Kyq0kFrZiQkyIGco9EHQ5yzaPCDzbUydpq5bcHqcin1vLOhBpnqAeAW6D86dFvHrexhyJvo5jK0Brc4P-4f9241410ab5cf515ed4.png)

FABs have updated colors and sizes

## Differences from M2

![M2 circular FAB with a plus icon.](../../_assets/biMTAbEZ8apVSF9QNSr9S8V1F1DCCRCRckdBmlU0g9XLCrNJMwkw_cbBk_gvb6b0JbaulKKD9lAeDTQp-bb71e8396045e5c9246e.png)![M2 circular FAB with a plus icon.](../../_assets/biMTAbEZ8apVSF9QNSr9S8V1F1DCCRCRckdBmlU0g9XLCrNJMwkw_cbBk_gvb6b0JbaulKKD9lAeDTQp-791c2c493fc0726a8467.png)

M2: FABs are circles and always have a drop shadow

![M3 rounded corner square FAB with an artist’s palette icon.](../../_assets/eSZyi5bl8kk_aCpEVo6DV_KiYuZ3i_rEVB9y7rWbFd5SSILeUBlvQ3n2ztYzvPSTe1fyMK0LKDD_axvA-fe1bbfbd1420591df49b.png)![M3 rounded corner square FAB with an artist’s palette icon.](../../_assets/eSZyi5bl8kk_aCpEVo6DV_KiYuZ3i_rEVB9y7rWbFd5SSILeUBlvQ3n2ztYzvPSTe1fyMK0LKDD_axvA-cef6666af0dd880665b8.png)

M3: FABs have a boxier shape, can use dynamic color, and include a new large FAB variation
