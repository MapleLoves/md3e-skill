---
source: https://m3.material.io/components/checkbox/specs
title: "Checkbox"
captured: 2026-09-14
---

# Checkbox

> Checkboxes let users select one or more items from a list, or turn an item on or off

## Tokens & specs

Browse the component elements, attributes, tokens, and their values.

Token

Value

Close

## Checkbox

![Diagram of checkbox indicating the 2 parts of its anatomy.](../../_assets/o7Jd5nbugG-76fMDJwv-WD-ardrEfZF5Nxfq_8Pikz0V6pnzJXvDA6C4NPzOpZ3z39Rjb6tb1yxxQs8G-dff7ce0c610504d0c422.png)

1.  Container 
2.  Icon

## Color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)

![Checkbox color roles in light and dark themes.](../../_assets/tRScc_0bS1gM7jai2Ojj3qDzyhE696wedzZNPry2Pson8ONvZ_S_IoRUO6RwZBC5-YQUmgqLKG0xWldI-9249ba415215aa1faa85.png)![Checkbox color roles in light and dark themes.](../../_assets/tRScc_0bS1gM7jai2Ojj3qDzyhE696wedzZNPry2Pson8ONvZ_S_IoRUO6RwZBC5-YQUmgqLKG0xWldI-4efdf170998318d68251.png)

1.  Checkbox
2.  State-layer
3.  Icon

### Adjacent text label color

Use the color role Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme. **on surface** for adjacent text labels. This remains the same even if interacting with the label or component.

![Checkboxes with text labels. The text color is the same for checked and unchecked checkboxes.](../../_assets/712ygEoSMR9tGvygN9LKJ8DZ7BhOWkzxv1y86AilaXmqdTa30fz5WP68koUEZThkz30akxDDI3CUbIxJ-f7371a67e5a1246174ec.png)![Checkboxes with text labels. The text color is the same for checked and unchecked checkboxes.](../../_assets/712ygEoSMR9tGvygN9LKJ8DZ7BhOWkzxv1y86AilaXmqdTa30fz5WP68koUEZThkz30akxDDI3CUbIxJ-315a844ae6414b37efec.png)

The text color remains the same regardless if the checkbox is selected or not

## States

States are visual representations used to communicate the status of a component or interactive element. [Learn more about interaction states](/m3/pages/interaction-states/overview)

![Side by side view of states in light and dark themes.](../../_assets/Yor59BqmDg2qk4vgXtDVI9FzkAcqUFQZ4EjWrwLc_rYafcVTgirLkf-bt1t7JbvpRyPYQYvrP8ZM_ZgY-b04bb20c7df0e601a4c0.png)![Side by side view of states in light and dark themes.](../../_assets/Yor59BqmDg2qk4vgXtDVI9FzkAcqUFQZ4EjWrwLc_rYafcVTgirLkf-bt1t7JbvpRyPYQYvrP8ZM_ZgY-8bde9f61955f1c3800b0.png)

1.  Enabled 
2.  Disabled 
3.  Hovered 
4.  Focused 
5.  Pressed

## Measurements

![Diagram of a selected checkbox with a container width and height of 18dp and a state-layer width and height of 40dp.](../../_assets/CcUqIZiHlrkBXYmqL54pCjCjsNpVnHsMf6QdUXITGzV89PkHrNbV84_w9I5ZgcNPlMFcCVbTxYhZzVbM-e03e93404306b0cd7d51.png)![Diagram of a selected checkbox with a container width and height of 18dp and a state-layer width and height of 40dp.](../../_assets/CcUqIZiHlrkBXYmqL54pCjCjsNpVnHsMf6QdUXITGzV89PkHrNbV84_w9I5ZgcNPlMFcCVbTxYhZzVbM-2c34b6215ba25ef51a5d.png)

| Attribute | Value |
| --- | --- |
| Container size | 18dp |
| Container corner shape | 2dp |
| Icon size | 18dp |
| Icon alignment | Center-aligned |
| Target size | 48dp |
| State-layer size | 40dp |
