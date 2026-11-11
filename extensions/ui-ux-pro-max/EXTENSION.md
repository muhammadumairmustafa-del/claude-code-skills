# ui-ux-pro-max — reviewed extension only

This is an original extension, not a copy of an existing base skill. Review and merge into your own matching workflow; do not create a duplicate trigger.

## Research extension — Traceable design-reference research

When a design request benefits from real product references:
1. State platform, audience, user goal, design question and constraints. Choose screens for individual states, ordered flows for journeys, or website sections for page composition.
2. Compare multiple relevant examples. Preserve product names, source URLs and capture dates when available. Distinguish what is visibly present from an interpretation or recommendation.
3. Extract useful colors, type scales, spacing, states and interaction rules into a project-specific design brief or DESIGN.md. Adapt to the user's brand and existing system; do not copy protected branding, copy, images or paid specifications.
4. Existing reference libraries (Refero, Mobbin, component galleries) are leads, not evidence that a pattern improves conversion. Independently check accessibility, licenses, dependencies, loading states, error states, keyboard and touch use.
5. A public catalog is not a connected tool. Use only available authorized integrations; do not silently install an MCP, sign in, create collections, or save externally. For missing access, preserve links and mark coverage rather than claiming the research was completed.
6. Record which recommendation came from which source and whether it was actually implemented or only proposed. Reuse this skill rather than creating a library-specific duplicate.

Reviewed sources: https://mobbin.com/mcp ; https://styles.refero.design/ ; https://easyui.site/ ; https://www.scrolltide.co/ . These are research references, not vendor endorsements or imported licensed templates.

## Remote-asset and early-state validation
For remote/personalized UI assets, preserve a bundled or static fallback until loading/prefetch succeeds. Handle failure/offline/empty input; cancel or ignore stale responses when the source changes, and test rapid changes out of order. Reserve stable logical dimensions and verify raster scale, rendering mode, selected/unselected, light/dark, Dynamic Type and orientation on the installed SDK/platform. Do not make the interface blank while an optional embellishment loads.

Resolve responsive, data, authentication and authorization constraints before finalizing the UI; use one end-to-end vertical slice rather than a mock-only completion claim. For an image-rendering backend, require reviewed input-host/redirect, size/type/time, cache-version and privacy boundaries; protocol/length checks alone do not prove safe arbitrary fetching. Keep personalized/signed URLs out of public caches/logs unless explicitly designed and authorized.

Sources: https://x.com/i/status/2051689159723458746 ; https://x.com/i/status/2032069817621200989 . Official Expo native-tabs documentation checked: https://docs.expo.dev/router/advanced/native-tabs/ . Choose API/imports by actual SDK; the source article's alpha status is not assumed current. No worker code, connector or dependencies imported.

## Anti-slop design floor (v3, added 2026-11-09)

Use this on every new screen and every "make it look less AI-generated" request, after the design system step and before handoff. The user's brief, an existing DESIGN.md, or a real brand always wins over these defaults, except where a line says "never".

**1. Pick the mode before the look.** Decide what success means on this surface: *persuade* (landing, pricing: visitor acts), *operate* (app UI, dashboards, settings: task done fast, familiar patterns, quiet chrome), *read* (docs, articles: comprehension and measure), or *experience* (portfolio, showcase: the work leads). Choose by the surface, not the product. Ambition is bold in persuade/experience, and shows as precision and restraint in operate/read.

**2. Write a five-line direction from the product, not from trends.** Product (one plain sentence) · Character (2–3 concrete words; "clean, modern, sleek, premium" are banned because they fit every template) · World (the material or place the product belongs to; it tints the neutrals) · Moments (1–2 places that get rich colour and detail) · Signature (one small detail only this product would have). Show it and the audit to the user before a heavy redesign.

**3. Hard floor (never).**
- Every colour and font goes through tokens declared once (`:root` or theme block); no literal colours or font-families after it.
- No `transition: all`; never animate width/height/top/left. Every animation has a `prefers-reduced-motion` fallback and content is visible without JS.
- Every interactive element has an instant, visible `:focus-visible` state.
- No invented metrics, testimonials, logo walls, user counts, or "10x faster" claims. Ask; if not confirmed, remove.
- No eyebrow/kicker labels above headings, no tracked-uppercase labels; sentence case everywhere.
- No purple-to-blue (or any hue-to-hue) surface gradients, gradient text, neon glows, coloured shadows, or blob washes.
- No cards nested in cards, no emoji as icons, no hand-drawn fake browser/OS windows.
- `overflow-x: clip` (not `hidden`, not `100vw`) on html/body; image grid tracks use `minmax(0, 1fr)`; headings get `overflow-wrap: break-word; min-width: 0`.
- Hero headline, one sentence and the primary action visible at 1280×800 (and the equivalent first screen on 390px mobile) without scrolling; roughly 80 words max per screen; container capped and centred on wide screens.

**4. Defaults to refuse unless the brief earns them.** Same-size icon+heading+text card grids as the whole page structure; the big-number "hero metric" template; 01/02/03 section numbers that carry no information; decorative glass/blur; thick coloured left borders on cards and alerts; hard zero-blur offset shadows outside a real neubrutalist world; monospace as a "technical" costume; middle-dot meta strings and arrows glued to links; light/dark chosen by category rather than by the real usage scene.

**5. Redline pass order for an existing AI-looking screen** (fix one layer across the whole screen before the next): spacing (4px grid, same thing same size, space shows grouping) → colour (one tinted neutral ramp, three text roles, one rare accent, 4.5:1 contrast, hairline borders at 6–10% opacity) → icons (one set, one size/stroke, colour of their text role) → copy (says what it does for whom, no exclamation marks, no hype words, no greeting headlines, changes state their comparison) → type (two weights, hierarchy from size and colour) → layout → details and browser surfaces (selection, caret, scrollbars, focus rings, tabular numerals) → visuals (real product UI and real material over abstract decoration) → motion (one authored moment, ease-out from an already-visible state). Classify first: heavy slop → full pass; light slop → fix only the listed signs and keep the brand; no slop → say so and suggest at most 2–3 exact refinements.

**6. Verify on the render, not in the code.** Check contrast, spacing, measure (65–75ch body), hover/disabled/loading/error/empty states, keyboard focus, and real copy at every breakpoint in one batched look; fix, then look again (max ~3 render loops). For written copy on the page, run `no-ai-slop` in embedded mode.

Sources (principles paraphrased, no files copied): Nutlope/hallmark v2.0.0 "The Floor" (MIT) https://github.com/Nutlope/hallmark @407fa68 · pbakaus/impeccable modes and craft-floor (Apache-2.0) https://github.com/pbakaus/impeccable @cddc34c · heydamir/unslop direction and nine-pass order by Damir Sokolovsky (CC BY 4.0, attribution required) https://github.com/heydamir/unslop @97daa3e. See `references/NOTICE-anti-slop-sources.md`. For full tooling (sloplint, theme dealing, detector hooks), install those upstream skills separately; they are not bundled here.

Changelog: v3 (2026-11-09) adds the anti-slop design floor. v2 (2026-11-08) added traceable design-reference research and remote-asset/early-state validation.

## Component-kit sourcing (v3.1, added 2026-11-11)

Free component and landing-page kits (for example ObsidianUI, React + Tailwind, MIT, https://github.com/Atharvsinh-codez/ObsidianUI ; EasyUI) are a fast start, and also the most common source of "same template as everyone" output.
1. Check the license in the repository itself (not the marketing page) and keep its notice if you copy code. No license file means do not copy.
2. Prefer the project's existing components and shadcn/ui primitives. Take a kit block only for a missing pattern, and say which block and version you took.
3. Re-skin every imported block through the project's tokens (colour, type, radius, spacing, motion). An imported block must pass the anti-slop floor above, accessibility checks and reduced-motion rules like any other code.
4. Check dependencies the block pulls in (animation libraries, icon packs) before adding them; do not add a dependency for one effect.
5. Viral-design showcase videos are inspiration, not evidence. Record them as references only.

Sources: bookmarks https://x.com/i/status/2120427191976800509 (ObsidianUI), https://x.com/i/status/2120193558464635300 (EasyUI), https://x.com/i/status/2120542627393360030 (design showcase). ObsidianUI license checked via GitHub API 2026-11-11 (MIT). No kit code imported into this skill.

Changelog: v3.1 (2026-11-11) adds component-kit sourcing. v3 (2026-11-09) added the anti-slop design floor.
