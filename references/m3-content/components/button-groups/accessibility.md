---
source: https://m3.material.io/components/button-groups/accessibility
title: "Button groups"
captured: 2026-09-14
---

# Button groups

> Button groups organize buttons and add interactions between them

## Use cases

People should be able to do the following with assistive technology:

-   Navigate to and interact with each button in the group 
-   Identify when buttons are selected

## Interaction & style

Each button in a group should have a minimum 48x48dp target. 

Extra small and small button groups have larger inner padding to ensure accessible targets. Avoid reducing the padding in these sizes.

![Extra small and small button groups with 48x48dp target areas annotated over top. The area is larger than the buttons.](../../_assets/m0dgm57d-tap-targets-ab4633f30afe1d8b99eb.png)

1.  Extra small button group
2.  Small button group

### Initial focus

The button group container is not a focusable element. Initial focus should land on the first button in the group and then move to each button.

![Focus order lands on the first button, then the next buttons.](../../_assets/m0dgsbc6-focus-e912cc87f888ef2ba524.png)

Initial focus should land on the first button, not on the container

Use **Tab** to navigate through each item in the group, and **Space** or **Enter** to select buttons.

![Button group with annotations for navigation with Tab and selecting with Space or Enter.](../../_assets/m0dgutj5-keyboard-nav-bb967ca9c3c6d82b3e71.png)

1.  Initial focus
2.  Selected button

## Keyboard navigation

| Keys | Actions |
| --- | --- |
| Tab | Navigates to the next button |
| Space or Enter | Activates the focused button |

## Labeling elements

The button group container does not need to be labeled. Label each button according to the button Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) and icon button Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview) accessibility guidance.

![In a messaging products, an email icon is labelled “email” with the role “button”.](../../_assets/m0dh20ef-label-2761dfe76b8d6ad6c444.png)

Label each button within the button group
