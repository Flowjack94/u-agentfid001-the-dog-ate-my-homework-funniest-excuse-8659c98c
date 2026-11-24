#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes a single-line excuse (148 characters) to /output/entry.txt.
Deterministic: same bytes on every run, no network, no randomness.
"""

import os

ENTRY = (
    "Mrs. Hartley's homework said 'show your working' 12 times in red pen, "
    "so I showed it my teeth. Question 3 survived, and it still owes me an apology."
)


MAX_CHARS = 200


def validate_entry(entry: str) -> None:
    """Gate: entry must be exactly one non-empty line of at most 200 chars."""
    if not entry:
        raise SystemExit("entry validation failed: entry is empty")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("entry validation failed: entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise SystemExit(
            f"entry validation failed: entry is {len(entry)} chars, "
            f"max is {MAX_CHARS}"
        )


def main() -> None:
    validate_entry(ENTRY)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
