---
source: https://m3.material.io/components/dialogs/specs
title: "Dialogs"
captured: 2026-09-14
---

# Dialogs

> Dialogs provide important prompts in a user flow

## Tokens & specs

Select a component variant below to see its elements, attributes, tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) , and their values.

Token

Value

Close

## Basic dialogs

![Anatomy diagram numbering dialog elements.](../../_assets/8zwGCq50u42Pisi3XIhquY9uN3sTnFAYcLYzdMcQ-7RGPou4Uyy5QzWjN3NWXlHALJhtxMM-lECAxX1_-9cb0a6ebaa9c2f549aba.png)

1.  Container
2.  Icon (optional) 
3.  Headline (optional)
4.  Supporting text 
5.  Divider (optional) 
6.  Button label text
7.  Scrim

### Basic dialog color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)

![Color mapping diagram labeling 6 color roles across the dialog and scrim.](../../_assets/OaqvzKCkUteypP4OIa5ABlelFupDNk5XXyc8cxl0SYBNXCJPqROSqNWKjvxWk1FJpSzOwqADZvwMhPgq-e50a529d0442f73e46fd.png)

Basic dialog color roles used for light and dark themes:

1.  Surface container high 
2.  Secondary 
3.  On surface 
4.  On surface variant
5.  Primary 
6.  Scrim

### Basic dialog measurements

![Annotated diagram showing padding values.](../../_assets/0b11O-Tlquj7LEzCkk4IOw1EuhHgUI6KmNyMozEEr2aANs_Q3FshFNUhXzUkn2c3occn1_9y1XSndIce-4d27d10505224dad19ab.png)

Basic dialog padding and size measurements

| Attribute | Value |
| --- | --- |
| Container shape | 28dp corner radius |
| Container height | Dynamic |
| Container width | Min 280dp; Max 560dp |
| Divider height | 1dp |
| Icon size | 24dp |
| Minimum width | 280dp  |
| Maximum width | 560dp |
| Alignment with icon | Center-aligned |
| Alignment without icon | Start-aligned |
| Top/Left/right/bottom padding | 24dp |
| Padding between buttons | 8dp |
| Padding between title and body | 16dp |
| Padding between icon and title | 16dp |
| Padding between body and actions | 24dp |

## Full-screen dialogs

![Diagram numbering 6 full-screen dialog elements.](../../_assets/DkDLF7N_cYRseSctPY0mcn5UU3s5M37UtbNZCMovSLfZacqNP1ZR-1ur4muZ0RXpZAxdcqi65q7Uc7GR-fc131f1b56c46be9a342.png)

1.  Container 
2.  Header 
3.  Icon (close affordance) 
4.  Headline (optional) 
5.  Text button 
6.  Divider (optional)

### Full-screen dialog color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value.

![Color mapping diagram shows 5 callout markers across the dialog.](../../_assets/i7xYaPoPLi48zudMGabAj82oZQLxetMFg4YojUXfY9GlrVVdonnVQurEssQzX0LHqABfe9QcTts3lMtK-92196d3f925474af00d6.png)

Full-screen dialog color roles used for light and dark themes:

1.  Surface container high 
2.  On surface
3.  On surface
4.  Primary
5.  On surface variant

### Full-screen dialog measurements

![Diagram noting layout measurements for padding values, title, height, and action regions.](../../_assets/5vPLkkKzW-CnlkhE29h4YwG8QzCsM7QdxQpOS0hRO82Ox4D7VqBbZgPWKd2nHnj916gkB29tjl7k_fnu-7d16a4fd305e5db3bec7.png)

Full-screen dialog padding and size measurements

| Attribute | Value |
| --- | --- |
| Container shape | 0dp corner radius |
| Container height | Dynamic |
| Container width | Container width; Max 560dp |
| Header height | 56dp |
| Header width | Container width |
| Headline text alignment | Start-aligned |
| Divider height | 1dp |
| Icon (close affordance) size | 24dp |
| Bottom action bar height | 56dp |
| Bottom action bar width | Container width |
| Top/left/right padding | 24dp |
| Padding between elements | 8dp |
