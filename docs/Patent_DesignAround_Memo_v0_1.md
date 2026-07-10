# Hitch-Force Controller — Patent Design-Around Memo v0.1

**Date:** 2026-07-09 | **Purpose:** engineering-level claims analysis for the open-source hitch-force controller (Guide #4 / SS07 Phase B gate). Full claim pulls and prior-art timeline in the research transcript.
**⚠️ This is an engineering analysis, not legal advice.** Have patent counsel review this memo — and pull the complete claim set of US 12,416,536 (retrieval truncated) plus a fresh search for unpublished Lightship/Pebble applications — before the controller repo goes public. Budget a few hours of counsel time; the groundwork below should make it cheap.

## 1. Headline findings

1. **The suspected "Lightship patents" are not Lightship's.** US 12,162,363 and 12,416,536 belong to **Range Energy** (Class-8 electric semi-trailers). No granted Lightship patent on force-controlled propulsion surfaced; watch for pending applications (18-month publication lag).
2. **US 8,261,859 (Felt Racing, 2010) is LAPSED** — expired for non-payment of fees. It discloses *exactly* the simple architecture we want: single-axis hitch force metering, servo to a target tension band, cut power on compression, brake + regen. That makes our core approach both **freely practicable** and shielded — the '859 disclosure is invalidating-grade prior art against anyone later claiming generic longitudinal hitch-force-servo trailer propulsion.
3. **No in-force patent claims the generic combination we build:** ball-hitch caravan + single-axis drawbar load cell + one motor + follow-force control. Every in-force independent claim requires elements our architecture simply doesn't have.

## 2. Element-by-element: why Slipstream's architecture reads on nothing

| Patent (assignee, priority) | Requires (independent claims) | Slipstream flagship | Clear? |
|---|---|---|---|
| US 11,642,970 (K-Ryole, 2016) | Trailer coupled **to a cycle**; **motor on each wheel**; transverse-force sensing via two sensors in specific chassis geometry | Car-towed; ONE motor (Tesla rear DU + open diff); longitudinal sensing | ✅ misses ≥3 elements |
| US 12,162,363 (Range Energy, 2022) | **Rail-and-latch modular bogie** + separately latched battery under a semi-trailer floor; kingpin force only in dependents | Fixed axle, fixed pack, ball hitch — no rails, no bogie, no kingpin | ✅ misses the entire architecture |
| US 12,416,536 (Range Energy, 2022) | **Deriving** kingpin force **from acceleration + load** (virtual sensing); target preload force **proportional to incline**; **kingpin**; drive at distal end | **Direct measurement** with a physical load cell; ball hitch; control law = tension-band regulation, not incline-proportional preload | ✅ on retrieved claim 1 — counsel to confirm full claim set |
| US 12,187,133 (Erwin Hymer, 2018) | Conjunction of: **motor on each wheel** AND **3-axis** coupling force sensing AND an **observer with trailer system model** using articulation angle | One motor; **single-axis load cell + IMU**; plain PID force-following, no articulation-angle observer | ✅ misses all three conjuncts |
| US 8,261,859 (Felt, 2010) | — LAPSED — | This IS our architecture, now public domain | ✅ freely practicable |

**Prior-art shield (predates the in-force patents' priorities):** Felt '859 (2010, closed-loop hitch-force servo); US 4,676,330 (1987, powered trailer); Mr. Sharkey's pusher (~2000); K-Ryole's own 2017 publication; Dethleffs e.home coco public demo (Aug 2018 — prior art against Range's 2022 priority, though not against Hymer's own '133); Airstream eStream press (Jan–Feb 2022, also pre-Range).

## 3. Design rules for Guide #4 (bake these in)

1. **ONE motor.** The Tesla rear DU with its open differential is a single motor driving an axle — never describe or implement per-wheel torque control (that's K-Ryole/Hymer territory; it's also hardware we don't have).
2. **Single-axis, DIRECTLY-MEASURED drawbar force.** A physical tension/compression load cell at the ball coupler. Direct measurement distinguishes from Range '536's derived-force claim; single-axis distinguishes from Hymer's 3-axis. The IMU is for sway *supervision/cut-off*, not force estimation.
3. **Control law = tension-band regulation (Felt-style):** hold drawbar tension inside an adjustable band; increase torque when tension exceeds band, cut on compression, regen on brake signal. Do NOT structure (or document) the law as an "incline-proportional target preload force" — that's '536 claim language; we don't need inclinometer-scheduled setpoints anyway.
4. **Ball hitch, fixed axle, fixed battery** — already true of the design; keep it that way in the docs.
5. **Cite the lineage openly:** the repo README should credit Felt '859 (lapsed) and the pre-2016 art as the basis — it's honest, and it documents the freely-practicable foundation.
6. **Watch list** (re-check before v1.0 release): Range continuations (US 2024/0067278, 2025/0050745, 2025/0135899 — claims can broaden), any Lightship/Pebble applications publishing through 2026-27, US 11,607,918 "Tow assist" (assignee unconfirmed), US 2020/0355563 (force-sensing hitch ball — relevant to sensor placement).

## 4. Verdict

**Phase B is unblocked at the engineering level.** The architecture we already chose — for engineering reasons — happens to be the one the patent landscape leaves open, anchored by a lapsed 2010 patent that describes it exactly. Remaining action: one counsel session to bless this memo, confirm '536's full claim set, and run a pending-application search. Guide #4 (controller design + firmware) can proceed in parallel with that review; publication of the repo waits for it.
