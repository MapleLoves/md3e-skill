---
source: https://m3.material.io/components/navigation-bar/guidelines
title: "Navigation bar"
captured: 2026-09-14
---

# Navigation bar

> Navigation bars let people switch between UI views on smaller devices

![A nav bar with vertical items in a compact window, and horizontal items in a medium window.](../../_assets/malqgvk7-01-b3d9706bcad68ab2edb3.png)

Navigation bars adapt to different breakpoints

## Usage

Navigation bars provide access to three to five destinations. The nav bar is positioned at the bottom of windows for convenient access.

Each destination is represented by an icon and label text. One navigation destination is always active.

When a navigation bar icon is tapped or focused, people are taken to the navigation destination associated with that icon.

![A nav bar for a music app with 4 destinations: Home, Browse, Radio, Library, It’s in a compact window.](../../_assets/malnqdza-02-fa67ad8d2330398540bd.png)

Navigation bars can have three to five destinations

Navigation bars should be used for:

-   Three to five main pages in the product
-   Mobile or tablet only

Navigation bars shouldn’t be used for accessing single tasks, such as viewing one email.

![A nav bar for a music app with 4 destinations: Home, Browse, Radio, Library. It’s in a medium window.](../../_assets/malqhln7-03-78a688bb07888042c3fc.png)

On mobile or tablet, navigation bars should be used for top-level destinations

The navigation items can be **vertical** or **horizontal**.

-   Use vertical items in compact windows Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact breakpoints](/m3/pages/breakpoints/compact) , like mobile

-   Use horizontal items in medium windows Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium breakpoints](/m3/pages/breakpoints/medium) , like tablets

![A nav bar with vertical items in a compact window, and horizontal items in a medium window.](../../_assets/malqhs7x-04-6bd42b1b3a1cd77a1f6f.png)

Vertical navigation items work best in compact windows. Horizontal items work best in medium windows.

For products with more than five navigation items, don’t use a navigation bar; the elements may collide and there likely won’t be enough space for translated text.

Instead, consider using tabs Tabs organize content across different screens and views. [More on tabs](/m3/pages/tabs/overview) to organize similar content within a page, or hide the navigation behind a menu icon using a modal expanded navigation rail Navigation rails let people switch between UI views on mid-sized devices. [More on navigation rails](/m3/pages/navigation-rail/overview) .

![A nav bar with 7 items in a compact window.](../../_assets/malqi614-05-don-t-613b65676e97ada408fc.png)

close Don’t

Avoid putting more than five navigation items in a navigation bar

![A nav bar with no labels for each page item.](../../_assets/malqimzs-06-dont-23fe5901e34e3185bc92.png)

close Don’t

Don’t remove the labels from navigation items

![A nav bar with 2 page items.](../../_assets/malqir51-07-dont-5d39bcce70d50d91d97f.png)

close Don’t

Don’t use a navigation bar for fewer than three destinations. Instead, use tabs.

![A nav bar is on the Library page of a music app. Tabs at the top of the page have secondary navigation for playlists, artists, albums, and songs.](../../_assets/m0fp4omq-08-29f3d9d7d20b811afab6.png)

Use navigation for distinct pages and tabs for related content within a page

![Nav bar using horizontal items in a compact window. The items are too wide and flow off screen.](../../_assets/m0fp4ti0-09-658e92a57d0fb3d8be7a.png)

close Don’t

Navigation bar destinations have fixed positions. Don’t scroll them or modify their positions.

## Anatomy

![6 elements of the nav bar.](../../_assets/m3t918of-10-704c5e4362ecb47060e9.png)

1.  Container

2.  Icon

3.  Label text

4.  Active indicator

5.  Large badge (optional)

6.  Small badge (optional)

### Container

The container should always be placed at the bottom of the product and span the full length of the window. Navigation items are centered within the container.

The container has a color fill to provide separation from other content.

![The nav bar at the bottom of a medium window has a color fill to differentiate from the background.](../../_assets/m3t91cku-11-d741c9eff8c4fb0014cb.png)

The navigation bar container holds all elements

### Navigation items

Navigation items hold all elements for each destination: the icon, label text, and active indicator. They can be **vertical**, with the text below the icon and indicator, or **horizontal**, with the icon and text beside each other inside the indicator. 

Vertical items are best in compact windows Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact breakpoints](/m3/pages/breakpoints/compact) , and horizontal items are best in medium windows Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation [More on medium breakpoints](/m3/pages/breakpoints/medium) .

Horizontal items are centered in the nav bar with outer margins.

![The nav bar in a medium window with padding on each side.](../../_assets/m3t91mur-12-cc32c3efce132055b3f4.png)

The navigation bar is divided into equal-width segments with padding from the window edge

### Icons

Navigation rail items must use icons that symbolize the content of their page. Browse [popular icon](https://fonts.google.com/icons).

Use a filled icon for the active destination and outlined icons for inactive destinations. If an icon doesn’t have a filled version, apply **semibold** weight to the icon instead.

![An active nav item with a filled icon compared to inactive items with outlined icons.](../../_assets/m0fp9y48-13-1cfce4e5df2f4c71a807.png)

check Do

Use filled icons when the navigation item is active

![An active nav item with a semibold icon compared to inactive items with outlined icons.](../../_assets/m0fpa2te-14-6065e83bb4ac90845478.png)

exclamation Caution

If a filled version of an icon is unavailable, the icon’s weight must increase

Active and inactive icons must have a minimum 3:1 contrast ratio with the container.

![4 nav items that are each different colors with low contrast with the background.](../../_assets/malqnpkt-15-dont-cdae06ee62c6fc35739d.png)

close Don’t

Don’t use multiple or low-contrast colors in a navigation bar, as they make it harder for people to distinguish the active item and navigate to other destinations

### Active indicator

The active indicator shows which page from the nav bar is currently being displayed.

![The current page in a nav bar has an active indicator.](../../_assets/malqo0n5-16-do-85828e5d3d42c46d3a97.png)

check Do

Use the active indicator only for the active destination

![All items in a nav bar have active indicators.](../../_assets/malqo7ag-17-dont-5fda570a23749c2ec53a.png)

close Don’t

Don’t use the active indicator for more than one destination at a time

### Label text

The label text should be a short, meaningful description of each navigation destination and another way for people to understand an icon’s meaning.

All navigation items require a label text. It should be 1-2 words.

![A nav bar on a music app with clearly labelled destinations: home, browse, radio, library.](../../_assets/m0fpamvs-18-fb0113753fc295aa69e0.png)

Label text must be brief and clear

![A nav bar with 1-word labels for each page.](../../_assets/malqoweq-19-do-f6d5a48cd3a4aa5c2f30.png)

check Do

Use brief text labels to identify the purpose of a destination

![A nav bar with “Music catalog” for a label. The label is truncated.](../../_assets/malqp27c-20-dont-44ea47a7161aa5675f23.png)

close Don’t

Don’t wrap or truncate text as it can make the label hard to understand

![A nav bar with “Music catalog” for a label. The label is a smaller size to make the text fit.](../../_assets/malqpu1t-21-dont-86c08c1ef7153a42ce14.png)

close Don’t

Don’t shrink longer text to fit on a single line

### Badges (optional)

Navigation bars can display badges in the upper right corners of the destination icon.

Badges can contain dynamic information, such as the number of new messages.

![A nav bar with a destination called “Go” with a small badge and one called “Saved” with a large badge saying “3.”](../../_assets/malqqg5m-22-08a113553ed0a39a178f.png)

Use a small badge to indicate an update, and a large badge to show the amount of updates

![Horizontal nav items with the badges in the same place of the icon as vertical nav items.](../../_assets/malqqlk1-23-a0075020735db028da61.png)

Badges overlap the icon in both vertical and horizontal navigation items

## Placement

The floating action button (FAB) is placed above the navigation bar. Nav bars are always placed at the bottom of the window.

![The FAB should be right-aligned above the navigation bar](../../_assets/malqqsyh-24-do-5effd0f2569444a19982.png)

check Do

The FAB should be right-aligned above the navigation bar

![A mobile page with a FAB overlapping a nav bar.](../../_assets/malqqy0m-25-dont-9fe79d025fa0814937f4.png)

close Don’t

Don’t cover the navigation bar with a FAB

Navigation bars can be temporarily covered by dialogs, bottom sheets, navigation drawers, the on-screen keyboard, or other elements needed to complete a flow. They should not be permanently obstructed on any screen.

The search feature of the screen triggers the on-screen keyboard, temporarily covering the bottom navigation bar until the search flow is completed

## Adaptive design

Adaptive design allows an interface to respond or change based on context, such as the user, device, and usage. More on [adaptive design](/m3/pages/layout-overview/adaptive-design)

### Resizing

Only use navigation bars for compact Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact breakpoints](/m3/pages/breakpoints/compact) and medium Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium breakpoints](/m3/pages/breakpoints/medium)  breakpoints. 

**Compact**: For narrow windows, use a navigation bar or modal navigation rail.

**Medium**: Use a navigation bar or navigation rail. Decide based on whether horizontal or vertical space is more important.

**Expanded and extra-large**: Use a navigation rail instead. Decide based on available window space and the number of navigation destinations.

Navigation bars are best suited for compact and medium breakpoints

The navigation bar container spans 100% of the window width.

![Navigation bar spanning the full width of a compact window.](../../_assets/malo8a44-28-06ebc4e3e3a9bd1cac49.png)

Navigation bars use 100% of the screen width

The navigation bar is used on smaller devices. It’s not intended for desktop.

![Navigation bar spanning the full width of an expanded window size.](../../_assets/malqsfoq-29-1012c05d0d6688cd6313.png)

close Don’t

Don’t use navigation bars for desktop layouts. Instead, use a navigation rail or tabs.

### Presentation

In medium breakpoints, use horizontal nav items to better use available space.

Horizontal nav items should remain centered with the same padding at each breakpoint.

![Horizontal nav items have the same width in medium and expanded windows. Only the padding changes.](../../_assets/m0fpt5k2-30-04c6f6665c77e8892494.png)

A navigation bar in horizontal orientation keeps the same spacing between destinations

## Behavior

### Navigation

When selecting a navigation bar item not currently selected, the product navigates to that destination’s screen using a [top level](/m3/pages/motion-transitions/transition-patterns#f852afd2-396f-49fd-a265-5f6d96680e16) transition pattern. It can either remember where you left off, or reset to the default view.

1.  **Preserve state**: If someone has interacted with this destination, it returns to their scroll position, current tab, and in-line search status.
2.  **Reset state**: Any prior user interactions are reset, including scroll position, tab selection, and in-line search.

Choose the behavior that best suits the product and user needs. For example, an app that requires frequent switching between sections should preserve each section’s state.

After selecting an item on the bottom navigation bar, the app navigates to that destination’s screen

Re-selecting the currently active destination should reset the scroll position to the top of the page.

**Don't swipe between destinations**
Swiping across the screen does not navigate between destinations, and is not supported by the navigation bar. Swipe behavior should be reserved for related items, such as cards in a carousel, or actions such as archiving a list item.

Selecting the already selected navigation item scrolls to the top of the screen

### Scrolling

Upon scroll, the navigation bar can appear or disappear. 

Don’t hide the navigation bar on scroll when a [screen reader](https://m3.material.io/foundations/overview/assistive-technology#ec6f3e84-a51c-4dc0-a353-6844f5bde698) is active.

Scrolling downward can hide the navigation bar; scrolling upward reveals it

### Selection

The icon becomes filled and the active indicator expands from the center of the icon when switching between destinations.

The active indicator animation should only apply on one axis to better represent a flat, shared plane.

An active indicator appears when the item is selected.

When a destination is tapped, the destination screens use a [top level](/m3/pages/motion-transitions/transition-patterns#f852afd2-396f-49fd-a265-5f6d96680e16) transition pattern. In addition, the icon becomes filled and the active indicator expands from the center of the icon.

Tapping a destination uses a top level transition pattern
