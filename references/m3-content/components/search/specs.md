---
source: https://m3.material.io/components/search/specs
title: "Search"
captured: 2026-09-14
---

# Search

> Search lets people enter a keyword or phrase to get relevant information

## Variants

When a person executes a **search**, results appear in a list below the search bar

| Variant | M3 | M3 Expressive |
| --- | --- | --- |
| Search | Available | Available |

## Configurations

### Style

Search comes in two styles:

-   Contained: Has an expressive M3 Expressive is a major update to Material 3, adding visually stunning features, components, and variants, plus updates to the shape, motion, and typography systems. [More on M3 expressive](https://m3.material.io/blog/building-with-m3-expressive) look and feel. It uses a filled container to separate a search bar from a list Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) of suggestions or results

-   Divided ( baseline Baseline variants and styles are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles. ): Doesn’t have the latest visual style, motion, or flexibility

![An email inbox search bar in a contained style.](../../_assets/mZviJwGIZh_IpUNqJc4qSUDOLFrmDTpbjX_bufkF90qso_IE6fyfgB1e2VmG5N_E6Picjiw05l7vRqKS-2fa44978c78391f824a4.png)

The contained style has a persistent, filled container, expressive motion, and rounded shape

![An email inbox search bar in a divided style.](../../_assets/sA1JTXVXpg8LWSsXFxuxTShN08cJnxWigVkMDRzrHVQT6XnlvmPuvbVrmmeMZ7ZgDpNyRgv6T-zOjMh7-1bfd7d2a0ce0ca928668.png)

The divided (baseline) style uses a divider to separate the search bar from suggestions and results

### Layout

Search suggestions and results appear in customizable lists, with two layout options: full-screen and docked. [More on search layouts](/m3/pages/search/guidelines#4f6c921c-795f-4e06-9b12-27ae7d502adb)

![Full-screen search results with a search bar in the contained style.](../../_assets/UN8OMCnrmxaASc6CRHtAONOcdeZf71JD03xLHV9sDt8-A6pMWEWH2DxRbjhxM7M8_IE2H7_w8mtdqqE5-efcdcf5785a7b08632d2.png)![Full-screen search results with a search bar in the contained style.](../../_assets/UN8OMCnrmxaASc6CRHtAONOcdeZf71JD03xLHV9sDt8-A6pMWEWH2DxRbjhxM7M8_IE2H7_w8mtdqqE5-152a22a0e2341c144e0a.png)

Full-screen layout in the contained style

![Docked search results with a search bar in the contained style.](../../_assets/SlF8qBuCFFB-x7eQOBSJ6O2BgEmepkVWMQvU1b0gtBUdISdyG2QJbz0MeS6HPrO49nL_AZQaOil5-Rw8-4f28b197877422d1be72.png)![Docked search results with a search bar in the contained style.](../../_assets/SlF8qBuCFFB-x7eQOBSJ6O2BgEmepkVWMQvU1b0gtBUdISdyG2QJbz0MeS6HPrO49nL_AZQaOil5-Rw8-26a8600af7911298fdd1.png)

Docked layout in the contained style

![Full-screen search results with a search bar in the divided style.](../../_assets/xcvU3lGYJQELKKllc3w1uW68diJE9YJPeiCtbZM8tC9Gzg0qg5TBBzjEiFkl8hYOWcik2XUQfgqpeXvX-cc12187a4749302439f5.png)

Full-screen layout in the divided style

![Docked search results with a search bar in the divided style.](../../_assets/4FjOzW97D9JP3Mvu2GyfQ-PQhbAvpQRPjPjsqj3iM_125CTJgfv8X_u-qeSu4ti3i7ytSIZf4Crkoz5d-92a74396092f92d5fe90.png)

Docked layout in the divided style

| Category | Configuration | M3 | M3 Expressive |
| --- | --- | --- | --- |
| Style | Contained | \-- | Available |
|  | Divided | Available | Not recommended. Use contained. |
| Layout | Docked, full-screen | Available | Available |

## Tokens & specs

Use the table's menu to select a token set. The **search bar** set only contains tokens for the unfocused search bar. The **search view** set contains all other tokens when interacting with search, including all styles and layouts. [Learn more about design tokens](/m3/pages/design-tokens/overview)

Token

Value

Close

## Anatomy

Search includes a search bar and a container for suggestions and results. The container is empty by default. Use the list Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) component to add content. In the divided (baseline) style, a divider separates the search bar and results.

![6 elements of search.](../../_assets/nfgJlo7RsO4mElkJBSEo5E2yo1OPaLlu6o9PxA4lLhre5XuuiXAOj1LsjVPDk01MysoC5dasvtMXqSDJ-7375b5814b76c62f1f33.png)

1.  Search bar container

2.  Leading icon

3.  Supporting text

4.  Trailing icon and avatar (optional)

5.  Input text

6.  Container for search suggestions or results

### Examples

1.  With avatar

2.  With one trailing icon button Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview)

3.  With two trailing icon buttons

4.  With trailing icon button and avatar

![4 search bars with different trailing elements.](../../_assets/4DOSj_PCy0dVTh_Mwwa-JmNfmmABObXarzG6mlKcjL7V1kdeh9_yrI9kQM5t1UhpsVOtc4bIq7mUwNYh-da0bebe52c569cc0be9f.png)

## Color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value.

### Full-screen layout

![6 full-screen search color roles in light and dark themes.](../../_assets/GAGCWflTpnmoM0DwwKy1v0DdcEY5uW2zCwZpY8CaR61iuDKk3E7JY7yVPwx3ukkfq4B7qyOQOLInW7c7-4a278fd3a240f953a539.png)

Full-screen search color roles used in light and dark themes:

1.  Surface container low

2.  On surface variant

3.  On surface variant

4.  Surface container high

5.  On surface variant

6.  On surface

### Docked layout

![6 docked search color roles in light and dark themes.](../../_assets/nq53ckQlKsYuKPXvcEYzyrhQ7Fevp-zkK7TzePU0X7GjTIveyJLPIHzZrZ3ejyWOGKASNBS7Ir8_si6O-9efcb4dd9269b72115d0.png)

Docked search color roles used in light and dark themes:

1.  Surface container high

2.  On surface variant

3.  On surface variant

4.  Surface container high

5.  On surface variant

6.  On surface

## States

States are visual representations used to communicate the status of a component or an interactive element. In [focused search](/m3/pages/search/guidelines#a9b2df31-8561-4326-82cd-41ed6532b765), individual elements maintain their own interaction states. [Learn more about interaction states](/m3/pages/interaction-states/overview)

### Search bar

![4 search bar states in light and dark mode.](../../_assets/YhREfAtX7rK4eHN7NEAdJA3S1VPgesRkPzepAVAMJWT7aA0MSV9dxw8A248GG0PwSTS8FjyLqzorX8U4-e8b3a1ab8a6707f17249.png)

1.  Enabled

2.  Hovered

3.  Focused

4.  Pressed (ripple)

### Search suggestions & results

Search includes a container for suggestions and results. The container is empty by default. Use the list component to add content.

![4 search result states in light and dark mode.](../../_assets/r1ddmkgjt_KkZZC-S8XGOaYfxyTvkqH_xLNf6MgWq89lOToWeBm5mEo8Kz2QhMxh3H_FOF_EjatnziEy-f24302ba2c10db1998a9.png)

1.  Enabled

2.  Hovered

3.  Focused

4.  Pressed (ripple)

## Measurements

### Search bar

![Search bar with leading and trailing icon size and padding measurements.](../../_assets/mGptx_4JUwLVcbHz93O72eFnZN6uaFTxfpTyUe7VfjOxvJQn0kew6pVVDeiAeV4S5rWjZ0xQR-RsZMNC-4cb3417efd69149e02ed.png)

Unfocused search bar with leading and trailing icon measurements

![Search bar with trailing avatar size and padding measurements.](../../_assets/dURHAt9JC2YGWnXNGRK34cv-wK4xrn9GhPUNnWdQ3ZcgzjMRuwGi5KNwpFaWn19j7Nls-mp9PTDF79hT-7cb1302b66735602a7b7.png)

Unfocused search bar with avatar measurements

In M3 Expressive, the search bar expands when focused. The margins change from 24dp to 12dp.

![Unfocused search bar margins of 24dp.](../../_assets/OfNDMCVyfuBJXmI9HLNp26jlV-aQMKAawCfhfzbzlt-wYn0lR4BxkbXOVbiEP6I2tgz0HFbjC2SY5qvb-b3c6bb6d2e2dc5442589.png)

Unfocused search bar margin measurements

![Focused search bar margins of 12dp.](../../_assets/R4k1-IGNQH3zamzgc2laHGU70E3SDajTXtksf4eWJIQO7gmrwoj9PCGHzqhrOju-IKtpdeoOCRi7WqJ5-5b8d88f20bab5d40de89.png)

Focused search bar margin measurements

| Element | Attribute | Value |
| --- | --- | --- |
| Container | Width | Min: 360dp, max: 720dp |
| Height | 56dp |
| Label alignment | Start-aligned |
| Leading padding | Unfocused: 24dp, focused: 12dp |
| Trailing padding | Unfocused: 24dp, focused: 12dp |
| Leading icon and label padding (from tap target) | 4dp |
| Label and trailing icon padding (from tap target) | 4dp |
| Avatar | Size | 30dp |

### Focused search

#### Contained style

![Full-screen layout size and padding measurements in contained style.](../../_assets/b0xykJB3s1NEcZz6gQP37YfP-r6S3fbfqNKJaY-XbWy2AyoWViOPlmHhW6Lq6b4IbhmcDYAQJHonH59H-fc2c9311f85e99f34fe1.png)

Full-screen search padding and size measurements for contained style

![Docked layout size and padding measurements in contained style.](../../_assets/5Hst6KPsjyxhxQTptCBbkRahderHldeKa_33ucNVW9xZ9svHkx9eBhbhDKYR656D5DkvhdfdMIPhs5L9-5d511b62ba2e16ba11a2.png)

Docked search padding and size measurements for contained style

| Element | Attribute | Value |
| --- | --- | --- |
| Full-screen container | Width | Full width |
| Height | Full height |
| Docked container | Width | Min: 360dp, max: 720dp |
| Height | Min: 240dp, max: 2/3 of screen height |
| Search bar container | Height | 56dp |
| Label alignment | Start-aligned |
| Leading padding | 16dp |
| Trailing padding | 16dp |
| Leading icon and label padding (from tap target) | 4dp |
| Leading icon and label padding (from tap target) | 4dp |

#### Divided style

![Full-screen layout size and padding measurements in divided style.](../../_assets/RhpQaBUaokljf6Qv0Pb6sUHofotzoGbLGs7O74snG2B9yjauRk1iv6JFhmSRsHNdUu3nacOIuEmi0RoG-d85bbe15b136ad813f34.png)

Full-screen search padding and size measurements for divided style

![Docked layout size and padding measurements in divided style.](../../_assets/52yDW7vsdT_ythER_zFPD7eAyH2K5BvU_V9fB4COC5khSNA81CffErRCuS1kxNZkIfPYCWceEYxrnu07-5f6b6ec5e0c61c2aedae.png)

Docked search padding and size measurements for divided style
