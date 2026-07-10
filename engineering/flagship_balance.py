#!/usr/bin/env python3
"""Flagship longitudinal balance model - the authority for SS05a section 3.
x = inches from coupler. Box spans 42-186 (12 ft box, 3 ft tongue).
Coupled system: the 600 lb DU+subframe rides AT the axle. Update masses as
real hardware gets weighed; rerun; update SS05a. Usage: python3 flagship_balance.py [axle_x] [pack_x]
"""
import sys
FIXED = [  # (lb, x) - everything except pack and DU/subframe
    (300, 100),  # frame incl tongue steel
    (380, 114),  # shell + pop-up
    (280, 130),  # interior (bed rear)
    (160, 90),   # systems misc
    (120, 80),   # 12V spine
    (187, 95),   # fresh water (full) + tank
    (103, 150),  # gray water (full) + tank  <- aft of axle: empty RAISES tongue
    (70, 114),   # solar
    (310, 100),  # gear/food payload
    (30, 5),     # coupler hardware + jack share
]
PACK, DU = 966, 600

def tongue(xa, xpack, gray_full=True):
    ms = [(w, x) for w, x in FIXED] + [(PACK, xpack), (DU, xa)]
    if not gray_full:
        ms = [((10, x) if (w, x) == (103, 150) else (w, x)) for w, x in ms]
    W = sum(w for w, _ in ms)
    xcg = sum(w * x for w, x in ms) / W
    return W * (xa - xcg) / xa, W

if __name__ == "__main__":
    xa = float(sys.argv[1]) if len(sys.argv) > 1 else 120.0
    xp = float(sys.argv[2]) if len(sys.argv) > 2 else 110.0
    for gf, label in [(True, "loaded/full"), (False, "gray empty ")]:
        t, W = tongue(xa, xp, gf)
        flag = "OK" if t <= 350 else "OVER 350 CAP"
        print(f"{label}: total {W:>5.0f} lb  tongue {t:>5.0f} lb  axle {W-t:>5.0f} lb  [{flag}]")
    t0, _ = tongue(xa, xp); t1, _ = tongue(xa + 1, xp); t2, _ = tongue(xa, xp + 1)
    print(f"sensitivity: axle +1\" aft = {t1-t0:+.0f} lb tongue; pack +1\" aft = {t2-t0:+.0f} lb")
