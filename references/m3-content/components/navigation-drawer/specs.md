---
source: https://m3.material.io/components/navigation-drawer/specs
title: "Navigation drawer"
captured: 2026-09-14
---

# Navigation drawer

> Navigation drawers let people switch between UI views on larger devices

star

Note:

The navigation drawer is no longer recommended in the Material 3 Expressive update. For those who have updated, use an [expanded navigation rail](/m3/pages/navigation-rail/overview/), which has mostly the same functionality of the navigation drawer and adapts better across breakpoints.

![Navigation drawer diagram numbering 7 elements](../../_assets/wzWoGqZcYHmlxmZaJ6h1mIIrnKAN6-ORvn-bAgZGnzVfSFw35XvFKnVMZ6aKAqVtw5sMblQfd0dN7cb5-ef23d32848dcb504eabc.png)

1.  Container

2.  Headline

3.  Label text

4.  Active indicator

5.  Badge label text

6.  Scrim

7.  Icon

## Tokens & specs

The navigation drawer has one token set. [Learn about design tokens](/m3/pages/design-tokens/overview/)

Token

Value

Close

## Color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)

![Navigation drawer diagram numbering 9 color roles.](../../_assets/EFOoVjwBffIgl-Gs07m2W5WiNu8brQ2paefKx_U_eQexLGySjgLV_C9FYD7wkTs0o7j3_RvrcTcqh6oU-ce15a132a689bca435fb.png)![Navigation drawer diagram numbering 9 color roles.](../../_assets/EFOoVjwBffIgl-Gs07m2W5WiNu8brQ2paefKx_U_eQexLGySjgLV_C9FYD7wkTs0o7j3_RvrcTcqh6oU-15d47796eda15634142a.png)

Navigation drawer color roles used for light and dark schemes:

1.  Surface container low
2.  On surface variant
3.  On secondary container
4.  On secondary container
5.  Secondary container
6.  On secondary container
7.  On surface variant
8.  On surface variant
9.  Scrim

For divider color roles, go to [divider specs](/m3/pages/divider/specs).

## States

States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or interactive element. [Learn more about interaction states](/m3/pages/interaction-states/overview)

![4 navigation drawers illustrating enabled, hovered, focused, and pressed states.](../../_assets/xCUslUMH4a9wLA0cXIbv622e8KMYHe0R5TPMmzjG0lFKP2hX6vjQcnKVFwxI9HIdk1z3y6BR65wFxvps-97890b191b96837801c3.png)

Navigation drawer states: 

1.  Enabled 
2.  Hovered 
3.  Focused 
4.  Pressed

[State specs are in the tokens module above](/m3/pages/navigation-drawer/specs#6207b00f-a259-41d2-8146-b6efc6380976)

## Measurements

### Standard navigation drawer

![Standard navigation drawer with measurements shown for various elements.](../../_assets/bHQAcDd4Vluh3tirhRwnej1hWyUij6O-bjAclp-H5fmSqLHDanyQZsk-RQCLJtCnVYQhYeN1DM4GQG4I-606a794fbd4d5bcbe828.png)

Element size measurements

![Standard navigation drawer with measurements shown for padding and margins.](../../_assets/0b273CFdNyDt3yEDRLSSICnKHb8rktNAiXmruD2EO82_S9iBxGsq08CPpYTupKoj0SRnuaNR0fo8dICO-b187d1a2e7ce019bd31a.png)

Padding and margins

| Attribute | Value |
| --- | --- |
| Container height | 100% |
| Container width | 360dp |
| Container shape | 0,16,16,0dp corner radii |
| Icon size | 24dp |
| Active indicator height | 56dp |
| Active indicator shape | 28dp |
| Active indicator width | 336dp |
| Horizontal label alignment | Start-aligned |
| Left padding | 28dp |
| Right padding | 28dp |
| Active indicator padding | 12dp |
| Padding between elements | 0dp |

### Modal navigation drawer

![Modal navigation drawer with measurements shown for various elements.](../../_assets/invVA4iDTyiHnbFHAMhycwQRAZds3tEMmOOPGaiv1HnriGnDeAV4MSXpQ9gOcnALm0eQcxgml_hzP-tT-040c9ec5eecb95070c0f.png)

Element size measurements

![Modal navigation drawer with measurements shown for padding and margins.](../../_assets/2T9NqmBF4mES5SgaRMeuXBm0CXnjDhysHSNKT1lr_iIEUZKCbKtRtIXvzyFbVR8RnSZ17O4sK483ySXp-63c91d7dcc811eea3e13.png)

Padding and margins

| Attribute | Value |
| --- | --- |
| Container height | 100% |
| Container width | 360dp |
| Icon size | 24dp |
| Active indicator height | 56dp |
| Active indicator shape | 28dp |
| Active indicator width | 336dp |
| Horizontal label alignment | Start-aligned |
| Left padding | 28dp |
| Right padding | 28dp |
| Active indicator padding | 12dp |
| Padding between elements | 0dp |
