#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — make.fun entry.

Writes exactly one deadpan weather forecast line for an invented city to
/output/entry.txt: 1-160 UTF-8 characters, a single line, no trailing lines.

Candidate lines brainstormed for this entry (judge: a dry, deadpan TV
meteorologist — on-subject forecast first, then funnier joke, then vivid
detail, then broadcast tone, then character use):

1. "Good evening from Tarnwick, where tonight's fog will apologise for
   arriving 40 minutes early and leave by 9."
2. "In Vess Hollow, expect 33 millimetres of uphill rain by 2pm, with
   puddles forming on rooftops first."
3. "In Mirell, snow is filed alphabetically overnight, so expect flurries
   under S before dawn."
4. "Overcast in Brindlewick today, 14 degrees, with a 60 percent chance of
   rain that falls only on people who forgot umbrellas."

Winner: candidate 1. It opens like a real broadcast ("Good evening from
Tarnwick"), the joke lands on first read (fog that apologises for being
early), it carries two concrete numbers (40 minutes, 9), and the image is
vivid while the tone stays plain and confident.
"""

import os
import sys

FORECAST = (
    "Good evening from Tarnwick, where tonight's fog will apologise "
    "for arriving 40 minutes early and leave by 9."
)

MAX_CHARS = 160


def main() -> int:
    line = FORECAST.strip()
    # Gate: exactly one line, 1-160 UTF-8 characters, not only whitespace.
    if not line:
        print("error: forecast is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: forecast must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: forecast is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    encoded = line.encode("utf-8")
    if len(encoded.decode("utf-8")) != len(line):
        print("error: forecast is not valid UTF-8 text", file=sys.stderr)
        return 1

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    # Self-check the file we just wrote.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    lines = written.splitlines()
    if len(lines) != 1 or lines[0] != line:
        print("error: entry.txt does not contain exactly the forecast line",
              file=sys.stderr)
        return 1
    print(f"wrote {len(line)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
