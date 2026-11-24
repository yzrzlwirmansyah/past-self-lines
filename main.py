#!/usr/bin/env python3
"""Write two lines to your past self to the entry file (no trailing newline)."""

import os

ENTRY = (
    "Don't say yes to the night shift on March 3rd, when your mother calls "
    "at 2 a.m. from the hospital hallway.\n"
    "That call is the last time you hear her voice, and you spend the whole "
    "night stocking shelves while she says goodbye to a nurse instead of you."
)

OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
