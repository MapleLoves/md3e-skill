---
source: https://m3.material.io/components/tooltips/guidelines
title: "Tooltips"
captured: 2026-09-14
---

# Tooltips

![A plain tooltip labeling a button, and a rich tooltip announcing new settings available.](../../_assets/me6qnzgx-01-fc4acead35293664ec65.png)

Plain and rich tooltips serve different purposes

## Usage

A tooltip provides additional context for a UI element. 

**Plain tooltips**
Plain tooltips briefly describe a UI element. They're best used for labelling UI elements with no text, like icon-only buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) and fields.

**Rich tooltips**
Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks.

Rich tooltips are best used for longer text like definitions or explanations.

![2 variants of tooltips.](../../_assets/me6qs96y-02-ea6a708d7ce66c03a3d3.png)

1.  Plain tooltip
2.  Rich tooltip

![Plain tooltip labeling an icon-only button in Google Meet as "Present now".](../../_assets/me6qu5gx-03-do-a30e9e6b742cb9ad4ad1.png)

check Do

Use plain tooltips to label icon-only buttons

![Button with an icon and label text saying "Edit". It has a plain tooltip on hover that also says "Edit".](../../_assets/me6quvhe-04-dont-9047d1d8b3dc18c58a61.png)

close Don’t

Plain tooltips aren't needed when the UI element already has label text

![Rich tooltip describing a new button for adding people. It has a subhead, description, and a button to learn more.](../../_assets/me6qx7on-05-do-d5d26372a50061698ef1.png)

check Do

Use rich tooltips to provide extra information and actions about a UI element or new feature

![Rich tooltip explaining that an action is destructive and permanently deletes files.](../../_assets/me6qywbu-6-dont-518f64e7585bdb8a4de2.png)

close Don’t

Don't hide critical information within tooltips as it’s easy to miss. Use an interruptive dialog instead.

## Anatomy

### Plain tooltip

![2 elements of a plain tooltip.](../../_assets/me6r0a08-07-b73332c818aa03887942.png)

1.  Container
2.  Supporting text

### Supporting text

![Plain tooltip for an icon-only button shaped like a gear. The tooltip text is "Settings".](../../_assets/me6r2ci0-08-do-c522afd8edd5ae8522cb.png)

check Do

Briefly describe a UI element

![Plain tooltip for the account switcher. The supporting text includes the user's name and email address on new lines.](../../_assets/me6r3rse-09-caution-797a6c984b1564973d02.png)

exclamation Caution

Avoid wrapping text to multiple lines or including many pieces of information

### Rich tooltip

![4 elements of a rich tooltip.](../../_assets/Qrg3y9UWvNZtKfeefdMriNm0BUWNB_4KL5lW4pDAdtSVGnRbdnJq_bOmpBVvYt7o6eS-pUOtaKvGpPpV-6fde6498eb5e60362c55.png)

1.  Subhead (optional)
2.  Container
3.  Supporting text
4.  Text button (optional)

### Subhead (optional)

Keep subheads brief, ideally to one line. They should summarize or describe the message of the rich tooltip Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks. .

Subheads are important to include when the rich tooltip appears automatically, like when the page loads.

![Rich tooltip with a brief subhead, supporting text, and a text button.](../../_assets/me6r9edz-11-do-15a35d12195cc9c48971.png)

check Do

Summarize the message in a few words

![Rich tooltip with a subhead wrapping to multiple lines.](../../_assets/me6ra39j-12-dont-e545adae6cb97c6bb92e.png)

close Don’t

Avoid wrapping to more than one line

### Text buttons (optional)

Rich tooltips can have up to two text buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) . These should be brief and relevant to the message in the supporting text.

Keep buttons short so they can be side by side. Avoid stacking them when possible.

![Rich tooltip with 2 buttons stacked on each other.](../../_assets/me6rdax0-13-Caution-c685790362e1a899621a.png)

exclamation Caution

Avoid stacking buttons

## Placement

### Plain tooltips

By default, plain tooltips are positioned directly above the parent element. 

-   If there's a visual boundary, like a button, the distance is 4dp
-   If there's no visual boundary, like with text baselines, the distance is 8dp

If the element is in an app bar App bars contain page navigation and information at the top of a screen. [More on app bars](/m3/pages/app-bars/overview) , the plain tooltip appears below the element at the same distance.

![Plain tooltip appearing 4dp below a button with a clear visual boundary.](../../_assets/me6rg1hz-14-78c616416f3701dde41b.png)

Plain tooltip with a 4dp distance between the target and tooltip

### Rich tooltips

By default, rich tooltips are positioned to the bottom right of the parent element. They adjust position to avoid going off screen.  Tooltips shouldn't cover the parent element. 

**Dynamic positioning**
The position of the tooltip adjusts in increments of 8dp to avoid going off-screen.

**Desktop placement**
On desktop, tooltips may appear centered below the parent element and remain visible while moving within the target region.

![A rich tooltip in 4 different corners. It   changes position to remain fully on screen.](../../_assets/me6riq0z-15-52bddabe433754ee4e7a.png)

Four different rich tooltip locations based on dynamic positioning

## Behavior

To show a tooltip, hover A hover state communicates when a user has placed a cursor above an interactive element. [More on hover state](/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844) on the parent element on desktop, or tap and hold the element on mobile. Persistent rich tooltips Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks. only appear when clicked or tapped.

### Transient by default

Both plain Plain tooltips briefly describe a UI element. They're often used for labelling UI elements with no text, like icon-only buttons and fields. and rich tooltips disappear 1.5 seconds after navigating away from the target region.

Triggering a new tooltip immediately closes any other open tooltip.

Tooltips disappear after a 1.5 second delay when no other element is hovered

![2 buttons both showing plain tooltips at once.](../../_assets/me6ro0ii-17-dont-66d16e207550014dca8a.png)

close Don’t

Only display one tooltip at a time

### Persistent rich tooltips

Persistent rich tooltips appear when either:

-   The parent element is clicked
-   The page loads and a new feature is being explained

Persistent rich tooltips remain active even when leaving the target region. They only disappear once a person interacts with another UI element. Hovering doesn't trigger the tooltip.

When appearing on page load, the tooltip can introduce and explain new features on various parent elements.

Avoid using persistent rich tooltips on icon buttons.

![Persistent rich tooltip about a new sharing feature in the Photos app. The button says  "Learn more.”](../../_assets/me6rq50p-18-dont-5cb93eeb9f5e9b455634.png)

close Don’t

Don’t use a persistent rich tooltip on icon buttons
