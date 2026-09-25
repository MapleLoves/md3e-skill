---
source: https://m3.material.io/components/navigation-rail/accessibility
title: "Navigation rail"
captured: 2026-09-14
---

# Navigation rail

> Navigation rails let people switch between UI views on mid-sized devices

## Use cases

People should be able to do the following using the assistive technology:

-   Navigate between navigation destinations
-   Select a particular navigation destination from a set
-   Get appropriate feedback based on input type

## Interaction & style

When a navigation item is tapped, the active indicator appears, providing the following feedback to the user that it is selected:

-   A ripple passes through the indicator
-   The icon switches from outlined to filled
-   The icon and text change color

When hovered, the hover state appears, providing a visual cue that the destination is interactive.

![Colorful, purple navigation rail shown collapsed and expanded.](../../_assets/m0guemtv-01-static-4e25a25955ef531f5811.png)

Touch: Tap

![Tap indicator on a collapsed nav rail.](../../_assets/m0guep9g-02-static-5481413a1cda82af697a.png)

Cursor: Hover, Click

The target area for expanded navigation rails spans the full width of the container, even though the active indicator visually hugs the content.

![Touch indicator on a nav rail.](../../_assets/m0gud02c-03-static-2f5e89734cca1709fc7a.png)

Touch: Tap

Use a filled icon for the active destination and outlined icons for inactive destinations.

Active and inactive icon colors need sufficient contrast against the container.

![Navigation rail with filled element.](../../_assets/m0fut28q-04-59b72873d039c8e55d66.png)

check Do

Use the default color scheme to ensure proper contrast and emphasis on the active destination

![Nav rail with multiple navigation destinations and multi-colored contrast.](../../_assets/m0fut791-05-752117e26841401ebcb3.png)

close Don’t

Don’t use more than two colors for destinations or low-contrast colors in the navigation rail. This will make distinguishing active items difficult.

If an icon doesn’t have a filled style, use the semibold icon weight instead.

![Icon button with semibold weight, without filled options.](../../_assets/m2kvazns-09-5bb685fb5e421c7b97e9.png)

An icon with no filled option should use the semibold weight when active

### Text scaling and truncation

When someone sets their device to show a larger text size, the navigation rail items should grow vertically to accommodate larger labels while retaining the default padding. It’s okay for scaled text to wrap in navigation items.

To remain accessible, ensure the full label is always visible on-screen at up to 2x text sizing. Beyond this size, text can truncate. 

![Nav rail with text scaled to 1.5x size. All labels are on one line.](../../_assets/m36brxfu-04-4c0fe4ad21eb3ab78f14.png)

Text scaled to 1.5 size

![Nav rail with text scaled to 2x size. Some labels wrap to two lines.](../../_assets/m36bs1jw-05-e3a47df61e90701289df.png)

Text scaled to 2x size

### Initial focus

Initial focus lands directly on the first interactive item, whether it’s the menu, the FAB, or the first navigation item.

From the FAB or menu, **Tab** brings the person to the navigation items. **Tab** or **Arrows** then navigate between items.

![Arrows help people move between pages.](../../_assets/m0futkj8-07-67442fa1d77258cef2fc.png)

Use arrows to move between navigation items

![Space/enter help people choose a navigation destination.](../../_assets/m0futowb-08-1a3176dbdb8c2cc6e07d.png)

Use space/enter to activate the focused navigation item

### Visual indicators

Icons give the dominant cue of the navigation state. Use a filled icon for the selected destination to contrast with outlined icons for the non-selected destinations.

![Nav bar with an active, filled icon button.](../../_assets/m0futxf6-09-3f2bf21dfbc2953dd273.png)

check Do

Use a filled icon variant on the selected navigation item to differentiate from inactive navigation items

![Selected navigation item without filled icon style.](../../_assets/m0fv1bxc-10-0ac4170ce86bcde17b48.png)

close Don’t

Avoid using the same unfilled icon style for both selected and unselected items because it lacks important visual feedback cue

## Keyboard navigation

| Keys | Actions |
| --- | --- |
| Tab / Arrows | Navigate between interactive elements |
| Space / Enter | Selects an interactive element |

## Labeling elements

The accessibility label for a navigation item is typically the same as the adjacent text label.

When the visible UI text is ambiguous, accessibility labels need to be more descriptive. For example, a navigation item visibly labeled **Recent** would benefit from additional information in its accessibility label to clarify the destination's intent.

Note: On Android Views (MDC-Android), a more descriptive accessibility label is not available and the role is not announced.

![“Maps” is both the icon label text and the accessibility label.](../../_assets/m0fuvxlx-11-c9c029a32e1e7a747bfb.png)

While the visible label text reads **Recent**, the accessibility label for this switch clarifies its function: **Recent images**
