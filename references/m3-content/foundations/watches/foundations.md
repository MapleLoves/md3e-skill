---
source: https://m3.material.io/foundations/watches/foundations
title: "Design for watches"
captured: 2026-09-14
---

# Design for watches

> Watches have special design considerations and interaction patterns

## Resources

| Type | Resource |
| --- | --- |
| Design | [Get Started with M3 Expressive](https://m3.material.io/get-started) |
| [UI Design for Wear OS](https://developer.android.com/design/ui/wear/guides/get-started/design-for-wearables) |
| [Figma Design Kits for Wear OS](https://developer.android.com/design/ui/wear/guides/get-started/design-kits) |
| Implementation | [Android Developers: Wear OS](https://developer.android.com/training/wearables) |
| [Jetpack Compose for Wear OS](https://developer.android.com/training/wearables/compose?version=3) |

## Anatomy

### The watch face

Watch faces display the time, as well as  other information and can provide access to other functions through apps and tiles.

They can also include complications, self-contained details that can show contextual info like heart rate or progress.

Ongoing activities on the watch face show in-progress actions, like a stopwatch countdown or a workout timer.

![A watch face with hands showing analog time readout, and complications showing the date in a calendar, heart rate, water consumption, and weather.](../../_assets/mp4b8pnm-01-8992fbd8dc10563c4c5f.png)

**Complications** are details on the watch face that can be customized for style or function

![A watch face with an entry point for an ongoing exercise activity.](../../_assets/mp4b9kvw-02-56edcae62ad4b7f5f2c7.png)

**1\. Ongoing activities**, like timers, media players, or workouts, can be accessed from the watch face

### Physical buttons

Wearable devices can have a variety input surfaces, which include physical buttons and controls.

![3 watch faces with indications showing the locations of a rotating side button, system button, and multifuction button.](../../_assets/mp4bb056-04-6386674f6c4993c70465.png)

1.  Rotating side buttons: Used for volume control, or to scroll through options or lists

2.  System buttons: Dedicated to OS functions like powering on and off, and cannot be customized

3.  Multifunction buttons: Used by apps for custom actions like starting and stopping a stopwatch

## Design principles

-   Tailor layouts for different screen sizes with [adaptive design](https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design)

-   Design for short interactions to conserve battery

-   Focus on one or two tasks at a time rather than a full app experience

-   Test designs in situations that involve movement to make sure the design is usable at a glance

![Calendar screen with date, time of dentist appointment, and more button.](../../_assets/mp4bcxbd-05-do-6244f4df7eb37fea1a3a.png)

check Do

At-a-glance views allow people to quickly see calendar events

![3 columns with times, dates, and appointment names cut off.](../../_assets/mp4bdrul-06-dont-a0dc1ceea056ba2930d9.png)

close Don’t

Don't create complex and detailed apps such as a calendar grid

### Always relevant

Watches are always with people. Consider how to update app content based on context, such as time, place, and activity.

![A map search for a garden’s location on a watch and on a phone.](../../_assets/mp4befpv-07-28e35ef7ae2d6753ae1f.png)

Navigation on a watch complements the experience on a phone

### Works offline

Design for slow connections and offline use, such as exercising and commuting.

![2 watches: 1 with offline music downloads list. 1 with a dialog about no internet connection with dismiss and accept buttons.](../../_assets/mp4bf7c4-08-cad3ba070b2cc64b08b5.png)

The network state can be communicated through:

1.  An offline icon

2.  A dialog

## Interaction patterns

### Cross-device experiences

Watches are often dependent on connected phones for functionality or complex interactions. In some cases, a watch and a phone are used together to accomplish different parts of the same task.

Consider how experiences can be consistent and complement the strengths of each device.

[More on multidevice development for Android](https://developer.android.com/multi-device-development)

![A contact entry shown on a phone and a watch, with options to call or message.](../../_assets/mp4bg988-09-do-8f9ba97d2cdc73169364.png)

check Do

Consider which actions are appropriate for each device

### Always on displays

Watches can have always on displays, which allow ambient content to be shown when the watch isn’t in use.

This are especially helpful for ongoing experiences like a timer or a workout that should remain in view. Because they remain on the screen for long time periods, consider limiting the number of pixels that are illuminated.

[More on always-on apps and system ambient mode in Wear OS](https://developer.android.com/training/wearables/always-on)

![A watch face showing progress through a task and the current time.](../../_assets/mp4bgxlg-10-d60dc494750d2a313f12.png)

Limit the number of illuminated pixels for a display that's always on
