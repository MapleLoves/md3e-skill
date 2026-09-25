---
source: https://m3.material.io/components/progress-indicators/accessibility
title: "Progress indicators"
captured: 2026-09-14
---

# Progress indicators

> Progress indicators show the status of a process in real time

## Use cases

People should be able to do the following using the assistive technology:

-   Navigate to the progress indicator
-   Understand what progress the indicator is communicating

## Interaction & style

The active indicator, which displays progress, provides visual contrast of at least 3:1 against most background colors.

![Dark line of progress indicator stands out against the lighter colored track.](../../_assets/mlepc1r2-01-430185c6510480cf5ee9.png)

The progress indicator and stop indicator provide visual contrast of at least 3:1 against most background colors

When integrated into another component, such as a button, make sure that the active indicator provides visual contrast of at least 3:1 against the other component. 

For the active indicator, use the same color as the label text or icon. The track should be removed.

![Circular indicator on button passes 3 to 1 contrast test.](../../_assets/mlepcmau-02-2df9282dbc18c5d4a0f5.png)

check Do

Ensure the indicator’s color provides at least 3:1 contrast against the surface it's on

![Circular indicator on button fails 3 to 1 contrast test.](../../_assets/mlepd6dk-03-ffeccbde50d52d3cce89.png)

close Don’t

Avoid using a color below 3:1 contrast

For linear progress indicators, the stop indicator is required if the track has a contrast below 3:1 with its container or the surface behind the container.

Essentially, the end of the track must be easy to identify.

![Bright container holding the progress bar is on a dark surface, passing the 3:1 color contrast.](../../_assets/mlepdozy-04-12d92dff1935bdb35086.png)

check Do

Only remove the stop indicator when the linear progress indicator has at least a 3:1 color contrast with surrounding containers and surfaces

![Bright container holding progress indicator is on a bright surface, failing the 3:1 color contrast.](../../_assets/mlepe18t-05-d2f8cf9228d937d94536.png)

close Don’t

Avoid removing the stop indicator if any adjacent containers or surfaces are below the 3:1 color contrast

## Labeling elements

Since the progress indicator is a visual cue, it needs an accessibility label to describe the kind and amount of progress made.

Use the **progress bar** accessibility role, and write an accessibility label that describes the purpose of the progress indicator. The label should include the process, such as "loading,” and the affected content, such as a page, article, or episode. For example: "Loading news article" or "Refreshing page."

![Determinate linear progress indicator has an accessibility label of “loading news article” and role of “progressbar”.](../../_assets/mlepereg-06-0961d4b40c0a7994d9e7.png)

Progress indicator labels should explain which items are loading

![Indeterminate linear progress indicator has an accessibility label of “loading my episodes” and role of “progressbar.”](../../_assets/mlepf1vr-07-4b212f9d9e963198653d.png)

A label on an intedeterminate progress indicator on a screen which is loading a set of podcast episodes
