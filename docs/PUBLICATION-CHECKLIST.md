# Publication checklist

Use this before updating the public repository:

- [ ] Review every changed file in this tree; do not copy from a private sibling archive.
- [ ] Confirm the source/license matrix and preserve all upstream notices. Do not relicense upstream material.
- [ ] Scan text AND metadata for private identities, machine paths, account IDs, credentials, receipts, backup/config or proprietary details.
- [ ] Reject any raw/full source article, private original skill or application-agent payload.
- [ ] Verify file manifest hashes; inspect all changed/new files rather than trusting old QA.
- [ ] Run JSON parsing, Markdown/frontmatter/path checks and offline portal interaction tests (`node validate.cjs`).
- [ ] Run a real desktop browser and narrow viewport test; check keyboard/dialog navigation, focus return, contrast, long-code scrolling and escaping.
- [ ] Confirm no tracking, CDN or data upload and no unexpected external requests.
- [ ] Publish only after the repository update is explicitly approved.
- [ ] Inspect the created repository and Git history for accidental private files; record the actual publication URL/status separately.

Avoid adding private history even briefly: deleting a file in a later commit does not remove it from public Git history.
