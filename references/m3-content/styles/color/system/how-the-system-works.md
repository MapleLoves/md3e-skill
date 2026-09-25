---
source: https://m3.material.io/styles/color/system/how-the-system-works
title: "Color system"
captured: 2026-09-14
---

# Color system

> Create accessible, personal color schemes communicating your product's hierarchy, state, and brand

## It's like paint-by-number

Imagine your product screen as a paint-by-number canvas:

-   Each element on the screen has a number
-   Each number is assigned a color

![UI in "x-ray" view where each element has a number instead of a color](../../../_assets/m4mxjs2l-1-d7293f5bfed34099f778.png)

Each part of a UI is assigned a "number," and each "number" is assigned a color

You can hand-pick a color for every "number" to create a static color scheme.

![Green icon button in the UI, assigned a hand-picked color using a color picker](../../../_assets/m4mxjwiz-2-8dbbd7d901433d3aec34.png)

Static colors are hand-picked, like this green icon button

But now, you can also use Material's dynamic color system to automatically generate an entire palette of accessible colors for each "number" from a single source.

This source can be a user's wallpaper, or in-app content like imagery. If the source changes, the product colors update to match.

![Image showcasing how a source color is automatically applied to each "number"](../../../_assets/m4mxk5mu-3-167bb096a331764fed91.png)

Colors are generated dynamically from a user's wallpaper or in-app content

You can customize how dynamic color appears in your product by:

-   Setting the color source
-   Adding static or harmonized colors
-   Changing which "numbers" are assigned to which elements

[Learn about advanced customizations](/m3/pages/advanced/define-new-colors)

![Image showing a color wheel where a light red color is picked, which then populates the UI. In this example, some UI elements have been mapped to different "numbers"](../../../_assets/m4mxkasm-4-68bbd0744d97f3075bf2.png)

The color source can be changed, automatically changing the color scheme. The UI elements can have other "numbers" assigned to them.

## Essential terms

### Color role 

Like the "numbers" on a paint-by-number canvas, color roles are assigned to specific UI elements. They have semantic names like **primary**, **on primary**, and **primary container,** and matching color tokens. [See all color roles](/m3/pages/color-roles)

### Dynamic color

Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI. If the user's wallpaper or the in-app content changes, the colors in the UI will change to match.

### Static color

UI colors that don't change based on the user's wallpaper or in-app content. Static colors can be hand-picked or generated in design tools like the Material Theme Builder Material Theme Builder (MTB) is a Figma plugin that allows markers to emulate the color extraction process for dynamic color and create custom tonal schemes. [Material Theme Builder](https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder) . Once assigned to their respective color roles and UX elements, the colors remain constant.

#### **Baseline static color**

The default static color scheme for Material products. [See the baseline color scheme](/m3/pages/static/)

![Diagram illustrating the steps from source color to key colors to tonal palettes to color roles to the UI](../../../_assets/ln9uzzb5-from-source-color-to-UI-73d129769a1ca2700157.png)

The dynamic color process is automatic. A single source color is used to generate five key colors, which are used to make tonal palettes. Tones from the palettes are then assigned to color roles, which are in turn assigned to elements of the UI.

The system generates dynamic color schemes using colors from images like wallpapers and in-app content

## How dynamic color generates color schemes

### 1\. It starts with a source color

There are three ways to get a source color.

#### **A. Generate it from a wallpaper**

User-generated color is sourced from a user's personal wallpaper. The wallpaper is digitally analyzed through a process called quantization, and a single color is selected as the source color.

![Red source color is extracted from a wallpaper](../../../_assets/ln9v1jfc-wallpaper-source-color-27de3802c264ddd641ee.png)

Source color from a user's wallpaper

#### **B. Generate it from in-app content**

Content-based color is sources from in-app content, like an album thumbnail image, logo, or video preview. 

Like user-generated color, the image is digitally analyzed through quantization, and a single color selected as the source color.

![Blue source color is extracted from an podcast cover](../../../_assets/ln9v2356-in-app-content-d52656736d89f5a0adf1.png)

Source color from in-app-content

#### **C. Pick it by hand**

A hand-picked source color is deliberately selected by a designer.

**Did you know?** The baseline static color scheme Baseline is the default static color scheme for Material products. It includes colors for both light and dark themes. [More on baseline color](/m3/pages/static/) uses a hand-picked source color.

![Green source color selected from a color picker](../../../_assets/ln9v32x5-hand-picked-color-63b8a11144cd03f7bcf5.png)

Source color hand-picked by a designer 

### 2\. Feed the source color into an algorithm

Dynamic color is powered by the [Material Color Utilities](https://github.com/material-foundation/material-color-utilities) (MCU), a set of color libraries containing algorithms and utilities that develop color themes and schemes in your app.

There are many color algorithms, but the most common ones are:

-   **User-generated color algorithm
    **Uses personal wallpaper to identify source color. Maps colors of specific tones (lighter or darker) into the scheme according to a combination of system design choices and user preferences.

-   **Content-based color algorithm**
    Uses image for source color. Tones are adjusted to match the appearance of the source image, while maintaining accessible contrast. 

-   **Custom colors** 
    Colors closely match the chosen input colors, such as those representing brand or semantic meaning.

![Color palette made by the user-generated algorithm](../../../_assets/ln9v56si-content-vs-user-left-user-ae37fc069fb57246bee3.png)

1\. When run through the **user-generated color** algorithm, the source color is turned into a full color scheme

![Color palette made by the content-based algorithm](../../../_assets/ln9v5j63-content-vs-user-right-content-89135bced30cc2732157.png)

2\. When run through **content-based color** algorithm, the same source color creates a slightly different color scheme. Some tones are adjusted to better match the appearance of the source image.

![Color palette made by the custom color algorithm](../../../_assets/lnc8pq3o-content-vs-user-right-content-2416468f086752bc1b47.png)

3\. Custom colors, such as brand colors, can individually run through the algorithm to create a custom scheme that matches the brand

### 3\. The algorithm generates key colors

Material's color algorithms manipulate the source color's hue Hue is the perception of a color as red, orange, yellow, green, blue, violet, and so on. [More on hue, chrome, and tone](/m3/pages/color/how-the-system-works#395813c8-b314-48d1-bb55-266f421eb3a4) and chroma Chroma is how colorful or neutral (grey, black or white) a color appears. [More on hue, chrome, and tone](/m3/pages/color/how-the-system-works#395813c8-b314-48d1-bb55-266f421eb3a4) to generate **five complimentary key colors**.

1.  Primary
2.  Secondary
3.  Tertiary
4.  Neutral
5.  Neutral variant

![Diagram of a source color generating five key colors: primary, secondary, tertiary, neutral and neutral variant](../../../_assets/ln9w1sps-from-source-color-to-key-colors-c098290dd985c0fcb431.png)

A source color generates five key colors

### 4\. The algorithm creates tonal palettes

The system then manipulates tone Tone is how light or dark a color appears. Tone is sometimes also referred to as luminance. [More on hue, chroma, and tone](/m3/pages/color/how-the-system-works#dc7848f3-b094-4f9a-9e50-bfa5a5029617) and chroma Chroma is how colorful or neutral (grey, black or white) a color appears. [More on hue, chroma, and tone](/m3/pages/color/how-the-system-works#e4d1c787-e92f-4d6e-a757-cd6d5c3b298e) values to create a **tonal palette** for each key color. Colors in these palettes are given a number from 0 to 100 in increments of 10, as well as 95, 98, and 99. Some palettes include more values.

![Primary, secondary, tertiary, neutral and neutral variant tonal palettes, consisting of 13 tonal steps](../../../_assets/m612xcmj-13-f520d4aa3a9e20c85d03.png)

The smaller the tonal value, the darker the color

### 5\. The algorithm assigns tones to color roles

The algorithm uses accessible color relationships For example, a dark surface color is algorithmically paired with a light text label color so the UI automatically meets contrast requirements. [More on color relationships](/m3/pages/color/how-the-system-works#e1e92a3b-8702-46b6-8132-58321aa600bd) to **assign specific tones to the 26**  **color roles Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme. [More on color roles](/m3/pages/color-roles)** in both light and dark theme.

For example, the algorithm assigns the color tone primary40 to the **p****rimary** role and the tone primary100 to the **o****n primary** role.

[See all color roles](/m3/pages/color-roles)

![Diagram mapping color tones to roles](../../../_assets/m612xkza-14-5b46a2786df5a1e41462.png)

Tones from the tonal palette are assigned to different roles

![Diagram of tonal palettes mapped to all color roles across light and dark themes](../../../_assets/m612xrj4-15-e02c615731125977eaca.png)

Colors from the five tonal palettes are assigned to color roles. For example, primary roles are picked from the primary tonal palette, while surface roles are picked from the neutral tonal palette.

Dark theme A dark theme is a low-light version of a UI that displays mostly dark surfaces. colors are also automatically assigned so that apps receive both light and dark themes through a single set of color roles.

![Diagram of dark theme colors](../../../_assets/lnem28e4-color-roles-dark-theme-99398974478c1d04799e.png)

The same color roles are used in light and dark themes

### 6\. The new colors are applied to the UI

The 26 standard color roles are already assigned to elements of the UI. When a new source color is picked, the UI dynamically changes color.

![Diagram of all the color roles with an example of how it would look applied to a UI](../../../_assets/lna5nn2o-color-roles-UI-elements-4053b80ffaf315c352b8.png)

Color roles assigned to the UI

## Color roles support three levels of contrast

In addition to light and dark theme, color roles also support three levels of contrast. This helps people select the contrast setting that best suits their vision needs:

-   Standard (default)
-   Medium
-   High

The standard contrast emphasizes visual hierarchy using high and low contrast elements. People with vision disabilities may choose medium or high contrast options for better support.

![Email app in standard contrast.](../../../_assets/mrwa95yk-18-07caec7252c1789de665.png)

**Standard contrast**

The baseline color scheme already uses mixed levels of contrast to reduce cognitive load

![Email app in medium contrast.](../../../_assets/mrwa99t2-19-5027d4c359b8147a24ef.png)

**Medium contrast**

Provides a minimum contrast ratio of 3:1 for those who need more contrast, but may experience visual discomfort with higher contrasts from effects like halation.

![Email app in high contrast.](../../../_assets/mrwa9f4u-20-85c386886f0f3d6819f7.png)

**High contrast**

Further emphasizes essential elements with a 7:1 contrast ratio to reduce visual distractions and enable users to focus. For example, high contrast is applied to the content in a card but not the card container.

The contrast settings are automatically applied to both light and dark themes. 

![The same mail app at three contrast levels, all in light theme.](../../../_assets/mrwa9ldv-21-2cc7ba08a7b07f573f0c.png)

Light theme

![The same mail app at three contrast levels, all in dark theme.](../../../_assets/mrwa9q8s-22-1965a58efa653d21d754.png)

Dark theme

Custom components can support contrast levels by using Material's appropriate color roles Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme. [More on color roles](/m3/pages/color-roles) . For example, use **primary container** and **on primary container**.

Use design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on design tokens](/m3/pages/design-tokens/overview) to apply color roles to custom components.

![Custom volume slider component using Primary Container and On Primary Container roles, whose colors change automatically at standard contrast.](../../../_assets/lna5s0mi-user-controlled-contrast_12-651f20a146f445d2ee92.png)

A custom volume slider can use **p****rimary container** and **on primary container** color roles to support contrast levels

![Custom volume slider component using Primary Container and On Primary Container roles, whose colors change automatically at standard contrast.](../../../_assets/lna5shuk-user-controlled-contrast_13-bfb0f09eddbe74c5cdc4.png)

At medium and other contrast levels, those color roles apply the necessary new color values

## Pairing accessible tones

The system manipulates hue, chroma, and tone ( HCT) values HCT is a color space which defines all colors by assigning number values for three dimensions: hue, chroma, and tone. [More on hue, chroma, and tone](/m3/pages/color/how-the-system-works#395813c8-b314-48d1-bb55-266f421eb3a4) to **create a tonal palette for each color** with tones ranging from 0 to 100.

Color has physical limitations—whether it's actual physics, our own biological visual limitations, or the limitations of on-screen color rendering. For example, some hues cannot exist with certain chroma or tones. Color limitations are the reason colors such as bright light blue or bright light red are not quite possible. This is why the chroma value may increase or decrease for some tones in a tonal palette.

![13 tones derived from a key color. ](../../../_assets/m612y8rt-25-492f05e6d74f857e4c82.png)

Tonal values range from 0 (black) to 100 (white). The smaller the tonal value, the darker the color.

Material's color algorithms use these palettes to find and **pair contrasting tones,** creating accessible color combinations.

Because tone can describe the lightness or darkness of a color, it's used to define accessible color relationships. Those relationships are built into Material's color algorithms.

For example, the algorithms assign a dark tone to a button's container color and a light tone to its label color, ensuring that the colors have a 3:1 contrast.

![Colors of tones 50 and 98 used for button fill color and background fill color, which create a contrast greater than 3:1 between a button and its background.](../../../_assets/m612yd3c-26-03682d346d988c82a76f.png)

Using tones 50 and 98 for a button and its label creates an accessible 3:1 contrast

For even more contrast, the algorithms assign tones even farther apart, achieving a 7:1 contrast.

This is the concept powering **user-controlled contrast** features.

![Colors of tones 30 and 98 used for button fill color and background fill color, which create a contrast greater than 7:1 between a button and its background.](../../../_assets/m6134eza-27-9e119638c170453b9de9.png)

Using colors of tones 30 and 98 for a button and its label create a 7:1 contrast

## Defining colors with hue, chroma, and tone (HCT)

**The system uses a color space called HCT**, which defines all colors using three dimensions: hue, chroma, and tone.

Changing HCT values lets you manipulate colors in flexible but predictable ways. Unlike other color spaces (like HSL or RGB), HCT allows the manipulation of a color's hue and chroma without affecting its tone. Watch to learn more:

Hue, chroma, and tone are the three color dimensions used to create accessible color schemes

### Hue

Hue is the perception of a color as red, orange, yellow, green, blue, violet, and so on. Hue is quantified by a number ranging from 0-360 and is a circular spectrum (values 0 and 360 are the same hue).

![The hue spectrum looks like a rainbow circle.](../../../_assets/lna5w3u0-hue-0cde0cf03ad12c562a1d.png)

360 degree **hue** spectrum

### Chroma

Chroma is how colorful or neutral (grey, black or white) a color appears. Chroma is quantified by a number ranging from 0 (completely grey, black or white) to infinity (most vibrant), though Chroma values in HCT top out at roughly 120.

Because of biological and screen rendering limitations, different hues and different tones will have different maximal chroma values.

![Diagram showing chroma range from 120 (maximum intensity) to 0 (pure grey). A second diagram shows how pure black and pure white also correspond to 0 chroma](../../../_assets/lna5x1is-chroma-028da004c7f3f08bcca3.png)

1.  The higher the color purity, the higher the **chroma**
2.  Note how lightening and darkening a hue also affects its **chroma** value

### Tone

Tone is how light or dark a color appears. Tone is sometimes also referred to as luminance. Tone is quantified by a number ranging from 0 (pure black, no luminance) to 100 (pure white, complete luminance).

Tone is crucial for visual accessibility because it determines contrast. Colors with a greater difference in tone create higher contrast, while those with a smaller difference create lower contrast.

![Gradient showing the range of tones from 1 (black) to 100 (white)](../../../_assets/lna5xncz-tone-886397a15276df4ad35d.png)

The 100 **tone** is always 100% white, the lightest **tone** in the range; the 0 **tone** is 100% black, the darkest **tone** in the range

### HCT isn't interchangeable with other color spaces

Values from models like hue, saturation, and lightness (HSL) won't perfectly map to Material's hue, chroma, and tone (HCT). Don’t conflate color spaces when inspecting or adjusting colors.

For example, colors with the same perceived brightness share the same tone value in HCT, but can have different HSL lightness values.

![3 color dots with the same HCT tone of 78, and varying HSL lightness values of 83, 65, and 77.](../../../_assets/mrwafnpo-31-26c2291a04f54056ad9f.png)

HCT tone values remain constant when they have the same perceived brightness, while HSL lightness values can vary
