---
source: https://m3.material.io/components/side-sheets/accessibility
title: "Side sheets"
captured: 2026-09-14
---

# Side sheets

> Side sheets show secondary content anchored to the side of the screen

## Use cases

People should be able to dismiss the side sheet using assistive technology.

## Interaction & style

Material requires that a close affordance, such as a close icon button Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview) , is always present within a side sheet.

![Side sheet correctly designed with close icon in upper right corner.](../../_assets/0LSf0hnC19HAyDDf88fqzUUo62971bFb2XWjHguURc3jJbZpy8ejGuIyFR-2MSFM27gLA3LjupVjSj8E-34406766bace73c1559f.png)![Side sheet correctly designed with close icon in upper right corner.](../../_assets/0LSf0hnC19HAyDDf88fqzUUo62971bFb2XWjHguURc3jJbZpy8ejGuIyFR-2MSFM27gLA3LjupVjSj8E-bc7b8ae1c916323322c3.png)

check DoA close icon button makes the side sheet easy to dismiss 

![Side sheet incorrectly designed with no close icon button.](../../_assets/bGugN52A6j4bvI4smHp21cQzZbZv4qaF9YBYdKZDD51XL6yAkHSY_KVtpUF7HkL6G04T2w61MQeJo-E8-2a5b8e3c07ffb715045c.png)![Side sheet incorrectly designed with no close icon button.](../../_assets/bGugN52A6j4bvI4smHp21cQzZbZv4qaF9YBYdKZDD51XL6yAkHSY_KVtpUF7HkL6G04T2w61MQeJo-E8-c51e66b1af30954855bf.png)

close Don’t

Without a close icon button, people can’t predict the opening and closing flow of side sheets, or know if the sheet is transient or permanent

## Initial focus

Actions within a side sheet can be focused A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice. [More on focused state](/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f) by tab order using a keyboard or switch control.

![Side sheet diagram showing the focus order of headline, close, save, cancel.](../../_assets/MuS9aCeC3P_ukbbopUpL7M9rV8VhBbirg3UofV-_SA7g-v4ABLSE8zgMWQOlHo7WP5XEd7s-KyR15aPB-0ce88b4f0c06b366425d.png)![Side sheet diagram showing the focus order of headline, close, save, cancel.](../../_assets/MuS9aCeC3P_ukbbopUpL7M9rV8VhBbirg3UofV-_SA7g-v4ABLSE8zgMWQOlHo7WP5XEd7s-KyR15aPB-7e21f1ddcfb957c331df.png)

Visible focus shown on the available actions within a side sheet:

1.  Headline
2.  Close
3.  Cancel
4.  Save

## Keyboard navigation

| Keys | Actions |
| --- | --- |
| **Tab** | Focus lands on (non-disabled) icon button |
| **Space** or **Enter** | Activates the (non-disabled) icon button |

## Labeling

The accessibility role for a side sheet is **Dialog**.

![Side sheet showing the accessibility role as dialog.](../../_assets/ogti7RlWzhZNIER0PGHxR2hM--wMncqBhexq_aLUiY6OPM1C5NeuaWV29SOOqi5gjdr7dGbCFrlPMnQ2-e49115430c1ef0fc65d1.png)

The role for side sheets is **Dialog**
