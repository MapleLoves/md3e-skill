---
source: https://m3.material.io/components/bottom-sheets/guidelines
title: "Bottom sheets"
captured: 2026-09-14
---

# Bottom sheets

> Bottom sheets show secondary content anchored to the bottom of the screen

![Two variants of bottom sheets.](../../_assets/lvp7eqa7-1-20d353317b66745a16b6.png)

1.  Standard bottom sheets
2.  Modal bottom sheets

## Usage

Bottom sheets display supplementary content and actions on a mobile screen.

![Photo sharing bottom sheet with contact list, app icons, and action buttons.](../../_assets/lvp7jb72-2-3bea1dad7eaa85964fab.png)

Bottom sheet containing contacts and applications

Bottom sheets are a versatile component that can contain a wide variety of information and layouts Layout is the visual arrangement of elements on the screen. [More on layout](/m3/pages/layout-overview/overview) , including menu Menus display a list of choices on a temporary surface. [More on menus](/m3/pages/menus/overview) items (in list Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) or grid layouts), actions, and supplemental content.

![Bottom sheet displaying 3 menu options.](../../_assets/lvp7jy07-3-789c58e6849ce10cebd1.png)

Bottom sheet with menu items in a list

## Anatomy

A container is the only required element of a bottom sheet. Bottom sheet layouts Layout is the visual arrangement of elements on the screen. [More on layout](/m3/pages/layout-overview/overview) can vary widely to support the kinds of content they contain.

![3 elements of a bottom sheet.](../../_assets/lvp7l25p-4-9f136ca8eae72f030b10.png)

1.  Container
2.  Drag handle (optional)
3.  Scrim (modal only)

### Container

Bottom sheet containers hold all bottom sheet elements. Their size is determined by the space those elements occupy.

The container is the only required element of a bottom sheet. All other elements are optional.

![Empty bottom sheet container.](../../_assets/lvp7llpd-5-f25f25fadda7d06fec4d.png)

Bottom sheets are flexible containers that adapt to their content and available space

### List items (optional)

Lists Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) are a continuous group of text or images. List items can include label text, icons, and text buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) , among other elements.

![A bottom sheet displaying a list of actions for a song.](../../_assets/lvp7m0a5-6-d851794067a59748285f.png)

Bottom sheet containing a list with icons

### Dividers (optional)

Dividers Dividers are thin lines that group content in lists or other containers. [More on dividers](/m3/pages/divider/overview) can be used to separate related content in bottom sheets.

![Bottom sheet with image action buttons and contact list separated by an inset divider.
](../../_assets/lvp7t324-7-3d7024d4897806af76fb.png)

Bottom sheet with a divider separating kinds of actions

### Media (optional)

**Thumbnail**
Bottom sheets can include thumbnails for an avatar or logo.

**Image**
Bottom sheets can include photos, illustrations, and other graphics, such as weather icons.

**Video**
Bottom sheets can include video.

![A bottom sheet displaying various media formats, including thumbnails, images, and video.](../../_assets/lvp7tqb3-8-8d451582200195da6b5c.png)

Bottom sheets can contain thumbnails, images, and video

## Standard bottom sheets

Standard bottom sheets co-exist with the screen’s main UI region and allow for simultaneously viewing and interacting with both regions, especially when the main UI region is frequently scrolled or panned.

Use a standard bottom sheet to display content that complements the screen’s primary content, such as an audio player in a music app.

![Bottom sheet with music player controls visible while browsing albums.](../../_assets/lvp7ubva-9-6dc00862e5c697b0980c.png)

The music player in this standard bottom sheet allows people to control their music while browsing albums

At full-screen height, standard bottom sheets contain a collapse icon in an app bar to return to their initial position.

Standard bottom sheets can contain supplementary content that continues below the screen, such as location information over a map.

A bottom sheet can have preset positions from full-screen height to preview

## Modal bottom sheets

Like dialogs Dialogs provide important prompts in a user flow. [More on dialogs](/m3/pages/dialogs/overview) , modal bottom sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken.

![A modal sheet with filter options to categorize files in the app. ](../../_assets/lvp7yz9g-11-ea6abb111cd2853934e9.png)

A modal bottom sheet must be interacted with or dismissed. Its blocking behavior makes it suitable for a menu, such as in this files app, to help people focus on their available choices.

Use a modal bottom sheet as an alternative to inline menus Menus display a list of choices on a temporary surface. [More on menus](/m3/pages/menus/overview) or simple dialogs Dialogs provide important prompts in a user flow. [More on dialogs](/m3/pages/dialogs/overview) on mobile, especially when offering a long list Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) of action items, or when items require longer descriptions and icons.

Modal bottom sheets are used in mobile apps only.

![A modal bottom sheet displayed as an alternative to a traditional menu, presenting a list of actions.](../../_assets/lvqcnuc5-12-964c908a034ca053f6cf.png)

Modal bottom sheets can be used instead of menus to present additional actions

### Visibility

To provide access to its top actions, the initial vertical position of modal bottom sheets Modal bottom sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken. is capped at 50% of the screen height.

Modal bottom sheets whose contents exceed 50% of the screen height can then be pulled across the full screen and scrolled internally to access their remaining items.

![A modal bottom sheet covering half of the screen, so both images and actions are accessible.](../../_assets/0hAPkL3uzyvqMvvRWFno-49bG4xDEWveRgFgP06QiwL9TTPtIatzwZnFBVZI70GmAn_NyU9lVQQ-8JkR-0790dec83d37c67e26bb.png)

The initial vertical position of modal bottom sheets can't exceed 50% of the screen height

Modal bottom sheets Modal bottom sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken. appear when triggered by a user action, such as tapping a button Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) or an overflow icon. They can be dismissed by:

-   Tapping a menu Menus display a list of choices on a temporary surface. [More on menus](/m3/pages/menus/overview) item or action within the bottom sheet
-   Tapping the scrim
-   Swiping the sheet down
-   Using a close affordance within the bottom sheet’s app bar App bars display information and actions at the top of a screen. [More on app bars](/m3/pages/app-bars/overview) , if available

Display a close affordance in a full-screen modal bottom sheet.

![A modal bottom sheet disappearing by tapping the scrim.](../../_assets/lvp80k55-14-23ffb2d06c3c28b217b2.png)

Tapping the scrim dismisses a modal bottom sheet

![A modal bottom sheet disappearing by swiping the sheet down.](../../_assets/lvp81a31-Bottom_sheet_dismiss_swipe-cec50b0e2dcdd5fe199e.png)

A modal bottom sheet can be dismissed by swiping the sheet down

## Responsive layout

### Compact breakpoint

In compact breakpoints Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact breakpoints](/m3/pages/breakpoints/compact) , like mobile devices, bottom sheets extend across the width of a screen and are elevated above the primary content.

![A bottom sheet extended to the width of a mobile screen.](../../_assets/lvp86bt1-15-18d1f1b9813e2994584d.png)

Bottom sheets should extend to the width of the screen on mobile

### Medium and expanded breakpoints

For larger screens with medium Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium breakpoints](/m3/pages/breakpoints/medium) and expanded breakpoints Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded breakpoints](/m3/pages/breakpoints/expanded) , bottom sheets have a default max-width to prevent undesired layouts Layout is the visual arrangement of elements on the screen. [More on layout](/m3/pages/layout-overview/overview) and awkward spacing. However, this can be overridden if needed. For more complex tasks and flows, consider using a non-transient surface such as a floating sheet Floating sheets show secondary content on a surface that can be anchored to the screen or moved. .

![A bottom sheet extended to its max-width on a large screen device, not spanning the full screen.](../../_assets/lvp86pgb-16-3e9da44f434ddc414dc1.png)

Bottom sheets on larger screens like tablet have a max width that can be overridden

On larger expanded breakpoints Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded breakpoints](/m3/pages/breakpoints/expanded) , like desktop, a bottom sheet can be swapped for a side sheet Side sheets show secondary content anchored to the side of the screen. [More on side sheets](/m3/pages/side-sheets/overview) that shows similar content.

![A side sheet on desktop.](../../_assets/lvp877lp-17-00ffc0fd5ac544cf9710.png)

Side sheets can contain the same content as bottom sheets and may be more suitable for desktop

## Behavior

Bottom sheets can offer an expansion option where the sheet is fully raised and toggled between a collapsed and expanded state States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) . This provides a more predictable footprint of the sheet, and can be set by the system or toggled by the user.

![Bottom sheet fully raised, showing photo actions, sharing options, and albums to add the photo to.](../../_assets/lvp87qvd-18-4bb0fe3d1e43b2fc33e2.png)

A bottom sheet for sharing can appear fully raised if needed

![Collapsed bottom sheet, showing focused set of options.](../../_assets/lvp8870t-19-fc8e633f810236884d28.png)

Alternately, a bottom sheet for sharing can appear collapsed for a more focused set of actions

### Custom positioning

The drag handle can be dragged or selected to change the bottom sheet height. 

Sheets should be able to cycle through preset heights and close completely without dragging. Selecting the drag handle should toggle through preset heights or close the sheet, while selecting the scrim should always close the bottom sheet.

If the bottom sheet has multiple preset heights but can’t use a drag handle, Material requires the inclusion of a single-pointer alternative to change height.

![Bottom sheet with a visible drag handle that can be used to adjust its height.](../../_assets/lvp8argg-20-640aa11249f461a942c6.png)

Interacting with the drag handle can quickly move a bottom sheet through preset heights

![Bottom sheet resized using the visible drag handle.](../../_assets/lvp8b6u5-21-2b4ea019dc20e120514a.png)

A bottom sheet can automatically resize to another height after interacting with the drag handle

### Scrolling

Bottom sheets can be horizontally scrolled, independent of the rest of the screen’s content.

![Bottom sheet that can be scrolled horizontally.](../../_assets/lvp8bo42-22-f774fa72c59e0d9911a3.png)

Bottom sheets should be scrollable when their content exceeds the initial viewable height

### Back

On Android, a gesture Gestures are all the ways people interact with UI elements using touch. [More on gestures](/m3/pages/gestures) called predictive back allows a user to swipe left or right on the bottom sheet. 

-   Bottom sheet detaches from the left and right edges of the screen to signal it will close
-   Previous screen is revealed in a preview

A list of compatible components is available in the [gestures article](/m3/pages/gestures).

Preview of the result of the gesture, **release** to commit, **fling** to commit, and **cancel**
