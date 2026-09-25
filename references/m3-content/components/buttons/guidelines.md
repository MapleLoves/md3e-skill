---
source: https://m3.material.io/components/buttons/guidelines
title: "Buttons"
captured: 2026-09-14
---

# Buttons

> Buttons prompt most actions in a UI.

![Buttons in various shapes and sizes.](../../_assets/mmlqkp7g-01-d6beeee81d7c71d0ca45.png)

Buttons and icon buttons come in many shapes, styles, and sizes

## Usage

Buttons communicate actions that people can take. They are typically placed throughout the UI, in places like:

-   Dialogs Dialogs provide important prompts in a user flow. [More on dialogs](/m3/pages/dialogs/overview)

-   Modal windows

-   Forms

-   Cards Cards display content and actions about a single subject. [More on cards](/m3/pages/cards/overview)

-   Toolbars Toolbars display frequently used actions relevant to the current page. [More on toolbars](/m3/pages/toolbars/overview)

They can also be placed within standard button groups Standard button groups add interactions between adjacent buttons when they're pressed. [More on button groups](/m3/pages/button-groups/overview) .

Use visually-prominent filled buttons for the most important actions

Buttons are just one option for representing actions in a product and shouldn’t be overused. Too many buttons on a screen can disrupt the visual hierarchy.

Consider placing additional actions in a navigation rail Navigation rails let people switch between UI views on mid-sized devices. [More on navigation rail](/m3/pages/navigation-rail/overview) , set of chips Chips help people enter information, make selections, filter content, or trigger actions. [More on chips](/m3/pages/chips/overview) , text links, or icon buttons Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview) .

![1 button placed on bottom right of screen.](../../_assets/mmlqpj6e-03-do-97a40f731f30c4ac6b9b.png)

check Do

Use buttons for discrete actions

![3 buttons side by side on bottom of screen.](../../_assets/mmlqpykn-04-don-t-07feae460184d769f204.png)

close Don’t

Don’t clutter your UI with too many buttons. Consider presenting low-priority actions in overflow menus or as icon buttons.

![Filled button on menu screen.](../../_assets/mmlqs2ix-05-do-96bdb978f87ea7a1d361.png)

check Do

A button container’s width is dynamically set to fit its label text

![Filled button as wide as layout grid.](../../_assets/mmlqslcx-06-do-f5afdae867d8743f6b8c.png)

check Do

Button container width can be responsive, which allows it to stretch horizontally

![Filled button with label text overflowing the container. ](../../_assets/mmlqt8jf-07-don-t-421921bbfbe05057a23e.png)

close Don’t

A button container’s width shouldn’t be narrower than its label text

![Diagram of button styles and toggle behaviors.](../../_assets/mmlquaj1-08-7986cdbc4e5f9392a836.png)

A: Default button; B: Toggle (unselected); C: Toggle (selected) for five button styles, in order of emphasis:

1.  Elevated button

2.  Filled button

3.  Filled tonal button

4.  Outlined button
5.  Text button

A button group Button groups organize buttons and add interactions between them [More on button groups](/m3/pages/button-groups/overview) is a collection of buttons that relate to each other and can respond to one another. Both buttons and icon buttons can be used inside a button group.

In some cases, there are primary and secondary actions within a button group. Buttons with primary actions should have a higher visual emphasis through size, color, or shape.

[More on button groups](/m3/pages/button-groups/overview)

![Audio app with play, next, and back buttons.](../../_assets/m3t81e1q-9-d09da5f17370d50e9094.png)

Different sized buttons in a button group help emphasize the main action from secondary actions

## Toggle buttons

Toggle buttons should be used for binary selections, such as **Save** or **Favorite**. When toggle buttons are pressed, they can change color, shape, and labels.

Toggle buttons should use an outlined icon when unselected, and a filled version of the icon when selected. If a filled version doesn’t exist, increase the weight instead.

By default, toggle buttons change from round to square when selected.

Use toggle buttons for binary actions

If the label changes on selected or unselected states, be mindful of the character count. Changing the label significantly is disruptive to the user and the page layout.

![Toggleable “start” and “reset” buttons.](../../_assets/mmlt4ivd-11-do-fe44e50d79610d608077.png)

check Do

When using toggleable buttons, keep the label character count a similar length for both states

![Toggleable “start” and “reset back to beginning” buttons.](../../_assets/mmlt52gk-12-dont-a85c65ef0715bffdb4da.png)

close Don’t

The label length shouldn’t change dramatically to be longer or shorter

## Anatomy

![3 parts of a button.](../../_assets/mmlt6b63-13-12ac83a93e0405690477.png)

1.  Label text
2.  Container
3.  Icon (optional)

### Label text

Label text is the most important element of a button. It describes the action that will occur if someone taps a button. It should be very brief, ideally 1–3 words.

Use sentence case, which only capitalizes the first word and proper nouns. This allows the text to distinguish proper nouns, for example: **Book with Flights**, not **BOOK WITH FLIGHTS**.

Don’t truncate or wrap label text. It should always be fully visible on a single line.

![Button with label text “See all recipes.”](../../_assets/mmlt7k3u-14-do-5db5b145c5270ff9f87f.png)

check Do

Use sentence case for button label text, capitalizing the first word and proper nouns

![Button with wrapped label.](../../_assets/mmlt7yj0-15-dont-cc12deb0a16400f81032.png)

close Don’t

Don’t wrap text. For maximum legibility, label text should remain on a single line.

Buttons with the **outlined** and **text** color style depend on the colors to be recognizable from other text and elements. Use caution when putting these buttons next to visually similar elements, such as chips or large text.

![Chips next to an outlined button, highlighting their similarities.](../../_assets/mmlt97u1-16--caution-6fa67a4ed709f7aec1f2.png)

exclamation Caution

The outlined button style is very similar to chips. Consider using a filled or tonal button instead.

### Container

Button containers hold the label text and optional icon. Buttons with the **text** color style have a visible container only when hovered, focused, or pressed.

Buttons with a round shape have containers with fully rounded corners.

![Round button.](../../_assets/mmltabq2-17-412a425acc83712bfb77.png)

Round buttons have containers with fully rounded corners

Buttons with a square shape have containers with more subtle rounding that changes based on button size.

![Square buttons with different radii.](../../_assets/mmltba1r-18-727f6dbde009b43ca07d.png)

Square buttons have square containers and change radius as the button size changes

![Button with the label text “Edit playlist” within the container.](../../_assets/mmltc6hg-19-do-22da4fb36efbee0c0844.png)

check Do

A button’s width dynamically adjusts to the label text

![Button with text larger than its container.](../../_assets/mmltdu8d-20-dont-0701744245632616b397.png)

close Don’t

Avoid setting a fixed width smaller than the label text

### Icon (optional)

Icons visually communicate the button’s action and help draw attention. They should be placed on the leading side of the button, before the label text.

![Filled button with the icon to the left of the label in a left-to-right language.](../../_assets/mmltfge9-21-do-5adce41e399bafd2cb50.png)

check Do

Place the icon to the left of the label in buttons with text in left-to-right languages

![Filled button with the icon to the right of the label in a right-to-left language.](../../_assets/mmltfyz4-22-do-fee67ae19c5828333b5a.png)

check Do

Place the icon to the right of the label in buttons with text in right-to-left languages

![Button with shopping cart icon and text label “Add to cart”.](../../_assets/mmlthjj7-23-do-2d99f7287291339798e6.png)

check Do

Use icons that clearly communicate their meaning

![Button with Plus icon vertically above the text label “Add to watch list”.](../../_assets/mmltnhb2-24-dont-d185d4ecebc0ba9fcb30.png)

close Don’t

Don’t vertically align an icon and text in the center of a button

![Button with two icons.](../../_assets/mmltof7i-25-dont-0c8832bb4b19d23349d9.png)

close Don’t

Don’t use two icons in the same button

## Color styles

### Elevated style

The **elevated** button style is the same as the tonal button, but with a shadow. 

To avoid overusing shadows, use the elevated style only when absolutely necessary, such as when the button requires visual separation from a visually prominent background.

![Elevated button on a scrim background.](../../_assets/mmltpyn5-26-870fa63f3693f9d1e749.png)

Elevated buttons provide separation from a visually prominent background

Buttons at higher elevations typically have more emphasis in a design, and should be used sparingly. For high emphasis, consider the filled style instead.

![Elevated button in a shopping experience.](../../_assets/mmltrnw9-27-caution-095c4c7a57f4a59bd0d5.png)

exclamation Caution

Higher elevation increases the emphasis of a button

### Filled style

The **filled** button style has the most visual impact after the FAB Floating action buttons (FABs) help people take primary actions. [More on FABs](/m3/pages/fab/overview) , and should be used for important, final actions that complete a flow, like **Save**, **Join now**, or **Confirm**.

![Filled button reading “Make payment.”](../../_assets/mmlz52ml-28-2ed92e39964232e35fc9.png)

Filled buttons have high visual impact when used for important actions

Since they have such strong emphasis, the filled style should be used sparingly, ideally for only one action on a page.

In some cases, filled buttons can use tertiary colors.

![Filled “pause” button in a music app.](../../_assets/mmlz6rew-29-6bcbb79207b0cfdd96e4.png)

Filled buttons can be responsive to the layout grid and help emphasize main actions

### Tonal style

The **tonal** button style is useful in contexts where a lower-priority button requires slightly more emphasis than an outline would give, such as **Next** in an onboarding flow. Tonal buttons use the secondary color mapping.

![Shopping app with 2 tonal-style filled buttons.](../../_assets/mmm0gmxc-30-a6a677fa433aaec5f54e.png)

The tonal style has less emphasis than filled or emphasis

### Outlined style

The **outlined** style is ideal for medium-emphasis buttons which contain actions that are important, but aren’t the primary action in a product.

Outlined buttons pair well with filled buttons to indicate alternative, secondary actions.

![Outlined buttons for less important actions, including a back button and a button that reads “Next movie.”](../../_assets/mmm0loal-31-7591049b8d1987b6877f.png)

Outlined buttons contain less important supporting actions

Outlined buttons display a stroke around the button container, and have no fill by default. 

They should be placed on simple backgrounds, not visually prominent backgrounds such as images or videos. 

![Outlined button for “add to cart” in shopping app.](../../_assets/mmm0mtua-32-af32105e8d061944d4ff.png)

Outlined buttons display a stroke around the button container

![Outlined button labeled Add to calendar on a pink/purple background.](../../_assets/mmm0nymp-33-do-63bf794044cd0c608d1c.png)

check Do

Outlined buttons can be used on backgrounds with a color gradient

![2 photos, each with an outlined button with a custom fill.](../../_assets/mmm0oqjx-34-caution-6c8638f985c4e9bc359c.png)

exclamation Caution Use caution when placing outlined buttons on top of images. Customizing the button to have a contrasting container fill can help ensure legibility of label text. Or, use a filled button instead.

### Text style

The text button style should be used for the lowest priority actions, especially when presenting multiple options.

They should be placed on simple backgrounds, not visually prominent backgrounds such as images or videos. The container isn’t visible until someone interacts with the button.

Don’t underline the text button. Use hyperlinked body text instead to emphasize links. [More on hyperlinks](/m3/pages/typography/applying-type#24856f70-f759-45df-a06c-92018f286083)

![Example calendar screen with 2 text buttons and 1 split button.](../../_assets/mmm0q822-35-7129edb770f4075b39b1.png)

Use text buttons for the lowest priority actions

Text buttons are often placed within components such as cards Cards display content and actions about a single subject. [More on cards](/m3/pages/cards/overview) , dialogs Dialogs provide important prompts in a user flow. [More on dialogs](/m3/pages/dialogs/overview) , and snackbars Snackbars show short updates about app processes at the bottom of the screen. [More on snackbars](/m3/pages/snackbar/overview) . Since text buttons don’t have a visible container in their default state States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) , they don’t distract from nearby content.

However, since there’s no container, the label text color must always be recognizable from non-button text and elements.

![Text button labeled “Retry” in a snackbar.](../../_assets/mmm0rpw4-36-447b0a013ec2474b4b97.png)

Text button in a snackbar

![Text button labeled “View album” on an album cover background.](../../_assets/mmm0s6c1-37-04b2172286d442b5a4ea.png)

Text button against an image background

In cards, text buttons help maintain an emphasis on card content.

![Text button labeled “Learn more” in an information card about sourdough bread.](../../_assets/mmm0tlmd-38-af3131a3f987fef7b654.png)

Text button in a card

Dialogs use text buttons because the absence of a container helps unify the action with the dialog text.

Align text buttons to the trailing edge of dialogs, on the right for left-to-right languages and on the left for right-to-left languages.

![Modal dialog with the title “Subscribe to our newsletter?” and trailing buttons “Cancel” and “Subscribe”.](../../_assets/mmm0v0go-39-d5d1a83155454c617747.png)

Text buttons in a dialog

## Adaptive design

### Resizing

When scaling layouts for large screen devices, buttons can adapt their visual presentation, size, alignment, and arrangement to fit different contexts and user needs.

Choose the best button position based on screen size.

![Flights app in compact screen with buttons below flight information.](../../_assets/mmm0vwgx-41-5322f8adc0ebe391b5fa.png)

Filled buttons are end-aligned below flight information in a compact window

![Flights app in large screen with buttons to the left of flight information.](../../_assets/mmm0wuqe-40-afb066a528168ae0b8e7.png)

Filled buttons are start-aligned beside flight information in a large window

The icon and label text in a button stay centered and grouped as the button's width changes.

![2 buttons with horizontally centered text labels.](../../_assets/mmm0y1g6-42-do-f2f9ed8fe7172a7cc9f2.png)

check Do

Keep the icon and label text grouped and centered

![1 button with centered text label, 1 button with icon and label aligned to opposite edges.](../../_assets/mmm0yith-43-dont-214b6fa5ad599f5d2d09.png)

close Don’t

Don't ungroup the icon and label text or let them anchor to opposite sides of the button

Buttons can be customized to change size and scaling behavior across different breakpoints Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes). [More on breakpoints](/m3/pages/breakpoints) . 

To avoid creating very long buttons in large windows, constrain button width or place buttons beside other elements.

![Button width is over-stretched with screen width.](../../_assets/mmm0zsof-44-dont-4dd3b79b9b11266dc13f.png)

close Don’t

Don’t allow the button to stretch in a way that creates long, flat buttons with very little content inside

### Presentation

The size and placement of buttons can change as parent containers, such as cards, adapt for larger screens. 

Keep items, including buttons, in the same order between large and small screens to provide a consistent experience for screen readers and keyboard navigation.

![2 buttons scaling to accommodate different device sizes.](../../_assets/mmm11hfb-45-dff7435dbd1bbb1ffa1e.png)

Buttons can move in the layout, but elements should remain in the same order
