---
source: https://m3.material.io/components/text-fields/specs
title: "Text fields"
captured: 2026-09-14
---

# Text fields

> Text fields let users enter text into a UI

## Tokens & specs

Browse the component elements, attributes, tokens, and their values. [Learn about design tokens](/m3/pages/design-tokens/overview)

Close

## Filled text field

![Diagram of a filled text field indicating the 10 parts of its anatomy.](../../_assets/X9POJ7yw_vGiALE8gBKfttJ_56zdy0ncjv5fYNyJVl1Y8SzdDbDA2VCVqWZDA0BYUfjgn3o1jfQ__CB1-01ff3895efa8536bd3a3.png)

1.  Container

2.  Leading icon (optional)

3.  Label text in empty field

4.  Label text in populated field

5.  Trailing icon (optional)

6.  Focused active Indicator

7.  Caret

8.  Input text

9.  Supporting text (optional)

10.  Enabled active indicator

### Filled text field color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)

![Diagram of a filled text field indicating its color mappings. ](../../_assets/3QvK6g9HSsTheSVwbJnhS3xny_okcH05M7S-VzIzT8Y20T1azDNw3ab6oTjCFDJDqfz8rgA9If_Ra96--2f4844214eb269b49128.png)

Filled text field color roles used for light and dark schemes:

1.  Surface container highest

2.  On surface variant

3.  On surface variant

4.  Primary

5.  On surface variant

6.  Primary

7.  Primary

8.  On surface

9.  On surface variant

10.  On surface

### Filled text field states

States are visual representations used to communicate the status of a component or interactive element. [Learn more about interaction states](/m3/pages/interaction-states/overview)

![Side by side view of empty and populated filled text fields across different states, showing the differences between enabled, focused, hovered, and disabled. ](../../_assets/oKmfNMCJ_ViUQMDGqTLkxCQj9pqlu69kIuzt96fo0YC7mb_vceZF4LQUwYQViUk_oDf38-KSOFZVsM8C-8c9f48c16510f80fbfb3.png)

1.  Enabled (empty)
2.  Focused (empty)
3.  Hovered (empty)
4.  Disabled (empty)
5.  Enabled (populated)
6.  Focused (populated)
7.  Hovered (populated)
8.  Disabled (populated)

### Filled text field error states

Error states States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or interactive element. An error message can display instructions on how to fix it. Error messages are displayed below the text field as supporting text until fixed.

![Side by side view of empty and populated filled text fields across different error states, showing the differences between enabled, focused, hovered. ](../../_assets/nuNzqyBbqzPQww1YvytMccqt-cGwmw0Brm79oYB6w-Z1am626wYtqGd6pN2nx393wXxEIJRPia-Fb3Wu-c3fed180df5e1675449b.png)

1.  Enabled (empty)
2.  Focused (empty)
3.  Hovered (empty)
4.  Enabled (populated)
5.  Focused (populated)
6.  Hovered (populated)

### Filled text field measurements

![Diagram showing layout values and paddings for filled text fields without icons. ](../../_assets/2AoiwzxCOioxZi9xQyWBalI9wO_Q2Xvt-udVeaI-UDY00zFWxtWZHUvOZa5PFbRwRJrOOQDlMra63kpm-2785789c9a07575d72d6.png)

Padding and size measurements without icons

![Diagram showing layout values and paddings for outlined text fields with leading and trailing icons. ](../../_assets/hG_Z6Lx5Jfmhqu7Rnds8d_Ia4DGHtlVW1oCZbwwqD29FtoXf2_g24bzr81cvy3i7nQxSxDzTXYqKrZ4k-52e3f06e7d63eb92bbfc.png)

Padding and size measurements with icons

![A diagram showing layout values and paddings for supporting text, and supporting text in combination with a character count. ](../../_assets/QbiBv3lVHm9nL8hoQllo5jKgQ6AA37Ngmcd3R0DuB37MAANtap_k0woqbUvLxZJqDgPznP0tIBzy1o0G-431fbc7ef9f4ead2a94f.png)

Padding and size measurements with supporting text and character count

| Attribute | Value |
| --- | --- |
| Default container height | 56dp |
| Label alignment (unpopulated) | Vertically centered |
| Top/bottom padding | 8dp |
| Left/right padding without icons | 16dp |
| Left/right padding with icons | 12dp |
| Icon alignment | Vertically centered |
| Padding between icons and text | 16dp |
| Supporting text and character counter top padding | 4dp |
| Padding between supporting text and character counter | 16dp |
| Target size | 56dp |

### Filled text field configurations

![Side by side view of filled text fields in different configurations.](../../_assets/KpOprJPDbuBUSURPtov109LS7MrNCFY0Ek20qjx5tGAzycWbhUb1YSwjT7Bc7KEu3_7woFXY5msSf47V-545464f7a4c582634917.png)

Empty and populated filled text fields with:

1.  Supporting text

2.  Trailing icon

3.  Leading icon

4.  Leading and trailing icons

5.  Prefix

6.  Suffix

7.  Multi-line text field

## Outlined text field

![Diagram of an outlined text field indicating the 9 parts of its anatomy](../../_assets/juT_ZbiIpoR4u-rL6ab7C0pqjMMp9nEOCEx43GdSNJ0jPkt4RAwIeOy3k047QwD4VLaHhkG4Xc7ZW5tN-872c20f2c7b84ffc0d88.png)

1.  Enabled container outline

2.  Leading icon (optional)

3.  Label text in empty field

4.  Label text in populated field

5.  Trailing icon (optional)

6.  Focused container outline

7.  Caret

8.  Input text

9.  Supporting text (optional)

### Outlined text field color

Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)

![Diagram of an outlined text field indicating its color mappings ](../../_assets/QRrrzuYpe5zpPsCu6AbhllIu1DaJBehUTcv2cIVtd6O7bLdl-ZuUnukzJePt9Y4_-szZKPRj8u0vgwnR-22fdcc9209d99a48da63.png)

Outlined text field color roles used for light and dark schemes:

1.  Outline
2.  On surface variant
3.  On surface variant
4.  Primary
5.  On surface variant
6.  Primary
7.  Primary
8.  On surface
9.  On surface variant

### Outlined text field states

States are visual representations used to communicate the status of a component or interactive element. [Learn more about interaction states](/m3/pages/interaction-states/overview)

![Side by side view of empty and populated outlined text fields across different states, showing the differences between enabled, focused, hovered, and disabled. ](../../_assets/7ChV4X-ZSeY8_BCyeu3u3qdlGOmI9fGOOM00iO7V4hK0Ci3rwp_hy9EoMRpsX5t-SnO-nesLg-wBoom_-3e628ac5c97a7c694848.png)

1.  Enabled (empty)
2.  Focused (empty)
3.  Hovered (empty)
4.  Disabled (empty)
5.  Enabled (populated)
6.  Focused (populated)
7.  Hovered (populated)
8.  Disabled (populated)

### Outlined text field error states

Error states States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or interactive element. An error message can display instructions on how to fix it. Error messages are displayed below the text field as supporting text until fixed.

![Side by side view of empty and populated filled text fields across different error states, showing the differences between enabled, focused, hovered. ](../../_assets/JzpL2KJVz10gQRdqaY43CbT_rimzZySTQc-l3ZSUVIdVIYgAXeOvtbuBqIpR3MUIV7uGKVPnHPzTZ8N0-905c3c753ec6e11bd64f.png)

1.  Enabled (empty)
2.  Focused (empty)
3.  Hovered (empty)
4.  Enabled (populated)
5.  Focused (populated)
6.  Hovered (populated)

### Outlined text field measurements

![A diagram showing layout values and paddings for outlined text fields without icons. ](../../_assets/fbPahcRVZOrZP4b6Iro8dbT09lSK22S5Fy_Pi_z0Kjiqd_11BD-7MOoRsO3qcXo5x--D8HprVru2ChlR-7f9f8825423720519238.png)

Padding and size measurements without icons

![A diagram showing layout values and paddings for outlined text fields with leading and trailing icons. ](../../_assets/IPC3bKvB5geLDysQJQQsC4IYzNggiZUaqGguykwiwZvUKkNbtAH4_QXRM2MRS3kK04txiDciUgwDAPqL-fd1edd82ed1b95193cd6.png)

Padding and size measurements with icons

![A diagram showing layout values and paddings for supporting text, and supporting text in combination with a character count. ](../../_assets/JjJwZsUzwXoqZBtCVcypOsMMq3BPaHVC11s604XWSrXVgPsm5_Jd2mFcMk0lbxVFr2XZSOrtwQeGZAyt-ae0f14e224646ef6c733.png)

Padding and size measurements with supporting text and character count

| Attribute | Value |
| --- | --- |
| Container height | 56dp |
| Left/right padding without icons | 16dp |
| Left/right padding with icons | 12dp |
| Padding between icons and text | 16dp |
| Icon alignment | Vertically centered |
| Supporting text and character counter top padding | 4dp |
| Padding between supporting text and character counter | 16dp |
| Label alignment | Vertically centered |
| Left/right padding populated label text | 4dp |
| Target size | 56dp |

### Outlined text field configurations

![A side by side view of outlined text fields in different configurations.](../../_assets/FpsbRTgumDQyTLpD4LAvrmPPGOU5CXnJFFxPPHNWfN6Fml9KUbuwsV-Uzz7EWlfTKXjfUnGqwv0l1HqT-4d674151b36e6f48abbe.png)

Empty and populated outlined text fields with:

1.  Supporting text

2.  Trailing icon

3.  Leading icon

4.  Leading and trailing icons

5.  Prefix

6.  Suffix

7.  Multi-line text field
