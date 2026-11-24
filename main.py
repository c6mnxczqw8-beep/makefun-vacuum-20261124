#!/usr/bin/env python3
"""Entry program for "The Vacuum's Alibi: One Line, 200 Characters".

Writes one line -- a robot vacuum's deadpan excuse for missing a spot --
to the output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The line is 1 to 200 characters of UTF-8 text.

Candidate alibis drafted for this entry (first pass):
  1. I didn't miss that spot. I surveyed it with LiDAR, judged it
     emotionally unavailable, and respected its boundaries.
  2. That spot was not missed. It was placed under witness protection
     after seeing what I did to the rug fringe.
  3. I was nowhere near that spot at 14:02. I was busy being stuck under
     the sofa, screaming internally at 3% battery, like a professional.
  4. My sensors saw the spot, my schedule saw the spot, my battery saw
     God -- I chose God.
  5. I didn't miss the spot; the spot filed a restraining order after I
     bumped the vase, and legally I must stay 40cm from its feelings.
  6. At 14:02 I was recharging, which is vacuum for 'in a meeting.' The
     spot knew. The spot has my calendar. The spot chose chaos.
  7. I avoided that corner because the cat was sitting there conducting
     surveillance, and I do not cross the union.
  8. Technically I cleaned that spot in a previous firmware update.
     Memories may vary. Mine were wiped.
  9. That 'missed spot' is where I buried the evidence -- sorry, dust --
     from the vase incident, and I was respecting the crime scene.
 10. I have cleaned that spot 47 times. If dust returns within 9 minutes,
     that is not my failure, that is a haunting.

First-pass pick: candidate 1 (deadpan, sensor-smug).

Second edit pass: candidate 1's punch ("respected its boundaries") is a
cute observation rather than a surprise. The final line fuses the best
parts of candidates 1, 6 and 7 instead: smug about both its LiDAR and
its schedule, a specific timestamp (14:02) as the alibi's evidence, and
the cat -- the vacuum's natural nemesis -- landing the surprise punch
in the final three words: "claiming diplomatic immunity."
"""

import os

LINE = (
    "I didn't miss that spot. My LiDAR mapped it, my schedule cleared "
    "14:02, and I rolled up to find the cat sitting there claiming "
    "diplomatic immunity."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
