---
source: https://m3.material.io/components/fab-menu/guidelines
title: "FAB menu"
captured: 2026-09-14
---

# FAB menu

> The floating action button (FAB) menu opens from a FAB to display multiple related actions

![On a page of music albums, a FAB menu shows options to make a new playlist, collection, or station.](../../_assets/m0al2scq-01-2eb10d966ff3da55ae5c.png)

Use the FAB menu to show multiple related actions in a prominent, expressive style

## Usage

A FAB menu opens from a FAB to show multiple related actions. It should always appear in the same place as the FAB that opened it.

This makes actions immediately accessible, and keeps the UI clean by concealing actions when they’re not needed.

Don’t open a FAB menu from an extended FAB Extended floating action buttons (extended FABs) help people take primary actions. [More on extended FABs](/m3/pages/extended-fab/overview) or any other component.

![1 mobile screen with a FAB, 1 with a FAB menu. Both are right aligned.](../../_assets/m0al39xa-02-9433aaa1904c49648c68.png)

The FAB menu should always open from a FAB

The FAB menu should be aligned to the trailing edge of the window. 

In right-to-left (RTL) languages, this means the FAB and FAB menu should be aligned to the left edge, and the layout of elements should be mirrored.

![1 mobile screen with a FAB, 1 with a FAB menu. Both are left aligned and mirrored for a right-to-left language.](../../_assets/m0al3tfx-03-f50661d3e10947a8361a.png)

In RTL languages, the FAB menu should be left-aligned with the icon and text placement mirrored

FAB menus can contain 2–6 items. These should be closely related under a single action, like **Share**. 

Avoid grouping unrelated actions in the same FAB menu.

![A FAB menu with 5 options on a photo gallery UI.](../../_assets/m0al46l0-04-713619816c4e6fedbd42.png)

check Do

FAB menus can have 2-6 items

![A FAB menu with 1 option on a photo gallery UI.](../../_assets/m0al4jux-05-1a6c163bdffc63d62f8b.png)

close Don’t

Don’t use a FAB menu with one item

When a FAB is paired with other components, like the floating toolbar Floating toolbars float on top of page content and can provide contextual, dynamic actions. [More on toolbars](/m3/pages/toolbars/overview) or navigation rail Navigation rails let people switch between UI views on mid-sized devices. [More on navigation rails](/m3/pages/navigation-rail/overview) , don’t use the FAB menu. This prevents cognitive overload and interface clutter. 

![A toolbar with a FAB directly next to it.](../../_assets/m0al73q3-06-58bb18f30f15eb2dbbac.png)

check Do

FABs can be placed next to toolbars and other components

![A toolbar with a FAB menu next to it.](../../_assets/m0al7run-07-611705d18f5dbdd88a03.png)

close Don’t

Don't use a FAB menu with a toolbar or navigation rail

### Color sets

FAB menus have three color sets: primary, secondary, and tertiary. Use the color set that best matches the FAB color style.   

Use the primary FAB menu color set with the **primary** or **primary container** FAB color styles. 

![A FAB menu using the primary color set. ](../../_assets/m0al91ki-08-b9a38401d6bf0565fb2a.png)

A primary FAB is paired with a primary FAB menu

Use the secondary FAB menu color set with the **secondary** or **secondary container** FAB color styles. 

![A FAB menu using the secondary color set.](../../_assets/m0alljh0-09-71bd24d5beee1567168d.png)

A secondary FAB is paired with a secondary FAB menu

Use the tertiary FAB menu color set with the **tertiary** or **tertiary container** FAB color styles. 

![A FAB menu using the tertiary color set.](../../_assets/m0almfyg-10-ca8583397b51eac61edd.png)

A tertiary FAB is paired with a tertiary FAB menu

## Anatomy

![2 elements of a FAB menu.](../../_assets/m0alqq5m-11-c496a8e96df69fa3a53a.png)

1.  Close button
2.  List item

FAB menu items should always have label text. The icons shouldn’t be removed since they make each item easy to identify. 

![A FAB menu with 3 options for selecting Food, People, or Nature. There are no icons next to the text.](../../_assets/m0alqzgn-12-c494663cbbe8be9e5b8f.png)

exclamation Caution

Only remove the icon if necessary. The icon provides a differentiation between items.

![A FAB menu with 3 options for selecting Food, People, or Nature. The options are only icons, no text.](../../_assets/m0feodak-13-a70cb075944737235b04.png)

close Don’t

Don’t remove the label

The list item should always hug its contents and look consistent. Avoid truncating text or setting fixed widths. All FAB menu elements should be rounded.

![A FAB menu used out of the box with no configurations.](../../_assets/m0alssof-14-394c35380e2bbf7601c4.png)

check Do

Keep the padding between the container and icon, icon and text, and text and container consistent

![FAB menu items are equal width despite having different lengths of text.](../../_assets/m0alt3lp-15-13dc75eaf5c0930e3374.png)

close Don’t

Don’t expand container sizes

![FAB menu items are square instead of round.](../../_assets/m0altd3s-16-b4c974dd73fd3ecfecd0.png)

close Don’t

Don’t change FAB menu shapes

## Adaptive layout

The FAB menu can open from any sized FAB Floating action buttons (FABs) help people take primary actions. [More on FABs](/m3/pages/fab/overview) . Use with a FAB size suitable for the window size class. For example, larger FABs are recommended for larger windows.

The FAB menu works in any window size. Pair it with the FAB suitable for that window size.

The FAB menu should remain anchored to the same corner or edge regardless of window size. 

In large and extra large windows, the FAB and FAB menu margins should increase from 16dp to 24dp.

![A FAB menu with 24dp margins from the edge of the window.](../../_assets/m0alwg82-18-329cdcdeb0ccc0664475.png)

On desktop, use larger FABs and margins

On web, the FAB menu uses a menu Menus display a list of choices on a temporary surface. [More on menus](/m3/pages/menus/overview) component for an experience that's consistent with other desktop apps.

![A FAB menu using menu component on web and traditional FAB menu on compact screen.](../../_assets/JR39TV-vwPs6mYgmYNupLSLvGTNxo5S0wG8x-r0qVa89Q8qAGCVWxuhQLATpYedNHvIvXtfJrhfK7HIH-ab92732c1d1491a7aec8.png)

The same FAB menu options on both large window (left) and an Android compact window (right)

## Behavior

### Appearing

The FAB should transform into the close button of the FAB menu. The menu items should appear using the [enter and exit](/m3/pages/motion-transitions/transition-patterns#e1c2a650-d7a4-4a6d-9025-e6b7845291ed) transition.

Originate the transition from one of the FAB's trailing corners, preferably the top-aligned corner.

Animate FAB menus from the top-aligned corner of FABs

To ensure accessibility for keyboard users on the web, avoid positioning the FAB menu to completely obscure the focus indicator of an actionable element. 

Partially covering the desired element is fine, as long as the focus indicator is visible.

![FAB menu doesn’t obscure actionable element and its focus indicator.](../../_assets/m4hkgdmm-21-95ea9718780b09e190a4.png)

check Do

Ensure the actionable element and its focus indicator are visible behind the FAB menu

![FAB menu obscures both an actionable element and its focus indicator.](../../_assets/m4hkgqnr-22-22d9f207d48b21b2d73f.png)

close Don’t

Don’t block an actionable element and its focus indicator completely with the FAB menu

### Scrolling

When window height is limited, like when viewing phones in horizontal orientation, FAB menu items can scroll. 

The items should scroll behind the close button.

FAB menus can scroll if the window height is too short to contain all the options

### Expanding

Any FAB menu item can expand and adapt to any shape using a [container transform](/m3/pages/motion-transitions/transition-patterns#b67cba74-6240-4663-a423-d537b6d21187) transition pattern. This includes a surface that is part of the app structure, or a surface that spans the entire screen.

FAB menu items can transition into any kind of shape when selected
