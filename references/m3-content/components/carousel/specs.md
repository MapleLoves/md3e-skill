---
source: https://m3.material.io/components/carousel/specs
title: "Carousel"
captured: 2026-09-14
---

# Carousel

> Carousels show a collection of items that can be scrolled on and off the screen

![4 elements of a carousel.](../../_assets/Bfe7F5i-YHBu3MctH6XdfsSYD1VNZVWrAC2hTpG-vOuHgn1-npiiivwifJe1ddHkbRZxlXtKJuq0GV9S-557a2d44bbfedbc4f6cd.png)![4 elements of a carousel.](../../_assets/Bfe7F5i-YHBu3MctH6XdfsSYD1VNZVWrAC2hTpG-vOuHgn1-npiiivwifJe1ddHkbRZxlXtKJuq0GV9S-81865a5c725a5f46a740.png)

1.  Container
2.  Large carousel item
3.  Medium carousel item
4.  Small carousel item

## Tokens & specs

Browse the component elements, attributes, tokens, and their values.

Close

## Color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview/)

![2 color roles of a carousel.](../../_assets/Mzrpy7os0Evw3KGIkxaFfkon8IgFJgpyqGgYD2DIMMbywuPHponDXt8yaG9F6u0lJAhluoYHtJE1Sv2K-c4450f1ed1ef7d093e92.png)![2 color roles of a carousel.](../../_assets/Mzrpy7os0Evw3KGIkxaFfkon8IgFJgpyqGgYD2DIMMbywuPHponDXt8yaG9F6u0lJAhluoYHtJE1Sv2K-b63d5aa36f34caa311c7.png)

Carousel color roles used for light and dark schemes:

1.  Container
2.  Surface

## States

States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or interactive element. [Learn more about interaction states](/m3/pages/interaction-states/overview)

![5 states of a carousel in light and dark schemes.](../../_assets/D7QutV1hQsVv50Nbn-UkT_BAJ4JRYAHLcohN50l4y2t5BDjn0pSq5jHk29phmxHU4H-UZszf7UaQoCPD-b88d5191b813e559e277.png)![5 states of a carousel in light and dark schemes.](../../_assets/D7QutV1hQsVv50Nbn-UkT_BAJ4JRYAHLcohN50l4y2t5BDjn0pSq5jHk29phmxHU4H-UZszf7UaQoCPD-9d51cd57acbc2938282e.png)

1.  Enabled
2.  Hovered
3.  Focused
4.  Pressed
5.  Disabled

## Carousel item dynamic widths

All kinds of carousel items dynamically adapt to the width of the container.

Large items have a customizable maximum width that's used to optimally fit carousel items into the available space.

Small carousel items have a minimum width of 40dp and a maximum width of 56dp.

Items change size as they move through the carousel layout.

![Measurements for a small carousel item.](../../_assets/l_O_4sY-OWT2K7Ot5jY_yhXxSErGV6Cu33URxwXPnt8D6oTDXh3oWlg5utAL2Iw0afdYNvkjpYZzLlsX-ac668d63deca68c21a84.png)

Small carousel items have a minimum and maximum width

## Multi-browse

The multi-browse layout The multi-browse carousel layout shows at least one large, medium, and small carousel item at a time. shows at least one large, medium, and small carousel item.

![4 elements of a multi-browse carousel layout.](../../_assets/evx3sPQvpKArdG4MTkQQCOFPM387eGsABK9x_Ecv_LeJy23RGxJyVZU50_GThcTacMUgP5tuLoPOXRwk-bca68f94787f016b6835.png)

1.  Container
2.  Large carousel item
3.  Medium carousel item
4.  Small carousel item

### Measurements

![Measurements of a multi-browse carousel layout.](../../_assets/Py7GKPNbLAGSs7Zx0w19v21_MWZgZSX5ztGYvSQ8bDM4DeZ-ilsU5Ra3bR2_24qAgkiEn8j7dTfdKO7Y-f026c9e14fe1b01acb82.png)

Multi-browse carousels have padding on both sides of the container

| Attribute | Value |
| --- | --- |
| Alignment | Vertically centered |
| Leading/trailing padding | 16dp |
| Top/bottom padding | 8dp |
| Padding between elements | 8dp |
| Large item width | Dynamic, or user-set |
| Medium item width | Dynamic |
| Small item width | 40–56dp, dynamic |
| Item corner radius | 28dp |

## Uncontained

The uncontained The uncontained carousel layout show items that scroll to the edge of the container. layout shows items that scroll to the edge of the container.

![4 elements of an uncontained carousel layout.](../../_assets/p9Q_QbNpwi3QeDBOCZ64MWO3Vm83NIV7SFc6IqJ7BPGlsGidp5FJdTOq4yVq6zCZkqkSf03SLJ2pSEU4-38c0a26e77abbdc68da9.png)

1.  Container
2.  Large carousel item

### Measurements

![Measurements of an uncontained carousel layout.](../../_assets/kHmHj0O9aT5Nlb2KyOQq6CWd8sRWmGjzg3TMKEzoHQLd9OG08KSdrH7g3vUxMkGebXOb17s3kAT6fh16-eda61ec399fabe2df7d8.png)

Uncontained carousel items bleed over the padding on each side when scrolling

| Attribute | Value |
| --- | --- |
| Alignment | Vertically centered |
| Leading padding | 16dp |
| Top/bottom padding | 8dp |
| Padding between elements | 8dp |
| Item corner radius | 28dp |

## Uncontained mutli-aspect ratio

The uncontained multi-aspect ratio layout shows carousel items of various widths.

![4 elements of an uncontained carousel layout](../../_assets/FM3l_rU4tOFqCVj-gmDwOG9zyWk279AI0tz5aHQa5hRW5v3P4cS3ydvtXKwZMy_ClxODMX76POePAuI9-e5dfe61615fd444a07f3.png)

1.  Container
2.  Carousel item (16:9)
3.  Carousel item (9:16)
4.  Carousel item (1:1)
5.  Carousel item (3:4)

### Measurements

![](../../_assets/1SazYXoMFnNnFpmqXCe7pchjco1F_R03ws6GfweuJDv4cgafUAQ0l0P_8ELNDh-l8UEyycEhodtkGYJg-ec6fa3a226c499a674aa.png)

Uncontained multi-aspect ratio carousels only have leading padding, with 8dp of padding between items.

| Attribute | Value |
| --- | --- |
| Alignment | Vertically centered |
| Leading padding | 16dp |
| Top/bottom padding | 8dp |
| Padding between elements | 8dp |
| Item corner radius | 28dp |

## Hero

The hero layout The hero carousel layout shows at least one large and one small item at a time. shows at least one large item and one small item.

![3 elements of a hero carousel layout.](../../_assets/I9ALEx4jwdluVMjRmR2zhTCFVHo3N05uccMHUOXxA1pAD-XMUdr9GNHJPfOT9mkNz862VyWH2ItNhseE-0686f8422be1d40bd0d7.png)

1.  Container
2.  Large carousel item
3.  Small carousel item

### Measurements

![Measurements of a hero carousel layout.](../../_assets/LOm-yrGl6Hmuxn-eQ995_1ZlFqkd90so8hX-xPss8PWGCyXWDJECAupl-paVut_4taB6DVA7OENO39mx-d38322b08deaaa274c92.png)

Hero carousels have padding on both sides of the container

| Attribute | Value |
| --- | --- |
| Alignment | Vertically centered |
| Leading/Trailing padding | 16dp |
| Top/bottom padding | 8dp |
| Padding between elements | 8dp |
| Large item width | Dynamic |
| Small item width | 40-56dp, dynamic |
| Item corner radius | 28dp |

## Center-aligned hero

The center-aligned hero layout shows at least one large item and two small items.

![3 elements of a center-aligned hero carousel layout.](../../_assets/4LmjbjezXxY7ctWR2bmLAa35m3No8ErHZO31L0jTLxRBc3ivUMC_DA5rDEEZRILu8VlJLE__deFfvXQx-f1dc5bd1efe5778a204c.png)

1.  Container
2.  Large carousel item
3.  Small carousel item

### Measurements

![Measurements of a center-aligned hero carousel layout.](../../_assets/SuFPyTcmkMVHYU4NubWqAMrraBaL0OAFzvUcuXPWlkmIsASj8fOjlwGNfNpl4LP9revB2iU8dc-oFBOX-f094dc22efccf4b6a3ee.png)

Center-aligned hero carousels have padding on both sides of the container

| Attribute | Value |
| --- | --- |
| Alignment | Vertically centered |
| Leading/Trailing padding | 16dp |
| Top/bottom padding | 8dp |
| Padding between elements | 8dp |
| Large item width | Dynamic |
| Small item width | 40-56dp, dynamic |
| Item corner radius | 28dp |

## Full-screen

The full-screen layout The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically. shows one edge-to-edge large item.

![2 elements of a full-screen carousel layout.](../../_assets/bn-epGZhbTWJijBRurEco_OYDKB-s-DEYMJgCwj7OSBbLJMEm34yEZY1AaKy2gEKjnMCT--UTHHqR0IO-e9d5237a140cedaf8ae1.png)

1.  Container
2.  Large carousel item

### Measurements

![Measurements of a full-screen carousel layout.](../../_assets/qo38AJlGFDaPzNKJX24tQG5PrvIQ_PRl0ZEmeh-7YE8FvikHGuh96N5ggGpDoOStYSzbhUAg0-36VmHV-7c1adaf66ba48580c8f5.png)

Full-screen carousels fill the window edge-to-edge

| Attribute | Value |
| --- | --- |
| Alignment | Centered |
| Leading/Trailing padding | 0dp |
| Top/bottom padding | 0dp |
| Padding between elements | 16dp |
