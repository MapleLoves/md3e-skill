# Motion Intent, Relationships, and Expression

[中文](motion-physics.md)

This note treats motion as design language. Recommendations are an editorial synthesis of design
resources. Consult the applicable specifications and project motion system for exact parameters;
no framework API is a prerequisite.

## Explain what happened

Motion should explain action feedback, object relationships, or state changes. Decide which
question it answers: did the action take effect, where did content go, how are states related,
and is the next action available?

If a static state already communicates clearly, movement may add little. Expression can support
meaningful moments, while frequent actions need prompt, reliable feedback. Do not require people
to wait for decoration to finish.

## Motion types and design judgment

| Type | Main purpose | What to consider |
| --- | --- | --- |
| Spatial change | Explain position, size, shape, and object relationships | Trackability and effects on surrounding reading and operation |
| Color and opacity | Explain state, visibility, and shifts in emphasis | Clear states without unreadable intermediate appearances |
| Content transition | Explain the relationship between current and incoming content | Whether continuity exists and where focus and task position go |
| Emphasis or celebration | Recognize meaningful progress or completion | Context, frequency, and interruption of subsequent actions |

Controlled overshoot can suit some spatial changes; oscillating color or opacity is not a useful
way to express elasticity. Avoid inventing an object transformation between unrelated pages just
for visual spectacle.

## Springs are an expressive tool

A spring model can support continuous, interruptible motion. First describe the desired feedback:
prompt response, gentle settling, or restrained bounce. Then use the project's motion tokens and
implementation capabilities to express it.

M3E does not mean bouncing everywhere. Choosing a spring does not establish that motion is natural,
fast, or suitable for every device. Duration and easing remain options where appropriate; choose
for relationships and experience rather than an API name.

Use related rhythms for related interactions while allowing different scale and purpose to vary.
Do not copy unverified stiffness, damping, or duration values and present them as universal
Material requirements.

## Control, interruption, and alternatives

Keep the state understandable during repeated input, cancellation, return navigation, or gesture
takeover. For significant interactions, consider input before animation completion and where focus
and content move.

Provide reduced-motion treatments according to the actual platform and user preference, preserving
feedback and operability. Less movement does not mean deleting state information; a simpler change
or alternative cue may suffice. Essential states must not be perceivable only through animation.

## UI Kit and custom motion

Reuse suitable kit feedback. New components should share the project's rhythm and state language.
When kit motion does not fit the task, adapt or replace it and explain the mismatch resolved. One
library's animation implementation is not a requirement for other platforms.

## Consult by question

- [How motion works](../m3-content/styles/motion/overview/how-it-works.md)
- [Motion specifications](../m3-content/styles/motion/overview/specs.md)
- [Transition patterns](../m3-content/styles/motion/transitions/transition-patterns.md)
- [Applying transitions](../m3-content/styles/motion/transitions/applying-transitions.md)
- [Easing and duration specifications](../m3-content/styles/motion/easing-and-duration/tokens-specs.md)
- [Applying interaction states](../m3-content/foundations/interaction/states/applying-states.md)

Evaluate timing, interruption, and reading impact in actual motion. If only a static design was
inspected, identify those aspects as unverified.
