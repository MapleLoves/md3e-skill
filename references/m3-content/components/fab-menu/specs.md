---
source: https://m3.material.io/components/fab-menu/specs
title: "FAB menu"
captured: 2026-09-14
---

# FAB menu

> The floating action button (FAB) menu opens from a FAB to display multiple related actions

## Variants

![The FAB menu in its single variant.](../../_assets/aEJrDU0HXKoBxMGFWOq1I7O6QB2fl6EPJGEDSP0L7CVDgvAjMdaM_LX10txGb1GDquvp0R-IiszOHSY2-756460606ad2a3e6e99b.png)

There’s one variant of FAB menu

| Variant | M3 | M3 Expressive |
| --- | --- | --- |
| FAB menu | \-- | Available |

## Configurations

![3 color configurations of FAB menus.](../../_assets/ysJ9Ea896_EYwed_YofScZMv_HuE8BH4IJVkWyw4v2Xw-KInaEtXmOyWaaQNTTAZw0oLB9neXbgOnHTv-4688da3e483418ec9d31.png)![3 color configurations of FAB menus.](../../_assets/ysJ9Ea896_EYwed_YofScZMv_HuE8BH4IJVkWyw4v2Xw-KInaEtXmOyWaaQNTTAZw0oLB9neXbgOnHTv-e354984afcb532b87539.png)

Three color sets:

1.  Primary

2.  Secondary

3.  Tertiary

| Category | Configuration | M3 | M3 Expressive |
| --- | --- | --- | --- |
| Color | Primary set, secondary set, tertiary set | \-- | Available |

## Tokens & specs

Use the table's menu to switch token sets. The FAB menu has a common token set and six color sets, three for each element (close button and menu item). [Learn about design tokens](/m3/pages/design-tokens/overview/)

Token

Value

Close

## Anatomy

![2 elements of a FAB menu.](../../_assets/CsC2u7L3QL6svcrFzmZM2foCzJxzUjF93lwZuZ-oJW7RK-lKsp4Ei0iNdLiNhbFST2y9U34PClKaRDJV-0eaca74863524a928a92.png)![2 elements of a FAB menu.](../../_assets/CsC2u7L3QL6svcrFzmZM2foCzJxzUjF93lwZuZ-oJW7RK-lKsp4Ei0iNdLiNhbFST2y9U34PClKaRDJV-63473909aecbf6923ff1.png)

1.  Close button
2.  Menu item

![5 FAB menus showing the range of 2–6 items.](../../_assets/KIWWfbv6JG0LIK8rzUSHcalH5BrNbW8_o8_U3uLqVkUDcdZNw4VS_nwoQ33DaomQXt95s6R_EY49aEQs-c0e21275ac0d15fae5bf.png)![5 FAB menus showing the range of 2–6 items.](../../_assets/KIWWfbv6JG0LIK8rzUSHcalH5BrNbW8_o8_U3uLqVkUDcdZNw4VS_nwoQ33DaomQXt95s6R_EY49aEQs-bfbeebf16d324a3780dc.png)

The FAB menu can have up to six items

## Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)

![12 colors of the FAB menu.](../../_assets/tZxH6WCjbJBIqPlpd4_nt_npacUlh9WWyrIqJWs6Z1BCdGKbGFPt_BaW0CrG9HHNVQzBFYxxGU4hYm8L-92554ecf4cc4f89da88b.png)

1.  On primary container
2.  Primary container
3.  On primary
4.  Primary
5.  On secondary container
6.  Secondary container
7.  On secondary
8.  Secondary
9.  On tertiary container
10.  Tertiary container
11.  On tertiary
12.  Tertiary

## States

States are visual representations used to communicate the status of a component or interactive element. [Learn more about interaction states](/m3/pages/interaction-states)

### Close button

![4 states of the FAB menu close button.](../../_assets/IBxWcDPavbWf55MsedxQZnCouJM3OZfbOudsfZQNrILcXhsyU_EI9iIEZ1UeKo-BwB7btsT0_0ZApQFH-da71acc2b8eb49e9ebdd.png)

Close button states in light and dark themes: 

1.  Enabled

2.  Hovered

3.  Focused

4.  Pressed

### Menu item

![4 states of the FAB menu items.](../../_assets/GHST3WLAtYjpsKWjXfoTtSy1pybwjIFPYgrw1GBjynLRHHSxmZWT-t8VhnSMGbOvYWG0O65po5ceeOVr-d39fd9ffe98e9af546fc.png)

Menu item states in light and dark themes:

1.  Enabled

2.  Hovered

3.  Focused

4.  Pressed

## Measurements

FAB menu items share the same measurements as the medium button Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) specs. 

The close button should always be 56dp.

![FAB menu size measurements.](../../_assets/6K5OibGh_d83LTRduhambKrHPD8JMVCHm19eHlen8e58fVWnoLyh8wWGZyLrdCPSO8Q3m01icndNcp7u-6a787591832dbc440157.png)

FAB menu size measurements

The FAB menu animates from the top trailing edge of the FAB to ensure a smooth animation.

![FAB on a mobile screen with 16dp margins annotated.](../../_assets/WhBYTHZseZ9EfjdiU3CqPLeEC36wFENc3fV_9h5eR9T5ze6ooQya6w3-f1JWj7bBOkJnQHFL3LpbcmG_-f42981804085b835f02b.png)

The FAB should always have 16dp margins

![FAB menu opened from a FAB has matching margins of 16dp.](../../_assets/HWYLNxfsd_aBEZRMazrMRxUthRgVqeA8_evmV1IZrkKg878uq7DK0dg5EZaR8q7n-QP_kLrEaYALuBpm-49f4e655d37df0b8a0a5.png)

The close button and FAB share the top trailing corner as an anchor and appear in the same place

Larger FABs will place the FAB menu slightly higher, with larger margins underneath.

![Medium FAB on a mobile screen with 16dp margins annotated.](../../_assets/gce3Kgv0OcZSOCiWq672oYOzAE9YJhGCC0oGLAcdxJ59BPnVhlV3HdjJPyrHiJy1LgUNnQkTKyOc9d6e-6b1c8c3db4e2962b95d4.png)

The medium FAB placement has 16dp margins

![FAB menu opened from the medium FAB has a 40dp margin from bottom of screen.](../../_assets/kfovl3xRwL77xd7_XYJlFsLMybMdv16Nd0U9T5f87iZTyW3lo8gU72nkr81ZLumjSbxXIYnkvJX7ea84-f090f7a359ed9627abf2.png)

The close button is placed higher to align with the top of the medium FAB

![Large FAB on a mobile screen with 16dp margins annotated.](../../_assets/9hh4PDq9vnfiJ2AAOX8VKeIFe9De47Av_acmKjjFbTkWQOGjZTLOqGY5cWqLsxkDLWjG4bgquVe81njJ-cfdb91db08cfd0bbc61b.png)

The large FAB placement has 16dp margins

![FAB menu opened from the large FAB has a 56dp margin from bottom of screen.](../../_assets/zGkr1v4xtHihId5hAGO-4ESfqwzsweXE2xqXba2w8m0zl9Hswn3RWimV53apAvslPo7y0G2yrUchBqCB-89dd399b89d913781ed9.png)

The close button is placed higher to align with the top of the large FAB

On web, the FAB menu opens from the FAB, and inherits its states and specs from the baseline  menu Menus display a list of choices on a temporary surface. [More on menus](/m3/pages/menus/overview/) component. 

The gap between the FAB and menu can vary, but 4dp is recommended.

![FAB menu on web states and specifications.](../../_assets/EvVSXxIPCIQmi5H_Tf238AlVWE4QCT1NNKDXE9IYMtRbF3FF7S-t0Y_sxaQ1dCGsRSQGM6EkWT2LI5yH-e5fa98bb402e6235e734.png)

Spacing and interaction on FAB menu for web:

1.  Enabled

2.  Hovered

3.  Selected
