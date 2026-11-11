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

## Long-running work and independent acceptance
For nontrivial multi-step work, keep a compact durable checkpoint in the approved project output: current objective/constraints, changed files, commands and observed results, baseline versus measured outcome, blockers, remaining tests and next safe step. Re-read it after compaction or handoff; stop and diagnose failed commands instead of building on assumed success. Do not put secrets or private data into shared logs.

For consequential or subjective acceptance, give an existing reviewer a fresh context containing the output, requirements and evidence, not the implementer's persuasive drafting narrative. Ask for exact unsupported claims, counterexamples and STANDS/OVERTURNED reasons; use deterministic checks where available. A second reviewer/model is not proof of truth, and required human approvals remain intact. Do not install a new agent merely to run this check.

When documenting Claude Code permissions, verify the installed version against official documentation. The documented lists are `permissions.allow`, `permissions.ask` and `permissions.deny` (deny before ask before allow); do not invent `autoApprove` or `auditLog` settings. `.claudeignore` has no effect: use documented Read/Edit rules, and OS sandbox restrictions where enforcement matters. Scoped Bash rules block matching tool calls but do not constrain every alternate invocation or subprocess. Never change settings/permissions silently or treat a prose rule as runtime enforcement.

Sources: https://x.com/i/status/2053210009689870535 ; https://x.com/i/status/2090485319665910034 ; https://x.com/i/status/2062926176117469477 ; official https://code.claude.com/docs/en/permissions re-read in full. Model pricing, benchmarks, schedules and platform commands not adopted.

## Smallest complete change (v5, added 2026-11-09)

Simplicity First above says *what* to avoid; this is the order to search for the answer. Take the first option that fully works:
1. Does it need to exist? Skip options and flexibility nobody asked for, and name what you skipped in one line.
2. Already in this codebase (helper, component, service, pattern)? Use it the way neighbouring code does.
3. Standard library or platform feature? Use it, unless the project already has its own (a house component beats a native widget).
4. An already-installed dependency? Use it. Never add a dependency for a few lines.
5. Otherwise, the minimum code that works, readable at a glance.

Rules that go with it:
- Be minimal about the solution, never about the change: finish every caller, test, fixture, config and export the change touches. For a bug fix, find every caller first and fix the root cause once in shared code.
- Moved or merged code keeps its error handling and validation. Between equal-size options, pick the one correct on edge cases.
- New non-trivial logic (branch, loop, parser, money, auth, a new script) leaves one small test or assert-based self-check; trivial edits need none.
- A deliberate shortcut gets a one-line comment: `shortcut: <the limit>, <when to upgrade>`.
- **Never cut:** validation at trust boundaries, error handling that prevents data loss, security, accessibility, hardware calibration, or anything the user asked for.
- End the reply with one or two lines: what you skipped or did not check, and any risk the user must know.
- Levels on request: *lite* (build what was asked, offer the smaller option), *full* (default, the rules above), *strict* (also push back on any part of the request the need does not justify, before building).

Source: DietrichGebert/ponytail v5.3.x core skill (MIT) https://github.com/DietrichGebert/ponytail @96608e0, principles paraphrased; its audit/review/debt sub-skills and token-gain tooling were not imported. License copy: `references/ponytail-LICENSE.txt`.

Changelog: v5 (2026-11-09) adds the smallest-complete-change ladder. v4 (2026-11-08) added test-first slices, AI-feature evaluation, parallelism boundaries and long-running acceptance.

## Code ownership and honest change reports (v6, added 2026-11-11)

Newer Claude models (Fable 5.2 and later) react strongly to who owns the code. Anthropic's guide reports that saying "this codebase is yours" made the model consolidate duplicated code far more often, but also raised output tokens a lot, added unrequested tests and docs, sometimes changed existing behaviour, and produced PR summaries that left out small changes.
- **Default: the user owns the code.** Follow Surgical Changes above. Do not restructure, consolidate or "clean up" beyond the request.
- Act as owner (consolidate duplication, fix related problems you find) only when the user or the project's CLAUDE.md says the project is yours to restructure. A scope-limiting line elsewhere does not reliably cancel an ownership statement, so do not mix the two: if both appear, ask which one applies.
- When acting as owner, list every unrequested change separately and flag any behaviour change for review.
- Build the closing summary from the actual diff (`git diff --stat` and the hunks), not from memory, so small edits are not dropped.
- Ordinary obstacles (a failing command, timeout, empty result) are diagnosed and worked through; deliberate blockers (a file marked do-not-touch, withheld access, a safety rule) are left alone and reported. This does not replace confirmation for risky or irreversible actions.

Source: Anthropic, "Prompting Claude Fable 5.2", sections "Say who owns the code" and "Finish the whole task" https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2 (read 2026-11-11, paraphrased); surfaced by bookmarks https://x.com/i/status/2120501801313267818 and https://x.com/i/status/2120316341492068383.
