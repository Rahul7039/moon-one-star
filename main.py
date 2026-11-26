#!/usr/bin/env python3
"""Entry for make.fun — The Moon Gets One Star.

Writes the chosen one-star review of the Moon to /output/entry.txt
and prints it. The review is a landlord-style grievance: the Moon
keeps raising the tides and never fixes its craters.
"""

import os

RATING = "One star."
GRIEVANCE = "It raised my tides twice this month"
PUNCH = "and never fixed a single crater."

ENTRY = " ".join([RATING, GRIEVANCE, PUNCH])

MAX_CHARS = 120


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
