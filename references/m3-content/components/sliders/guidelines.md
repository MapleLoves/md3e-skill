---
source: https://m3.material.io/components/sliders/guidelines
title: "Sliders"
captured: 2026-09-14
---

# Sliders

> Sliders allow users to make selections from a range of values

Sliders can adjust values in real time, such as image attributes

## Usage

Sliders are used to select values along a track. They’re ideal for adjusting settings such as volume and brightness, or changing the intensity of image filters.
Sliders can use icons or labels to represent a numeric or relative scale. 

![Sound settings screen with continuous sliders labeled call volume and alarm volume.](../../_assets/mabg8tbj-02-e11b1ef17fd5ff0d257a.png)

Use sliders to pick a value from a range, like volume loudness

Changes made with sliders must take effect immediately, so people can understand the effects of their selection as they're moving the slider.

Selection changes are immediate

There are three different variants of sliders: **standard**, **centered**, and **range:**

Standard sliders select one value from a range of values. Use this when the slider should start from zero or the beginning of a sequence.

![Horizontal standard slider with an end stop indicator.](../../_assets/m7lk01w5-04-c5315155e153d477b26f.png)

Horizontal standard slider

![Vertical standard slider  with an end stop indicator.](../../_assets/m7lk1j0t-05-1cfca454d06ac03267a3.png)

Vertical standard slider

Centered sliders select a value from a positive and negative value range. Use this when zero, or the default value, is in the middle of the range.

![Horizontal centered slider with a negative value and visible stop indicators at each end.](../../_assets/m7lk3lyv-06-11664060d5298b5ad27d.png)

Horizontal centered slider

![Vertical centered slider with a negative value and visible stop indicators at each end.](../../_assets/m7lk4tsn-07-c6637e756c356cca37a8.png)

Vertical centered slider

Range sliders select two values on one slider to create a range. Use this when defining a minimum and maximum value.

Avoid using range sliders vertically, as this can add too much cognitive load. People are used to most sliders being horizontal.

![Horizontal range selection slider with 2 values selected, and a stop indicator at each end.](../../_assets/m7lk6981-08-2257dd269168bb156d33.png)

check Do

Horizontal range slider

![Vertical range slider with 2 values selected, and a stop indicator at each end.](../../_assets/m7ln45vm-09---don-t-e8c810f9569a644638a5.png)

close Don’t

Because of the additional cognitive load of a range slider, avoid using it in vertical orientation.

## Anatomy

![6 elements of a slider.](../../_assets/m7m553sk-04-1-ae12298d12c3d9031d69.png)

1.  Value indicator (optional)
2.  Stop indicators (optional)
3.  Active track
4.  Handle
5.  Inactive track
6.  Inset icon (optional)

### Track

The track shows the full range of values that can be selected on the slider. It has two sections: active and inactive.

-   The **active** section of the track is from the minimum value to the handle. For range sliders, the active track is between the two handles.
-   The **inactive** section of the track is from the handle to the maximum value, or outside the two handles of a range slider.

For left-to-right (LTR) languages, the values increase from left to right. For right-to-left (RTL) languages, this is reversed.

![Sliders for font size and display size with stop indicators along the track.](../../_assets/m7lk9dsb-11-98fcb53569262d577c81.png)

The track on a slider shows the available range

### Handle

The handle can be moved along the track to choose a value.

When sliders have two handles, the handles choose the minimum and maximum values in a range.

The handle changes shape to indicate when it’s pressed.

![The handle is a vertical line on the current value of the slider. It shrinks in width when selected.](../../_assets/m7lkaurk-12-410e88c176fa5b011c88.png)

A handle changes shape when it's being pressed or dragged

![2 unselected handles on a slider with range selection.](../../_assets/m7lkbdhm-13-43dd7ea80d4bf5b7abf1.png)

Two handles are used for sliders with range selection

## Configurations

### Value

The value displays the specific value that corresponds with the handle’s placement. 

A value appears when interacting with the corresponding handle. For range sliders, only one value should be shown at a time.

If the value is shown elsewhere, the indicator is not required.

![A value of 50 is above a slider handle in the middle of the track.](../../_assets/lx1s2vu5-13-29e6da7912073c502822.png)

A value can appear while the handle is being pressed or dragged

![A value of 75 is above the pressed range slider handle. The unselected slider doesn’t show the value.](../../_assets/m7lkclo7-14-1aecbcb46ceb89b8ca29.png)

For range sliders, the value only appears on one handle at a time

Instead of showing the built-in value label, a separate text input field can be added outside of the slider. If this is added, the slider and value in this text field should automatically update to match each other.

Make sure people can tab to the text field directly after the slider.

Use **Tab** to navigate to values that are shown outside the slider, like a text input field

### Stop indicators

Stop indicators show which predetermined values can be chosen on the slider. The slider handle snaps to the closest stop. 

Avoid having too many stop indicators on a slider, because it can become visually crowded and difficult to adjust the value.

All sliders have stops at the end of the inactive track to ensure at least a 3:1 contrast with the background. If the inactive track has this level of contrast already, the end stops can be removed.

![Stop indicators are equally spaced out on a slider.](../../_assets/lx1s1ozg-10-8a6ac13c1deec0e4ea49.png)

Stop indicators show each available value on a slider

Icons or text can be added outside the slider to indicate the range of values and make the slider more accessible. This can be used instead of a stop indicator.

![Plus and minus icons on each end of the slider.](../../_assets/m7lkfou6-17-657de37f4f86a51c40d1.png)

Plus and minus icons, or text, can be added to the left and right of the slider

### Orientation

Sliders can be oriented either horizontally or vertically, depending on what is best for your use case.

![Horizontal slider.](../../_assets/m7lkhuu1-18-e2f40b9867c370c53f95.png)

Standard slider in horizontal orientation

![Vertical slider. Zero is at the bottom.](../../_assets/m7lkj1b8-19-e8e299ea03ffdbba93d0.png)

Standard slider in vertical orientation

### Inset icon

Standard sliders that are M, L, or XL can include an icon within the track. This icon should illustrate what the slider controls. Avoid adding inset icons to XS or S sliders.

When there’s not enough space for the icon on the active track, like at a low value, the icon moves to the inactive track.

Consider swapping which icon is displayed at zero, like a volume icon becoming a mute icon.

![Inset icon on the active track when the handle is at 50%, and on the inactive track when the handle is at 0.](../../_assets/m7lkmte8-20-ab08d4362b09b9bd16ce.png)

check Do

Inset icons change placement based on the handle

![An inset icon on an XS slider. The icon bounds are cut off by the slider container.](../../_assets/m7lni1k4-21---don-t-44dc4faaa4b86c123124.png)

close Don’t

Don’t use an inset icon with sliders that have track thicknesses under 40dp

Don’t use inset icons on centered or range sliders. It makes it unclear where the start of the slider is.

![Centered slider with an inset icon on one end, and a stop indicator on the other.
](../../_assets/m7lnlfie-22---don-t-0f4998d06b0e6d28386e.png)

close Don’t

Don’t use an inset icon on a centered slider

![Range slider with an inset icon on one end, and a stop indicator on the other.
](../../_assets/m7lnor7e-23---don-t-86ad75aaa08367471585.png)

close Don’t

Don’t use an inset icon on a range slider

### Size

Sliders come in different sizes: XS, S, M, L, and XL. Use larger sizes to increase the targets and provide a larger visual emphasis.

The active and inactive tracks should always be the same size.

![5 sizes of sliders.](../../_assets/m7lkolpk-24-2cb7c46a91b8ed3b0f34.png)

1.  XS: 16dp
2.  S: 24dp
3.  M: 40dp
4.  L: 56dp
5.  XL: 96dp

XL sliders should be reserved for hero moments, where the slider itself is the most important element on the page.

![An XL slider used to adjust living room temperature on mobile. No other controls are on screen.](../../_assets/m7lkr4j4-25-2b37c421db4fa2c4f32f.png)

XL sliders should be the focus of the page

## Behaviors

### Select & drag

Select a value by dragging the handle.

**Standard slider**: The handle drags smoothly

**Slider with stop indicators:** The handle snaps to the closest stop indicator while dragged

### Select jump

Select a value by selecting part of the track. 

**Standard** **slider**: The handle moves to the selected location

**Slider with stop indicators:** The handle moves to the closest stop indicator

### Select & arrow

Select a value using the keyboard.

**Tab:** Focus lands on handle 

**Arrows:** Selected value increases or decreases by one value or stop indicator

**Space & arrows:** Selected value increases or decreases by a larger interval or stop indicator

**Standard** **slider**: The handle moves one value

**Slider with stop indicators:** The handle moves to the next stop indicator
