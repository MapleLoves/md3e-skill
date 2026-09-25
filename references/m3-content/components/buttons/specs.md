---
source: https://m3.material.io/components/buttons/specs
title: "Buttons"
captured: 2026-09-14
---

# Buttons

> Buttons prompt most actions in a UI.

## Variants

![Diagram comparing buttons with toggle buttons.](../../_assets/aWhLmNGkz1dTgFMtkYbi73APlAcBdOgT9xviQJI1Riu10oLOdnakrGGJv6HBp6_9LHBw9lPT-lqF_xNp-fd0b221f03b7d0bf35aa.png)

1.  Default button

2.  Toggle button

| Variant | M3 | M3 Expressive |
| --- | --- | --- |
| Default | Available | Available |
| Toggle (selection) | \-- | Available |

## Configurations

![Diagram showing configurations of buttons.](../../_assets/qtqOoy4NuC3QFb7pfhfLLiZPXFCDrM-rLo38WY2V4ao1NGmIml-wNHF0Gk4ydIEttrZsWWGMlACpZAu5-242a96a008aec002cc6e.png)![Diagram showing configurations of buttons.](../../_assets/qtqOoy4NuC3QFb7pfhfLLiZPXFCDrM-rLo38WY2V4ao1NGmIml-wNHF0Gk4ydIEttrZsWWGMlACpZAu5-66035cfbea364ed4ca31.png)

1.  Size

2.  Shape

3.  Color

4.  Small button padding

| Category | Configuration | M3 | M3 Expressive |
| --- | --- | --- | --- |
| Size | Small (default) | Available | Available |
| XS, M, L, XL | \-- | Available |
| Shape | Round (default) | Available | Available |
| Square | \-- | Available |
| Color | Elevated, filled (default), tonal, outlined, text | Available | Available |
| Small button padding | 24dp | Available | Not recommended.Use 16dp |
| 16dp | \-- | Available |

## Tokens & specs

Use the table's menu to select a token set. Button token sets are separated into common tokens, color, and size. [View baseline tokens](/m3/pages/common-buttons/specs#c305d304-a6c0-466a-a48c-8d0718a29ae2)

Token

Value

Close

## Anatomy

![Diagram labeling 3 parts of a button.](../../_assets/Vd3wDLwuuQXUGiUdmogIFMY3V4WzpDIz9WvepaTJAmdJhaiKXTxshhrlEwJizdXlvsISt1vMjtSw5AdE-e882873840c3f7090b98.png)![Diagram labeling 3 parts of a button.](../../_assets/Vd3wDLwuuQXUGiUdmogIFMY3V4WzpDIz9WvepaTJAmdJhaiKXTxshhrlEwJizdXlvsISt1vMjtSw5AdE-346501dc5351add9a24a.png)

1.  Container

2.  Label text

3.  Icon (optional)

## Color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value.

-   There are five built-in button color styles: elevated, filled, tonal, outlined, and text

-   The default and toggle buttons use different colors

-   Toggle buttons don’t use the text style

star

Note:

These color roles were chosen to create design coherence and familiarity. Other color roles can be used as long as the container and text have a 3:1 contrast ratio. For example, tertiary and on tertiary.

![Diagram shows dark and light color schemes for buttons.](../../_assets/rniAgyk0C8Ys1AH7Lxciu7xnv8p_HA8iVm0AmoTKx5Ntedg_FdE0W66BG1udiPwCbGek3f0g8R2vliru-1df12fb64f6d3bc53969.png)

A. Elevated, B. Filled, C. Tonal, D. Outlined, E. Text

1.  Default

2.  Toggle: unselected

3.  Toggle: selected

|  | 1\. Default | 2\. Toggle unselected | 3\. Toggle selected |
| --- | --- | --- | --- |
| Elevated containerElevated icon & label | Surface container lowPrimary | Surface container lowPrimary | PrimaryOn primary |
| Filled containerFilled icon & label | Primary On primary | Surface containerOn surface variant | PrimaryOn primary |
| Tonal containerTonal icon & label | Secondary containerOn secondary container | Secondary containerOn secondary container | SecondaryOn secondary |
| Outlined containerOutlined icon & label | Outline variant (outline)On surface variant | Outline variant (outline)On surface variant | Inverse surfaceInverse on surface |
| Text icon & label | Primary | \-- | \-- |

## States

States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or interactive element.

### Elevated button states

The elevated button style has an elevation of 1 by default and 0 when disabled.

#### Default

![Elevated button states.](../../_assets/n_5apeWPNXiSqDwG3UYvNY5A-FyHJOvbkdqH0Mq47KIxzVbHAq76C6DM1jG_TYTWiHgMPMjgdWA8N3zS-17e0b0cab965910a6bc5.png)

1.  Enabled
2.  Disabled
3.  Hovered
4.  Focused
5.  Pressed

#### Toggle

![Toggle elevated button states.](../../_assets/GQDxPmCDjJpgGWRA_VTNzseTsmouIs0lh8IVP8woIQk4cgCiAnDMZThBIfxG1GHEqTlUoL585KoCLj8c-85bcceb30515b572cd5e.png)

A. Unselected, B. Selected

1.  Enabled 
2.  Disabled 
3.  Hovered 
4.  Focused 
5.  Pressed

### Filled button states

#### Default

![Filled button states.](../../_assets/RwG9SEB4yIRACbW517DyRW2mUveISG198EE64jJb0f277Q33MLyuP9uiKdCmeWhZeWKXDx_yRiSQtlWl-a7e29ab84a3f8e3edfd1.png)

1.  Enabled
2.  Disabled
3.  Hovered
4.  Focused
5.  Pressed

#### Toggle

![Toggle filled button states.](../../_assets/oM057IT2WiygsF0GMglnN22051Pgx_Xop2in-So8huFo-CUC5_gyPnBYksLf-wCXu4r6pZJQ1Qg9tPTv-2d6b564bb774f1bdd49b.png)

A. Unselected, B. Selected

1.  Enabled 
2.  Disabled 
3.  Hovered 
4.  Focused 
5.  Pressed

### Tonal button states

#### Default

![Tonal button states.](../../_assets/wdF2kYSVD8W-FnPza7kOisTKCDc5FZKUskKzi8j3yZ0m7Ras4cKeoBCwUjpRr4EXjlSia_UfiRWFCCXl-4af291653fba6e7fefd7.png)

1.  Enabled
2.  Disabled
3.  Hovered
4.  Focused
5.  Pressed

#### Toggle

![Toggle tonal button states.](../../_assets/SKh3_709LukNHRLX1h-4h3GWRx_g-PfrLaU28b33QM11qyAwNH2d-NPumu2KYhi9TECvF2QqeQ4ptDYU-da67c3e50b2d18906505.png)

A. Unselected, B. Selected

1.  Enabled 
2.  Disabled 
3.  Hovered 
4.  Focused 
5.  Pressed

### Outlined button states

The outlined button’s container fill is invisible at rest, but the opacity and state layers behave the same as other button styles when disabled, hovered, focused, or pressed.

#### Default

![Outlined button states.](../../_assets/0RiSKbIPPzMC64WPAmZrA0Xi2bxyaBAQ8vmzHpEp1yjrhjSJqC0xv3_4jJgYaqh7v4BH7lAJZXkkN_HV-a81df27ce145306fdd35.png)

1.  Enabled
2.  Disabled
3.  Hovered
4.  Focused
5.  Pressed

#### Toggle

![Outlined button states.](../../_assets/U9yJ0EWfejvgr2j2FQRTLwN2Fk4H0pM4JxoYvRkql-jgBFGSqS26j--nqv_a23AL1Fhsjk5GAjgK4E1h-ec4ba82419419b0cc2cc.png)

1.  Enabled
2.  Disabled
3.  Hovered
4.  Focused
5.  Pressed

### Text button style states

The text button’s container is invisible at rest, but the opacity and state layers behave the same as other button styles when disabled, hovered, focused, or pressed. There is no toggle text button.

![Default text button style states.](../../_assets/BYjS_Tdp0yXd5Dh1aupX_ELYzONtiZU21cT0y1kA5Pb3ne2T43AcIQ85r6jYIkHW6yRp0kQb7TNPiw5q-ca61a10accd9250f2c7d.png)

1.  Enabled
2.  Disabled
3.  Hovered
4.  Focused
5.  Pressed

## Shape morph

### Pressed state

When pressed, buttons can morph to become more square. Both round and square buttons should have the same pressed shape.

The corner radius value differs for each button size. [See full button corner measurements](/m3/pages/common-buttons/specs#b1f39738-6f3a-409b-8f08-4cab6d78d756)

![Shape changes of a button.](../../_assets/Si9asaI7X7SFuvDU46W5nHcZ9p9EVqCsu1Tb4Qfp1iPp2ho_kp85z_RXtK9EcyBqT5eoV-A4i8sJSQeD-489c03c63e2946afb578.png)

A. Round button, B. Square button

1.  Enabled
2.  Hovered
3.  Pressed

### When selected

In addition to changing shape when pressed, toggle buttons also change the resting shape from round (unselected) to square (selected). 

If the resting unselected shape is square, the selected shape should be round.

![Shape changes of a toggle button.](../../_assets/5hC5Vdz-txbFAuGYY8Bkij-tCNyyjHc1B2zDoFQ5WWkR9Aw6yCNB8hKYi3CO0DJ2xlNab2JbXSPsm4Hr-0624f24522c390ac7646.png)

A. Round button, B. Square button

1.  Enabled

2.  Hovered

3.  Pressed

4.  Selected

## Measurements

![Diagram of measurements of all button sizes.](../../_assets/JI2E9iCMwHgDDeC9fzCaTP1M974jPyBdpsV1OJoM83PKO0IINS4OUaPbdn9iT6ogQQqtFeBYb_IBT_sy-af89dfcd49affdde70a5.png)

Padding and size measurements of each button size

1.  Extra small

2.  Small

3.  Medium

4.  Large

5.  Extra large

### Target areas

Extra small and small icon buttons must have a target size of 48x48dp or larger to be accessible.

![Diagram of small button target areas.](../../_assets/35JMIvVuBd4UPv4LMpZ6rM_Hkn4S2UZlra92CcqY20cPp9334PxNr8KPaR-1P1d8q6Emonifwrp79hmx-39c1cb05e2cbe2744ec5.png)

A. Extra small  B. Small

1.  Round button 
2.  Button with icon
3.  Square button

### Corner sizes

![Diagram of corner radii of buttons.](../../_assets/sULNWNl9-8wPo3EiYHaqeFSTE3FnFXFotQmIJzabpV-JJPCaSWvwhK3u82A6CeaMqBYmQz3dyWBArTDU-7944ca3834701b8e16c9.png)

|  | XS | S | M | L | XL |
| --- | --- | --- | --- | --- | --- |
| A. Round button | Full | Full | Full | Full | Full |
| B. Square button | 12dp | 12dp | 16dp | 28dp | 28dp |
| C. Pressed state | 8dp | 8dp | 12dp | 16dp | 16dp |

## Baseline tokens

Use the table's menu to switch token sets. The baseline button token sets are organized by color. 

Token

Value

Close
