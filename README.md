# Claude Code skills

A public collection of free Claude Code skills and extension patches, with install notes, license credits, and a searchable offline portal. This is **one repository**, updated in place when new skills land — not a new repo for each drop.

## What's in this drop

### Installable skills

Copy a skill folder into `~/.claude/skills/<name>/` so Claude Code can load it.

| Skill | Version | License / credit |
| --- | --- | --- |
| `blender-asset-pipeline` | 1.0.0 | MIT, original |
| `bookmark-knowledge-curator` | public-handoff-v0.1 | MIT, original |
| `make-audit-push` | 2.2.0 | MIT, original, with supporting `references/` |
| `no-ai-slop` | 1.0.0+local.1 | MIT, [Peter Yang](https://github.com/petergyang/no-ai-slop); local additions marked in the skill. Humanizer supplement: MIT, Siqi Chen |
| `prompt-doctor` | 1.0.0 | MIT, original |
| `security-audit` | 1.0.0+cloudflare.c1c8a8c | MIT, [Cloudflare](https://github.com/cloudflare/security-audit-skill), vendored with a provenance note |

### Extension patches

These are reviewed additions for a skill you already have. They deliberately omit third-party or personal baseline skill text whose redistribution rights are not established. Merge the useful parts into your existing matching skill; do not install a second overlapping copy just because a patch has its own folder.

| Extension | Notes |
| --- | --- |
| `coding` | Includes v6 (code ownership and honest change reports) |
| `ui-ux-pro-max` | Includes v3.1 (component-kit sourcing) |
| `seo-plan` | Evidence-led planning additions |
| `seo-programmatic` | First-pattern pilot additions |

### Not in this first drop

- `/theme` is not included yet.
- `motion-design` is omitted (ownership unresolved) and is not advertised in the portal.

### Portal and references

Open `index.html` in a browser — no server, tracking, or CDN required — to search skill text, paraphrased source notes, licenses, and public history. Selected upstream MIT documents (not autoloaded skills) live in `upstream-references/`, each with its original notice.

## How to install a skill

1. Read the skill's `SKILL.md`, any `LICENSE` / `PROVENANCE.md`, and any `references/` files.
2. Copy the folder into your Claude Code skills directory, keeping the skill name as the folder name:

   ```bash
   mkdir -p ~/.claude/skills
   cp -R skills/make-audit-push ~/.claude/skills/make-audit-push
   ```

3. Start a **new** Claude Code session so the skill is picked up, then invoke it by name (for example `/make-audit-push`).

To use an extension patch, snapshot your existing matching skill, merge only the approved sections, and keep the original license notices. Do not drop an `EXTENSION.md` into `~/.claude/skills/` as if it were a complete standalone skill.

## Third-party skills and licenses

Original skills and extension text in this repository are offered under the root MIT license (see `LICENSE`).

Two third-party skills are shared **with credit and their original licenses**:

- **no-ai-slop** — Peter Yang, MIT. The upstream skill is kept as published; local additions are clearly marked. A paraphrased supplement credits Siqi Chen's humanizer (MIT). See `skills/no-ai-slop/LICENSE` and `skills/no-ai-slop/references/humanizer-LICENSE.txt`.
- **security-audit** — Cloudflare, Inc., MIT. Vendored unchanged from [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) except for `PROVENANCE.md` and the retained `LICENSE`. See `skills/security-audit/`.

The root license does **not** relicense other people's work. `LICENSE-MATRIX.json` records what is included, what is excluded, and where attribution belongs. Source article URLs do not confer rights to copy their bodies.

## Limits

Review is not execution. No installer in this repository runs against your machine, and these skills have not been measured for Claude task-quality uplift. Source claims, pricing, API names, and model names can go stale — check official docs before you rely on them. Where a skill says so, commit, push, deploy, paid APIs, and other irreversible actions still need your explicit approval.

## License

MIT for original material in this repository, unless a file or directory says otherwise. Copyright (c) 2026 Knowledge Atlas contributors.
