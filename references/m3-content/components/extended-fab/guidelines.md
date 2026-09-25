---
source: https://m3.material.io/components/extended-fab/guidelines
title: "Extended FABs"
captured: 2026-09-14
---

# Extended FABs

> Extended floating action buttons (extended FABs) help people take primary actions

![Vibrant extended FAB on an email screen.](../../_assets/m0dfvsl8-01-d8f55fdf7459f4478997.png)

Extended FABs are more prominent than regular FABs

## Usage

Use an extended FAB on screens with long, scrolling views that require persistent access to an action, such as a checkout screen. 

Use it when label text helps understand the main action, or to add further emphasis to the button.

![A centered extended FAB is used to check out in a shopping app.](../../_assets/m0dfxjts-02-f01a5e527e1720245b4e.png)

Extended FABs ensure the main action is visible at all times

![Extended FAB on an article with lots of body content to publish that article.](../../_assets/m0dfymif-03-771fee102293ac922289.png)

Use an extended FAB to provide constant access to a primary action above long-scrolling surface content

![Extended FAB on a task list to create a new task.](../../_assets/m0dfzjai-04-2cce1a3a2657d6f6269d.png)

Use an extended FAB to emphasize a page’s primary action

### Additional emphasis

The extended FAB can provide more emphasis and clarity to a product’s primary action. 

Since it has room for both a text label and icon, the extended FAB can be effective where an icon alone is ambiguous. However, the relationship between an extended FAB's icon and label should be clear.

![Extended FAB labeled “find flights” with an airplane icon, which would be unclear on its own.](../../_assets/m0dg2hbe-05-947d0834a8fff27d609d.png)

An extended FAB can be effective where an icon alone is too vague

Like the regular FAB, only one extended FAB should be used per screen. 

Multiple FABs compete for attention. 

If additional high-level actions are required, consider adding more buttons elsewhere on the page.

![An extended FAB used on a screen.](../../_assets/m0dg63ur-06-92a14cd37ddbf68b7939.png)

check Do

Only show one prominent action at a time with the extended FAB

![2 extended FABs used on 1 screen.](../../_assets/m0dg6za4-07-9ae74ff29137884bfcc2.png)

close Don’t

Don’t use multiple extended FABs in one screen as it disrupts visual hierarchy

The extended FAB shouldn't be used as an option in a set of actions. 

Instead, use filled buttons for a similar level of emphasis.

![Filled button labeled “finish setup” next to a “back” button.](../../_assets/m0dg9f6o-08-9bcc8f7f8506edebb220.png)

check Do

Use a button with appropriate styling to emphasize it in a group of buttons

![Extended FAB labeled “finish setup” next to a “back” button.](../../_assets/m0dgacb3-09-4ae07cf48259355edf04.png)

close Don’t

Don’t use the extended FAB to convey an option in a set of actions

### Choosing a size

There are three variants of extended FABs: small, medium, and large.

Choose an appropriately-sized extended FAB to add the right amount of emphasis for an action. 

In compact windows with one prominent action, the large extended FAB can be appropriate.

In larger breakpoints, use a medium or large extended FAB.

![1 large, 1 medium, and 1 small extended FAB on 3 different screen sizes.](../../_assets/m0dhk1cf-10-a60eb6a8b22d3966177f.png)

There are three sizes of extended FABs

## Anatomy

![3 extended FAB elements.](../../_assets/m0dhlqdv-11-f77cd50729693d6e673c.png)

1.  Container 
2.  Label text 
3.  Icon (optional)

### Container

The extended FAB container is a rounded rectangle that hugs its contents. 

The extended FAB grows and shrinks with text length.

![Fixed-width extended FAB, centered, ignoring layout grid.](../../_assets/m0dhmym8-12-a44ae1e7c7e889de52fe.png)

The extended FAB container hugs the icon and text

### Icon (optional)

An extended FAB's icon should intuitively represent its action.

![Extended FAB without an icon, labeled “Save draft”.](../../_assets/m0dgr1oq-13-c1d6770c924828d0af44.png)

check Do

Unlike standard FABs, extended FABs don't require an icon

![Extended FAB with icon only, with no label text. ](../../_assets/m0e6c0j7-14-3142d1695ba09748984d.png)

close Don’t

An extended FAB can't have an icon without a text label

### Label text

The extended FAB’s label should clearly describe its action.

Use 1–2 words at most. Keep in mind that localization may increase the amount of characters and width of the extended FAB.

![Extended FAB with short text “Save”.](../../_assets/m0dhs8b9-15-b8cd13fd57ad4bba46c8.png)

check Do

Shorten the text as much as needed. Include an icon for additional context.

![Extended FAB with wrapping text “Save draft in folder”.](../../_assets/m0dhtaim-16-e411f9f109ee201a81bf.png)

close Don’t

Avoid wrapping or truncating text

## Placement

![Extended FAB placed above navigation bar.](../../_assets/m0di65x4-17-db281007347d3f550a7f.png)

check Do

Place the extended FAB above the rest of the UI, off of elements like app bars

![Extended FAB overlaid on a docked toolbar.](../../_assets/m0di94u1-18-389aeae79ff3121ce766.png)

close Don’t

Don’t place the extended FAB on top of toolbars. It disrupts the consistency of the elevation and surface layers.

![Extended FAB below an app bar at the top of a mobile screen.](../../_assets/m0dia4hb-19-309311151bf0a2acdf13.png)

close Don’t

Don’t place the extended FAB in the upper half of a mobile screen, as it disrupts the reading of the UI

![An extended FAB labeled "Confirm" on a dialog to "Confirm your location".](../../_assets/m0dib69h-20-239239741088cad672d1.png)

close Don’t

Don’t place extended FABs on cards or inside other containers

Avoid putting other floating components, like the floating toolbar Floating toolbars float on top of page content and can provide contextual, dynamic actions. [More on toolbars](/m3/pages/toolbars/overview) , on screen with the extended FAB.

![The extended FAB is next to a floating toolbar.](../../_assets/m0dif190-21-c195a2c53936aaac93a8.png)

close Don’t

Floating toolbars can be paired with FABs, but not extended FABs

## Responsive layout

The FAB and extended FAB can transform into each other depending on available space and layout. 

In a collapsed navigation rail Collpased navigation rails take up minimal space and are best for medium windows and wider. [More on navigation rails](/m3/pages/navigation-rail/overview) , a FAB would be used. When the rail is expanded, the FAB can transform into an extended FAB. 

![Example of extended FAB transforming into standard FAB.](../../_assets/m0djhpqm-23-8a8285290b7c4dd35fc0.png)

When space is limited, an extended FAB can transform into a FAB

### Right-to-left languages

Extended FABs should mirror their elements in right-to-left (RTL) languages.

![Extended FAB in a left-to-right language placed at the bottom right of a screen. The icon is to the left of the text.](../../_assets/m0djk489-24-246c1c9748f6325adf56.png)

Icons should be placed to the left of labels for left-to-right (LTR) languages

![Extended FAB in a right-to-left language placed at the bottom left of a screen. The icon is to the right of the text.](../../_assets/m0djl493-25-fd99155f32196c25dbd8.png)

Icons should be placed to the right of labels for RTL languages

### Breakpoints

In compact Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact breakpoints](/m3/pages/breakpoints/compact) and medium breakpoints Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium breakpoints](/m3/pages/breakpoints/medium) , the extended FAB should be placed at the bottom of the screen, either center-aligned or aligned to the trailing edge of the window.

![Extended FAB center-aligned on a mobile screen.](../../_assets/m0djn9nf-26-651d543da8e25321211b.png)

The extended FAB can be center-aligned

![Extended FAB right-aligned on a mobile screen.](../../_assets/m0djo3i8-27-253964bb839bf0383662.png)

The extended FAB can be aligned to the trailing edge of the window

In expanded Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded breakpoints](/m3/pages/breakpoints/expanded) and larger breakpoints, the extended FAB should appear either:

-   At the bottom right edge of the window, in both LTR and RTL languages

-   Within the navigation rail

![Extended FAB at bottom right of screen.](../../_assets/m0djp9q0-28-4470f334a4d08f38e3c0.png)

The extended FAB can be right-aligned in both LTR and RTL languages

![Extended FAB in navigation drawer.](../../_assets/m0djqcsu-29-412933a2ffcf57cf22b7.png)

The extended FAB can be at the top of the expanded navigation rail

## Behavior

### Appearing

The extended FAB surface expands when appearing on screen using an [enter and exit](/m3/pages/motion-transitions/transition-patterns#e1c2a650-d7a4-4a6d-9025-e6b7845291ed) transition pattern.

An extended FAB expands when appearing on screen

### Expanding

The extended FAB can expand and adapt to any shape using a [container transform](/m3/pages/motion-transitions/transition-patterns) transition pattern. 

This includes a surface that is part of the app structure, or a surface that spans the entire screen.

An extended FAB can expand and adapt to any shape

### Transforming

The extended FAB can transform into a FAB on scroll to temporarily take up less space on screen.

An extended FAB can transform into a FAB

### Scrolling

The extended FAB can transform into a FAB when scrolling down, and back to an extended FAB when scrolling up.

An extended FAB collapses and expands when scrolling

When the FAB switches to an extended FAB, the following transitions occur:

-   The FAB shape changes
-   FAB icon moves to the left
-   FAB text label fades in

FAB switches to an extended FAB
