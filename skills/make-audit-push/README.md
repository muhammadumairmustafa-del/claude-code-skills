# make-audit-push

Generic full-product orchestration for Claude Code, version **2.2.0**. Install into `~/.claude/skills/make-audit-push/` (include the `references/` folder). Invoke `/make-audit-push <requested change>`. With no argument, it asks what to build.

Discovers and briefs, designs only where relevant, builds, audits independently when available (labels self-review otherwise), runs actual tests, fixes and records coverage. Existing specialists are reused by reference, not duplicated or changed. Pushes only after explicit approval. Never deploys/releases/opens PRs unasked.

Supporting files:

- `references/studio-checklists.md`
- `references/evidence-templates.md`
- `references/testing-recipes.md`

Original generalized authoring, root MIT. Static/frontmatter review is not a real Claude task evaluation. No task-performance promise.
