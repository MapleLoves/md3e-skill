---
source: https://m3.material.io/components/floating-action-button/guidelines
title: "Floating action buttons (FABs)"
captured: 2026-09-14
---

# Floating action buttons (FABs)

> Floating action buttons (FABs) help people take primary actions

![3 screens with various FAB sizes.](../../_assets/mkapod2e-01-68cda235231684d20d9c.png)

FABs have multiple sizes that scale with the breakpoint

## Usage

Use a FAB for the most important action on a screen; it appears in front of all other content.

The FAB can be aligned left, center, or right. It can be positioned above the navigation bar, or nested within it.

![A Compose FAB is positioned above a nav bar on a mobile email inbox.](../../_assets/mkapp0w4-02-7463f4e628d6a549c39d.png)

FABs can use dynamic color

There are three FAB sizes:

1.  FAB

2.  Medium FAB (most recommended)

3.  Large FAB

Choose the FAB size based on the visual hierarchy of your layout. 

Note: The small FAB is no longer recommended.

![3 FAB sizes.](../../_assets/mkappjdx-03-aeb55d9eaccd49ba3b80.png)

1.  FAB 
2.  Medium FAB
3.  Large FAB

The FAB is the smallest size, and is best used in compact windows Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact breakpoints](/m3/pages/breakpoints/compact) where other actions may be present on screen.

The medium FAB is recommended for most situations, and works best in compact and medium windows Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium breakpoints](/m3/pages/breakpoints/medium) . Use it for important actions without taking up too much space. 

A large FAB is useful in any window size when the layout calls for a clear and prominent primary action, but is best suited for expanded Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded breakpoints](/m3/pages/breakpoints/expanded) and larger breakpoints, where its size helps draw attention.

![A medium FAB over an email app UI.](../../_assets/mkapq84r-04-faeb3f82e21831440c9f.png)

Use a medium FAB in most breakpoints

![A large FAB over an email app UI.](../../_assets/mkapqn1b-05-fd18cae909ce92358a61.png)

Use a large FAB when the primary action needs to be prominent

![A photo feed with no FAB.](../../_assets/mkapr8x3-06-do-3c6321bb7e89ecafc784.png)

check Do

FABs are not needed on every screen, such as when images represent primary actions

![A screen with 3 FABs makes it hard to tell what the primary action should be.](../../_assets/mkaps2z9-07-don-t-f079666d7a779c59a4b9.png)

close Don’t

Don't display multiple FABs on a single screen

A FAB can transform into an extended FAB Extended floating action buttons (extended FABs) help people take primary actions. [More on extended FABs](/m3/pages/extended-fab/overview) on larger screens, or it can transition into a FAB menu when selected. Use a FAB menu when there are many kinds of actions relevant to the FAB. 

[More on FAB menus](/m3/pages/fab-menu)

![A extended FAB saying “Share” with a less popular share icon.](../../_assets/6gVz4SSpnVYq28cYhUlwX36JiaNZLx-0A1NhL4z0IUA-RwlUz5tsApAkIXx0RAVE780uol-6VkeZZq7j-a41c2e996cef0712d7c0.png)![A extended FAB saying “Share” with a less popular share icon.](../../_assets/6gVz4SSpnVYq28cYhUlwX36JiaNZLx-0A1NhL4z0IUA-RwlUz5tsApAkIXx0RAVE780uol-6VkeZZq7j-302b3eb8e2913106ed53.png)

Use the extended FAB when label text is necessary

![A FAB menu showing 3 actions related to sharing.](../../_assets/YtrgWibQJDIheCADkeWKz14g7auX0_zMKtGJ8o45F48iJl9BvPomdwRJGi8bjtOnAH7gtd-8V5ki1gS2-403c54c91c7ba7895dc2.png)![A FAB menu showing 3 actions related to sharing.](../../_assets/YtrgWibQJDIheCADkeWKz14g7auX0_zMKtGJ8o45F48iJl9BvPomdwRJGi8bjtOnAH7gtd-8V5ki1gS2-fdce03665097cd582a5a.png)

Use the FAB menu when there are many kinds of actions relevant to the FAB

## Actions

A FAB can trigger an action on the current screen, or it can perform an action that creates a new screen.

A FAB promotes an important, constructive action such as:

-   Create
-   Favorite
-   Share
-   Start a process

![FABS for 12 common actions including, create, edit, and navigate.](../../_assets/mkaptzjv-10-167aa2defc42b6a24a57.png)

check Do

Use FABs for primary, positive actions

Avoid using a FAB for minor or destructive actions, such as:

-   Archive or trash

-   Alerts or errors

-   Limited tasks like cutting text

-   Controls better suited to a toolbar, like to adjust volume or font color

![FABs for 18 minor or destructive actions, such as cut, trash, and volume.](../../_assets/mkapug9u-11-e49130949bbb21535647.png)

close Don’t

Don’t use FABs for minor, overflow, unclear, or destructive actions

## Anatomy

![2 elements of a FAB.](../../_assets/mkapv2og-12-9de6b9e8184c42523f31.png)

1.  Container
2.  Icon

### Container

The FAB is typically displayed in a square container. The container shouldn’t be covered by other elements, such as badges.

The container must have sufficient color contrast with the surface it’s placed on.

![A bright colored FAB has high contrast with the background.](../../_assets/mkaq0msf-13-2cc02bd62e89d28a87e7.png)

A FAB container color needs to stand out from its background

### Icon

An icon in a FAB should be clear and understandable. When hovering over a FAB on web products, FABs should display a tooltip with an accompanying icon text label. Use a filled icon instead of an outlined icon.

A FAB shouldn't contain notifications or actions found elsewhere on a screen.

![4 FABs each with a simple icon.](../../_assets/mkaq1779-14-77b05b672fe6bcb488a8.png)

check Do

Use clear and simple icons such as add, message, or edit

![4 FABs each with an ambiguous icon.](../../_assets/mkaq1wxv-15-75376101fe8c9a3dcdcd.png)

close Don’t

Don’t use confusing or open-ended icons to symbolize less common actions

## Adaptive design

In compact Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact breakpoints](/m3/pages/breakpoints/compact) and medium breakpoints Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium breakpoints](/m3/pages/breakpoints/medium) , the best place for the FAB is typically the lower right corner of a screen, since it’s easy to reach and is less likely to cover important content.

In expanded breakpoints Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded breakpoints](/m3/pages/breakpoints/expanded) , consider placing the FAB in the upper left corner, like in the navigation rail Navigation rails let people switch between UI views on mid-sized devices. [More on navigation rails](/m3/pages/navigation-rail/overview) . This positions it as one of the first interactive elements people see when they land on the page.

Adjust the size of the FAB based on the context. Use a medium FAB for mobile layouts, and large FAB for tablets and large screens. 

![Large screen layout showing FAB in upper left region of the screen, below navigation rail icon.](../../_assets/mkaq2b6m-16-523f94c96fea178333b8.png)

For large screens, place the FAB in the upper left corner

![A screen layout with several interactive elements. A single FAB is in the navigation rail.](../../_assets/mkaq2qmb-17-0f0dcb3031fb7b381fcb.png)

check Do

A FAB can be used within a navigation component, such as a navigation rail

![A busy screen layout with 8 cards, each with their own FAB.](../../_assets/mkaq35yc-18-a500b3aabc8091b862c6.png)

close Don’t

Individual components, such as cards, shouldn’t have their own FAB

## Behaviors

### Appearing

When a FAB animates on screen, it expands outward from a central point. The icon within it can be animated as well.

While FABs should be relevant to screen content, they aren't attached to the surface on which content appears. FABs move separately from other UI elements because of their relative importance.

**Screen transitions
**FABs can morph to launch related actions. When a screen changes its layout, the FAB should disappear and reappear during the transition.

**Reappearance
**The FAB should only reappear if it's relevant to the new screen. It should reappear in the same position, if possible.

FAB animating on screen

### Expanding

The FAB can expand and adapt to any shape using a container transform transition pattern. This includes a surface that's part of the app structure, or a surface that spans the entire screen.

The FAB can also transition into a FAB menu. 

[More on FAB menus](/m3/pages/fab-menu)

FABs can expand and adapt to any shape

### Scrolling

FABs remain in place on scroll.

Extended FABs can collapse into a FAB on scroll and expand on reaching the bottom of the view.

FABs stay in place above a scrolling background

### Moving across tabs

When tabs are present, the FAB should briefly disappear, then reappear when the new content moves into place. This shows that the FAB is not connected to any particular tab.

check Do

The FAB should disappear and reappear when switching pages

Don't animate the FAB with body content.

close Don’t

Don’t keep the FAB on screen when switching pages
