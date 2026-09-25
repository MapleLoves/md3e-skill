---
source: https://m3.material.io/foundations/interaction/states/applying-states
title: "States"
captured: 2026-09-14
---

# States

> States show the interaction status of a component or UI element

## Enabled

An enabled state communicates an interactive component or element. Enabled states use the default styling for each interactive component.

![Enabled state of 4 components.](../../../_assets/ly2qpw4a-1-6cd1c2bf3bcf75331b1c.png)

Enabled states for:

1.  Button
2.  FAB
3.  Switch
4.  Text field

## Disabled

A disabled state communicates when a component or element isn’t interactive. This state is visually communicated through color changes and reduced elevation.

**Disabled states don't need to meet Material's contrast requirements.**

![Low opacity solitary button labeled disabled, indicates a  disabled/inoperable state.](../../../_assets/ly2qrzig-2-36a36b70dd192d2dc2c2.png)

Disabled button

Disabled states **are** inherited by action, selection, and input components:

-   Buttons
-   Cards
-   Checkboxes
-   Chips
-   List items
-   Radio buttons
-   Switches
-   Text fields

![Inoperable state of 4 components.](../../../_assets/ly2qtg0r-3-370d0fee2cf40aebc74d.png)

Disabled states for:

1.  Checkbox
2.  Icon button
3.  Radio button
4.  Segmented button

Disabled states **aren't** inherited by communication, containment, navigation, and some actions components: 

-   App bars
-   Badges
-   Dialogs
-   Floating action buttons (FABs)
-   Menus
-   Navigation bar, drawer, and rail
-   Sheets
-   Tabs
-   Tooltips

![Screen erroneously showing edit FAB in inoperable state, though the edit function is unavailable.](../../../_assets/ly2quyuj-4-aa9fd8cbba503fc2caa1.png)

close Don’t

If the action represented in the FAB is unavailable, the FAB shouldn't appear

### Behavior

Disabled components can’t be focused, dragged, or pressed, and they don’t change state when tapped or hovered over.

A disabled button doesn’t inherit hover or other state layers

There can be any number of disabled states in a layout.

![Disabled components on a screen.](../../../_assets/lyml0ix7-6-a88723f39ec064e5281b.png)

1.  Disabled redo icon button
2.  Disabled checklist icon button

## Hover

Hover states are initiated by the user pausing over an interactive element using a cursor.

The lower-emphasis surface overlay for hover states can be applied to the entire component, elements within a component, or as a circular shape over part of the component.

![Cursor moves toward button which reads “enabled” and when the cursor touches the button text changes to “hovered.”](../../../_assets/ly2vwc74-7-a61668434eb6b3e49ebb.png)

Hovered button

Hover states **are** inherited by action, selection, and input components:

-   Buttons
-   Cards
-   Checkbox
-   Chips
-   Date and time pickers
-   List items
-   Slider
-   Switch
-   Text fields

![Hover state of 4 components.](../../../_assets/ly2vxl8i-8-e13366e50df596ee48c1.png)

Hovered states for:

1.  FAB
2.  Icon button
3.  Chip
4.  Segmented buttons

Hover states **aren’t** inherited by communication, containment, or navigation components: 

-   App bars
-   Badges
-   Dialogs
-   Menus
-   Navigation bar, drawer, and rail
-   Sheets
-   Tabs

![Mobile screen with the whole  app bar wrongly in hover state.](../../../_assets/ly2vymng-9-5960b03e3b8b19fd929a.png)

close Don’t

The individual components that are actionable within the app bar inherit hover states, not the whole app bar

### Behavior

Hover states are initiated by the user pausing over an interactive element using a cursor.

Hover states appear and disappear using a low-emphasis animated fade

Hover states can be combined with focused, activated, selected, or pressed states.

A selected filter chip in both selected and hover states

There can only be one hover state at a time in a layout.

Hover state can only be on one element at a time based on cursor position

## Focused

A focused state communicates when a user has highlighted an element using a keyboard or voice. Focus states apply to all interactive components.

The higher-emphasis surface overlay for focused states can be applied to the entire component, elements within a component, or as a circular shape over part of the component.

![A button in focused state.](../../../_assets/ly2wa79s-13-ca670e39fd1b543a1d72.png)

Focused button

Focus states **are** inherited by action, selection, and input components:

-   Buttons
-   Cards
-   Checkbox
-   Chips
-   Date and time pickers
-   List items
-   Selection controls
-   Text fields

![Focus state of 4 components.](../../../_assets/ly2wb5y9-14-038aa3177299394b535e.png)

Focused states for:

1.  FAB
2.  Icon button
3.  Chip
4.  Segmented buttons

Focus states **aren’t** inherited by most communication, containment, or navigation components:

-   App bars
-   Badges
-   Banner
-   Card
-   Dialogs
-   Navigation bar, drawer, and rail
-   Sheets

![Mobile screen showing  entire app bar in focus state, which is an error.](../../../_assets/ly2wctgk-15-94651d4040b6f873b7c1.png)

close Don’t

The individual components that are actionable within the app bar inherit focus states, not the whole app bar

### Keyboard focus indicator

Many people use the **Tab** key or other shortcut to navigate the interactive elements of a web page, like links, buttons, and chips.

When an element is tabbed to, it appears in its focused state with a ring-like **keyboard focus indicator**. This indicator helps web users know where they are on the page.

While focused, an element can be acted on with the keyboard.

![A single filled button in focused state, displaying the keyboard focus indicator.](../../../_assets/ly2wdmfh-16-14407d225f894f0f80c7.png)

Keyboard focus indicator for a filled button

### Behavior

Focus states are initiated by the user by pressing the **Tab** key on the keyboard (or equivalent).

Focus states can be represented in combination with hover, activated, or selected states.

![A single filter chip simultaneously in selected state and focus state.](../../../_assets/ly2wf3qd-17-79bc90873a4680333433.png)

A selected filter chip in both selected and focused states

There can only be one focus state at a time in a layout.

A focus state applied to one card at a time

## Pressed

A pressed state communicates a user-initiated tap or click via cursor, keyboard, or voice input. This state applies to all interactive components.

Pressed states trigger a change in composition and should be high-emphasis.

A ripple overlay signifies a pressed state. It can be applied to an entire component or elements within a component, or as a circular shape over part of the component.

![Button using a ripple overlay to signify it’s in a pressed state.](../../../_assets/ly2wj03t-25-614931561d9a00b9d84b.png)

Pressed button

Some components, such as buttons or cards, can inherit elevation to signify a pressed state.

![Button using elevation to signify it’s in a pressed state.](../../../_assets/ly2wk46q-26-be2bac79affaa7e2af43.png)

Pressed button with elevation

Pressed states **are** inherited by action, selection, and some containment components: 

-   Buttons
-   Cards
-   Checkbox
-   Chips
-   List items
-   Text fields

![Four components shown in pressed state.](../../../_assets/ly2wl23l-27-bba5efb6a59110ce5f61.png)

Pressed states for:

1.  FAB
2.  Icon button
3.  Chip
4.  Segmented button

Pressed states **aren’t** inherited by communication, navigation, or some containment components: 

-   App bars
-   Badges
-   Bottom navigation
-   Dialogs
-   Menus
-   Sheets
-   Tabs

![Mobile screen showing  entire app bar in pressed state is an error.](../../../_assets/ly2wo5k7-28-0b2d859dc84a484e9167.png)

close Don’t

The individual components that are actionable within the app bar inherit pressed states, not the whole app bar

### Behavior

Pressed states are initiated by user keyboard or voice input on an interactive element.

Activated states appear in user-initiated order

Pressed states can be combined with hovered, focused, activated, or selected states.

Activated states can be represented in combination with hover and focus

There may only be a single pressed state at a time in a layout.

A pressed state applied to one card at a time

## Dragged

A dragged state occurs when a user presses and moves an element or component. Dragged states should be low emphasis, to avoid distracting users from their task.

Dragged states use a lower emphasis overlay. It can be applied to the entire component or to elements within a component.

Some components, such as list items, chips, or cards, can inherit elevation to signify a dragged state.

![List item shown in dragged state.](../../../_assets/ly2wu37e-32-fa7acea7e79a4a36d7f5.png)

Dragged list item

Dragged states **are** inherited by some containment and selection components: 

-   Cards
-   Chips
-   List items
-   Sliders

![A chip and a card both shown in dragged state.](../../../_assets/ly2wv77r-33-1ec3ef560b9fb9e4a197.png)

Dragged states for:

1.  Chip
2.  Card

Dragged states **aren’t** inherited by action, communication, navigation, or some containment components: 

-   App bars
-   Badges
-   Buttons
-   Dialogs
-   Menus
-   Navigation bar, drawer, and rail

![Mobile screen with app bar in dragged state is an error.](../../../_assets/ly2ww2lq-34-077535ce766858118596.png)

close Don’t

Components like an app bar that require consistent placement should not inherit dragged states

### Behavior

Dragged states are initiated when users touch and hold elements, using an input method such as a tap or click.

A list item in a dragged state

There may only be a single dragged state at a time within a layout.

Dragged state applied to one card at a time
