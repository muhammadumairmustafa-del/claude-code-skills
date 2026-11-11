# Lean evidence and handoff templates

Adapt these to the task. Keep them in chat or an agreed scratch location unless the user wants project documentation.
Do not create every file automatically. Do not store private records, secrets, raw environments, or full chat transcripts.
Replace placeholders with actual observations; a filled template is not evidence by itself.

## 1. Initial plan and brief

```text
Task/outcome:
Mode: implementation / design-only / audit-only
Lane: quick / standard / deep — reason:
Users and context:
Primary flow:
In scope:
Non-goals:
Existing stack/brand/contracts to preserve:
Known facts:
Assumptions safe to proceed with:
Decisions needed before proceeding:
Steps → verification:
1.
2.
3.
No commit/push until the final reviewed-change approval gate.
```

## 2. Acceptance traceability

| ID | Observable behavior / independent expected result | Changed area | Verification method | Current evidence | Status/gap |
| --- | --- | --- | --- | --- | --- |
| AC-01 | Given [state], when [action], then [outcome] | [path/flow] | [test/manual check] | [evidence ID and state] | [pass/fail/not tested/stale] |

Keep expected results independent of implementation details. An assertion that calls the same function twice is not a reliable oracle.
Do not mark AC-01 passed because a test file exists; record its actual execution or a relevant manual observation.

## 3. Phase coverage

| Phase | RAN / SKIPPED / NOT AVAILABLE / BLOCKED | Result or reason | Evidence and limitations |
| --- | --- | --- | --- |
| Discovery | | | |
| Brief and architecture | | | |
| Product/visual design | | | |
| Implementation | | | |
| Correctness and security | | | |
| Accessibility and interaction | | | |
| Rendered visual review | | | |
| Performance | | | |
| Tests/build | | | |
| Git handoff | | | |

“Skipped: backend-only; no visual interface changed” is different from “not available: no browser to check changed UI.”
A phase can run and fail. A final Git phase can remain blocked awaiting approval while implementation is complete.

## 4. Evidence log

```text
Evidence ID:
Claim / acceptance IDs:
Status: OBSERVED / REPORTED / INFERRED / NOT TESTED / STALE
Artifact state: HEAD + owned-diff fingerprint or equivalent
Command or manual steps:
Working directory / local test target:
Environment/tool version relevant to interpretation:
Outcome, exit status, selected tests, skipped tests:
Safe excerpt or screenshot location:
Coverage limits / follow-up:
```

Do not paste secret-bearing commands or URLs. Use safe descriptions or redacted excerpts when needed.
A changed revision does not automatically invalidate all tests; identify the affected checks and rerun the relevant subset with a reason.
A clean HEAD alone cannot identify dirty uncommitted work: include an owned-diff/content identifier.

## 5. Visual capture note

```text
Screen / route:
Revision + dirty-state scope:
Viewport/device and scale:
Fixture / account role (synthetic, no credentials):
State: normal/loading/empty/error/etc.
Theme, reduced-motion, zoom/text size:
What was actually exercised:
Observed discrepancy from brief:
Artifact location, privacy reviewed:
Not covered: e.g. physical device, screen reader, other browser
Reviewer: separate agent / self-review / not performed
```

A generated image or design mock is not an actual rendered screenshot. A screenshot alone is not proof of keyboard or screen-reader behavior.

## 6. Finding and retest

```text
Finding ID / priority:
Area / location / flow:
Observed failure or suspected risk:
Reproduction / counterexample:
Impact and evidence:
Introduced / pre-existing / attribution uncertain:
Proposed scoped fix:
Cycle 1: hypothesis, change, check, observed result
Cycle 2: hypothesis, change, check, observed result (if needed)
Cycle 3: hypothesis, change, check, observed result (if needed)
Disposition: fixed + verified / deferred with reason / blocked
```

P0/P1 block readiness and commit/push. P2/P3 may be explicitly deferred according to scope, not quietly dropped.
Do not give a “design score” unless an actual agreed, reproducible rubric and evaluation exist; concrete findings are preferable.

## 7. Fresh-context reviewer brief

```text
Review responsibility: correctness / security / design / accessibility / tests
Task and user acceptance criteria:
Scope / non-goals / contracts to preserve:
Current artifact revision and owned diff:
Relevant files and safe local execution instructions:
Observed evidence and known gaps:
Inspect artifacts directly. Seek counterexamples and unsupported claims.
Return: finding, location, reproduction/reasoning, impact, severity, evidence status.
Distinguish verified defect, plausible risk, and unknown.
Do not edit, install, publish, or change permissions.
```

Only call this independent if a real separate reviewer/tool session performed the review. Reading your own answer again is self-review.

## 8. Long-session checkpoint

```text
Current objective and mode/lane:
Constraints and approval boundaries:
Original HEAD/branch and pre-existing changes:
Owned files/hunks:
Latest current artifact fingerprint:
Acceptance status and last observed checks:
Open findings / blocked tools:
User decisions already given and their exact scope:
Next safe step:
```

On resume, recheck the repo and evidence freshness. A checkpoint records a state; it is not permission to commit, push, or bypass new drift.

## 9. Final approval packet

```text
Prepared outcome:
Changed files/areas and readable diff summary:
Pre-existing/user changes excluded:
Acceptance criteria and phase coverage:
Tests: exact safe commands, observed outcomes, current revision scope
Visual/accessibility/security/performance evidence and limitations:
Open findings and untested integrations:
Proposed commit message:
Owned paths/hunks proposed for inclusion:
Current HEAD + reviewed diff identifier:
Branch:
Sanitized remote/destination:
Actions requested: commit and push / commit only / push existing reviewed commit
Question: Approve committing these reviewed changes and pushing this branch to this remote?
Status now: not committed or pushed — awaiting approval
```

Adapt the question for commit-only/push-only requests. Do not imply approval of deploy/release/PR creation.
After approval, recheck content, HEAD, branch, staged index, and destination. Drift requires refreshed review and approval.

## 10. Final report

```text
Changed:
Verified (observed):
Not verified / known risks:
Git: [not committed / local commit hash / push failed / push confirmed to branch and remote]
Next safe action:
```

If a push fails, report the local commit and exact failure category without exposing credentials. Do not retry a denied action by another route.
