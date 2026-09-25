---
source: https://m3.material.io/components/tabs/specs
title: "Tabs"
captured: 2026-09-14
---

# Tabs

> Tabs organize content across different screens and views

## Tokens and specs

Select a component variant below to see its elements, attributes, tokens, and their values.

Token

Value

Close

## Primary tabs

![6 elements of primary tabs.](../../_assets/0bS99kVjUnrfIUIKGAMWl8zeoYciELsgT5jPWeC4JJ9gcDC2cfnKH-p9qOYsX0OJ000ePPYMARw_YXMt-b820714ec5305d465903.png)

1.  Container
2.  Badge (optional)
3.  Icon (optional)
4.  Label
5.  Divider
6.  Active indicator

### Primary tabs color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)

![7 color roles applied to primary tabs in light and dark themes.](../../_assets/dmXLWuK2u_6U_iIQaK_nWtayfYfcfZU6mZyf5IAPmgu9y14-Puo51QN7a74fZJ34z0ESD88OfHOvUOFc-e1a5f818423387d159e9.png)

Primary tab color roles used for light and dark schemes:

1.  Surface
2.  Primary
3.  Primary
4.  On surface variant
5.  On surface variant
6.  Outline variant
7.  Primary

### Primary tabs states

![Diagram of all primary tab states in both light and dark mode](../../_assets/SVFdAJr5_8cGN6FTMVabD3nie8TwI7380y6PuVzSxatYH1YBsdf49aWd1upXNO7uDcsKDd8Uge2WtDUP-550ad716a51d138d880d.png)

1.  Enabled (active destination)
2.  Hover (active destination)
3.  Focused (active destination)
4.  Pressed (active destination)
5.  Enabled (inactive destination)
6.  Hover (inactive destination)
7.  Focused (inactive destination)
8.  Pressed (inactive destination)

## Secondary tabs

![5 elements of secondary tabs.](../../_assets/kyON5nMIlowboe0XsmPdlYKlFdIzCFTab9gzT4uEJtS2WMvRd1uBJHEMDDOKujs1u1iJYlb66cSc7LBf-519985fb7b60bad5d885.png)

1.  Container
2.  Badge (optional)
3.  Label
4.  Divider
5.  Active indicator

### Secondary tabs color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)

![5 color roles applied to secondary tabs in light and dark themes.](../../_assets/mrLdFHBC7H_M0bhZxPDT-VaJeoB01vnZMaY_9Pyj_EenTQbIT6OO75CWFdZLyvMxD0ycppRCoWXustGm-8566234451298308eb8f.png)

Secondary tab color roles used for light and dark schemes:

1.  Surface
2.  On surface
3.  On surface variant
4.  Outline variant
5.  Primary

### Secondary tabs states

![Diagram of all secondary tab states in both light and dark mode](../../_assets/oEbOwsXXP2m1EE9Sh7tJFcTP1GIHVkX6lbOkKN-gdwnF4WbJnoyezqHEr1rtaeAPTY2cHj6txNpy91Yg-1adae7541c09dc80b001.png)

1.  Enabled (active destination)
2.  Hover (active destination)
3.  Focused (active destination)
4.  Pressed  (active destination)
5.  Enabled (inactive destination)
6.  Hover (inactive destination)
7.  Focused (inactive destination)
8.  Pressed (inactive destination)

## Measurements

![Diagram of measurements for four and two tabs per container, including icon and label placement.](../../_assets/KNDnEXfu6HZxqBLD84eQfamUeoe8b_N3wygSYqpk5Hq1MxT7_9RNL34wYce0tPDml6rb6lP7cQO8lYhx-6ceb568e2dce556c2818.png)

Tabs are divided into equal sections, with labels and icons positioned vertically centered. The divider is included in the height, placed inside the container.

![Diagram of Primary tab active indicator measurements.](../../_assets/lEVgg_QRIKA7HpYLAWEddeY7ZCHa5FmlPc1K3C0yx1c5cmW_wxci7cAmdW_55RvUextO4vEHupXxMrWX-fca163dd1f192c013351.png)

Primary tab active indicators are inset 2dp on each side, have a fully rounded corner radius, and a minimum length of 24dp.

| Attribute | Value |
| --- | --- |
| Container height (label text only) | 48dp |
| Container height (icon and label text) | 64dp |
| Icon size | 24dp |
| Divider height | 1dp |
| Primary active indicator height | 3dp |
| Secondary active indicator height | 2dp |
| Active indicator shape | 3, 3, 0, 0 |
| Active indicator minimum length | 24dp |
| Padding between inline icon and text | 8dp |
| Padding between inline text and badge | 4dp |
| Overlap of badge on stacked icon | 6dp |
