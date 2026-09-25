# Contributing

Contributions should improve the MD3E skill's design judgment, clarity, or supporting evidence.
The skill is framework-independent; Compose is an optional implementation appendix.

## Useful contributions

- Improve how design philosophy, values, principles, language, and ethics inform concrete choices.
- Add a well-scoped design example that clarifies hierarchy, expression, kit fit, or custom design.
- Correct or update component guidance and specification links with identifiable sources.
- Keep Chinese and English curated notes equivalent in meaning.
- Correct implementation notes when needed, without making them default design requirements.

Theme generators and starter code templates are outside this skill's scope. Exact measurements
belong in relevant specification references rather than dominating the entry point.

## Content conventions

Keep SKILL.md concise and route to references by design question. The entry point should explain
judgment and meaningful constraints without requiring every task to follow a rigid process.
Use the standard name and description fields, with the skill version under metadata.version.

Prefer official Material design guidance for design claims. Distinguish source requirements,
editorial recommendations, project decisions, and actual observations. Preserve capture dates;
editing a summary does not newly verify its source. Do not invent study results or mark a
recommendation as user-tested without evidence.

UI Kit guidance must cover suitable reuse, partial adaptation, and original design when no pattern
fits. Unavailable resources are not evidence of missing capability. Custom design should retain
shared semantics and interaction language while solving the task's actual mismatch.

## Workflow and validation

1. Create a focused branch and inspect the affected resources.
2. Make the scoped change, including corresponding translations and live references.
3. Run the repository audit from an environment with Python and PyYAML installed:

       python -m pip install PyYAML
       python audit_run.py

   Use a virtual environment for maintenance dependencies where appropriate. These dependencies
   are not needed by projects that consume the design skill.
4. If preparing a package, also run:

       python audit_run.py --archive ../dist/md3e.zip

   The archive is optional for ordinary source edits. The audit checks its content when explicitly
   supplied rather than relying on a hard-coded build date or line number.
5. Review relevant behavior cases, update CHANGELOG.md, and submit the focused change.

Useful review cases include a non-Compose UI task, an exact kit match, a partial match, no matching
pattern, and an unavailable kit. Confirm that the instructions lead to appropriate decisions and
the requested deliverable. Structural audit results alone do not prove model behavior or UI quality;
report separately any model execution or user testing actually performed.

## Release notes and license

Record breaking removals and changes in scope. Preserve historical changelog entries and follow
the version policy in [PUBLISH.md](PUBLISH.md).
Contributions use the project's [Apache License 2.0](LICENSE).
