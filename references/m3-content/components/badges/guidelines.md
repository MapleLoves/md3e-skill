---
source: https://m3.material.io/components/badges/guidelines
title: "Badges"
captured: 2026-09-14
---

# Badges

> Badges show notifications, counts, or status information on navigation items and icons

![Diagram of 4 badges in different configurations on a navigation bar's destination icons.](../../_assets/mg0wmkr4-01-53dc135c6979ed884781.png)

Large badges and a small badge in a navigation bar

## Usage

Badges are used to indicate a notification, item count, or other information relating to a navigation destination. They are placed on the ending edge of icons, typically within other components.

There are two variants:

1.  Small badge

2.  Large badge

![Diagram of 4 badges in different configurations on a navigation bar's destination icons.](../../_assets/mg0wmphl-02-d9e0a301761229878e0c.png)

Navigation bar with four badges

A **small badge** is a simple circle, used to indicate an unread notification.  

A **large badge** contains label text communicating item count information.

![A small badge is a circle with no characters.](../../_assets/Xnibw8kAnTzaV0TmLVU5oOfL5xZTO6E8gxqFFo843YlClRZ3TI3eTR7cGtDL76c7_3oQ6xVKU3l7NV0P-504c84cf1373ee7f9699.png)![A small badge is a circle with no characters.](../../_assets/Xnibw8kAnTzaV0TmLVU5oOfL5xZTO6E8gxqFFo843YlClRZ3TI3eTR7cGtDL76c7_3oQ6xVKU3l7NV0P-a76aeb523e23824920c7.png)

Small badge

![A large badge holds 4 characters and expands its container's width but not height.](../../_assets/UiES3FVbu4QTgh3y8L-WfQz6q2u2ao86ZpjIGDu6CxAIgDLxmu7zM-RC33uLQPuDaUJtgI1qqck8tM_b-dfd31be49116fcb6871b.png)![A large badge holds 4 characters and expands its container's width but not height.](../../_assets/UiES3FVbu4QTgh3y8L-WfQz6q2u2ao86ZpjIGDu6CxAIgDLxmu7zM-RC33uLQPuDaUJtgI1qqck8tM_b-39bdeef208b256e5d02b.png)

Large badge

### With other components

Badges are most commonly used within other components, such as navigation bar Navigation bars let people switch between UI views on smaller devices. [More on navigation bars](/m3/pages/navigation-bar/overview) , navigation rail Navigation rails let people switch between UI views on mid-sized devices. [More on navigation rails](/m3/pages/navigation-rail/overview) , app bars App bars display navigation, actions, and text at the top of a screen. [More on app bars](/m3/pages/app-bars/overview) , and tabs Tabs organize content across different screens and views. [More on tabs](/m3/pages/tabs/overview) .

![Navigation bar with 3 icon buttons. 2 icons buttons have badges and 1 doesn't.
](../../_assets/lvm8dp3k-5-f108f72d8c26cbff0393.png)

In navigation bars, hide the badge once the destination has been selected

## Anatomy

![Small and large badges on 2 icon buttons.](../../_assets/lvm8fkil-7-7682dc81a1e8f83a6bda.png)

1.  Small badge
2.  Large badge container
3.  Large badge label

## Container

There are two container options for the badge: 

-   Small badge Small badges are a simple circle used to indicate an unread notification. with no text

-   Large badge Large badges contain label text communicating item count information. with text

![A small badge on a navigation item.
](../../_assets/mg0womos-07-0a525ba9b3dd0c7c5734.png)

A small badge uses only shape to indicate a status change or new notification

![Number 10 displayed within large badge on a navigation item.](../../_assets/me8jybps-08-d1a9277f07f93c51dc33.png)

A large badge displays a number within a container to indicate a quantifiable status change related to a destination

Badge containers are anchored inside the icon bounding box. As the number count increases for large badges Large badges contain label text communicating item count information. , their width expands, but keeps the same placement.

Badges use a color intended to stand out against labels, icons, and navigation elements. Use the default color mapping to avoid color conflict issues.

![Small and large badges on the left side of 2 navigation items in a right-to-left language.](../../_assets/me8k2962-9-do-7560f8e1c00d96cdf202.png)

check Do

Change the position of the badge for right-to-left languages

![Small and large badges at random positions on 3 icon buttons on a navigation rail.](../../_assets/me8k2vet-10-dont-7dffa3adcb6c6501b58d.png)

close Don’t

Badges have fixed positions. Don’t change the position of the badge arbitrarily or place the badge over the icon.

![Small and large badges in default red color on 3 navigation items.](../../_assets/mg0wr0gz-11_do-9fa2d1ebc20a105e6f6f.png)

check Do

Use the default badge color

![Small and large badges in custom colors on 3 navigation items.](../../_assets/mg0wr4mw-12_dont-9ca9a02c154346014728.png)

close Don’t

Avoid using custom color roles for the badge container and label text. If custom roles are necessary, make sure they have contrast of at least 3:1.

### Label text

Label large badges Large badges contain label text communicating item count information. with counts or a status. The maximum number of characters within large badge label text is four, including a + to indicate more.

![4 icons with increasing number badges. The badges represent quantities, using a "+" symbol for quantities over 999.](../../_assets/me8ks60f-13-644f6f2c53f0facf95f3.png)

Large badges with one to four characters

Use the recommended maximum character count to ensure labels don’t extend beyond the badge container.

![4-digit numbers condensed to a 3-digit badge with "+" to fit the badge container's width.](../../_assets/mg0wrqi2-14_do-5e5ae536d3bf76349b0a.png)

check Do

Truncate badge labels as needed

![4-digit and 5-digit number badges on navigation items exceed the badge container's width and get cut off at the edge.](../../_assets/mg0wru4w-15_dont-e5eab57c98ff60e99bbf.png)

close Don’t

Don’t let the badge get cut off or collide with another element

## Placement

![Large badge to the right of a navigation rail item.](../../_assets/mg0wsl1o-16_do-8c4abddcb28818c62159.png)

check Do

Use a large badge to show count information when visual collisions aren’t an issue, such as in a navigation rail

![Small badge on an icon button in an app bar.](../../_assets/me8kxkle-17_caution-ae5a1b931b65c648eae2.png)

exclamation Caution

Use a small badge when spaces are tightly constrained, such as app bars. Small badges won’t run into the edge of the screen.

![Large badge placed at the end of a tab.](../../_assets/me8kyp7i-18_do-b9d30c453989f0206898.png)

check Do

When an icon with a badge is followed by text or another element, place a large badge at the trailing edge

![Large badge overlapping the icon and text in a tab.](../../_assets/me8kzbcm-19_dont-38faee1b3cdfe938a7ba.png)

close Don’t

Avoid using a large badge when it might overlap with a trailing element. Either place it at the trailing edge or use a small badge instead.
