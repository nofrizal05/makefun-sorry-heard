#!/usr/bin/env python3
"""Entry for make.fun "Sorry, I Heard That Wrong".

Writes a single one-line apology from a smart speaker that misheard
its owner, to /output/entry.txt. Standard library only.

The line: the speaker confused "pasta" with "panic", started both
timers, and reports that only one of them is going well.
"""

import os

LINE = (
    "I heard 'set a timer for pasta' as 'set a timer for panic'. "
    "Both are now running. The pasta is fine. You are not."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
