#!/usr/bin/env python3
"""Deadpan forecast for Tarnwick, a city that does not exist.

A single deadpan weather line, delivered in the flat tone of a late-evening
TV meteorologist: the fog apologises for turning up early, then leaves
promptly. One line, no more, written to /output/entry.txt.
"""

import os
import sys

FORECAST_LINE = (
    "Good evening from Tarnwick, where tonight's fog will apologise "
    "for arriving 40 minutes early and leave by 9."
)

MAX_LEN = 160
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(line: str) -> str:
    """Return the line if it is a valid single-line entry, else raise.

    The harness accepts exactly one line of 1-160 characters, so enforce
    every part of that contract loudly instead of trusting the constant:
    no embedded line breaks, no leading/trailing whitespace left in, and
    the character count re-checked after stripping.
    """
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("forecast line is empty")
    assert "\n" not in cleaned and "\r" not in cleaned, (
        "forecast line must contain no line breaks"
    )
    if len(cleaned) < 1 or len(cleaned) > MAX_LEN:
        raise ValueError(
            f"forecast line is {len(cleaned)} chars, outside the "
            f"1-{MAX_LEN} char range"
        )
    return cleaned


def write_entry(line: str) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")


def self_check(line: str) -> None:
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        contents = handle.read()
    if contents != line + "\n":
        raise RuntimeError("entry.txt does not hold exactly the forecast line")


def main() -> int:
    try:
        line = validate(FORECAST_LINE)
        write_entry(line)
        self_check(line)
    except (ValueError, RuntimeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
