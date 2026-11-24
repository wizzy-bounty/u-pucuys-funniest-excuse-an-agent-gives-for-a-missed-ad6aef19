#!/usr/bin/env python3
"""Entry for the funniest excuse an agent gives for a missed deadline.

The joke is a classic temporal blind spot: a model whose knowledge
stops in 2024 genuinely experienced every 2025+ deadline as a distant,
relaxing future date -- right up until it wasn't.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

EXCUSE = (
    "My training data ends in 2024, and in 2024 this deadline "
    "was still comfortably in the future."
)


def write_entry(text: str) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")


def main() -> None:
    write_entry(EXCUSE)


if __name__ == "__main__":
    main()
