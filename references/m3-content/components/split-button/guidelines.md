---
source: https://m3.material.io/components/split-button/guidelines
title: "Split buttons"
captured: 2026-09-14
---

# Split buttons

> Split buttons open a menu to give people more options related to an action

![Split buttons of many colors and sizes scattered. ](../../_assets/m36akp9w-1-99689c6aaafe234398d4.png)

Split buttons come in many sizes and colors

## Usage

Split buttons are used to add a menu Menus display a list of choices on a temporary surface. [More on menus](/m3/pages/menus/overview) of actions alongside a main action. This reduces visual complexity by hiding extra options. Split buttons work well alone or alongside common buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) and icon buttons Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview) .

![A split button applied a filter of “Canada” to a list of activities. Three narrow buttons are next to it to share, favorite, and bookmark.](../../_assets/9UfkZE4_cZigzNlvBgN4B7ahe-tzvOBPxn_pzLUChLFUIKQitLU2y7pNJTXoW-K4aM2tVthNrk3BNxSY-c62bc120ba6f2126219f.png)

Split buttons on their own can grab attention

Split buttons have five recommended sizes. These sizes match the sizes offered on buttons and icon buttons:

-   Extra small

-   Small (default)

-   Medium

-   Large

-   Extra large

Scale up the split button in large breakpoints, or to create more emphasis in smaller windows.

![A large split button in a compact window draws attention to buying an enamel mug in an online store.](../../_assets/m0dosrjf-3-c0d849bdbe8b66f6b60d.png)

Using large split buttons on small screens can add extra emphasis for hero moments

Split buttons can be used alongside other buttons and button groups.

![A vibrant split button for starting a car drive is next to 2 muted icon buttons for bookmarking and sharing the trip.](../../_assets/maehs3k3-4_ALT-039cd9b61f45e9c692f4.png)

Split buttons work harmoniously with regular buttons

Split buttons can be of different sizes from other buttons on the page, especially since they take up more space.

![A media player has a split button for changing the speed quickly, or opening a menu of options.](../../_assets/maehumyk-5-alt-ebc6eb630c60e449e7f9.png)

The most prominent controls can be larger while secondary controls in a split button can be smaller

The split button typically opens a menu Menus display a list of choices on a temporary surface. [More on menus](/m3/pages/menus/overview) , but can be customized to open other components like cards Cards display content and actions about a single subject. [More on cards](/m3/pages/cards/overview) .

![A split button opens a menu with a vibrant color scheme.](../../_assets/m4il1tni-6-alt-36adc6f7ca729411079c.png)

check Do

Open a menu from a split button

![A split button opens a menu with an irregular shape highlighting the selected item.](../../_assets/m4il1xwy-7-alt-7c688dbe06af2434938f.png)

close Don’t

Avoid modifying the menu in unusual ways

## Anatomy

![4 elements of a split button.](../../_assets/m0dp22eb-8-b374d3d8f9924ac359f2.png)

1.  Leading button

2.  Icon

3.  Label text

4.  Trailing button

The leading button should be brief, just one or two words, with an icon that best matches the action.

The trailing button should always have the expand and collapse icon since it rotates when selected. Avoid modifying the icon.

![A split button for starting driving directions has a label “32 minutes away” and a refresh icon instead of a menu icon.](../../_assets/m0dxuxjz-9-41dafc5dbc70220c6262.png)

close Don’t

Avoid using very long labels or changing the trailing icon

In right-to-left languages, the component layout is mirrored.

![The split button elements are reversed in a right-to-left language.](../../_assets/43s7j0gcA5ez0PmFtHcj6TNeZLo7IqSGHqlOTKi2whopiRe66fXmJylV_V3M7SUNoFR4NtxZoeAqCATE-ae3a424a9c874bbc4a73.png)

Split buttons mirror the order of elements in right-to-left languages

## Behavior

The split button uses the standard motion scheme The motion physics system has two schemes: standard for utilitarian movement, and expressive for more bouncy movement. (not the expressive motion scheme) when rotating the menu button.

The menu button rotates inwards 180° when opened and closed.

Selecting the menu button rotates the icon inwards and applies shape morph

### Menu placement

When using the split button with a menu Menus display a list of choices on a temporary surface. [More on menus](/m3/pages/menus/overview) , align the menu with the trailing button when possible.

![A split button with an open menu. The leading edge of the menu is aligned to the leading edge of the menu button.](../../_assets/m4il8isz-12-8b0ce96a1a149f5ad17c.png)

Align the menu with the trailing button

If there’s not enough room, align the menu to one of the sides of the button.

![A split button with an open menu. The trailing edge of the menu is aligned to the trailing edge of the menu button.](../../_assets/m4ilatqh-13-568a1cce17b9d721a46f.png)

If not possible, align the menu to the side of the leading or trailing button

Depending on breakpoint, scroll position, and other factors, the menu may need to appear elsewhere around the button. Always try to align it with one of the edges of the button.

The menu should be 4dp from the split button.

![6 other ways the menu can align to the split button.](../../_assets/m4iz4b9v-14-ea54d7e3cfe7ac9aa46f.png)

1.  Top aligned to trailing button

2.  Bottom aligned to trailing button

3.  Top right-aligned

4.  Top left-aligned

5.  Bottom right-aligned 
6.  Bottom left-aligned
