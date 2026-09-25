---
source: https://m3.material.io/components/badges/specs
title: "Badges"
captured: 2026-09-14
---

# Badges

> Badges show notifications, counts, or status information on navigation items and icons

![5 aspects of badge anatomy on a navigation bar.](../../_assets/1c2wjkW2_C9l1HmNkRT8GpeQ7WqSDcJdMKdNym4xk_wPBfFSgVP3NhSXBwBV52vI3L-Z7CAmnY7c-1WM-0a8573301613f54c3416.png)

Navigation bar

1.  Small badge
2.  Large badge container
3.  Large badge label
4.  Large badge maximum character count container
5.  Large badge maximum character count label

![5 aspects of badge anatomy on a navigation rail.](../../_assets/9yjKmecr7ZJh2Tm71DBDcwftLy2cMEpCW2yl73CCr7kUctUtmKaW78yFdO-0ZUSBXShJh9CDLZtQhcOy-9db70c2d3ed4a74df9c1.png)

Navigation rail

1.  Small badge
2.  Large badge container
3.  Large badge label
4.  Large badge maximum character count container
5.  Large badge maximum character count label

## Tokens & specs

Browse the component elements, attributes, tokens, and their values.

Token

Value

Close

## Color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)

![5 applications of badge color on light and dark theme navigation bars.](../../_assets/GXqQAaWohBPLwvJAZUGaxFwy8CI_R4BLcAXPDq-e4P67CObmbEHL-GzwJbo6hBOmuqFuoV8QrPMXhmL2-313896ec44c231ee2bd8.png)![5 applications of badge color on light and dark theme navigation bars.](../../_assets/GXqQAaWohBPLwvJAZUGaxFwy8CI_R4BLcAXPDq-e4P67CObmbEHL-GzwJbo6hBOmuqFuoV8QrPMXhmL2-c3c66455fc9b7fe876a7.png)

Badge color roles used for light and dark schemes in navigation bar:

1.  Error
2.  Error
3.  On error
4.  On error
5.  Error

![5 applications of badge color on light and dark theme navigation rails.](../../_assets/8-bcqHO-CggN9L5OTiWVxPDT-wPzcurO0xXI7dZeo5htfXRjDwMnoMl_Qco9Z8NGG9CE2_5qrO2QdLV--2a268cdb9e4e244e246a.png)![5 applications of badge color on light and dark theme navigation rails.](../../_assets/8-bcqHO-CggN9L5OTiWVxPDT-wPzcurO0xXI7dZeo5htfXRjDwMnoMl_Qco9Z8NGG9CE2_5qrO2QdLV--b576dc2febccf664c292.png)

Badge color roles used for light and dark schemes in navigation rail:

1.  Error
2.  On error
3.  Error
4.  On error
5.  Error

## Measurements

![Annotation of badge sizes, padding, and measurements from the corner of the icon to the badge opposite corner.](../../_assets/9tsQOYHX4YH6bQJJwi1ylkI-nu2RJBNb84ivjXE8ksTqqpuE4w-riSO17Sh2gclSOMxjzlDHS_B2zKmb-76cb81d1ed92073b3471.png)![Annotation of badge sizes, padding, and measurements from the corner of the icon to the badge opposite corner.](../../_assets/9tsQOYHX4YH6bQJJwi1ylkI-nu2RJBNb84ivjXE8ksTqqpuE4w-riSO17Sh2gclSOMxjzlDHS_B2zKmb-8ed33ee7bcff60d563f2.png)

Badge padding and size measurements

| Attribute | Value |
| --- | --- |
| Small badge shape | 3dp corner radius |
| Small badge size (HxW) | 6dp |
| Large badge shape | 8dp corner radius |
| Large badge one digit size (HxW) | 16dp |
| Large badge max character count size (HxW) | 16x34dp |
| Small badge: distance from top trailing icon corner to bottom leading badge corner (HxW) | 6x6dp |
| Large badge: distance from top trailing icon corner to bottom leading badge corner (HxW) | 14x12dp |
| Large badge padding between badge and text container | 4dp |

## Configuration

Different badges are shown on navigation destinations in various states. States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview)

![Diagram of 3 badge variations shown on navigation destinations in various states.](../../_assets/dmnjAmE1Ol38Ijd8REgLVSvLNv733cEX_WngU88yFKfiKjSdwanYmhHnCGueyMQAzJRxRMrvdgtC2KPa-d19f458fb3b0357acbec.png)

1.  Inactive with label - small badge
2.  Inactive with label - large badge
3.  Inactive with label - large badge max character count
4.  Inactive - small badge
5.  Inactive - large badge
6.  Inactive - large badge max character count
7.  Active with label - small badge
8.  Active with label - large badge
9.  Active with label - large badge max character count
10.  Active nav bar no label - small badge
11.  Active nav bar no label - large badge
12.  Active nav bar no label - large badge max character count
13.  Active nav rail no label - small badge
14.  Active nav rail no label - large badge
15.  Active nav rail no label - large badge max character count
