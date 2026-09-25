---
source: https://m3.material.io/foundations/watches/layout
title: "Design for watches"
captured: 2026-09-14
---

# Design for watches

> Watches have special design considerations and interaction patterns

## Resources

| Type | Resource |
| --- | --- |
| Design | [Wear OS common design layouts](https://developer.android.com/design/ui/wear/guides/foundations/common-layouts) |
| [Adaptive layout for Wear OS](https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design) |
| [Figma Design Kit for Wear OS Apps](https://www.figma.com/community/file/1506418396052412186) |
| [Figma Design Kit for Wear OS Tiles](https://www.figma.com/community/file/1507852095734722321/m3-wear-os-tiles-design-kit?fuid=1348995927136540612) |
| Implementation | [Android Developers: Wear OS](https://developer.android.com/training/wearables) |

## Layout principles

![A social networking scrolling screen showing Followers, sorting and search.](../../_assets/mp4d4yba-01-12e77941b61e8a277320.png)

**Prioritize content**

Place the most important information at the top of the screen.

![An audio interface showing headphones are connected with volume indicator and controls.](../../_assets/mp4d5pli-02-5bf5b9c0305fd1edd031.png)

**Limit choices**

Reduce the number of actions to prevent decision fatigue. Focus on critical tasks to help people get things done within seconds.

![A dialog confirming device access to call log and contacts.](../../_assets/mp4d6ew9-03-f12e90fc909a271d5192.png)

**Simplify navigation**

Use a clear, shallow hierarchy so people don't get lost in complex menus. Aim to display content and navigation inline.

## Standard layouts

For scrolling and non-scrolling apps:

-   The time is shown on most app screens

-   Edge-hugging buttons are used for round screens

-   Show an indicator if more content is available on a scrolling apps

Wear OS offers [Figma Design Kits](https://developer.android.com/design/ui/wear/guides/get-started/design-kits) for standard layouts, with components, styles, and variables.

![A watch screen showing a social media app and a watch screen showing a timer with element indicators.](../../_assets/mp4d7u52-04-db455f1ce56d153edf0e.png)

1.  Time text

2.  Page title

3.  Scroll indicator

4.  Action button

### Non-scrolling layouts

Non-scrolling layouts are for focused tasks or single-screen interactions where all content fits within the display, such as: 

-   Media players

-   Pickers and switchers

-   Fitness tracking screens

-   Confirmation dialogs 

[More on non-scrolling layouts for Wear OS](https://developer.android.com/design/ui/wear/guides/surfaces/apps/layouts/scrolling)

![A non-scrollable timer with current time 9:30, timer set for 00:25:52, and a start button.](../../_assets/mp4d8mdi-05-bc909c0654fa7deea9b3.png)

Use non-scrolling layouts for focused tasks like a timer

### Scrolling layouts

Scrolling layouts can show content that exceeds the screen height, such as lists or dialogs. These might include:

-   Message threads

-   Contact lists

-   Menu options

[More on scrolling layouts for Wear OS](https://developer.android.com/design/ui/wear/guides/surfaces/apps/layouts/scrolling)

![A scrollable layout with current time, search button, 1st follower and avatar on screen, and two followers off screen.](../../_assets/mp4d98d6-06-d74ff1eed1a28a5c2b0e.png)

Lists use scrolling layouts to show additional options

### Tiles

Tiles (or widgets) are designed for glanceability. Use them to show timely updates or to help people perform frequent tasks quickly, such as checking progress towards a goal or viewing the weather.

Tiles are accessible with a swipe from the watch face. They have a fixed screen height and don't scroll.

[More on tiles for Wear OS](https://developer.android.com/design/ui/wear/guides/foundations/common-layouts/tiles)

![Icon buttons for meditation, running, cycling, and a More button](../../_assets/mp4dbada-07-45f98d31ff6beea34ebb.png)

Use tiles for quick access to to a few key options

### Notifications

Notifications can be expanded to offer more interactions, such as replying to a message, opening a location on a map, or playing a song.

Wear OS provides notification templates for instant messaging and calendar events.

[More on notifications for Wear OS](https://developer.android.com/training/wearables/notifications)

![A message notification shown in a drawer with dimmed notifications above and below.](../../_assets/mp4dbzlj-08-dd7a15bddcf75e0296e5.png)

Notifications should offer easy access to more interactions

### Adaptive layout

Adaptive design allows apps to adapt to different screen sizes and device contexts. On Wear OS, this means apps scale and reorganize to maximize the available space on both small and large round displays. [The Material 3 Compose component library](https://developer.android.com/jetpack/androidx/releases/compose-material3?_gl=1*1ntglil*_ga*NzMzMjg1Nzc1LjE3NDg5MTM2NjI.*_ga_QPQ2NRV856*czE3NjQ3MDkwMjUkbzc2JGcxJHQxNzY0NzEwNjAyJGo0MCRsMCRoMA..) has built-in adaptive behavior.

-   Design for small screens first: Start by designing for the smallest common screen size

-   Use percentages: Define margins and padding using percentages rather than fixed pixel values. This prevents clipping and ensures content remains centered and proportional as the screen size increases.

-   Add value on larger screens: Use the extra space on screens larger to show more content, such as additional buttons, text lines, or data visualizations

-   Test all font sizes: Font scaling and accessibility settings such as bold text may cause changes in the size of UI elements

[More on adaptive layout for Wear OS](https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design)

![5, 10, and 15 minute alarm buttons plus an edge-hugging more button.](../../_assets/mp4dcvb2-09-549511cfd26b0fdfcf51.png)

Design for small screens first, starting with a 192dp size watch

![5, 10, 15, 20 &amp; 30 minute alarm buttons plus an edge-hugging more button.](../../_assets/mp4dg8dm-10-c8bcf2e46c0f6124bbad.png)

Show more content on devices that are larger than 225dp
