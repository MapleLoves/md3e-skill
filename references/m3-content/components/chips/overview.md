---
source: https://m3.material.io/components/chips/overview
title: "Chips"
captured: 2026-09-14
---

# Chips

> Chips help people enter information, make selections, filter content, or trigger actions

-   Use chips to show options for a specific context

-   Four variants: assist Assist chips represent smart or automated actions that can span multiple apps, such as opening a calendar event from the home screen. , filter Filter chips use tags or descriptive words to filter content. They can be a good alternative to toggle buttons or checkboxes. , input Input chips represent discrete pieces of information entered by a user, such as Gmail contacts or filter options within a search field. , and suggestion Suggestion chips help narrow a user’s intent by presenting dynamically generated suggestions, such as suggested responses or search filters.

-   Chip elevation Elevation is the distance between two surfaces on the z-axis. [More on elevation](/m3/pages/elevation/overview) defaults to 0 but can be elevated if they need more visual separation

![4 chip variants.](../../_assets/lzthj7vk-1-94e7b51fb88770af8566.png)

1.  Assist chip
2.  Filter chip
3.  Input chip
4.  Suggestion chip

## Availability & resources

| Type | Resource | Status |
| --- | --- | --- |
| Design |
| [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) | Available |
| Implementation |
| [Flutter](https://api.flutter.dev/flutter/material/Chip-class.html) | Available |
| [Jetpack Compose](https://developer.android.com/develop/ui/compose/components/chip) | Available |
| [Android Views (MDC-Android)](https://github.com/material-components/material-components-android/blob/master/docs/components/Chip.md) | Available |
| [Web](https://github.com/material-components/material-web/blob/main/docs/components/chip.md) | Available |

Close

## Updates

**Aug 2024**

Updated stroke color from **outline** to **outline variant**.

![A chip with a clear outline is now a chip with a subtle outline.](../../_assets/m8sdpshu-02-83589bd4c6c39bb220d5.png)

The stroke color was softened to improve visual hierarchy between chips and buttons

## Differences from M2

-   Color: New color mappings and compatibility with dynamic color Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI. [More on dynamic color](/m3/pages/dynamic/choosing-a-source)

-   Shape: Rounded rectangle 

-   Variants: Action chips have been separated into assist chips Assist chips represent smart or automated actions that can span multiple apps, such as opening a calendar event from the home screen. and suggestion chips Suggestion chips help narrow a user’s intent by presenting dynamically generated suggestions, such as suggested responses or search filters. . Choice chips are now a subset of filter chips Filter chips use tags or descriptive words to filter content. They can be a good alternative to toggle buttons or checkboxes.

![M2 chip variants.](../../_assets/2QvL9BG6dybkEq8-MxokwRvnU_5-Yxey0SZtSxa9o6KlczyP2t5hAtUxTyZRJbGF9i7m6oOrZCWKJT4C-7e071157c865ef68abc3.png)![M2 chip variants.](../../_assets/2QvL9BG6dybkEq8-MxokwRvnU_5-Yxey0SZtSxa9o6KlczyP2t5hAtUxTyZRJbGF9i7m6oOrZCWKJT4C-b5b5da3a1ad1f4421690.png)

M2: Variants of chips are input, choice, filter, and action chips

![M3 chip variants.](../../_assets/3W0HJhJSBgfi_3TWYvZlXCPDg42elT_0VwxJmTTK5l61ZFdC9l9mPQPqPcUOBXNIce2r3aDWGNECHLco-ce07c0aadde927c7b2fc.png)![M3 chip variants.](../../_assets/3W0HJhJSBgfi_3TWYvZlXCPDg42elT_0VwxJmTTK5l61ZFdC9l9mPQPqPcUOBXNIce2r3aDWGNECHLco-5f1e1a7e7b21af62857d.png)

M3: Variants of chips updated to assist, filter, input, and suggestion chips
