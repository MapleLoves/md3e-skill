---
source: https://m3.material.io/components/lists/overview
title: "Lists"
captured: 2026-09-14
---

# Lists

-   Use lists to help people find a specific item and act on it

-   Order list items in logical ways, like alphabetical or numerical

-   Keep items short and easy to scan

-   Show icons, text, and actions in a consistent format

-   Choose between standard and segmented styles

![1 list contains 3 items, each with a label text, supporting text, and trailing text. A music app shows list items with leading images.](../../_assets/mi8nxjh0-01-63b9796f40c170e42491.png)

A list item's label text, supporting text, image, and trailing icon can be customized to create a variety of lists

## Availability & resources

Close

## M3 Expressive update

Lists have a new segmented visual style, improved selection treatment, and support for slots. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive)

**December 2025** 

Variants:

-   Added **expressive** list

    -   Recommended for new designs

-   List ( baseline Baseline variants are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles. [More on M3 Expressive](<https://m3.material.io/blog/building-with-m3-expressive >) ) is still available

New visual styles:

-   Standard or segmented

-   Highlighted selection states

-   Flexible slots

Supported platforms:

-   [Android Views (MDC-Android)](https://github.com/material-components/material-components-android/blob/master/docs/components/List.md#m3-expressive)

-   [Jetpack Compose](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ListItem%28kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.material3.ListItemColors,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp%29)

![2 party planning lists with 2 completed list items each. In 1 list, the selected items are highlighted.](../../_assets/mi8pwbjv-02-890a074f84e2875348b0.png)

Expressive lists feature improved selection states

## Differences from M2 to M3 baseline

-   **Color:** New color mappings and compatibility with dynamic color Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI. [More on dynamic color](/m3/pages/dynamic/choosing-a-source)

-   **Layout:** Padding and spacing rules are updated to be more consistent

-   **Height:** The tallest element within a list item determines the list item’s height - either 56dp, 72dp, or 88dp

-   **Alignment:**

    -   In most cases, elements in a list item are middle-aligned

    -   If a list is 88dp or larger, or contains three or more lines of text, elements are top-aligned

![3 variants of lists in M2.](../../_assets/mi8q1tdh-03-f13ab1b086a1068924e3.png)

M2: Non-standard heights and alignments

![3 variants of lists in M3 baseline.](../../_assets/mi8q2xsp-04-8027a26ba8ba7383340e.png)

M3 (baseline): Standardized heights and alignments
