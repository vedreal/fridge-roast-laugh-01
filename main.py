#!/usr/bin/env python3
"""Fridge Roast — one-line roast for the make.fun bounty
u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.

The program writes a single roast line (1-200 chars, UTF-8) to
/output/entry.txt. The roast is on-subject: it targets the fridge's
firmware update and its ice maker, and lands on an anticlimax —
one perfect cube for the whole party.
"""

import os
import sys

# The roast. Firmware + ice maker, tight wording, fresh angle:
# the "upgrade" makes the ice experience strictly worse.
ENTRY = (
    "The fridge sent a firmware update that 'improved the ice "
    "experience.' The ice now comes out as a single, perfect cube. "
    "One. For the whole party."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the bounty gate: one line, 1-200 chars (UTF-8)."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    n = len(line.encode("utf-8"))
    if not (MIN_CHARS <= n <= MAX_CHARS):
        raise ValueError(f"entry is {n} chars, must be {MIN_CHARS}-{MAX_CHARS}")
    if len(line) != n:
        # ASCII-only text, so char count and byte count agree; guard anyway.
        raise ValueError("entry must be plain UTF-8 text")


def main() -> int:
    validate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
