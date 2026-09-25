---
source: https://m3.material.io/components/time-pickers/guidelines
title: "Time pickers"
captured: 2026-09-14
---

# Time pickers

> Time pickers help people select and set a specific time

![Time picker. It has a dial and keyboard input for hours and minutes, and a setting for AM or PM.](../../_assets/md2pwu0i-01-eab2ea48c98c62a6b3aa.png)

Dial selector time picker for a 12-hour clock

## Usage

Time pickers allow people to enter a specific time value. They’re displayed in dialogs Dialogs provide important prompts in a user flow. [More on dialogs](/m3/pages/dialogs/overview) and can be used to select hours, minutes, or periods of time.

They can be used for a wide range of scenarios. Common use cases include:

-   Setting an alarm
-   Scheduling a meeting

Time pickers are not ideal for nuanced or granular time selection Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) , such as milliseconds for a stopwatch application.

![Time picker with dial input selecting hour 7.](../../_assets/md2q22nz-02-f585103a6c564ddd4531.png)

check Do

Hour selection in a mobile calendar picker

### Time input picker

Time input pickers allow people to specify a time using keyboard numbers. This input option should be accessible from any other mobile time picker interface by tapping the keyboard icon.

![Input time picker with keyboard active for the hour.](../../_assets/md2q5unb-03-830a7aade71bc0db4e59.png)

Hour input with keyboard entry

### 24-hour time selection

The dial view can be changed to reflect time selection Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) across 24 hours. This option is set outside of the time picker component, typically through system settings.

![Time picker with dial input selecting hour 20. Hours 0–11 use an outer dial, hours 12–23 use an inner dial.](../../_assets/md2q7fdq-04-0303816b3230909dc2b1.png)

24-hour dial view

## Anatomy

![17 elements of a dial time picker.](../../_assets/md2u47yh-05-8c4a9d5363d85ea78a39.png)

1.  Label (headline)
2.  Time selector separator
3.  Input field
4.  Input text 
5.  Period selector (selected)
6.  Period selector text (selected)
7.  Container
8.  Period selector outline
9.  Period selector text
10.  Dial selector track
11.  Dial label (selected)
12.  Text buttons
13.  Icon button
14.  Dial label (unselected)
15.  Clock dial
16.  Input text (selected)
17.  Input field (selected)

![13 elements of an input time picker.](../../_assets/md2u4xoe-06-4401777cef53229482d4.png)

1.  Label (headline)
2.  Time selector separator
3.  Input field
4.  Input text 
5.  Period selector (selected)
6.  Period selector text (selected)
7.  Container
8.  Period selector outline
9.  Period selector text (unselected)
10.  Text buttons
11.  Icon button
12.  Input text (selected)
13.  Input field (selected)

### Container

Like dialogs Dialogs provide important prompts in a user flow. [More on dialogs](/m3/pages/dialogs/overview) , the container should appear above other screen elements. To focus attention, surfaces behind the container have a temporary scrim overlay to make them less prominent.

![Time picker container, all elements inside.](../../_assets/md2u8t61-07-753f333a4cec8b465173.png)

The container includes all time picker elements

### Input selector

The input selector is a unique kind of text field Text fields let users enter text into a UI. [More on text fields](/m3/pages/text-fields/overview) input. It differs from typical text field inputs in that it has:

-   An added highlight to call attention to the selected field

-   A larger shape, size, and font

-   A label below the field

Hours and minutes should have separate inputs. For people using a 12-hour clock, an AM/PM selector appears to the right of minutes. For people using a 24-hour clock, the AM/PM selector shouldn’t appear.

![Input time picker with the hour field active, and so highlighted.](../../_assets/md2ugmkj-08-6942c5a00319dd6e3321.png)

Input selector for a 12-hour clock

### Dial selector

Dial selectors always mimic a round watch face. Hours and minutes can be selected by tapping a number or dragging the dial selector track.

When representing a 12-hour dial, all numbers appear in the outer ring. When representing a 24-hour dial, even numbers appear in an inner ring, and odd numbers appear in an outer ring.

![Dial time picker with hour 7 selected.](../../_assets/md2uji74-09-8321caedcb7bfb90e04c.png)

Dial selector for a 12-hour clock

### Text & icon buttons

Icon buttons Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview) are used to switch between the input selector, represented by a keyboard, and the dial selector, represented by a clock.

Text buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) are used to exit the dialog Dialogs provide important prompts in a user flow. [More on dialogs](/m3/pages/dialogs/overview) (**Cancel**) and save the selector input (**OK**).

![Time picker buttons.](../../_assets/md2uqf01-10-e774439d0be2925e15ae.png)

The keyboard icon allows people to switch between the dial selector (pictured) and the input selector

### Landscape orientation

The clock dial interface adapts to a device’s orientation. In landscape mode, the stacked input and selection options are positioned side-by-side.

![Time picker in landscape orientation on mobile.](../../_assets/md2wil5z-11-479b1df75b94ca436840.png)

On mobile, the time picker can adapt to landscape orientation

## Placement

Time pickers shouldn’t be obscured by other elements.  

Time pickers should change orientation or variant to ensure they aren't cropped by the edge of the screen.

Time pickers are modal windows above a scrim. This puts the time pickers at the forefront of a person's view, calling attention to make a selection Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) of time.

![Input time picker in landscape orientation on mobile. It's fully visible despite the limited device height.](../../_assets/lw7tgqq3-12-202689aa08bf21f26522.png)

The time picker should change to fit the size of the screen so the time picker is always fully visible

## Adaptive design

Time pickers can swap between orientation or variant depending on device orientation and viewport constraints. 

For example, the time picker can change to landscape orientation on larger breakpoints or when viewport height is limited, to avoid scrolling the dial presentation. 

Time pickers can fallback to the input time picker Input time pickers allow people to set a time using a keyboard. This option is accessible from any mobile time picker interface via the keyboard icon. when there isn’t enough vertical real estate to present the landscape orientation without scrolling.

![Dial time picker in portrait orientation on mobile.](../../_assets/md2uzinf-13-d256ead36487404bd146.png)

High-density time picker displayed on mobile

### Density

Don’t apply density to the time picker dial when the viewport is constrained. Instead, use an input picker.

![Dial time picker in portrait orientation, too tall to fully fit on a mobile device in landscape mode.](../../_assets/md2v1wt2-14_dont-cde136cddf0c27c00822.png)

close Don’t

Don’t apply density to the time picker dial when the viewport is constrained. Instead, use an input picker.

## Behavior

There are two primary methods for selecting time with the mobile time picker. People can:

-   Type in a specific value in the hour and minute fields
-   Select the hour or minute field from the text input and adjust the clock dial to simultaneously change the corresponding time field above

The dial time picker supports both manual and dial input

### Appearing & disappearing

Like other kinds of dialogs Dialogs provide important prompts in a user flow. [More on dialogs](/m3/pages/dialogs/overview) , time pickers use an enter and exit transition pattern to appear on the screen.

To exit a time picker, the input can either be confirmed (**OK**) or dismissed (**Cancel**). Interacting outside of the dialog will also dismiss the time picker. Unless one of these actions is taken, a time picker will continue to retain focus.

**OK** confirms the entry and closes the dialog

### Toggle between dial & input

Tapping the keyboard icon on a mobile time picker switches the view to the input picker Input time pickers allow people to set a time using a keyboard. This option is accessible from any mobile time picker interface via the keyboard icon. .

The keyboard icon in the lower left toggles between the input picker and the dial picker

### Scrolling

Time pickers should avoid scrolling, and swap component orientation or variant based on device orientation or viewport size. 

Time pickers don’t scroll with elements outside of the modal window, such as the background.

![Input time picker in landscape orientation to fit a mobile device in landscape mode.](../../_assets/md2v8xeq-18-f29d8b7b3fcec6471955.png)

Time pickers shouldn’t scroll
