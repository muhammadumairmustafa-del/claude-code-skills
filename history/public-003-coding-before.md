# coding — reviewed extension only

This is an original extension, not a copy of an existing base skill. Review and merge into your own matching workflow; do not create a duplicate trigger.

## Research extension — Evidence-backed test-first slices

When the user requests test-first implementation or a bug fix:
1. State the observable behavior, public interface and one independent expected result. Identify what the test will not cover.
2. Agree the meaningful test boundary; read existing domain vocabulary and architecture decisions rather than inventing new layers.
3. Add one failing behavioral test, observe the failure, make the smallest implementation change and observe it pass. Repeat one vertical slice at a time.
4. Avoid testing private methods, over-mocking internal collaborators, or computing expected values with the implementation's own formula. Include a known literal, worked example or independently derived oracle.
5. Keep refactoring separate and scoped; re-run relevant existing tests and report exact commands, observed outcomes and remaining gaps. Do not claim a test ran if only its code was reviewed.

Upstream reference reviewed: https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md (MIT). Adapted principles only; no upstream scripts or implicit dependency on its other skills. Reviewed source and original MIT notice are included under upstream-references/mattpocock-skills/.

## AI-feature evaluation loop

For work whose output depends on an LLM, passing deterministic unit tests is not sufficient evidence of product quality. Preserve representative real failure cases and a held-out regression set. Classify each check as deterministic, model-judged or human-reviewed; calibrate model judges against independent human examples and report their limitations. Compare a baseline against one controlled change using task-relevant quality, failure, latency and cost measures. Record prompt/model/data versions and inspect traces for drift, prompt injection and data exposure. Use scoped goals, resource/turn caps and a no-progress abort; never let an implementer alone declare a subjective quality target satisfied. Security, finance, authorizations and deployment still require the appropriate human gates.

Source: https://x.com/i/status/2090840747738374568 (full article read; conceptual roadmap, not a reproduced benchmark). See also the critically reviewed harness/loop article https://x.com/i/status/2107826459804840072 . Provider prices, model claims and runtime command semantics from that article are not adopted as facts.

## Parallelism and enforcement boundaries
Before parallel writers, assign disjoint worktrees/branches and an integration owner. Worktrees isolate checkouts, not credentials, shared databases, production services or provider budgets. A prose NEVER rule is guidance, not an enforced permission. State which runtime permissions/sandbox restrictions actually exist and what was only requested; do not copy broad allowlists or call a short deny-pattern list a security boundary. Validate command/flag semantics for the installed tool version before use.

Sources: https://x.com/i/status/2056319284641460626 ; https://x.com/i/status/2068468824421364103 ; official permission semantics checked at https://code.claude.com/docs/en/permissions . Attributed corporate configurations and cost anecdotes remain unverified.
