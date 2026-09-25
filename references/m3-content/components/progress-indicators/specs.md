---
source: https://m3.material.io/components/progress-indicators/specs
title: "Progress indicators"
captured: 2026-09-14
---

# Progress indicators

> Progress indicators show the status of a process in real time

## Variants

![2 variant of progress indicators.](../../_assets/fLmSSW0vCAz72TSdfqeo9FQY5YlgLT7ktKAZkxs-FEetsANoory1UPDxRd3-jESQSkUeq6xuwEtp1NcR-617718d72fdad578ecec.png)

1.  Linear progress indicator
2.  Circular progress indicator

| Variant | M3 | M3 Expressive |
| --- | --- | --- |
| Linear progress indicator | Available | Available |
| Circular progress indicator | Available | Available |

## Configurations

![4 configurations of the linear determinate progress indicator.](../../_assets/Cf6AdPUEQffL-k5D1on9M3H1oyAGh20uJyfa7sbOwip6oRPvmqv7u2MSLKrH70PpyL0bCJdy2fGRNg_1-be3bff14a7c00cc45cbb.png)

1.  Behavior: Determinate and indeterminate
2.  Thickness: Default (4dp) and variable
3.  Shape: Flat and wavy

| Category | Configuration | M3 | M3 Expressive |
| --- | --- | --- | --- |
| Behavior | Determinate (default), Indeterminate | Available | Available |
| Track thickness | Fixed (4dp)  | Available | Available |
| Configurable | \-- | Available |
| Shape | Flat (default) | Available | Available |
| Wavy | \-- | Available |

## Tokens & specs

Browse the component elements, attributes, tokens, and their values. [View baseline tokens](/m3/pages/progress-indicators/specs#c6f484b0-2bc6-4d37-bd75-f859a35a3594)

Token

Value

Close

## Anatomy

![3 elements of a progress indicator.](../../_assets/d1mWcS4gytQf_XcgwvUqsNTf47P5BT9PUo-Ivi-7Ld1_Vc_HAtLGPARxwbqUcN7gdc-JH4iXM0nRH137-6076e017725fba3e3dc7.png)

1.  Active indicator
2.  Track
3.  Stop indicator

## Color

![2 color roles of a linear progress indicator in light and dark themes: the active indicator and stop indicator are primary and the track is secondary container.](../../_assets/CrzKce-9x2GrD2SOdyYCmDhdK37XcZoiMv9mT6N0NjUybL1GwXLN52_LbXb1AKfzmLUna1jMew5x0skK-a02ec68dcf4b53c93f2d.png)

Progress indicator color roles used for light and dark schemes:

1.  Primary

2.  Secondary container

## Measurements

Wavy indicators use **amplitude** and **wavelength** to determine the shape of the wave. The height is the overall container height.

![Definitions of wave measurements for height and amplitude.](../../_assets/Aii3LLGqfr5jLHSdMLKx4rMUceBixyyXu77IqvYcUoMGwV8MxqqZgcB0XU6nx7GpVeU7_sqdq6ScJE4e-9094e9a156ebfd8d7079.png)

**Amplitude** measures from the center of the resting position to the center of the peak

![Definitions of wave measurements for wavelength.](../../_assets/hYbEOpy3GfIuFxLUfMLU_r3VijC9KNldOlFhXM3oEYputn_p6YvzArLiC3dZWgzuuzVOfrsX2LUhP6BQ-b3537aab5943ad78ec74.png)

**Wavelength** measures the distance between two adjacent peaks

![Linear progress indicator measurements.](../../_assets/M-64WwKIqgmV6lWqTh7Ar7vJuUsvjqLTnOJcMLrFPbW4nxRmYITD4GbXXEGCjwK2eJLUBGlfD1rtb86s-3b97d019e806029969a8.png)

Size measurements for linear progress indicators. The thicker variants are provided as sample measurement for makers to adjust the default version based on their use cases. 

![Circular progress indicator measurements.](../../_assets/8oX70XRFeRqxFH1vBkx8z4hy6nKrvShQvQsQuR8emIWoXRKU8OWnK5pdFx-Q8ZwF0d4w8qDLi5NqPYAq-9a7679edaf6a2bb9479a.png)

Size measurements for circular progress indicators. The thicker variants are provided as sample measurement for makers to adjust the default version based on their use cases. 

![4dp padding on the left and right of the linear progress indicator.](../../_assets/6_sdBcuvKe2j9XDUC70bzaxi8QsZW1507V6pQ9ZQstst3B_Y8w26_5Yuz504uIxL_GcrMfNhJFvNiQot-7b01c3dd22670a95cfbe.png)

The linear progress indicator is inset from the edge of the screen by 4dp

## Baseline tokens

The circular and linear progress indicator had separate token sets. These are no longer recommended.

Token

Value

Close
