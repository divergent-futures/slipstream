# SS06 — Aero / CFD · Design Track

**Status:** Detailed v0.1 · **Sequence:** runs continuously · **Depends on:** locked geometry (roadmap I.2 #1/#9: Model Y slipstream, 78" × 15', ~5' roof-down)
**Feeds V0.1 Gates 4–5:** CFD predicts ≤10% drag added to Model Y at 65 mph (≈25% range loss); 1:8 wind-tunnel article matches CFD within 15%.

## 1. Purpose & requirements

Aero is the product thesis — the trailer must live in the Model Y's slipstream or the "EV trailer" claim dies. Operating principle (roadmap I.3): gains hide in the REAR — rear taper, belly smoothness, and edge radii dominate; the front face rides in the tow car's wake. Requirements: combined car+trailer drag ≤ 1.10× solo car at 65 mph · gap flow between vehicle and trailer characterized (tongue-length fork sensitivity) · every shell revision re-runs the model (V0.5 basic → V1.0 refined).

## 2. Toolchain (the $2–5K swing item)

| Stage | Tool | Cost |
|---|---|---|
| Geometry | CAD master (SS05/SS04 single source) + published Model Y body scan | $0 |
| CFD | **OpenFOAM** (simpleFoam/DES on ~20–30 M cell mesh), cloud burst on spot instances | ~$200–600 compute |
| Sanity | Ansys Discovery trial / consultant spot-check of one run | $0–1,500 |
| Physical | 1:8 scale print/foam article, university or club tunnel session | ~$800–2,000 |

Self-run OpenFOAM keeps the bucket at the low end; consultant only to audit methodology, not to run the program.

## 3. Run matrix (V0.1)

1. Solo Model Y baseline (validates mesh/method against published Cd ≈ 0.23)
2. Y + trailer, roof down, 3' tongue — the money run (gate 4)
3. Tongue sensitivity: 2.5' / 3' / 4' (feeds `tongue_length` fork numbers)
4. Rear geometry sweep: flat / partial taper / full taper (feeds `rear_geometry` fork dragPct — currently ±3–5% placeholders)
5. Belly: sealed vs open frame (validates the +8% placeholder and the belly-pan doctrine)
6. Crosswind 10° yaw on config 2 (sway margin input to SS05)

Each fork-relevant run replaces a first-order `dragPct` estimate in `configurator/slipstream.config.json` with a computed one — **the configurator becomes CFD-traced, not vibes-traced.**

## 4. Wind tunnel article

1:8 → ~22" long. FDM print + fill/sand, magnet-mount to a Model Y body at matched scale. Measure drag delta car-alone vs car+trailer at matched Re as achievable; correlation target ±15% on the *delta* (gate 5), not absolute Cd.

## 5. Open questions

1. Model Y geometry source: photogrammetry scan community files vs. simplified body-of-revolution stand-in (affects wake fidelity — scan preferred)
2. Moving ground plane / rotating wheels simplification error budget
3. Tunnel access: university aero lab day-rate vs. AMA/club tunnel — quotes needed
4. Popped-up drag (campsite wind only) — skip in V0.1?  Yes: parked structure load handled in SS03 margins.

## 6. Deliverables

CFD report (method, mesh independence, run matrix results) + tunnel correlation memo + updated dragPct table for the configurator + geometry freeze recommendation to SS04/SS05. Gate 4/5 pass = composite tooling money unlocks.

---
*Detailed 2026-07-07. The run matrix is the bridge between engineering truth and configurator honesty.*
