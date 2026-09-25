---
source: https://m3.material.io/components/extended-fab/overview
title: "Extended FABs"
captured: 2026-09-14
---

# Extended FABs

> Extended floating action buttons (extended FABs) help people take primary actions

-   Use for the most common or important action on a screen

-   Three variants: small, medium, and large

-   Use instead of FAB when label text is needed to understand action

![3 extended fab sizes.](../../_assets/m0df17xu-01-184b55314ff020def7f7.png)

1.  Small extended FAB
2.  Medium extended FAB
3.  Large extended FAB

## Availability & resources

| Type | Resource | Status |
| --- | --- | --- |
| Design |
| [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) | Available |
| Implementation |
| [Flutter](https://api.flutter.dev/flutter/material/FloatingActionButton-class.html) | Available |
| [Jetpack Compose](https://developer.android.com/develop/ui/compose/components/fab?hl=en#extended) | Available |
| [Jetpack Compose: Expressive](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ExtendedFloatingActionButton\(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1\)) | Available |
| [Android Views (MDC-Android)](https://github.com/material-components/material-components-android/blob/master/docs/components/FloatingActionButton.md#extended-fabs) | Available |
| [Android Views (MDC-Android): Expressive](https://github.com/material-components/material-components-android/blob/master/docs/components/FloatingActionButton.md#extended-fabs) | Available |
| [Web](https://github.com/material-components/material-web/blob/main/docs/components/fab.md) | Available |
|
Web: Expressive

 | Unavailable |

Close

## M3 Expressive update

**May 2025**

The extended FAB now has three sizes: small, medium, and large, each with updated type styles. These align with the FAB Floating action buttons (FABs) help people take primary actions. [More on FABs](/m3/pages/fab/overview) sizes for an easier transition between FABs. The baseline extended FAB is no longer recommended and should be replaced with the small extended FAB. Surface and FABs are also no longer recommended. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive)

Variants and naming:

-   Added new sizes

    -   Small: 56dp

    -   Medium: 80dp

    -   Large: 96dp

-   No longer recommended

    -   Baseline extended FAB (56dp)

    -   Surface extended FAB

Updates:

-   Adjusted typography to be larger

![The baseline extended FAB and the small, medium, and large extended FABs from the expressive update.](../../_assets/o8RP_K8msVBonOVgmcnANIcH_obxNxoaP2OKhzTpcLR6f6W8f2TJH0x2t0k703n-EIp_WM4_fMyA4JBq-4c38825d3397b1093984.png)![The baseline extended FAB and the small, medium, and large extended FABs from the expressive update.](../../_assets/o8RP_K8msVBonOVgmcnANIcH_obxNxoaP2OKhzTpcLR6f6W8f2TJH0x2t0k703n-EIp_WM4_fMyA4JBq-5ee6a7aacc452e235109.png)

The baseline extended FAB is replaced with a set of small, medium, and large extended FABs with new typography

## Differences from M2

-   Color: New color mappings and compatibility with dynamic color
-   Layout: Extended FAB is the same height as the FAB
-   Shape: Boxier style with smaller corner radius

![Diagram comparing the M2 FAB and extended FAB.](../../_assets/CLwhLFrMkpEgnOAWORcnTMHBqt8gZ67coHMiSw1taCuxR0nRqasV1w7XWJ50w6ZT6gD6aZql87KrxZHd-a7a38ff9fb55be19f4ce.png)![Diagram comparing the M2 FAB and extended FAB.](../../_assets/CLwhLFrMkpEgnOAWORcnTMHBqt8gZ67coHMiSw1taCuxR0nRqasV1w7XWJ50w6ZT6gD6aZql87KrxZHd-253cdcaab338d81c7e53.png)

M2: Extended FABs are pill-shaped and have a different height and elevation

![Diagram comparing the M3 FAB and extended FAB.](../../_assets/m0dff6p3-05-08c26e20fb2e70f23d81.png)

M3: Extended FABs share the same height, boxier shape, and simpler elevation model as FABs
