---
source: https://m3.material.io/components/dialogs/guidelines
title: "Dialogs"
captured: 2026-09-14
---

# Dialogs

> Dialogs provide important prompts in a user flow

![Basic dialog in isolation](../../_assets/m8sf9qay-01-68c0d68b0c0b8801eb01.png)

A basic dialog

## Usage

A dialog is a modal window that appears in front of app content to provide critical information or ask for a decision. Dialogs disable all app functionality when they appear, and remain on screen until confirmed, dismissed, or a required action has been taken.

Dialogs are purposefully interruptive, so they should be used sparingly. A less disruptive alternative is to use a dropdown menu Menus display a list of choices on a temporary surface. [More on menus](/m3/pages/menus/overview) , which provides options without interrupting a user’s experience.

![Diagram of basic and full-screen dialogs.](../../_assets/m8sfc7pz-02-5a83b92362bee073decc.png)

There are two variants of dialogs:

1.  Basic dialog

2.  Full-screen dialog

![Dialog in front of app content.](../../_assets/m8sfcqhr-03_do-2a1ac7ea588f2e400f25.png)

check Do

Use dialogs for prompts that block an app’s normal operation, and for critical information that requires a specific user task, decision, or acknowledgement

![Low-priority dialog in front of app content.](../../_assets/m8sfdc9w-03_dont-8d72e57553b5a731d7e6.png)

close Don’t

Don’t use dialogs for low- or medium-priority information. Instead use a snackbar, which can be dismissed or disappear automatically.

### Similar components

Snackbars Snackbars show short updates about app processes at the bottom of the screen. [More on snackbars](/m3/pages/snackbar/overview) are also designed to show important messages.

Choose the right component based on the importance of the message. This component messaging strategy helps avoid overusing dialogs.

![Snackbar on a phone saying that new photos were synced to the device. No buttons exist.](../../_assets/XLiUu7mOltTNoUojZheRl95_BXn_O9vc9-PwyzL2W_vZPBccPC1bntpTZ6KwgzKDMDt8UGih90E9GPDG-29fa533dd47ddfb8226e.png)![Snackbar on a phone saying that new photos were synced to the device. No buttons exist.](../../_assets/XLiUu7mOltTNoUojZheRl95_BXn_O9vc9-PwyzL2W_vZPBccPC1bntpTZ6KwgzKDMDt8UGih90E9GPDG-55ce6c54d0ffc2bf7a84.png)

Snackbars can disappear automatically

| **Component** | **Importance** | **Action needed** |
| --- | --- | --- |
| Snackbar | Low importance | Optional: Snackbars may not have a button Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) , and can disappear automatically |
| Dialog | High importance | Required: Dialogs block the main content until an action is confirmed |

## Anatomy

### Basic dialog

![Diagram of 7 elements of basic dialog.](../../_assets/m8sfhos4-07-f43e2f6859e91b335e47.png)

1.  Container
2.  Icon (optional)
3.  Headline (optional)
4.  Supporting text
5.  Divider (optional)
6.  Buttons label text
7.  Scrim

### Full-screen dialog

![6 elements of full-screen dialog.](../../_assets/m8sfick9-08-e1f2ebc441bd937f24e2.png)

1.  Container
2.  Header region
3.  Icon (close affordance)
4.  Headline (optional)
5.  Button label text
6.  Divider (optional)

### Container and scrim

Dialog containers appear above other screen elements and hold the dialog’s headline, text, buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) , and list Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) items.

To focus attention on the dialog, surfaces behind the container are scrimmed with a temporary overlay to make them less prominent.

![Basic dialog shown above a scrim overlay that reduces the prominence of the background elements.](../../_assets/m8sfkf69-09-c12d338c63b54243a829.png)

Basic dialogs appear over a background scrim

### Headline (optional)

A dialog’s purpose should be communicated by its headline and buttons or actionable items.

Headlines should:

-   Contain a brief, clear statement or question
-   Avoid apologies (“Sorry for the interruption”), alarm (“Warning!”), or ambiguity (“Are you sure?”)

![Dialog title asking “Use location service?”](../../_assets/m8sfl8j1-10_do-3005ac8a703204520b6b.png)

check Do

This dialog title poses a specific question, concisely explains what’s involved in the request, and provides clear actions

![Dialog title asking “Are you sure?”](../../_assets/m8sflmm0-11_don-t-cb93420c4936ec5b122b.png)

close Don’t

Don’t use dialog titles that pose an ambiguous question

Headlines should always be succinct. They can wrap to a second line if necessary, and be truncated.

In full-screen dialogs, long headlines or headlines of variable lengths (such as translations), can be placed in the content area instead of the app bar.

![Example full-screen dialog with truncated long headline.](../../_assets/m8sfm2yt-12_Caution-aec4bc7d7b07495d3ed1.png)

exclamation Caution

Avoid placing long headlines in a full-screen dialog’s app bar (1), as the truncated text may lead to misunderstanding

![Example full-screen dialog with short headline, and longer text in content area.](../../_assets/m8sfmezr-13_do-52bdf11c9faf1d0a256b.png)

check Do

Find ways to shorten app bar text, and place longer headlines into the content area (1) of a full-screen dialog

### Buttons 

Dialog actions are most often represented as buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) and allow users to confirm, dismiss, or acknowledge something.

Buttons are aligned to the trailing edge of the dialog for easier interaction. The confirmation button is always closest to the edge. 

Button alignment responds automatically for right-to-left languages, where the confirmation button is aligned to the left edge.

![Dialog with the confirmation button disabled because a required radio selection is missing.](../../_assets/m8sfmqqd-14_do-13682c558c7df3f8c0be.png)

check Do

Disable confirming actions (1) until a choice is made. Dismissive actions are never disabled.

![Dialog with the dismissing action "Cancel" on the right of the 2 buttons.](../../_assets/m8sfn276-15_don-t-c429265de68d049cea87.png)

close Don’t

Don’t place dismissive actions (1) to the right of confirming actions. Instead, place them to the left of confirming actions.

![Dialog with a single-action button: “OK”.](../../_assets/m8sfq9tm-16_do-e55f733114df7c1783a8.png)

check Do

A single action may be provided only if it’s an acknowledgement

![Dialog with 2 button choices: “Cancel”, “Got it”.](../../_assets/m8sfqm2i-17_don-t-adc7f98339ffb0786077.png)

close Don’t

Avoid presenting people with unclear choices. **Cancel** doesn't make sense here because no clear action is proposed.

Dialogs should contain a maximum of two actions.

-   If a single action is provided, it must be an acknowledgement action
-   If two actions are provided, one must be a confirming action, and the other a dismissing action

![Dialog with 2 buttons side-by-side: “Disagree”, “Agree”.](../../_assets/m8sfqzp1-18_do-16e187a18df7b643c105.png)

check Do

Display two text buttons next to one another

![Dialog with 2 stacked buttons: “Turn on speed boost”, “No thanks”.](../../_assets/m8sfre4i-19_caution-65f3db822f85e0f69b51.png)

exclamation Caution

Stacked buttons accommodate longer button text, but take up more room. Confirming actions appear above dismissive actions.

Providing a third action, such as **Learn more**, is not recommended as it navigates the user away from the dialog, leaving the dialog task unfinished.

Rather than adding a third action, an inline expansion can display more information. If more extensive information is needed, provide it prior to entering the dialog.

![Dialog with 3 text buttons: Learn more, Disagree, Agree.](../../_assets/m8sfrskh-20-a3047922406536a7ce86.png)

exclamation Caution

The **Learn more** action (1) navigates away from this dialog, potentially leaving it in an indeterminate state

## Basic dialog

Basic dialogs interrupt users with urgent information, details, or actions. Common use cases for basic dialogs include alerts, quick selection Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) , and confirmation.

![Example of basic dialog action request.](../../_assets/m8sfumns-21-60bf0a95128b3418ed08.png)

Basic dialogs require a person to take action before it will close

![Example of basic dialog confirmation.](../../_assets/m8sfuxlx-22-72910fb3e18396e44e97.png)

Basic dialogs can give people the ability to provide confirmation of a choice before committing to it

Basic dialogs most often appear as alerts or lists Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) , but can have a variety of layouts Layout is the visual arrangement of elements on the screen. [More on layout](/m3/pages/understanding-layout/overview) and component combinations, including lists, date pickers Date pickers let people select a date, or a range of dates. [More on date pickers](/m3/pages/date-pickers/overview) , and time pickers Time pickers help users select and set a specific time. [More on time pickers](/m3/pages/time-pickers/overview) .

![Date picker dialog.](../../_assets/m8sfzk1g-23-dc551dc323b4ecf65830.png)

Date picker dialogs allow people to tap a date, then confirm it by tapping **OK**

![Time picker dialog.](../../_assets/m8sfxxnd-24-73ee67854bb1c4e76735.png)

Time picker dialogs allow people to move the clock hand and then confirm by tapping **OK**

## Full-screen dialog

Full-screen dialogs fill the entire screen, containing actions that require a series of tasks to complete. One example is creating a calendar entry with the event title, date, location, and time.

Because they take up the entire screen, full-screen dialogs are the only dialogs over which other dialogs can appear.

Use a [container transform](/m3/pages/motion-transitions/transition-patterns#b67cba74-6240-4663-a423-d537b6d21187) pattern to transition a FAB Floating action buttons (FABs) help people take primary actions. [More on FABs](/m3/pages/fab/overview) into a full-screen dialog.

Full-screen dialogs contain actions that require a series of tasks to complete

When a full-screen dialog is closed without being saved, a basic dialog appears in front of it to confirm selections Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) should be discarded without saving changes.

A basic modal dialog appears when a full-screen dialog is closed without being saved

Full-screen dialogs may be used for content or tasks that meet any of these criteria:

-   Dialogs that include components which require keyboard input Inputs are devices that provide interactive control of an app. Common inputs are a mouse, keyboard, and touchpad. , such as form fields

-   When changes aren’t saved instantly

-   When components within the dialog open additional dialogs

Full-screen dialogs are for compact breakpoints Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact breakpoints](/m3/pages/breakpoints/compact) only, like mobile devices. For medium and expanded breakpoints Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded breakpoints](/m3/pages/breakpoints/expanded) , use a basic dialog.

### Saving selections

To save a selection in a full-screen dialog, use **Save**.  The close icon or dismissive action, such as **Cancel** or **Back**, should close the dialog.

### Confirmation

The confirmation action should be clear about what happens next, like **Send** or **Create**. Avoid using vague terms like **Done**, **OK**, or **Close**. Only trigger an additional basic dialog if the action fails. Don’t disable A disabled state communicates an inoperable component or element. [More on disabled state](/m3/pages/interaction-states/applying-states#4aff9c51-d20f-4580-a510-862d2e25e931) the confirmation button.

![Full-screen dialog with create button as confirmation action.](../../_assets/m8sg5wkr-27_do-83bba68e740054265d28.png)

check Do

A **Create** button is clear that the event will be created

![Full-screen dialog with an additional basic dialog asking if you want to create this event.](../../_assets/m8sg67kv-28_don-t-90e965be2a17e54d663d.png)

close Don’t

Don’t trigger a basic dialog when the confirming action is selected

### Dismissing

When someone dismisses a full-screen dialog, a basic dialog should appear to confirm that they want to discard the unsaved changes.

![A basic dialog with options to either keep editing or discard unsaved changes.](../../_assets/m8sg91cq-29_do-cc6acd80cedf3f5710aa.png)

check Do

Use a basic dialog to confirm that the user wants to discard unsaved changes

![A full-screen dialog with a Close button as the confirming action.](../../_assets/m8sg9bz5-30_don-t-b3d5ca89bd7010653037.png)

close Don’t

Don’t use the confirming action to dismiss the full-screen dialog

### Error messages

Errors about the dialog fields should always appear inline where they occur. Some components like text fields Text fields let users enter text into a UI. [More on text fields](/m3/pages/text-fields/overview) have built-in error messaging, while others like checkboxes Checkboxes let users select one or more items from a list, or turn an item on or off. [More on checkboxes](/m3/pages/checkbox/overview) and radio buttons Radio buttons let people select one option from a set of options. [More on radio buttons](/m3/pages/radio-button/overview) need error messages to be added next to the fields.

General errors such as network issues preventing saving or submitting should appear in a basic dialog when the confirming action fails.

Error messages should clearly but briefly explain the source of the error and how to fix it. Show all errors on the page at once so people can fix everything before trying again.

![A full-screen dialog with inline error messages for text fields.](../../_assets/m8sg9nzm-31_do-7a8e8bd321d1cc9b2eea.png)

check Do

Error messages related to the fields should be displayed inline

![A basic dialog mentioning that entries were not saved due to a connection issue.](../../_assets/m8sg9xoh-32_caution-bf9d87d70df68836f787.png)

exclamation Caution

Errors unrelated to the fields can be displayed in a basic dialog

### Dialog windows

Launching a full-screen dialog temporarily resets the app’s perceived elevation, allowing simple menus Menus display a list of choices on a temporary surface. [More on menus](/m3/pages/menus/overview) or dialogs to appear above the full-screen dialog. They cover the screen and don’t appear as a floating modal window.

### Navigation

Because full-screen dialogs can only be completed, dismissed, or closed, the close “X” icon button should be the only navigation option in the app bar App bars display information and actions at the top of a screen. [More on app bars](/m3/pages/app-bars/overview) .

## Adaptive design

Dialogs can swap variants as the breakpoint Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes). [More on breakpoints](/m3/pages/breakpoints) changes. For example, a full-screen dialog Full-screen dialogs fill the entire screen, displaying actions that require a series of tasks to complete. They're often used for creating a calendar entry. [More on full-screen dialogs](/m3/pages/dialogs/guidelines#007536b9-76b1-474a-a152-2f340caaff6f) can change into a basic dialog Basic dialogs interrupt users with urgent information, details, or actions. They're often used for alerts, quick selection, or confirmation. [More on basic dialogs](/m3/pages/dialogs/guidelines#97ac3858-3932-4084-ae8e-73e42b7cb752) at larger breakpoints.

![Example of full-screen dialog on left, simple dialog on right](../../_assets/m8sgbmj3-33-f9b0cf4c183135f05ece.png)

1.  Full-screen dialog on mobile
2.  Dialog on a tablet

### Medium breakpoint

Basic dialogs appear in a center position by default.

Their position can be overridden to provide a more ergonomic experience.

![Basic dialog on tablet photos app.](../../_assets/m8sgc676-34-d35a9869f73a33468b96.png)

Dialog custom positioned on the right side of the screen

### Expanded breakpoint

Dialogs on expanded breakpoints Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded breakpoints](/m3/pages/breakpoints/expanded) , like desktop, are modal windows above a scrim. This puts the dialog at the forefront of a person's view, calling attention to the action prompted in the dialog.

![Example of desktop dialog.](../../_assets/m8sgj2r1-35-cb38994ebed930df2f87.png)

Desktop dialogs call attention to the required action

Basic dialogs can be custom-positioned anywhere on larger screens, respecting margins Margins are the spaces between the edge of a nested element and its parent element, such as the space between a button's label text and the edge of its container. [More on margins](/m3/pages/understanding-layout/spacing#38a538d7-991f-4c39-8449-195d32caf397) to prevent edge collision.

![Basic dialog position diagram.](../../_assets/m8sgjir4-36-63d995855586c7b44cd1.png)

Custom placement area for basic dialogs that respects a 56dp margin from the edges of the screen

## Behavior

### Appearing

Dialogs appear without warning, requiring users to stop their current task. They should be used sparingly, as not every choice or setting warrants interruption.

Dialogs use an [enter and exit](/m3/pages/motion-transitions/transition-patterns#e1c2a650-d7a4-4a6d-9025-e6b7845291ed) transition pattern to appear on screen.

A dialog appears with an enter and exit transition

### Position

Dialogs retain focus until dismissed or an action has been taken, such as choosing a setting. They shouldn’t be obscured by other elements or appear partially on screen, with the exception of full-screen dialogs.

![A basic dialog covering a full-screen dialog.](../../_assets/m8sgqe15-38-2cd98a20af2775b133fd.png)

Dialogs shouldn’t be obscured by other elements except for full-screen dialogs

### Scrolling

Most dialog content should avoid scrolling. Even when scrolling is required, the dialog title is pinned at the top, with buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) pinned at the bottom. This ensures selected content remains visible alongside the title and buttons, even upon scroll.

Dialogs don’t scroll with elements outside of the dialog, such as the background.

When viewing a scrollable list of options, the dialog title and buttons remain fixed
