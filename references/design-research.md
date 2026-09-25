# Design Evidence, Questions, and Verification

Use this reference when a design choice depends on evidence or when evaluating whether a treatment
helped. The recommendations below are an editorial synthesis, not a new study. Bundled official
snapshots retain their source and capture date; external reading links are retained references,
not a claim that those pages were reverified during this revision.

## Distinguish the kind of support

- **Source guidance:** a specification describes a role, component behavior, or design principle.
  Preserve its scope when applying it to another platform or project.
- **Research finding:** a study observed an outcome for particular people, tasks, and conditions.
  Read the original evidence before quoting an effect size or generalizing to a new interface.
- **Design hypothesis:** a proposed treatment is expected to help this task. Explain its intended
  effect without presenting it as an observed result.
- **Project observation:** an inspection, interaction check, or user session supplies evidence about
  this artifact. Report what actually happened and what the check did not cover.

A library's default behavior is not an independent usability finding. A popular design kit is not
proof that every arrangement of its components works.

## Color and perception

Material's color system provides a vocabulary for perceptual relationships and semantic roles.
For design work, the useful questions are what the color means, how it relates to its surroundings,
and whether its content is readable in the actual state. Theme generation belongs to the project's
existing infrastructure; this skill evaluates the resulting role relationships.

Inspect actual text, icons, surfaces, transparency, images, and light/dark states. Generated colors
or standard role names do not remove the need to check a customized composition. Semantic states
also need understandable cues beyond color.

Sources: [Color system](m3-content/styles/color/system/how-the-system-works.md),
[color roles](m3-content/styles/color/roles.md), and
[color contrast](m3-content/foundations/designing/color-contrast.md).
Background reading: [The science of color and design](https://m3.material.io/blog/science-of-color-design),
[dynamic color harmony](https://m3.material.io/blog/dynamic-color-harmony), and
[tone-based surfaces](https://m3.material.io/blog/tone-based-surface-color-m3).

## Typography and reading

A visually striking heading and comfortable sustained reading solve different needs. Evaluate the
chosen font with actual language coverage, line length, hierarchy, scale, and theme. Variable axes
can help tune expression, but do not assume a fixed weight change improves every dark-mode design.

Sources: [Applying type](m3-content/styles/typography/applying-type.md),
[fonts](m3-content/styles/typography/fonts.md), and
[text resizing](m3-content/foundations/writing/text-resizing.md).
Background reading: [Roboto Flex](https://m3.material.io/blog/roboto-flex) and
[readability research](https://m3.material.io/blog/readability-research).

## Motion and comprehension

Ask what relationship or state the animation communicates. Inspect the real transition for
interruption, repeated input, focus, and the ability to continue. A screenshot can establish
appearance, but not timing, gesture handling, or reduced-motion behavior.

Sources: [Motion](m3-content/styles/motion/overview/how-it-works.md),
[transition patterns](m3-content/styles/motion/transitions/transition-patterns.md), and
[applying transitions](m3-content/styles/motion/transitions/applying-transitions.md).
Background reading: [Choosing transitions](https://m3.material.io/blog/motion-research-container-transform).

## Hierarchy, adaptation, and inclusion

Use realistic tasks and content to ask whether the next action is discoverable, information is
grouped meaningfully, and relevant choices remain available. Width alone cannot establish a usable
layout: comparison, editing, reading, and input needs may change the appropriate composition.

Consider affected users and contexts rather than claiming universal preferences. Apply relevant
accessibility guidance during design, and distinguish visual inspection from keyboard, assistive
technology, or participant testing. Do not add a full research process to every small reversible
change; choose evidence proportional to what is uncertain.

Sources: [Applying M3 Expressive](m3-content/foundations/usability/applying-m3-expressive.md),
[adaptive design](m3-content/foundations/layout/layout-overview/adaptive-design.md),
[accessibility principles](m3-content/foundations/overview/principles.md),
[user needs](m3-content/foundations/building-for-all/user-needs.md), and
[co-design](m3-content/foundations/building-for-all/co-design.md).

## UI Kit evidence and custom design

Inspect the project's actual kit rather than assuming that a component exists or has particular
states. Official design kits can inform appearance and behavior, while project resources determine
what can actually be reused. Do not automatically use a Compose API to settle a design question
for a different stack.

When a kit lacks a suitable solution, state the mismatch and the intended benefit of the custom
proposal. Check the new composition's important relationships and behavior. Novelty alone does not
validate it, just as reuse alone does not validate a standard component arrangement.

Guidance: [Kit selection and custom design](m3e/components.en.md) / [中文](m3e/components.md).
Background reading: [Material 3 Figma Design Kit](https://m3.material.io/blog/material-3-figma-design-kit).

## Reporting a design decision

A useful short rationale names the relevant need, the consequential choice, and the expected
benefit or tradeoff. Add actual verification and remaining uncertainty when they matter. Do not
require a long process report for a small edit or claim a study was conducted because the design
was reviewed against these notes.
