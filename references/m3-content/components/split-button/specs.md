---
source: https://m3.material.io/components/split-button/specs
title: "Split buttons"
captured: 2026-09-14
---

# Split buttons

> Split buttons open a menu to give people more options related to an action

## Variants

![1 type of split button.](../../_assets/F2kUnhi2ZrsjiRH1K8Vru69-_x8fiFll-_4x9F4Nn-Y2X-KktX3SGtz5KBK4EkCQx5So3aXSeDexmjR--e2aefdf86ef5d54ef8a6.png)

| Variant | M3 | M3 Expressive |
| --- | --- | --- |
| Split button | \-- | Available |

## Configurations

![4 colors and 5 sizes of split buttons.](../../_assets/1yQajxz3WCQRMH3AdX8Tg7OPVxOT2Lcj8f3T7pDYmRcVZhFzkHR55JK8u7zD0did-AL95AJrs_xn2391-249d56f96945e14ff578.png)

1.  Color configurations: Elevated, filled, tonal, outlined

2.  Size configurations: XS, S, M, L, XL

| Category | Configuration | M3 | M3 Expressive |
| --- | --- | --- | --- |
| Size | XS, S, M, L, XL | \-- | Available |
| Color | Elevated, filled, tonal, outlined | \-- | Available |

## Tokens & specs

Use the table's menu to select a token set. Split button token sets are organized by size. [Learn about design tokens](/m3/pages/design-tokens/overview/)

Close

## Anatomy

![4 elements of a split button.](../../_assets/y1PQA-NhEihuhB7tNeqbtGZu6b_yL6_kxPmh2Hghbj4dahZfyaxnimD4KhbRfGdnXlsy0NKEyxaMuWbr-1e5b5db0307f9de4db14.png)

1.  Leading button

2.  Icon

3.  Label text

4.  Trailing button

The leading button in split buttons can have an icon, label text, or both. The trailing button should always have a menu icon.

![3 customizations of the leading button in the split button.](../../_assets/136pHVBxZ_A3wzi6-X1sKmbfnuqeUu_FIMeP4lGM3iVNjPqQH-SA62_w0wEZPalIigsfGp_6G4V08WZH-eb0cf7bd783e45a8007c.png)

1.  Label + icon

2.  Label

3.  Icon

## Color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For designers, this means working with color values that correspond with tokens; in implementation, a color value will be a token that references a value.

Split buttons use the same color schemes as standard buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) . However, unlike toggle buttons, the split button color doesn’t change when selected—only a state layer is applied.

Split buttons use the same colors and state layers as buttons, shown in the following token module. [Go to buttons](/m3/pages/common-buttons/overview) for more details.

![4 color roles of the split button when unselected and selected in light and dark theme.](../../_assets/ocKi_dfwn4Uv_N5ArrzqUKti6uAj79S5f8KVg0BvXDI_BLYgT1-VC55NzHO8NHePXEQ6ygQevbqAq8rZ-28e1c7ff0842e22fb9e6.png)

A: Unselected, B: Selected trailing icon

1.  Elevated

2.  Filled

3.  Tonal

4.  Outlined

Close

## States

States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or an interactive element. 

Split button states use the same colors and state layers as buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/specs) and icon buttons Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/specs) . Go to those specs for details. 

### Leading button shape

The inner corners change shape for hovered, focused, and pressed states.

![5 states of the leading button in the split button.](../../_assets/HXNWWohWOFX1IuFh8xMMnWtDczymOUA8I7CDja4WgwY3y_9LL-Ns0MjX2KsGanjBtco9oWxaL-tY3t7V-1562f7b9af8e0ee3fcc7.png)

1.  Enabled

2.  Disabled

3.  Hovered

4.  Focused

5.  Pressed, pressed with focus

### Trailing button shape

The inner corners change shape for hovered, focused, and pressed states, and the icon becomes centered when selected.

![6 states of the trailing menu button in the split button.](../../_assets/h_N1go5ViA5xTyg6nI2IBVOYKAqFx_-KIIRe4x3G3zHumq0gfQTZ3RUz1nUquSZJgSjeTLW5cRqDjcCA-3e98efd943696edeee02.png)

1.  Enabled

2.  Disabled

3.  Hovered

4.  Focused

5.  Pressed, pressed with focus

6.  Selected, selected with focus

## Measurements

Text and icons are optically centered when the buttons are asymmetrical. They’re centered normally when symmetrical.

![Padding and size measurements of the split button.](../../_assets/e6qwxAXA90nObGQBZ7-_IkTOn31Iw8LdEp8ua6AHcsG-8wRtfxpgADUbK2qbkwUwJkNad-EAPoVxOhil-1a8ff3a03bd3bbeb3d15.png)

Menu icon offset when unselected:

1.  XS: -1dp from center
2.  S: -1dp from center
3.  M: -2dp from center
4.  L: -3dp from center
5.  XL: -6dp from center

The inner corner radius changes depending on button sizing. The space should always be 2dp.

![Inner padding and inner corner measurements of the split button.](../../_assets/JOPyvu0AZccMCkuvHxbfK-M5B8_rVrEfV4GQ0Zgy0heMSDFJWtwU20dCLmW2HU4SM4JiEu-AfEg7BxqA-4f864b834f094e8afc31.png)

1.  Extra small 4dp

2.  Small 4dp

3.  Medium 4dp

4.  Large 8dp

5.  Extra large 12dp
