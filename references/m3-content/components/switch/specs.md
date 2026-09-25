---
source: https://m3.material.io/components/switch/specs
title: "Switch"
captured: 2026-09-14
---

# Switch

> Switches toggle the selection of an item on and off

![3 elements of a switch.](../../_assets/a4JkZitJC-KZ1qxKfHvM-B2tuC0JqMsA08tY-fRrBhlXDf6JpvjpQD9IAZ0_zg-R1E0tvzAst-VwpSYD-d7049208846e92013427.png)

1.  Track 
2.  Handle (formerly "thumb")
3.  Icon

## Tokens & specs

Browse the component elements, attributes, tokens, and their values. [Learn more about design tokens](/m3/pages/design-tokens/overview)

Token

Value

Close

## Color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview/)

![6 color roles of a switch in light and dark themes.](../../_assets/0fyIBhV6SPL8tV1Vk7CtpveaYQ1-am9tJ41EVA-QaywC5FoZ6CmY7Cevkh6gG8HklU2Ojaj4r0d4Po-J-ced3e93b0cd8c775c70a.png)

Switch color roles used for light and dark themes:

1.  Surface container highest
2.  Outline
3.  Outline
4.  Primary
5.  On primary
6.  On primary container

### Adjacent text label color

Use the color role Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme. [More on color roles](/m3/pages/color-roles) **on surface** for adjacent text labels. This remains the same even if interacting with the label or component.

![The large body text adjacent to switches uses "on surface" color and the body text uses "on surface variant."](../../_assets/0Xmcv7IiazLYf6Bpg_WWIU0Cnp32mkTymcUwcgN2QxXbvz2KyCIvTMXDW4sOR-m-jzDd4IO3aHqdSxaX-d364c8ef507b9dd9898a.png)![The large body text adjacent to switches uses "on surface" color and the body text uses "on surface variant."](../../_assets/0Xmcv7IiazLYf6Bpg_WWIU0Cnp32mkTymcUwcgN2QxXbvz2KyCIvTMXDW4sOR-m-jzDd4IO3aHqdSxaX-994457985023ef0998e8.png)

The text label uses **on surface**. Supporting text may use **on surface variant**.

## States

States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or interactive element. [Learn more about interaction states](/m3/pages/interaction-states)

![5 states of a switch shown in light and dark themes.](../../_assets/PnpKeMQPpfXYol0STNFLWY--Fet6iOSy9Skw-SxaiktaHsBbPbHkXNl2RX7aLYHsrUbIN8LwPshZzNEQ-07829cd0b85f293b9e2f.png)

1.  Enabled 

2.  Hovered 

3.  Focused 

4.  Pressed 

5.  Disabled

[State specs are in the token module above](/m3/pages/switch/specs#3708644e-b4d7-4237-bb0a-7afeeae4a9b0)

## Measurements

![Measurements of switches without icons.](../../_assets/QjZaSle3gkHOtKy1j-YDhEIIdbjF3_Uy3kVXdJnmx7F4Gt-Af66rcmJpNFIKXrGIUg2NSEb9U4UAJ8kx-79aa04a4957c9494758c.png)

Switches without icons

![Measurements of pressed switches without icons.](../../_assets/vFaJZa1Ic9jL9_q6ayhWZw_21xhx2LeDKKJpLRhHisCUpo7tFW-cIHTOdD0mj75_m3ov2BhZQavFK8Sq-0c5a9ce0f6188188b163.png)

Pressed switches without icons

![Measurements of switches with icons.](../../_assets/pOvYPjVd1P1HEOyZPLp4jziQmmbT5uMefs4zGCMSHg-fiRFgzXIeAz75RDSyfyZSu3yObf70vL6iiPgR-6ac08bc2759c4f1f1287.png)

Switches with icons

![Measurements of pressed switches with icons.](../../_assets/wZm_0fDk5iJbWdd6SZL2P6FkEw8Q94mZ9g0laAAb99hOsR4dk08iyhObA6p4OuqUuf8azFV_9Th006NH-674573405b1f23ce46c8.png)

Pressed switches with icons

| Element | Attribute | Value |
| --- | --- | --- |
| Track | Height | 32dp |
| Width | 52dp |
| Outline width | 2dp |
| Shape | [md.sys.shape.corner.full](/m3/pages/shape/corner-radius-scale#56e2bfb5-4bec-49bd-b3a3-bd822c8ab88e) |
| Handle | Height (unselected) | 16dp |
| Height - with icon | 24dp |
| Height (selected) | 24dp |
| Height (pressed) | 28dp |
| Width (unselected) | 16dp |
| Width - with icon | 24dp |
| Width (selected) | 24dp |
| Width (pressed) | 28dp |
| Shape | [md.sys.shape.corner.full](/m3/pages/shape/corner-radius-scale#56e2bfb5-4bec-49bd-b3a3-bd822c8ab88e) |
| State layer | Size | 40dp |
| Shape | [md.sys.shape.corner.full](/m3/pages/shape/corner-radius-scale#56e2bfb5-4bec-49bd-b3a3-bd822c8ab88e) |
| Target | Size | 48dp |
| Icon | Size (selected) | 16dp |
| Icon | Size (unselected) | 16dp |

## Configurations

1.  Without icons
2.  Icon on selected switch
3.  Icon on selected and unselected switch

![3 example switches with and without icons in on and off states. ](../../_assets/yZbAEZRgNI6uOkunAfaXCx8NAExJ8RsY6DkIjWJMH0DanJdyakTEzO8YFyw1bd3AZdvfJv229_maPQKB-e3241e011f6497da5802.png)
