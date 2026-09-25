---
source: https://m3.material.io/components/toolbars/guidelines
title: "Toolbars"
captured: 2026-09-14
---

# Toolbars

> Toolbars display frequently used actions relevant to the current page

![5 toolbars of various colors, elements, and actions.](../../_assets/m7xi1w6d-01-f04a97c90886114e6585.png)

Toolbars can be used for a wide variety of use cases

## Usage

Use a toolbar to provide actions related to the current page. 

Toolbars can contain many actions and can scale to show more actions in larger windows.

![Vibrant toolbar at bottom of mobile screen.](../../_assets/m0akotbi-02-04bee459ade7d0cd2e10.png)

A toolbar provides actions related to the current page

There are two variants of toolbars:

-   **Docked toolbar** 
    Spans the full width of the window. It’s best used for global actions that remain the same across multiple pages.

-   **Floating toolbar** 
    Floats above the body content. It’s best used for contextual actions relevant to the body content or the specific page.

The baseline **bottom app bar** is no longer recommended, but is still supported.

![Docked toolbar example.](../../_assets/m0akx0bq-03-9b4860a2d4b5f9db2e7c.png)

Docked toolbar shows global controls

![Floating toolbar example.](../../_assets/m0akxxgm-04-cb6d4904c18eddbbe3a0.png)

Floating toolbar show controls relevant to the current page

When actions don’t fit in a toolbar, add a menu Menus display a list of choices on a temporary surface. [More on menus](/m3/pages/menus/overview) .

![Toolbar showing local navigation.](../../_assets/m2ytl4us-05-a6c4a142b4e63a10a466.png)

Toolbar actions can open a menu

There are two color configurations:

-   **Standard** 
    A low-emphasis color scheme best used for focusing attention on the body content.

-   **Vibrant** 
    A high-emphasis color scheme that draws attention to the controls. It can also indicate a temporary change in the page behavior, such as entering edit mode.

Consider using alternative color roles to create greater or lesser emphasis depending on the needs of the app. Experiment with different color roles to achieve different effects. 

![Toolbar with low-emphasis controls.](../../_assets/m0al28lo-06-66922f68e8c1ff35c5c7.png)

Use the standard color scheme to draw focus to content outside the toolbar

![Toolbar with high-emphasis controls.](../../_assets/m0al3avf-07-08dcb321033f5051070c.png)

Use the vibrant color scheme to emphasize controls or actions

### Toolbars & navigation bars

The toolbar and navigation bar Navigation bars let people switch between UI views on smaller devices. [More on navigation bars](/m3/pages/navigation-bar/overview) are both placed at the bottom of the window, so should **not** be shown at the same time. Show the navigation bar on primary pages, and toolbars on subsequent pages with actions.

![A navigation bar shown on the main email Inbox page, and a toolbar shown when reading the email.](../../_assets/m0al4vpg-08-57d91d52b3d26a8556ad.png)

1.  Navigation bar on a primary page

2.  Toolbar on a secondary page with contextual actions

Floating toolbars can be used as tabs between related subsequent pages in the product hierarchy. 

This helps group similar pages together, and shows that the selection affects the body content underneath.

![Floating toolbar with secondary navigation labels.](../../_assets/m0alklw0-09-b7cc7c7f4926247384f1.png)

check Do

Keep navigation distinct, and use a toolbar to display local navigation on a specific page

Consider the existing app hierarchy when using a toolbar for local navigation. 

Avoid redundant or confusing navigation combinations in the same view.

![Floating toolbar with secondary navigation labels displaying above a bottom navigation bar.](../../_assets/m0aln2r9-10-801c15203f76eaa23e4c.png)

close Don’t

Don’t show a navigation bar and a toolbar with navigation controls at the same time

## Anatomy

![Diagram of toolbar layouts.](../../_assets/m7xiiwbe-11-a337b420893443299163.png)

1.  Container

2.  Elements

### Container

The docked toolbar’s container spans the full width of the window. 

Avoid applying rounded corners to the container. This can imply the container expands or changes upon interaction.

![Docked toolbar with square corners.](../../_assets/m0als248-12-a078e039b868332176e2.png)

check Do

Use straight corners for docked toolbars

![Docked toolbar with rounded corners.](../../_assets/m0alr7n0-13-487405ce34cffd50a970.png)

close Don’t

Avoid modifying the container shape

As long as there's a minimum of 16dp padding on the leading and trailing edge, arrange controls inside however you see fit. The 32dp padding between items is just the default. 

All elements need a minimum 48x48dp target area to be accessible.

Be cautious of including too many controls as it can be overwhelming.

![Docked toolbar with too many controls.](../../_assets/m0altzpa-22-12d3871049185d8531a8.png)

close Don’t

Don’t overwhelm people with too many controls

The floating toolbar’s container should be fully visible on screen. If more actions are needed, use an overflow menu.

![Floating toolbar with overflow menu icon.](../../_assets/m0alvr9d-14-2b2bf48b5e48f15a7075.png)

check Do

Choose the most essential actions to show on screen by default

![Floating toolbar that expands off edge of screen.](../../_assets/m0alwqwe-15-e1545bb09ea8718f052d.png)

close Don’t

Floating toolbars shouldn’t exceed the edge of the window or pane

#### Elevation

Floating toolbars have elevation by default. 

If the content beneath the toolbar is visually distinct, elevation can be removed.

![Vibrant floating toolbar that's easy to see in front of a neutral text background.](../../_assets/m7xiazxd-17-006e93ad11ff6dfe41f0.png)

The elevation on floating toolbars can be removed if on a visually distinct background

### Flexibility & slots

When configuring a toolbar, think of it as a container with several slots.

These slots can be populated by buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) , icon buttons Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview) , images, text fields Text fields let users enter text into a UI. [More on text fields](/m3/pages/text-fields/overview) , or any kind of custom component.

Icon buttons provide an even hierarchy of controls. Mixing in a filled icon button can help add emphasis to a single action.

![5 toolbars with slots, and various combinations of buttons, icon buttons, filled icon buttons, and text fields.](../../_assets/m0aly7tp-16-112bf1c92cf5b21344af.png)

Toolbars are made of slots that can contain many kinds of actions

Visually emphasizing a single action more than others is an effective way to create hierarchy and guide people to controls they use most often. Avoid emphasizing more than one action at a time.

Some common ways to add emphasis to toolbar actions include:

-   Use different icon button Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview) color styles, such as filled, tonal, and standard
-   Customize the color roles Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme. [More on color roles](/m3/pages/color-roles/) of a single action, such as a primary or secondary palette
-   Use wide and narrow icon buttons 
-   Pair the toolbar with a FAB Floating action buttons (FABs) help people take primary actions. [More on FABs](/m3/pages/fab/overview)

![2 floating toolbars, 1 with a filled action button and 1 paired with a FAB.](../../_assets/m0am06ae-18-58cb6cc877fc40bd00b5.png)

Two different ways to create a high emphasis action in toolbars

![Floating toolbar with primary action and FAB.](../../_assets/m0am2tq8-19-09b94b8fd24921145f9f.png)

close Don’t

Don’t emphasize multiple buttons with bold, primary colors, such as a button and FAB together. Emphasize one action at a time.

![Floating toolbar with different control designs.](../../_assets/m0am3wil-20-3f3e1f8ac1897a9bd21d.png)

close Don’t

Avoid mixing too many different controls in the same toolbar. A consistent control design keeps things clear.

Avoid using square icon buttons in floating toolbars. Their square shape conflicts with the fully-rounded shape of the floating toolbar container.

Square buttons can be used in the docked toolbar.

![A floating toolbar, which is rounded, with squared icon buttons inside.](../../_assets/m7xigk3q-22-d334e290c5f72eab3a4f.png)

close Don’t

Don’t use square filled icon buttons in floating toolbars

### Floating toolbar with FAB

A FAB Floating action buttons (FABs) help people take primary actions. [More on FABs](/m3/pages/fab/overview) can be placed next to a floating toolbar to present one high-priority action alongside a unified set of toolbar actions.

Use a FAB for the highest-priority action in the view, or to complement the controls.

![3 toolbars paired with FABs.](../../_assets/m0am631l-21-bf154466780e886e86b3.png)

Floating toolbars can be paired with FABs

## Position & orientation

Only place docked toolbars at the bottom of the window. 

If using other bottom-aligned elements, such as a navigation bar, don't use a docked toolbar.

![Docked toolbar on mobile.](../../_assets/m0ama5z3-22-53f2a276be5481d4274f.png)

Docked toolbars are always at the bottom of the window

Floating toolbars can be horizontal or vertical. 

Horizontal toolbars should have a minimum 16dp margin from the edge of the window.

![Floating toolbar on mobile.](../../_assets/m0amca2n-23-0ac941b88b0628222031.png)

Horizontal floating toolbars should be at least 16dp from the edge of the window

In larger breakpoints, floating toolbars can be vertical and placed on either side of the screen.

Vertical toolbars should have a minimum 24dp margin.

![Vertical floating toolbar with 24dp margin.](../../_assets/m7ximrxw-26-c268916a3e7aa0d4dcb5.png)

Maintain at least a 24dp margin for vertical toolbars

To keep vertical toolbars compact, don’t use wide icon buttons. 

Use narrow or default icon buttons instead.

![Toolbar showing local navigation.](../../_assets/m0amgeqc-24-2d57994807c2d20d3e69.png)

close Don’t

Using wide buttons with vertical toolbars can unnecessarily widen toolbar containers and hide other UI elements

Vertical toolbars should be positioned opposite the navigation rail Navigation rails let people switch between UI views on mid-sized devices. [More on navigation rails](/m3/pages/navigation-rail/overview) to balance out the screen and keep actions easy to access.

When showing a navigation rail and vertical floating toolbar at once, use the centered configuration of the navigation rail.

![Large screen UI showing both a navigation rail and vertical floating toolbar.](../../_assets/m0amkwhr-TBD-1bf26d50f0333c23c83a.png)

When a nav rail is visible, the floating toolbar should be vertical on the opposite edge of the window

## Adaptive design

Adaptive design allows an interface to respond or change based on context, such as the user, device, and usage. [More on adaptive design](/m3/pages/layout-overview/adaptive-design)

### Resizing

#### Docked

The docked toolbar should always span 100% of the screen width.

In compact breakpoints Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact breakpoints](/m3/pages/breakpoints/compact) , elements in the toolbar should be evenly spaced.

In medium breakpoints Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium breakpoints](/m3/pages/breakpoints/medium) and larger, adjust the padding between controls to create a comfortable layout. This can be achieved by: 

-   Centering all elements

-   Customizing to center a key action, and aligning other elements to the edges

![Docked toolbar with evenly spaced elements.](../../_assets/ma2vff01-29-cbd648381a1edb1f8f2e.png)

Docked toolbar items should be evenly spaced in compact windows

![Docked toolbar with centered elements.](../../_assets/ma6y2uq6-30-68ce59c82a3e4f833039.png)

In medium breakpoints and larger, create a spacious layout by centering all elements

![Docked toolbar with central action and some elements pushed to the edge.](../../_assets/ma6y2g0q-31-dc6e3ec6421e9324d482.png)

Align controls to the edge of the screen to make them easier to reach on tablets, and to better highlight a primary action in the middle

On web and large screens, the docked toolbar can be rounded. Dividers can be used to organize large amounts of items. Only shrink the height and use extra small buttons if vertical space is limited.

![Docked toolbar with 15 actions for text editing on large screens, organized with dividers.](../../_assets/mbv5jv5l-33-Old-5bcb08a4c71811360dfc.png)

On web and other large screens, docked toolbars can be rounded and placed in different parts of the page

#### Floating

The container should only be as big as needed to hold the items inside before reaching the 16dp margin.

If there’s not enough space for all items, put them in an overflow menu in the trailing slot. As the breakpoint expands, more actions can be revealed.

The floating toolbar width can also be capped to keep it smaller and hide more elements.

![Floating toolbar in compact window with excess padding.](../../_assets/ma1lkstz-32-8efc79e744000c35fea2.png)

close Don’t

Don’t add extra space to a toolbar beyond its necessary items

![Floating toolbar in expanded window class.](../../_assets/image-97c79f930ee77955a96d.png)

At larger screen sizes, the container can display more controls before hitting the 16dp margin

Vertical toolbars aren’t recommended for compact windows.

They take up a significant area of the screen and may feel visually overwhelming, especially on screens with complex layouts.

Only use them when the screen is simple or when the toolbar has a few controls.

![Vertical toolbar in a compact window.](../../_assets/m7xmqa2l-34-742ece2b2cd6878c4d6c.png)

exclamation Caution

Vertical toolbars can cover important content in compact windows

### Presentation

In larger breakpoints, floating toolbars can be aligned to opposite edges of the screen so they're easy to reach and group similar actions. For example, consider placing the undo and redo actions in one toolbar, and editing controls like highlight, erase, and select in another. Stylistic differences can help emphasize each toolbar’s purpose and clarify hierarchy.

![2 toolbars, each with distinct stylistic treatment and actions.](../../_assets/m0amsqw6-29-4d279abce58f56f100e8.png)

Multiple toolbars with different stylistic treatments can create hierarchy and distinguish different kinds of actions

Don’t use multiple toolbars in compact windows. There typically isn’t enough room on screen. 

Instead, use one toolbar for all actions.

![Multiple toolbars in a compact window.](../../_assets/m7xmw01r-36-7cb7a76c5414f15c308c.png)

close Don’t

Avoid using multiple toolbars in smaller windows

Actions at the trailing edge of the toolbar can collapse into an overflow menu at smaller breakpoints, and become visible again at larger sizes. 

Actions at the trailing edge collapse into an overflow menu

### Right-to-left languages

In right-to-left (RTL) languages, mirror individual items that need it, like icons and text direction. If the order of actions is important, flip the order of the actions as well.

![Next button is on trailing edge for a LTR language.](../../_assets/m7xmygdb-37-591ad4563c793378bf8f.png)

In LTR languages, the **Next** button is intentionally placed on the trailing (right) edge

![Next button is now on the trailing edge, at left, for RTL language.](../../_assets/m7xmz6n4-38-971af6581c6b557aa0a4.png)

In RTL languages, reverse the order so **Next** remains on the trailing edge when flipped, now on the left. Text is not translated to illustrate mirroring.

## Behavior

### Scrolling

Docked toolbars can either remain on the screen during scroll, or animate offscreen.

Docked toolbars can animate offscreen

Floating toolbars can remain on the screen, animate offscreen, or collapse into a single, high-emphasis action on scroll.

Floating toolbars can animate off screen

On Jetpack Compose, the floating toolbar can collapse to a FAB or key action on scroll. 

Floating toolbars can be customized to do other actions on scroll, like collapse into a single action

Don't collapse actions and scroll at the same time.

close Don’t

Toolbars shouldn't both collapse and transition off page
