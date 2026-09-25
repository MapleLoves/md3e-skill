---
source: https://m3.material.io/components/segmented-buttons/guidelines
title: "Segmented buttons"
captured: 2026-09-14
---

# Segmented buttons

> Segmented buttons help people select options, switch views, or sort elements

star

Note:

Segmented buttons are no longer recommended in the Material 3 expressive update. For those who have updated, use the [connected button group](/m3/pages/button-groups/overview/) instead, which has mostly the same functionality but with an updated visual design.

![Two types of segmented buttons.](../../_assets/lw7mlxdq-1-c34371b7149da9de4c29.png)

1.  Single-select 
2.  Multi-select

## Usage

Segmented buttons help people select options, switch views, or sort elements.

![A segmented button for switching between restaurants and bar options. ](../../_assets/lw7mnnk2-2-b82ea1e551bbbf52572f.png)

A segmented button can help switch between viewing restaurant and bar options

There are 2 variants of segmented buttons:

1.  Single-select

2.  Multi-select

![Side by side view of single and multi-select segmented buttons](../../_assets/lw7mz9ev-3-bd83bf9c748223f9cbbf.png)

1.  Single-select segmented button can only have 1 segment selected
2.  Multi-select segmented button can have multiple segments selected

## Anatomy

![Diagram of segmented button indicating 5 parts of its anatomy](../../_assets/lw7n59nt-4-b03cac3c48c8023c57d9.png)

1.  Segment
2.  Container
3.  Icon (optional)
4.  Label text (optional)
5.  Selected icon

### Segments

Segmented buttons can have 2-5 segments. Each segment is clearly divided and contains label text, an icon, or both.

![Side by side view of segmented buttons each with additional segment starting from 2 to 5](../../_assets/lw7nap4m-5-e5addedb2736082f82eb.png)

There can be anywhere from 2 to 5 segments in single-select and multi-select segmented buttons

![Mobile UI of data usage screen with segmented button](../../_assets/lw7ngd39-6_do-f497041df3bdd88ca7e1.png)

check Do

Segmented buttons are best used for selecting between 2 and 5 choices

![Incorrect use of segmented button with 6 segments](../../_assets/lw7o4u2i-7_dont-aeeffd6a03368be94262.png)

close Don’t

Don’t use more than five segments in a single segmented button. Choices should be scoped. If you have more than five choices, consider using another component, such as chips.

### Container

Like common buttons Buttons let people take action and make choices with one tap. , segmented buttons have fully rounded corners by default.

![Close up detail of segmented button with fully rounded corners](../../_assets/lw7o7un8-8-a13e5beab0c39de97d29.png)

Segmented buttons have fully rounded corners

### Icons

Icons may be used as labels by themselves or alongside text. 

If an icon is used without label text, it must clearly communicate the option it represents. 

![Side by side view of segmented buttons with different configurations of icons and label text](../../_assets/lw7okkk9-9-fd699b27327c588dd1af.png)

Segmented buttons can include icons

### Label text

Labels should be short and succinct. If a label is too long to fit within its segment, consider using an icon alone.

![Mobile UI of music app showing a segmented button with options for music, albums, podcasts](../../_assets/lw7omu8a-10-846169a9465f4fedbb7d.png)

Use labels that are as clear and short as possible

![Segmented button with options for day, week, month](../../_assets/lw7pqz1e-11_do-3be3d2522ea6ac010f32.png)

check Do

Keep labels short and consistent in length

![Segmented button with 4 segments. 3 are next to each other. The 4th is wrapped on a new line.](../../_assets/lw7prory-12_dont-bf406302bb3ebacb3e3d.png)

close Don’t

Don’t allow segments to wrap onto a new line

![Segmented button with text labels reading day, week, month](../../_assets/lw7psieh-13_do-a64d5d9c9a9b40288faf.png)

check Do

Use consistent label types

![Segmented button with icons only labels for walking, transit, driving](../../_assets/lw7pt9gl-14_caution-c3bd25b5655199005f8a.png)

exclamation Caution

Icons can be used in place of labels, but they must clearly communicate their meaning

![Segmented button with 2 icon only options indicating favorite and bookmark and 3rd option with text label reading recent](../../_assets/lw7ptzzf-15_dont-af7e496810cae24fdf1b.png)

close Don’t

Avoid mixing icon-only labels with text labels. Choose one label type and use that type for all segments.

## Single-select

Use a single-select segmented button to select one option from a set, switch between views, or sort elements from up to five options. 

For example, use a single-select segmented button to choose one of a set of sizes, such as this beverage size selector.

![Mobile UI for ecommerce app with segmented button with 3 beverage size options](../../_assets/lw7puwq3-16-5679157a28ab312e5597.png)

A single select segmented button for choosing beverage size

## Multi-select

Use a multi-select segmented button to select or sort from two to five options. Unlike single-select, selection is not required and a user may concurrently select anywhere from all to none of the options. 

For example, multi-select segmented buttons can be used to filter by price range when searching for a restaurant. 

![Mobile UI for ecommerce app with multi-select segmented button with 4 price range options ](../../_assets/lw7pvpf7-17-9615b603cd0dbe507a1d.png)

A multi-select segmented button for filtering restaurant search options

## Placement

Segmented buttons should have adequate margins Margins are the spaces between the edge of a nested element and its parent element, such as the space between a button's label text and the edge of its container. [More on margins](/m3/pages/spacing/overview) from the edge of the viewport or frame. 

On larger screens, set a maximum padding for all button segments so the set doesn't fill the screen.

![Mobile UI with 2-segment segmented button and 4-segment segmented button each with same margins to the viewport edge.](../../_assets/lw7pwh9i-18-954f8e58d569283e5ffc.png)

check Do

Allow adequate space for margins. The button container shouldn’t reach the edge of the viewport.

![Game store UI with a segmented button the proper width](../../_assets/lw7pxu9q-18-a_do-227e767bdd3ee18c3b78.png)

check Do

Set a maximum padding within the segments to ensure usability on larger screens

![Game store UI with a segmented button improperly spanning the entire width of the screen](../../_assets/lw7pyzy1-18-b_dont-42e30c850f4cf7a5ba0e.png)

close Don’t

Don’t allow segmented buttons to span the full width of larger screens or panes. This can leave too much padding on either side of the segment label, making the button less usable.

Segmented buttons can be placed on other components, such as bottom sheets Bottom sheets show secondary content anchored to the bottom of the screen. [More on bottom sheets](/m3/pages/bottom-sheets/overview) or full-screen dialogs Full-screen dialogs fill the entire screen, displaying actions that require a series of tasks to complete. They're often used for creating a calendar entry. . 

![Mobile UI with segmented button in bottom sheet](../../_assets/lw7q0vrm-19-36e0b62b3c0c17a9d92a.png)

A segmented button can be placed on a bottom sheet

## Behavior

When using both icons and label text in segmented buttons, the icon label is replaced by the checkmark icon when the segment is selected. 

Icons become checkmarks when selected in buttons that also use label text
