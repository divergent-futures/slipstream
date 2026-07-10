# Hitch-Force Controller — Design & Bench Guide

**v0.1 · 2026-07-09 · Slipstream open-source build series · Guide #4 (working name: `followdrive` — rename freely)**
**What this is:** the design of the open-source controller that makes the flagship range-neutral — reading drawbar force at the ball coupler and commanding drive-unit torque so the trailer carries itself while the tow car always leads. This is the piece no one has published. Design authority: the convergent production architecture (Lightship TrekDrive / Pebble Easy Tow / ZF-Dethleffs — all sense coupling force, all hold the coupler in tension), the public-domain control law of lapsed US 8,261,859, and the design rules of `docs/Patent_DesignAround_Memo_v0_1.md` (**read it first; its six rules are binding on this design**).

> **⚠️ The safety contract, before any code:** this controller can push a 3,400 lb trailer into the back of your car. Every design decision below flows from one principle — **any fault, ambiguity, or disagreement between sensors results in ZERO torque and a free-wheeling trailer.** A dead trailer is always safe (it's just a trailer). An overeager one is not.

---

## 1. Design rules (from the patent memo — binding)

ONE motor (the Tesla rear DU + its open diff) · **directly-measured, single-axis** drawbar force via a physical load cell · control law = **tension-band regulation** (hold drawbar tension in an adjustable band; never structure or document as "incline-proportional target preload") · ball hitch, fixed axle, fixed battery · IMU is for **sway supervision and cut-off only**, never force estimation · credit the Felt '859 lineage in the repo README.

## 2. Hardware

| Block | Spec | Est. |
|---|---|---|
| **Load cell** | Tension/compression, inline in the drawbar load path, **±5,000 lbf** range (working forces: ~1,000 lbf @0.3g accel, ~1,750 lbf @0.5g braking on 3,500 lb; 3× shock margin), IP67, fatigue-rated. Formats: S-type in a compression cage, or a shear-pin cell replacing the coupler pivot pin | $150–400 |
| **Amplifier/ADC** | 24-bit, ≥500 Hz sample, CAN output preferred (0–5V analog fallback); NOT an HX711 hobby board (too slow, too noisy for a control loop) | $100–200 |
| **IMU** | Automotive 6-axis (yaw rate + lateral accel are the signals that matter), CAN or SPI | $30–80 |
| **Controller** | **Option A (bench + v1): the ZombieVerter VCU we already have** — open STM32 firmware, spare analog/CAN inputs, already speaks torque-CAN to the Maguire DU board. The force loop becomes a custom input mapping: load cell in where a throttle pedal would go. Minimal new hardware, maximal reuse. **Option B (v2): dedicated STM32 board** once the loop is proven — cleaner packaging, own watchdog | (owned) / ~$150 |
| **Brake-signal sense** | Optocoupler on the 7-pin brake circuit (regen trigger + assist cut) | $15 |
| **Speed source** | DU motor RPM over CAN ÷ 9.036 ÷ tire circumference — no extra sensor | $0 |
| **7-pin presence sense** | Running-light circuit monitor — unhitched/unplugged = FAULT state | $10 |

Total ≈ **$550** (matches the configurator's `hitch-load-cell` part). Vertical tongue load is carried by the coupler *structure*, not the cell — single-axis means single-axis; the mechanical design must isolate the cell to longitudinal force (spherical seats / linkage, SS05 coupler machining scope).

## 3. Control law (tension-band regulation)

Sign convention: **tension positive** (trailer pulling back on the car — the normal towed state). Compression = trailer pushing the car = the thing that must never persist.

```
F        = filtered drawbar force (load cell, 100 Hz LPF from 500 Hz raw)
BAND     = [F_lo, F_hi] target tension, driver-adjustable (default 20–60 lbf)
v        = speed from DU RPM

ASSIST (15 ≤ v ≤ 55 mph, no brake signal, no faults):
    error = F − F_mid          (F_mid = band center)
    torque_cmd = PI(error)     — anti-windup, slew-limited (≤ X Nm/s),
                                 ceiling = torque_max(v) (tapers to 0 at 55 mph)
    F < F_lo (approaching compression) → reduce torque FAST (asymmetric gain:
        shedding thrust is always faster than adding it)
    F ≤ 0 (compression) → torque_cmd = 0 immediately; re-engage only after
        F > F_hi for t_hold (hysteresis — no hunting at the zero crossing)

BRAKE (7-pin brake signal present):
    torque_cmd = −regen_level (calibrated, ramped); drums remain the legal
    service brake; regen releases with the signal

COAST (v < 15 or v > 55, no faults): torque_cmd = 0 (mild coast regen optional)
```

The trailer **never pushes the tow vehicle**: the control target is *reduced tension*, not thrust. Deliberate underpowering (torque ceiling well below the DU's capability — software-capped per Guide #3) is a design feature, matching Lightship's stated posture.

## 4. Supervision & fail-safe state machine

```
INIT ──self-tests──> STANDBY ──v≥15, all-green──> ASSIST ⇄ BRAKE/REGEN
  any fault, from any state ──> FAULT (torque=0, then contactors open) ──manual reset──> INIT
```

**FAULT triggers (each one individually sufficient):**
- Load cell out of physical range, frozen value, or rate-of-change beyond physics (plausibility window)
- Load-cell vs IMU disagreement: commanded torque should produce predictable force *trend* — if force doesn't respond to torque within t_check, the sensor or the mechanics are lying → FAULT
- **Sway detected**: IMU yaw-rate oscillation in the 0.5–1.5 Hz band above amplitude threshold → assist ramps to zero (assist during sway feeds sway); drums remain available to the tow vehicle's controller
- CAN heartbeat loss (DU board, Battery-Emulator, or amplifier) beyond t_timeout
- 7-pin disconnect (breakaway also fires the drums independently — hardware path, not ours)
- Watchdog starvation, undervoltage, isolation warning from pack
- **No propulsion when unhitched, ever** (7-pin presence is a permissive for ASSIST; regulatory line per SS08)

FAULT is latching per trip — re-engagement requires stopped vehicle + driver action. Log everything (the Cerbo/tablet dash shows state + force trace live).

## 5. Bench bring-up (Gate B)

1. **Loop on the desk:** load cell in a bench vise fixture + hand-applied force via turnbuckle; controller in ASSIST-simulation (DU torque commands go to a logger, not hardware). Verify: band-following, asymmetric shed, compression cut, hysteresis, every FAULT trigger.
2. **Loop against the benched DU** (Guide #3 rig): torque commands live, DU spinning unloaded at walking pace; force still hand-applied. Verify command latency end-to-end (<50 ms sensor-to-torque target).
3. **Force-following demo = Gate B:** a scripted force profile (simulating accel/cruise/decel) tracked by the controller within band, plus induced faults each dropping to zero torque cleanly. Record it — this video is also the community's proof-of-concept.
4. Only after Gate C (rolling chassis) does the loop ever run with real trailer inertia — low-speed, closed course, per the Phase D graduated plan.

## 6. What gets published

The repo (post-counsel-review, per the memo): firmware (control law + state machine), amplifier/load-cell wiring, ZombieVerter input mapping, bench test scripts + the recorded force profiles, and the design-rule rationale including the Felt '859 lineage. License: MIT (code) per repo scheme.

## STOP conditions

| Condition | Verdict |
|---|---|
| Any urge to make compression "a little bit ok" for smoothness | No. Zero-crossing hysteresis exists for smoothness. Tension only. |
| Sensor disagreement "handled" by trusting one of them | FAULT means torque zero, not arbitration |
| Testing ASSIST with the trailer hitched to a car before Gate B passes on the bench | The bench is cheaper than your bumper |
| Skipping the latching-fault reset because it's annoying in testing | The annoyance is the feature |

*v0.1 — design-complete, pre-firmware. Feeds SS07 (Gate B) and the future `followdrive` repo. When this guide and the patent memo disagree, the memo wins; when either disagrees with physics on the bench, physics wins.*
