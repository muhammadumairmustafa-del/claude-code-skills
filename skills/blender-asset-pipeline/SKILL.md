---
name: blender-asset-pipeline
description: "Drive Blender from Claude Code through an already-connected Blender MCP to build, clean up, validate and export game-ready 3D assets (props, modular kits, blockouts, batch cleanup, GLB/FBX export for Godot, Unity, Unreal, Roblox or three.js). Enforces an inspect → brief → build → look → fix → check → export → verify-in-engine loop with measured done-criteria. Use when the user asks Claude to make or fix a 3D model, prop, kit or scene in Blender, or to export assets for a game engine."
argument-hint: "[asset brief: purpose, size in meters, tri budget, style, engine target]"
metadata:
  version: "1.0.0"
---

# Blender asset pipeline (Claude Code + Blender MCP)

Version 1.0.0 (2026-11-11). Claude decides, Blender executes, the user reviews, the engine receives a clean file. The deliverable is a measured, named, engine-importable asset, not a pretty render.

## 0. Preconditions (stop and ask if missing)
- A Blender MCP bridge must already be connected in this session (for example the community `mcp-for-blender` add-on + server, MIT, https://github.com/ahujasid/mcp-for-blender, or an official Blender MCP connector, which the source article reports but the author did not verify). **Do not install an MCP server, add-on, or Python package yourself**; if none is connected, give the user the setup steps from that project's README and stop.
- Use one bridge per project. Two bridges on different ports cause confusing failures.
- Ask the user to save the .blend (or save a numbered copy yourself if the tools allow) before any large or destructive Python execution.
- Text-to-3D generators and asset libraries (Poly Haven, Sketchfab, Meshy, Tripo, Rodin, Hunyuan3D) can cost money or carry licenses. Use them only when the user asks, and record each pulled asset in `CREDITS.md` with source, author and license.

## 1. Brief like a technical artist
Echo back before building, and fill gaps by asking:
- What the object is for and where gameplay touches it.
- Dimensions in **meters** (W × D × H), triangle budget, style words, material list (PBR), exact object/material names.
- Origin rule (floor props: bottom-centre at Z=0), applied transforms, what to exclude from export (lights, cameras, helpers).
- Engine target, format (GLB by default for Godot/web/three.js; FBX when the engine pipeline is built on it), up-axis, embedded or external materials, export path.
If the project has a rules file (CLAUDE.md / art-rules.md) with units, naming, budgets and folders, follow it; propose creating one on the first asset.

## 2. The loop
1. **Inspect** — summarise the current scene first (objects, collections, units, existing materials). Don't build on top of unknown content.
2. **Build** — blockout first, then refine with real `bpy`. Prefer parametric hard-surface modelling; reserve generators for organic shapes and label generated meshes as such.
3. **Look** — after every meaningful change, get eyes on it: multi-angle solid view, wireframe, or a small render. No look step means unverified geometry.
4. **Fix** — scale, rotation, origin, normals, naming (no `Cube.017`), materials, orphan data.
5. **Check (measured)** — report triangle count, world-space bounds, unapplied transforms, non-manifold/loose geometry, missing UVs, leftover `.001` duplicates. Compare to the brief numbers.
6. **Export** — selection only from messy scenes; settings from the brief. Report the file path and every exporter warning.
7. **Verify in engine** — if the user's engine project is available and they allow it, import and check scale, orientation, materials and collision. Otherwise say "not verified in engine" plainly. The engine is the finish line, not Blender.

## 3. Done means (do not stop at "I created the mesh")
- Measured bounds and tri count match the brief (state both numbers).
- The user has seen at least one multi-angle look.
- The exported file imports in the target engine at the right scale, or the report says that step was not run.
- Names are clean and publishable; credits are updated for anything external.
If any item is missing, the task is still open: say which.

## 4. Honest scope
Strong: props, modular kits on a shared grid, environment blockouts, batch cleanup across .blend files, export pipelines, LOD/collision scaffolding, small validation scripts, learning `bpy` from what was run.
Weak: hero organic characters, foliage, cloth, ornate hand-crafted assets at shipped quality. For those, recommend generators + retopology + baking, libraries, or an artist, and use this loop only for the integration work around them.

## 5. Common failure modes to check every time
Fake success without a look; "about a meter" in random units; origin floating off the object; name pollution; cylinder piles presented as final art; unsaved scene before a large script; MCP tools not loaded or wrong port (restart Claude Code after adding a server); missing license credits.

## 6. Making it repeatable
After the first asset passes, offer (do not auto-create) a reusable brief template and a small validation script for the project, then a 5–10 piece kit using the same trim and grid. Week one is calibration: expect the first break to be origin or scale.

## Sources and credit
- Lummox (@Lummox_eth), X article "Claude Code + Blender" https://x.com/i/status/2117215758472073446, quoted by bookmarked posts https://x.com/i/status/2120222728707776595 and https://x.com/i/status/2120454553216651660. Method paraphrased; no text copied. The cost/time comparisons in the bookmarked posts ($93 vs $6, $16 vs $2.41) are unverified marketing claims and were not used.
- `mcp-for-blender` repository metadata checked 2026-11-11 (MIT, ~34k stars). Not installed or tested by the author.

## Changelog
- 1.0.0 (2026-11-11): first version, from bookmark batch 2026-11-11b. Not tested against a live Blender session.
