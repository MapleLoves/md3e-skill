---
source: https://m3.material.io/components/icon-buttons/specs
title: "Icon buttons"
captured: 2026-09-14
---

# Icon buttons

> Icon buttons help people take actions with a single tap

## Variants

![Side by side view of default and toggle icon buttons.](../../_assets/eJRJf0S1ywGr8CdhzgukcRgQpKxbZOCEZ12g2HeJrldunvEVBgg_65CzvyHntvAMJWJYApy-BpompKTb-edeb7cb2c9cee2db5307.png)

1.  Default icon button
2.  Toggle icon button

| Variant | M3 | M3 Expressive |
| --- | --- | --- |
| Default | Available | Available |
| Toggle (selection) | Available | Available |

## Configurations

![Side by side view of size, shape, color, and width variations.](../../_assets/8uQEXQa18WJuSmuK5CLloUJ69m6TGCdj5C9FBDFAETglM5PWdtNDxW62KriOfOjurHZ9ThRY_yfM_pfR-2eade3069744a9023715.png)

1.  Five sizes

2.  Two shapes

3.  Four color styles

4.  Three widths

| Category | Options | M3 | M3 Expressive |
| --- | --- | --- | --- |
| Size | Small (default) | Available | Available |
| XS, M, L, XL | \-- | Available |
| Shape | Round (default) | Available | Available |
| Square | \-- | Available |
| Color | Filled (default), tonal, outlined, standard | Available | Available |
| Width | Default | Available | Available |
| Narrow, wide | \-- | Available |

## Tokens & specs

Icon button token sets are organized by common tokens, color, and size. Select the token set from the table’s menu. [Learn about design tokens](/m3/pages/design-tokens/overview/)

Close

## Anatomy

![Diagram indicating anatomy of filled icon button.](../../_assets/awRYSAQ6XdaVBsLtLmUSRj56cqySERCiE8qj36eLHxsk8YXYMMkaU_tkx606qnJKv41RtQKLV9uSyAwk-375c2254398ea20bc281.png)

1.  Icon 
2.  Container

## Color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For designers, this means working with color values that correspond with tokens; in implementation, a color value will be a token that references a value.

There are four built-in color styles: filled, tonal, outlined, and standard. Default and toggle buttons use different color roles per style.

star

Note:

These color roles were chosen to create design coherence and familiarity. Other color roles can be used as long as the container and text have a 3:1 contrast ratio. For example, tertiary and on tertiary.

![Color roles of default and toggle buttons in 4 visual styles.](../../_assets/CWKvmXvNaFk4LwtZcFhYyOOgq-OJEnRgXVifhpYTwewAHQXGsA8SAcHgpi4_BO2o6CIT-ERoIMpSI41h-8fbcb80b687a8612848c.png)

A: Filled, B: Tonal, C: Outlined, D: Standard

1.  Default

2.  Toggle, unselected

3.  Toggle, selected

|  | 1\. Default | 2\. Toggle, unselected | 3\. Toggle, selected |
| --- | --- | --- | --- |
| Filled containerFilled icon | Primary On primary | Surface containerOn surface variant | Primary On primary |
| Tonal containerTonal icon | Secondary containerOn secondary container | Secondary containerOn secondary container | Secondary On secondary |
| Outlined containerOutlined icon | Outline variant (outline)On surface variant | Outline variant (outline)On surface variant | Inverse surfaceInverse on surface |
| Standard icon | On surface variant | On surface variant | Primary |

## States

States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or interactive element. State layers slightly change button color. Disabled states have different base colors. [View tokens for details](/m3/pages/design-tokens/overview)

### Filled button states

#### Default

![5 states of filled icon button.](../../_assets/f_CiuCyosU5CvebQEKN5zF51JfbHKIee5oqSFrP2od51IfqDJ3SLx35_e9J-heZw83g2JpUqslKhGoeM-33576596edfda409b474.png)

1.  Enabled 
2.  Disabled (10% state layer)
3.  Hovered (8% state layer)
4.  Focused (10% state layer)
5.  Pressed (10% state layer)

#### Toggle

![5 states of filled toggle icon button.](../../_assets/Sv4DWzeNFz0bHgKddC2o6jcm4_Mg65zw0e9QF5y_PHOChQFHOkMGw_c05fE1srSoY50_RoTis4N2-bKg-91dfd4783965fd477863.png)

A: Unselected. B: Selected

1.  Enabled 
2.  Disabled (10% state layer)
3.  Hovered (8% state layer)
4.  Focused (10% state layer)
5.  Pressed (10% state layer)

### Tonal button states

#### Default

![5 states of tonal icon button.](../../_assets/tgEuyiPL-Ux4Egj4kNTjvchlPIoplTaK_XukYj-4rC8T0MY8-7lsHzNq6wVpithFm43UqjQC-Ymy9Ek9-037818b3b5a143e4c30c.png)

1.  Enabled 
2.  Disabled (10% state layer)
3.  Hovered (8% state layer)
4.  Focused (10% state layer)
5.  Pressed (10% state layer)

#### Toggle

![5 states of tonal toggle icon button.](../../_assets/3K-szMHugOwyybK3LjFoitWWxa6kcW8TKvzoBTvLDYFKK2hePutHe3uPnaZlY9-87q4g-CJ_cNUXZJF4-1bbe82f5ca21c6847f46.png)

A: Unselected. B: Selected

1.  Enabled 
2.  Disabled (10% state layer)
3.  Hovered (8% state layer)
4.  Focused (10% state layer)
5.  Pressed (10% state layer)

### Outlined button states

#### Default

![5 states of outlined icon button.](../../_assets/yinTmVHDt3kOx1KIpfsX9V_-EkqnaUvj7hBjMWu90VQ3MgbEsjFJFPlV_-i4k9ACyP1Vt4uJMABCGejE-0d026f138f58e627a6d3.png)

1.  Enabled 
2.  Disabled (10% state layer)
3.  Hovered (8% state layer)
4.  Focused (10% state layer)
5.  Pressed (10% state layer)

#### Toggle

![5 states of outlined toggle icon button.](../../_assets/BcxmjH6ecztV2npud8AveNazSZr__0H66nlq-j3xggQLcQvKLxLCXDbyXs13fVtB-A3l_zU1wq8aY84b-112fe53aee01c01a2fa1.png)

A: Unselected. B: Selected

1.  Enabled 
2.  Disabled (10% state layer)
3.  Hovered (8% state layer)
4.  Focused (10% state layer)
5.  Pressed (10% state layer)

### Standard icon button states

The standard icon button’s container is invisible at rest, but visible when the state layer is applied.

#### Default

![5 states of standard icon button.](../../_assets/dwZOlhE1Y0s7U-eyHTYVA9aLYhUf9oSQBoay9bRBmlE-yPvG59Cu80jkcB3VNU6876dcNy34dIYjt_OC-0640fad3196139769df4.png)

1.  Enabled 
2.  Disabled (10% state layer)
3.  Hovered (8% state layer)
4.  Focused (10% state layer)
5.  Pressed (10% state layer)

#### Toggle

![5 states of standard toggle icon button.](../../_assets/Saes8VH33LRUx0xEd2BgfqFb39GzpjdT-z4HRzdjv3hST24J--BeF4JV_r0do5wk4jbPBb-AsSLMeWqI-ac4411ff3697741785f0.png)

A: Unselected. B: Selected

1.  Enabled 
2.  Disabled (10% state layer)
3.  Hovered (8% state layer)
4.  Focused (10% state layer)
5.  Pressed (10% state layer)

## Shape morph

### Pressed state

While pressed, icon buttons can morph to become more square. 

Both round and square icon buttons should have the same pressed shape radius.

The corner radius value differs for each button size. [See full icon button corner measurements](/m3/pages/icon-buttons/specs#b3df1f02-d313-44e9-9542-37f7e0e24dc7)

![Shape changes for round and square icon buttons in 3 states.](../../_assets/R4g7sI29Fu5i_IbuatO_g8K3lOfiXc5bWqBhR3s_5fhlg_yRXIbj6n26wEoi5SKZBszsh2CYiN6iioN9-dc2149c0a528f6165ace.png)

A. Round, B. Square

1.  Enabled
2.  Hovered
3.  Pressed

### When selected

In addition to changing shape when pressed, toggle icon buttons also change the resting shape from round (unselected) to square (selected) by default.

If the resting shape is square, the selected shape should be round.

![Shape changes for round and square toggle icon buttons in 3 states.](../../_assets/BnUdAgpdenC-evMYsprXRd489dyTMpWrSuPeQgbXSYXyJipJESFG-v4OLvX9K0aWOHkWjS7-k7qXXmQj-ca66b9a22f6e5344388e.png)

A. Round, B. Square

1.  Enabled
2.  Hovered
3.  Pressed
4.  Selected 

## Measurements

![Diagram of 5 sizes of icon buttons in 4 widths.](../../_assets/jjXoUxycgTulKAlvK7SJG4QJ6ok6z-OJVsuMM4Q79_6fBauVYYA_TBTzTFzKa3-HvqYbWV9SR13zv35H-e354967e1d8595c16aad.png)

A. Extra small  B. Small  C. Medium  D. Large  E. Extra large

1.  Icon size
2.  Default width size 
3.  Narrow width size  
4.  Wide width size

### Target sizes

Extra small and small icon buttons must have a target size of 48x48dp or larger to be accessible.

![Diagram of target sizes.](../../_assets/elGowRNNI3axprldZYy7RbpofXNr_DB-TAdJep-DZ_sRF0WCCACN-pxCEBBeF6_5FJADjm_fVuRgRNNG-3606bcdfd135a85e3c0e.png)

A. Extra small icon button size  B. Small icon button size

1.  Narrow width 
2.  Default width
3.  Wide width

### Button corner radius

![Diagram of icon button corner radius.](../../_assets/qbTMBYNLCAPi3CIr8hTDFwdc0GclxQmGaA67KohT7UMz509-iBAlMzevRQwXVvthTGyaA_7lA4DR060w-25182a051e4a4bc40b24.png)

|  | XS | S | M | L | XL |
| --- | --- | --- | --- | --- | --- |
| A. Round button | Full | Full | Full | Full | Full |
| B. Square button | 12dp | 12dp | 16dp | 28dp | 28dp |
| C. Pressed state | 8dp | 8dp | 12dp | 16dp | 16dp |

## Baseline tokens

Use the table's menu to select a token set. Filled, tonal, and outlined icon button tokens are now deprecated in favor of the new token sets. All other tokens are still available in the module at the top of the page.

Close
