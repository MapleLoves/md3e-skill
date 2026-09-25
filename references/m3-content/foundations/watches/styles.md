---
source: https://m3.material.io/foundations/watches/styles
title: "Design for watches"
captured: 2026-09-14
---

# Design for watches

> Watches have special design considerations and interaction patterns

## Resources

| Type | Resource |
| --- | --- |
| Design | [M3 Expressive on Wear OS](https://developer.android.com/design/ui/wear/guides/get-started) |
| [Typography for Wear OS](https://developer.android.com/design/ui/wear/guides/styles/typography) |
| [Color for Wear OS](https://developer.android.com/design/ui/wear/guides/styles/color) |
| [Motion for Wear OS](https://developer.android.com/design/ui/wear/guides/get-started/apply#shape-motion) |
| Implementation | [Android Developers: Wear OS](https://developer.android.com/training/wearables) |
| [Jetpack Compose for Wear OS](https://developer.android.com/training/wearables/compose?version=3) |

## Typography

GM3 Expressive adds two type styles specially designed for watches. [More on the type scale for Wear OS](https://developer.android.com/design/ui/wear/guides/styles/typography/type-scale-tokens)

### Numerals

Numeral text styles display numbers, usually only a few digits at a time. This text can take on more expressive properties at larger display sizes without the accommodations usually required by text that must be localized.

![A watch face with an indication for the numeral text style used to show the time.](../../_assets/mp4bxhlf-22-c0f9c2102f66ea7eea6e.png)

1.  Numeral Large

### Arc text

Arc text is specially designed for text following a curved path on a round screen, such as page titles, confirmation overlays, or a call to action. It optimizes character spacing for text displayed along a curve at the top or bottom of a round screen.

![A close-up of a watch face with arc text showing “check your phone” hugging the bottom bevel of a round screen.](../../_assets/mp4byceo-23-5ba545927e860316f362.png)

1.  Arc Large

## Color

Material for Wear OS provides a custom [color system](https://developer.android.com/design/ui/wear/guides/styles/color/system) to create vibrant experiences and clear visual hierarchy.

### Build from black

Watches are designed with a black background, instead of the tinted background that phones use.

![2 watch screens showing sleeping app and a number picker.](../../_assets/mp4bz1nw-1-958d9e390c652b75b1ef.png)

Watches use a black background to conserve battery

### Color roles

Since watches are used throughout the day, color tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) for Wear OS are specifically tailored for dark themes in low-light environments and light themes for daylight environments.

[More on color roles for Wear OS](https://developer.android.com/design/ui/wear/guides/styles/color/roles-tokens)

![3 examples of “Accept” and “Decline” buttons that are legible.](../../_assets/mp4bzy9c-21-96bdd4ed4538273fb2a4.png)

check Do

Buttons with (2) **on primary** on (1) **primary** and (4) **on** **primary container** on (3) **primary container** stay legible as the contrast level changes

![Buttons with (2) primary dim on (1) primary or (4) primary dim on (3) primary container become illegible as contrast levels shift](../../_assets/mp4c1f7y-22-87a67962bb588a73a61b.png)

close Don’t

Buttons with (2) **primary dim** on (1) **primary** or (4) **primary dim** on (3) **primary container** become illegible as contrast levels shift

### Recommended color combinations for Wear OS

Below are some common color pairings that can help establish priority, function, and elevation.

-   Use **primary dim** to highlight important elements and **tertiary** to provide standout feedback, such as tap responses

-   When the main action isn't clear, use **tertiary** and **primary** for main actions and **secondary container** for complementary actions

-   Use **secondary** and **primary container** to show two equally important options or containers, while maintaining contrast

![Three buttons, with the center one in Primary and side ones in Primary Dim. ](../../_assets/mp4c3ekq-23-b314e0754cef4ed1831e.png)

1.  Primary

2.  Primary dim

![ A number pad with most keys in Primary Dim and the pressed key in Tertiary. ](../../_assets/mp4c4fsb-24-b893f4e53772bec8aff3.png)

1.  Primary dim

2.  Tertiary

![Call button in tertiary color, open button in primary color and open on phone button in secondary-container.](../../_assets/mp4c72hg-28-fa005f9d0df5631a37c0.png)

1.  Tertiary

2.  Primary

3.  Secondary container

![accept button in primary and delete button in primary container.](../../_assets/mp4c6oau-30-5026900648f1c8731c65.png)

1.  Primary

2.  Tertiary

3.  Primary container

![Plus button in primary color, date button is in tertiary color and appointment summary is in primary container color.](../../_assets/mp4cam7e-27-6b354aad495297ec9cac.png)

1.  Primary dim

2.  Tertiary dim

![Bicycle button in primary, weight button in tertiary dim.](../../_assets/mp4c7zvn-31-3fe3e3de36ae4b7554eb.png)

1.  Primary

2.  Tertiary dim

## Motion and transitions

Expressive motion makes interactions feel more alive, fluid, and natural. Use transitions give intuitive feedback to show how an app works, such as standard patterns for changes in state or hierarchy.

[More on shape and motion for Wear OS](https://developer.android.com/design/ui/wear/guides/get-started/apply#shape-motion)

Use expressive motion to show items selected

## Haptics

Haptics are tactile effects used to grab a person’s attention for something important, or add emphasis to an interaction on the screen. You can use haptics to provide responsive feedback to scrolling and selecting items from a list, or controlling volume.

Use system-defined patterns and tokens (when available) to reinforce interaction expectations. Synchronize haptics with UI motion and sound to provide richer feedback.

-   Use stronger haptics for key interactions, such as a payment confirmation

-   Use subtler haptics for precision interactions, such as scrolling through a list

[More on haptics for Wear OS](https://developer.android.com/develop/ui/views/haptics/haptics-principles)

![2 watch faces with lines indicating haptics for a payment being accepted and scrolling through notifications.](../../_assets/mp4c8vp7-x-28ef84515132ff6bd653.png)

Use stronger haptics for key interactions and subtler feedback for precision interactions
