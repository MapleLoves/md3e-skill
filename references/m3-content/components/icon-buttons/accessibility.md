---
source: https://m3.material.io/components/icon-buttons/accessibility
title: "Icon buttons"
captured: 2026-09-14
---

# Icon buttons

> Icon buttons help people take actions with a single tap

## Use cases

People should be able to do the following using assistive technology:

-   Understand meaning of the icon
-   Navigate to and activate an icon button
-   When applicable, a tooltip should be available to help describe the icon button's purpose

## Interaction & style

Ensure the icon has contrast of at least 3:1 with the surface or background.

![Icon button with correct contrast ratio.](../../_assets/sxEm_qQA7j39jtqbpiH6Lnec5G_ZIJs-b8cWfSYYldZIAEjGTT52yeEfaF8M1HLTZCe0_0zqKfBBPGW9-42bcdf78c58ebe5f6962.png)

check Do

Icon buttons should have a 3:1 contrast ratio with the surface or background

![Icon button with insufficient contrast ratio.](../../_assets/FqCMh3l6_zJ396vQUK3U2--BcmNuXzVzQHPsd2a9kOXz6CjN4pE_mugSVMkSsZep6dHnnmhA-1_JIyca-c8e12ba8e4964c943582.png)

close Don’t

Avoid using colors with contrast below 3:1

## Keyboard navigation

| **Keys** | **Actions** |
| --- | --- |
| Tab | Focus lands on (non-disabled) icon button |
| Space or Enter | Activates the (non-disabled) icon button |

## Labeling elements

The accessibility label for icon buttons describes the action the button is executing, such as **Add to favorites**, **Bookmark**, or **Send message**.

![Icon button label and role.](../../_assets/Veran4xIuwOjaUK-TME0CkyE4D03sjgbC1O1fGyyeie01_pz6s0p7PoibSPSPzTNT7bmFKJy4kG40AnF-45043e7612bfcdea6d2d.png)

The icon button label describes the action, such as Add to favorites for the heart icon

## Layout & density

Groups of similar components can be nested together inside a component, or they can stand alone.

The target size of each icon button should be at least 48dp, even when nested.

![Icon buttons with 48dp target sizes.](../../_assets/m0c1h7ba-4-34d5520d50adfd746d97.png)

Icon buttons can be used within other components, such as an app bar

### Avoid applying density by default

Don't apply density to icon buttons by default. This lowers their targets below the required 48x48 CSS pixels minimum size. 

Provide density options that allow people to choose a higher density, such as selecting a denser layout or changing the theme. Controls for adjusting density must maintain a target size of at least 48x48 CSS pixels.

## Hover

On web, icon buttons should display a tooltip with an accessibility label.

![“Heart” icon with "Add to favorites" tooltip on hover.](../../_assets/m0c1j2b9-5-506180e221e49b7fe70e.png)

The tooltip label text should be clear and concise
