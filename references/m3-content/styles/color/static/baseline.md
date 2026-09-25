---
source: https://m3.material.io/styles/color/static/baseline
title: "Static color schemes"
captured: 2026-09-14
---

# Static color schemes

> Static color schemes are ideal for branded products that should have a consistent, uniform design

**Baseline** is the default static color scheme. It uses accessible color pairings and includes colors for both light and dark themes.

**With the baseline color scheme, end-users see**

-   An accessible UI with static colors 

![Mobile screenshot of music app.](../../../_assets/6Qlfeo75opgKmNSYcxRy92aHk4VOLoQrE4VFYmSSfElw9CrWNI12sziVlF4ZPyEjADYSrfLICk2zmSSw-928cc120c467ab5c4729.png)

Music app with the static baseline color scheme

![Tablet screenshot of a news app.](../../../_assets/8Vtp4zasYWpnr556HQJFq60r0jwZw9541OZ7JtkFYG0Ol4LmRidQA_ABD2bMWZCYPodMyV3LvVF8Fsq7-647271fd0b7812f0b6c8.png)

News app with the static baseline color scheme

## Baseline colors

Get baseline colors in Figma using the Material Theme Builder Material Theme Builder (MTB) is a Figma plugin that allows markers to emulate the color extraction process for dynamic color and create custom tonal schemes. [Get the MTB](https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder) .

![Color swatches showing the entire baseline color scheme and derivative accent colors.](../../../_assets/rfxJv95pIoJ3cEZ9ypfimJFC5Ps8sEEVBNWD36C-fy3DYvec8J_VLRosBkwTNsnpSCgSpxWXBypOXT8Y-b531dba67d426d3226a7.png)

Baseline scheme colors in light theme

![Color swatches showing the entire baseline color scheme and derivative accent colors.](../../../_assets/S-tgf061eUWcbEBhyicTYR9PWVDeXSsSgZ2e2yYSr6Jn4W-F9z5czZCG6sv58wgJQODQakVRBDvUX5ga-b7c283776ceef278ecb3.png)![Color swatches showing the entire baseline color scheme and derivative accent colors.](../../../_assets/S-tgf061eUWcbEBhyicTYR9PWVDeXSsSgZ2e2yYSr6Jn4W-F9z5czZCG6sv58wgJQODQakVRBDvUX5ga-950a003ca2f607fec363.png)

Baseline scheme colors in dark theme

## Baseline color tokens

Close

## Design with baseline

### Use the Design Kit and M3 baseline colors in new design files

1.  Create your Figma file. Enable the [M3 Design Kit](https://www.figma.com/community/file/1035203688168086460) in your Assets panel.

2.  Compose screens and layouts using Material Components from the design kit

3.  Apply M3 baseline color roles to custom components and UI elements by hovering on the element's color property in the Design panel on the right of the screen and selecting the **Style** icon (four dots). This opens a selection dialog.

4.  Search for "M3" to see the baseline color roles

5.  Select the baseline color role that most closely matches the use case and intent (see [Color roles](/m3/pages/color-roles) for more information on what color to use where)

6.  Repeat until all custom elements are using M3 baseline color roles

### Apply baseline colors to an existing file

**First, get the M3 baseline colors into your file**

1.  Open your Figma design file. Select the **Actions** menu (or Ctrl/Command+K).

2.  Find the [Material Theme Builder plugin](https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder) and select **Run**. This will open a plugin dialog showing the default color scheme, including Core colors and Extended colors.

3.  Open the plugin's **Settings** (gear icon at lower right of dialog) and select the checkbox for **Generate State Layers**. This makes sure there are color for the state layers needed to design interactions. [Learn more about state layers](/m3/pages/interaction-states/state-layers)

4.  Navigate out of settings.

5.  With the Current Theme dropdown at the top of the dialog, select **Baseline.**

6.  Select the frames or components in your file and then hit **Swap** in the bottom right of the dialog. This will automatically update the colors for any M3 Design Kit components.

**Then, update any remaining non-M3 color styles**

1.  Manually change any hex values or non-M3 color styles by selecting all and looking through the Selection colors in the Design panel on the right of the screen.

2.  Any colors that don't start with "M3" need to be replaced with a corresponding baseline color.

3.  Hover on a non-M3 color row in the Design panel and select the **Style** icon (four dots). This opens a selection dialog.

4.  Search for "M3" to see the baseline color roles.

5.  Select the baseline color role that most closely matches that color's use case (see [Color roles](/m3/pages/color-roles) for more information on what color to use where) and select **Use style** to apply it to the selected objects.

6.  Repeat until all non-M3 colors in the file have been replaced with M3 baseline color roles.

**Need to make adjustments to the scheme? Check out** [**Advanced customizations**](/m3/pages/advanced/overview)
