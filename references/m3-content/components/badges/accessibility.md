---
source: https://m3.material.io/components/badges/accessibility
title: "Badges"
captured: 2026-09-14
---

# Badges

> Badges show notifications, counts, or status information on navigation items and icons

## Use cases

People should be able to use assistive technology to:

-   Understand the dynamic information conveyed in badges, such as counts or labels
-   Address badge announcements by selecting corresponding navigation destinations

## Interaction & style

Badges are most commonly used within other components, such as navigation bar Navigation bars let people switch between UI views on smaller devices. [More on navigation bars](/m3/pages/navigation-bar/overview) , navigation rail Navigation rails let people switch between UI views on mid-sized devices. [More on navigation rails](/m3/pages/navigation-rail/overview) , app bars App bars display navigation, actions, and text at the top of a screen. [More on app bars](/m3/pages/app-bars/overview) , and tabs Tabs organize content across different screens and views. [More on tabs](/m3/pages/tabs/overview) .

When a badge is used to indicate an unread notification, the badge gets hidden once it's selected.

## Visual indicators

Badges use a color intended to stand out against labels, icons, and navigation elements. Use the default color mapping to avoid color conflict issues.

![Diagram of large and small badges showing that they need to pass 3 to 1 contrast.](../../_assets/mg0x2h51-02_do-e91ca3e52bb49b3d11f9.png)

check Do

Badges must use default color with at least 3:1 contrast

![Diagram of large and small badges not passing 3 to 1 contrast.](../../_assets/mg0x2kti-03_dont-2f8bb7386b8f0074adf5.png)

close Don’t

Avoid using custom color roles for the badge container and label text. If custom roles are necessary, make sure they have contrast of at least 3:1.

## Labeling elements

The accessibility Accessible design makes products usable for people with all kinds of abilities. [More on accessibility](/m3/pages/overview/principles) label for a badge item will be read after its navigation destination. Any numerical badges will have their number read, while non-counting badges will simply announce **New notification**.

![Navigation bar highlighting numerical badge.](../../_assets/me8l8lhl-04-77ea3e1d4ad39a0d53dc.png)

Numerical badges will have their number read

![Navigation bar highlighting non-counting badge.](../../_assets/me8l9na6-05-3b18199b5fe5450978a1.png)

Non-counting badges will simply announce **New notification**
