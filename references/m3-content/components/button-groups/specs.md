---
source: https://m3.material.io/components/button-groups/specs
title: "Button groups"
captured: 2026-09-14
---

# Button groups

> Button groups organize buttons and add interactions between them

## Variants

![Various colors and shapes of standard and connected button groups.](../../_assets/Zlys4Fta71zY-GAiCcT-oqug62NMk2muBeMcrPxVq_ZyoZhWxZrY5QlyYMHMI8wb6GSstakH8BmszYQQ-713ac91f3b424287c566.png)![Various colors and shapes of standard and connected button groups.](../../_assets/Zlys4Fta71zY-GAiCcT-oqug62NMk2muBeMcrPxVq_ZyoZhWxZrY5QlyYMHMI8wb6GSstakH8BmszYQQ-bea260410ffd53df3ca4.png)

1.  Standard button group
2.  Connected button group

| Variant | M3   | M3 Expressive |
| --- | --- | --- |
| Standard button group | \-- | Available |
| Connected button group | Available as segmented button Segmented buttons help people select options, switch views, or sort elements. Note: They're deprecated in the expressive update. Use a nav rail instead. [More on segmented buttons](/m3/pages/segmented-buttons/overview) | Available |

## Configurations

![Five sizes of button groups and two shapes of button groups.](../../_assets/tXvGi5QNHXaEdYS0QIwTTJHGUdhlUv1s8dzEvt3yvdhs0CCvXGe3Y3bBOTJvHKv2VA3DPdHEWmLb9UAY-3821a8be0bd1242f0f73.png)![Five sizes of button groups and two shapes of button groups.](../../_assets/tXvGi5QNHXaEdYS0QIwTTJHGUdhlUv1s8dzEvt3yvdhs0CCvXGe3Y3bBOTJvHKv2VA3DPdHEWmLb9UAY-fb7feff995b8e35d7125.png)

Configurations for both variants of button groups:

1.  Extra small

2.  Small

3.  Medium

4.  Large

5.  Extra large

6.  Single-select and multi-select

7.  Round and square

| Category | Configuration | M3 | M3 Expressive |
| --- | --- | --- | --- |
| Size | XS, S, M, L, XL | \-- | Available |
| Default shape | Round, square | \-- | Available |
| Selection | Single-select, multi-select, selection-required | Available as  segmented button Segmented buttons help people select options, switch views, or sort elements. Note: They're deprecated in the expressive update. Use a nav rail instead. [More on segmented buttons](/m3/pages/segmented-buttons/overview) | Available |

## Tokens & specs

Standard and connected button group tokens are organized by size. Select the variant and size from the token set menu. Go to the [button](/m3/pages/common-buttons/specs/) and [icon button](/m3/pages/icon-buttons/specs/) pages to view their tokens. [Learn about design tokens](/m3/pages/design-tokens/overview/)

Close

## Anatomy

Button groups are invisible containers that add padding between buttons and modify button shape. They don’t contain any buttons by default.

![The container outlined on both variants of button groups.](../../_assets/909fUN1vEim33Fg-tzKVqEEl_EQRq_GsNWP9dPCSA181-jk63D2BmlLmh8pisBn2zBlyE581QGQUAggr-8254e9bf215741bda57d.png)![The container outlined on both variants of button groups.](../../_assets/909fUN1vEim33Fg-tzKVqEEl_EQRq_GsNWP9dPCSA181-jk63D2BmlLmh8pisBn2zBlyE581QGQUAggr-e41cffbd3284f5e36da6.png)

1.  Container

### Common layouts

Mix and match buttons and icon buttons for different scenarios.

![4 common layouts of button groups.](../../_assets/mB9JxUhRXlbUJhjAnZciD7yqHtJQpwyqJME-B-dTSOz6AQVQbdOHskFsAM7E60jDTOOPx9qjA7YiJt_4-74e47f193cacb61153bb.png)![4 common layouts of button groups.](../../_assets/mB9JxUhRXlbUJhjAnZciD7yqHtJQpwyqJME-B-dTSOz6AQVQbdOHskFsAM7E60jDTOOPx9qjA7YiJt_4-8181fe6c23e109778dd5.png)

1.  Label buttons
2.  Label buttons and icon buttons
3.  Extra small icon buttons
4.  Large icon buttons

### Color

Button groups have no color properties. They can use the default button or toggle button color styles, like filled, tonal, and outlined. Avoid using standard icon buttons or text buttons, as they have no container treatment.

![The container outlined on both variants of button groups.](../../_assets/9hbmv_ziBEblvbLNhjPIK994tZijzcHgGhHBn_z-e52FBeulOHrdGeVlk4y0G8YWkUVABgf5EvmfpWPJ-288d285eeacbf617448f.png)![The container outlined on both variants of button groups.](../../_assets/9hbmv_ziBEblvbLNhjPIK994tZijzcHgGhHBn_z-e52FBeulOHrdGeVlk4y0G8YWkUVABgf5EvmfpWPJ-2ab2c876dae6919862be.png)

1.  Filled

2.  Tonal

3.  Outlined

4.  Elevated

## Selection & activation

**Standard button groups** add interaction between adjacent buttons when a button is selected or activated.

This interaction changes the width, shape, and padding of the selected or activated button, which adjusts the width of buttons directly next to it.

A selected button changes shape, and briefly changes the width of itself and adjacent buttons

**Connected button groups** don’t add any interaction between buttons when selected or activated. 

They only affect the shape of the button being selected or activated.

A selected button changes shape without affecting adjacent buttons

## States

### Standard button group

When a button is pressed, standard button groups modify the width and shape of that button and adjacent buttons.

![5 states of a standard button group.](../../_assets/gQSD-N83stSwtNWu4Vgei7se_1vFmSqc8L7QyZ_u66ja9ZsX_71o7I8800O7qg8TBICKzr6L2vBtv09c-557f001c2dce4d6a4d2e.png)

1.  Enabled
2.  Disabled
3.  Hovered
4.  Focused
5.  Pressed

When a toggle button is selected in a standard button group, its shape should change between square and round. The color should change according to the [button specs](/m3/pages/common-buttons/specs).

![5 states of a standard button group with toggle buttons.](../../_assets/81FApYiTXho8D7eyhKVzVF5qhIRk02bF6rEp6QoLXRtnuW94g2EoBt1EQLLK7h2vRiKsRbNHUyYa3OCv-2aadec00dd796c707ccf.png)

1.  Enabled
2.  Disabled
3.  Hovered
4.  Focused
5.  Pressed

### Connected button group

Connected button groups have different shape changes than standard button groups. Selecting a button does not affect adjacent buttons.

![5 states of a segmented button group.](../../_assets/zh7Dh6_ChlGUt5mWmhDpY_dTPHFXlFOmdfy2AJEpn013_utxmX5it3VZuG3iyveqk3N3Pj07dV4a2XtW-fe54e308658d5c68178a.png)

Connected button group unselected states:

1.  Enabled
2.  Disabled
3.  Hovered
4.  Focused
5.  Pressed

![4 states of a segmented button group with toggle buttons.](../../_assets/N09iT9pfuy2j_ZfeAqJIUzPo31zdiKwWd0P-BH5eVSj3QR3JWxULGnjVnTbavy0VNZX5lhBc9Dyw1NTB-dfa42883d571171100f4.png)

Connected button group selected states:

1.  Enabled
2.  Hovered
3.  Focused
4.  Pressed

## Measurements

### Standard button group

Standard groups apply padding between all buttons. The amount of padding changes based on button size to ensure a minimum accessible target size of 48dp. More details on padding: [Button specs](/m3/pages/common-buttons/specs), [icon button specs](/m3/pages/icon-buttons/specs)

![Standard button group padding measurements.](../../_assets/RGY_WzbLD07B3K6DGITtC-0NcW5LQI1HS1L-g0O4Lt0wttv2BWMZQWR2LqpG39dzWUHBNqCx12noXUfN-eb8188fc0a71ea45c200.png)

Standard button group inner padding:

1.  XS: 18dp
2.  S: 12dp
3.  M: 8dp
4.  L: 8dp
5.  XL: 8dp

### Connected button group

For all connected button groups, use 2dp padding. This provides visual consistency at scale. 

![Connected button group padding and corner radius measurements.](../../_assets/tyj4mLRYzA86JWOUFPOV0mFMQxD7ckw1kX2zjPh0iOs4KV_jy6SCEtBmeQASzBTE9ULLNl0NY_jT32BX-a56b98db956d29dadf19.png)

Round connected button group inner padding is 2dp at every size. The outer shape is fully round, and the inner shape remains square with the following corner sizes:

1.  XS: 4dp
2.  S: 8dp
3.  M: 8dp
4.  L: 16dp
5.  XL: 20dp

![Connected button group padding and corner radius measurements for square buttons.](../../_assets/DiysV2VqS8bJV3jH34XtaPeeGGi2Svo6ZIFJhmjAeYH0zOw7-6P-5qgZeRy2A6CoXA2mgQ0WMXanpp3k-01bde558b93f4f8c7647.png)

Square connected button group inner padding is 2dp at every size. The outer shape has the following corner sizes:

1.  XS: 4dp
2.  S: 8dp
3.  M: 8dp
4.  L: 16dp
5.  XL: 20dp

### Minimum widths

Extra small and small connected button groups have 48dp target areas and a minimum width of 48dp.

![48x48dp accessible target areas on the XS and S connected button groups.](../../_assets/3YpaF7-0WXRLTv6vxHgKCSJBsLTOFIaTw5JZ5795oi7393Y_y8hlC-gNbJh57zwFbM8SJ6VsaQMH9dVZ-bf54c28758abb19c586b.png)

1.  Extra small
2.  Small

## Density

Button groups adapt to density of the buttons inside. [More on density](/m3/pages/grids-spacing/density)

![Connected button groups at 0, -1, -2, and -3 density.](../../_assets/yW6GJfPC6vob2O0uaXXiMDGwKXMv7majvHsxv9MEQGBjXCtZg0YERe27DGduNwB1ofpRLw4evKy_CZWs-86daea149ece780bfa5e.png)

Button groups adapt to the height of the buttons inside, including when density is applied
