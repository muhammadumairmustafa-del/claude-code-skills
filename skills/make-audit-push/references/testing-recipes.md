# Stack-neutral testing recipes

Select checks for the actual acceptance surface and risk. These are test designs, not executable scripts or claims of passing tests.
Use the repository's existing runner after inspecting script behavior and environment targets. No implicit installs, downloads, live paid calls, or production mutations.
If the runner or environment is missing, report the gap and perform only authorized safe analysis.

## 1. Localized regression or tiny fix

1. Record the reported input/state and expected observable outcome.
2. Reproduce safely before editing, or state why reproduction is unavailable.
3. Add one behavioral check at the narrowest stable public boundary.
4. Observe failure for the actual bug, not a syntax error or unavailable dependency.
5. Make the smallest fix; observe the check pass and run adjacent relevant checks.
6. Inspect the diff for unrelated formatting and side effects.

A copy typo may need content/render inspection rather than a full E2E suite. A tiny authorization change is not low risk.
If no test was executed, report “test written, not run”; do not describe an imagined red/green cycle.

## 2. Domain logic with an independent oracle

- Choose explicit input/output examples including a known literal result.
- Include boundaries: empty/null where allowed, minimum/maximum, invalid types, precision, time zones, or ordering as relevant.
- Do not calculate expected values using the same implementation formula or helper under test.
- Check invariants only when they reflect the contract; round-trip tests alone may hide paired bugs.
- Keep tests on public behavior; private methods and internal call counts are rarely the right acceptance boundary.

Example design: a formatter must output a specified string for a known locale/value and handle an agreed unsupported input; do not compare it with a second call to itself.

## 3. API and contract changes

- Verify valid request/response schema, status, pagination/sort stability, and backward compatibility.
- Exercise malformed input, missing required input, unknown IDs, missing/expired session, forbidden role, and cross-tenant IDs.
- Check that denied requests disclose no forbidden record payload or sensitive diagnostic.
- Confirm stable error structure and useful safe messages, not just “some error occurred.”
- Use an isolated local service or adapter fixture; label any external contract not actually contacted.
- Check caller behavior on changed contracts, not only the endpoint in isolation.

Do not send test requests to production just because an environment variable points there; inspect the target safely first without printing credentials.

## 4. Persistence, tenant isolation, and migrations

- Use disposable local/test fixtures, not customer records.
- Verify create/read/update/delete according to authorized roles and ownership.
- Test tenant A access to tenant B resources, including lists, exports, joins, and alternate identifiers where relevant.
- For direct client-accessible databases, test actual applicable row-level policies with representative roles if an authorized test environment exists.
- Verify transaction/constraint behavior and rollback on a representative failure.
- Draft migration compatibility/backfill/rollback and rehearse only in an authorized disposable environment.

Inspecting policy text is useful static evidence; it is not an executed access-control test. Never disable RLS or auth to make fixtures pass.

## 5. Async UI and resilience

Test the changed flow under controlled timing:
1. Initial load, success, background refresh, and no results.
2. Slow response; controls remain understandable and the app does not look frozen.
3. Error with retry; entered data remains and a safe next action exists.
4. Two rapid changes; resolve requests out of order and verify stale results cannot overwrite the current selection.
5. Cancellation/navigation away; stale side effects do not leak into another screen.
6. Duplicate submit/retry; state changes happen only as intended.
7. Partial/offline behavior if supported; never imply offline support that was not implemented.

Use controlled local fixtures/test doubles for timing; do not flood a live service to simulate failures.

## 6. Real rendered UI and accessibility

- Start the inspected local app using an authorized environment.
- Record route, fixture, viewport/device, theme, zoom/text scale, state, and revision.
- Compare narrow and wide views; inspect an intermediate width if layout changes there.
- Exercise keyboard-only main flow, focus visibility, label/error association, dialog lifecycle, and recovery.
- Inspect long content, no content, missing images, fixed headers/footers, and reduced motion.
- Run available automated checks, recording their actual output and scope.
- Test a screen reader or native accessibility tool only if actually available; otherwise mark NOT RUN.
- Capture screenshots without private data and explain discrepancies using concrete observations.

Browser emulation is not real-device evidence. Automated accessibility results are not assistive-technology certification.
A code-only review cannot truthfully claim the layout was visually verified.

## 7. CLI, library, and non-visual changes

For a CLI, check relevant help/usage, exit codes, stdout versus stderr, valid/invalid inputs, piped/noninteractive behavior, and safe file handling.
For a library, check public imports/exports, behavior contracts, supported runtime versions, serialization, and packaging with existing local tools.
For a non-behavioral refactor, compare observable behavior before/after and run regressions around changed seams.
For configuration/infra, validate or inspect the plan; no live apply, resource creation, publishing, or production changes by implication.
Skip visual branding when no interface is affected, but keep error/output usability where it matters.

## 8. Performance and dependency changes

- Define the relevant user outcome: faster route, smaller payload, bounded memory, fewer queries, or stable rendering.
- Measure the baseline and changed version with representative inputs in a stated environment.
- Use repeated samples appropriate to the tool; distinguish cold/warm state and local noise.
- Report observed values and limitations, not absolute product-wide guarantees.
- For motion/sequences, inspect byte budget, decode/memory, frame loading, low-resource fallback, and reduced motion.
- For dependency changes, inspect purpose, compatibility, license, transitive scope, and lockfile changes.
- Advisory status is NOT CHECKED if an authorized existing advisory source was unavailable; do not auto-install a scanner.

Do not introduce caching, memoization, or virtualization without evidence that complexity is justified and behavior remains correct.

## 9. AI-dependent product behavior

- Separate deterministic plumbing checks from quality evaluation.
- Use representative cases, known failures, and a held-out regression set when authorized data exists.
- Label each evaluation deterministic, model-judged, or human-reviewed.
- Preserve relevant prompt/model/data versions without recording private prompt payloads in public artifacts.
- Compare one controlled change; review regressions as well as wins.
- Check prompt injection, sensitive data exposure, tool authorization, and resource/turn caps.
- Do not make paid inference calls by default, invent quality scores, or treat a judge model as ground truth.
- Unknown live behavior remains NOT TESTED rather than silently passed.

## 10. Evidence refresh and blockers

After any fix, rerun the failing check and affected adjacent checks. Mark evidence stale if relevant code or fixtures changed.
Record exact commands, selected/skipped checks, exit statuses, and observed results with the current artifact identity.
If a command fails, inspect the failure before continuing; do not assume it was an environment problem without evidence.
Use at most three focused fix cycles per unresolved issue by default, then escalate with hypotheses and observed outcomes.
Do not weaken a test, skip a security assertion, or replace a broken real integration with a passing mock just to report green.
The final approval packet must say what was not tested and why, even when all available checks pass.
