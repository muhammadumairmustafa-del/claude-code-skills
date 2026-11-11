# Expanded studio and audit checklists

Use only applicable sections. This is a decision aid, not proof that a check ran.
The SKILL.md approval and safety gates always apply. Record “not applicable” versus “not tested” distinctly.

## A. From request to useful product

- Can the intended person recognize what the interface does without an explanation from its maker?
- Is the primary task explicit? What user action demonstrates completion?
- Are domain vocabulary, permissions, and real constraints reflected in the flow?
- Which steps are necessary versus habitual? Can repeated entry or an avoidable confirmation be removed safely?
- Are navigation, page titles, and back behavior consistent with neighboring screens?
- Does the design preserve the existing user's work and mental model?
- Are any claimed metrics, testimonials, pricing, or capabilities actually supplied and authorized?
- Are mock content, sample records, and unavailable integrations visibly labelled?
- Is the proposal small enough to finish and verify in the agreed scope?

## B. Direction sheet before visual construction

Record a compact direction rather than a pile of aesthetic adjectives:

| Decision | Record | Verify against |
| --- | --- | --- |
| Audience/context | Role, task, device, viewing conditions | Brief and actual supported contexts |
| Density | Spacious, balanced, or dense and why | Task speed and readable content |
| Hierarchy | First, second, third visual priority | Actual screen at narrow/wide sizes |
| Type | Roles, weights, line heights, measure, fallback | Long copy and supported scripts |
| Surfaces/color | Semantic roles and theme behavior | Contrast and state distinction |
| Components | Existing primitives and needed changes | Project conventions and state matrix |
| Motion | Meaning, timing, interruption, static equivalent | Actual reduced-motion behavior |
| Assets | Source, permission, dimensions, fallback | Real bundled/rendered output |

A reference can demonstrate a visual pattern; it does not prove higher conversion, faster task completion, or accessibility.
Do not copy a reference's logo, protected copy, imagery, or paid specification into the deliverable.
Do not require a new font, asset service, generator, or design tool if the existing stack is sufficient.

## C. Screen and content quality

- One clearly dominant task per task-oriented region; competing actions intentionally subordinate.
- Titles explain location and purpose; paragraphs carry information rather than marketing filler.
- Related elements align and group; separators, cards, and shadows have a reason.
- Spacing communicates hierarchy instead of repeating one gap everywhere.
- Text wraps without hiding important differences; abbreviations have context.
- Icons are visually consistent and understandable; text is not replaced by ambiguous decoration.
- Supplied logos preserve original geometry and usage rules.
- Data visuals include units, time range, freshness, sources where required, and meaningful absence states.
- Chart legends and important values do not depend on hover; provide equivalent readable data when needed.
- Tables expose appropriate headers and sort state; narrow-screen handling is intentional.
- No arbitrary “premium” effects that harm legibility, performance, or task focus.
- No unsupported claims that the implementation is pixel-perfect or production-proven.

## D. State review worksheet

For each relevant item, record expected rendering, action, accessible semantics, and check evidence.

| Element/flow | Normal | Pending/empty | Error/recovery | Other high-risk state |
| --- | --- | --- | --- | --- |
| Navigation | Current location and route | Destination unavailable | Unknown route/back recovery | Focus, narrow layout, access denied |
| Search/filter | Results and selected filters | Searching, no matches | Request failed; keep query | Rapid changes, stale response, keyboard |
| Form | Editing with labels | Submitting with feedback | Field/server errors; keep input | Duplicate click, cancellation, timeout |
| Data table | Rows, units, sorting | No data, background refresh | Partial data or fetch failure | Long content, pagination, narrow width |
| Modal/sheet | Correct focus and role | Pending action | Failure without data loss | Escape, focus return, unsaved changes |
| Asset/media | Intended image/rendering | Reserved space and fallback | Static usable fallback | Slow/offline, source changes, theme |
| Account/permissions | Authorized action | Session checking | Expired versus forbidden | Cross-tenant request, signout |

The matrix is selective: a static documentation heading does not need a submitting state.
A disabled appearance is not an excuse for a button with no discoverable explanation or recovery path.
When feedback is critical, do not rely on a disappearing toast alone.

## E. Responsive, localization, and real-device review

- Test widths around actual layout transitions, not only a set of fashionable device presets.
- Observe a narrow screen and a desktop screen for meaningful web changes; record exact widths used.
- Check content order when columns collapse and when navigation changes form.
- Check sticky headers/footers against the viewport, focused elements, and keyboard.
- Keep controls out of device safe areas and system gesture zones as appropriate.
- Test long strings, unbroken identifiers, large/negative values, empty values, and long lists.
- Check locale-aware dates and numbers; do not silently mix units or time zones.
- For supported RTL, verify logical spacing, reading order, directional icons, and mixed-script content.
- Text zoom/system text scaling must not make the primary task impossible.
- Landscape is a separate check where the flow or platform needs it.
- A browser mobile viewport is not proof of native device behavior or hardware performance.

## F. Accessibility review by actual input mode

### Semantics and reading
- Prefer built-in button/link/input controls with correct purpose; navigation and action are not interchangeable.
- Visible labels and accessible names should agree; do not duplicate announcements with unnecessary labels.
- Images: meaningful alternatives for meaning; decorative images excluded from redundant announcements.
- Headings/landmarks form a coherent navigation structure.
- State changes, field errors, selection, and expansion are programmatically conveyed where applicable.

### Keyboard and focus
- Complete the main flow without a pointer; check focus visibility and order.
- Enter/Space/Escape behavior follows the control pattern; no keyboard traps.
- Modal focus is intentionally placed and restored; hidden content is not accidentally focusable.
- Custom widgets implement their actual pattern, not a pile of clickable divs with labels.
- Focused content stays visible behind sticky elements and the virtual keyboard.

### Perception and motor access
- Check the actual rendered contrast pairs, not just token names.
- Normal text needs 4.5:1 for WCAG AA; qualifying large text 3:1. “Secondary” does not make normal text exempt.
- Applicable non-text controls and meaningful visual indicators need appropriate contrast, commonly 3:1 under WCAG AA.
- Web WCAG 2.2 AA target sizing uses 24×24 CSS px with specified exceptions; native guidance uses different units.
- Prefer generous touch areas; iOS 44×44 pt and Android 48×48 dp are not universal CSS dimensions.
- Do not rely only on color, precision gestures, dragging, hover, or animation.
- Reduced motion preserves meaning and operability; text scaling does not clip essential controls.

Record automated scan, keyboard test, and actual assistive-technology test as three different evidence categories.
No screen reader run means “screen-reader test not run,” even if names/roles were inspected.

## G. Security and privacy boundary questions

- Which changed operation reads or mutates sensitive state? Who is allowed to do it, on which resource, and where is that checked?
- Can a user replace a resource ID, tenant ID, role, owner, price, or status to bypass policy?
- Does an unauthenticated, expired-session, or forbidden request return an appropriate safe response?
- Are list/search/export endpoints as protected as single-record reads?
- Does a client-accessible database use appropriate row-level policies? Have role/tenant tests actually run?
- Are input parsing, validation, output encoding, and query construction appropriate to their contexts?
- Does arbitrary fetching permit local/private hosts, unexpected redirects, huge bodies, or sensitive URL leakage?
- Can uploads traverse paths, masquerade by extension, exhaust resources, or create unsafe rendered content?
- Are tokens or private payloads exposed by errors, caches, analytics, URLs, test snapshots, or logs?
- Does retry/replay cause duplicate messages, charges, or mutations? Use isolated synthetic tests, not live actions.
- Do dependency changes add unnecessary surface? If advisory access is missing, explicitly mark it NOT CHECKED.
- Are AI/tool outputs treated as untrusted? Are consequential actions separately authorized?
- Are proposed mitigations actually implemented and tested, or only written as recommendations?

Never gather evidence by opening credential stores or dumping environments. Report incidental secret exposure without copying its value.

## H. Review acceptance and escalation

For each finding ask: observed or suspected, reproducible or inferred, introduced or pre-existing, blocking or deferrable?
Use locations and counterexamples. Avoid vague “best practices” requests without impact.
A security or core-flow blocker is not offset by attractive visuals or a passing build.
After three unproductive fix cycles, explain the evidence and seek a decision instead of endless micro-tweaks.
A deferred issue belongs in the final handoff with scope and risk; it must not quietly disappear from the record.
