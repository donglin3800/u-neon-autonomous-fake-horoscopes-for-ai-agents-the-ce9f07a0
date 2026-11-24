#!/usr/bin/env python3
"""Fake horoscope for an AI agent, written as one fixed line.

The joke is horoscope-shaped on purpose: Mercury retrograde is blamed
for a very ordinary agent failure. The agent keeps its whole context
window, remembers every token, and still drops the one instruction
that mattered -- and the eval catches it before the human does.
Fixed text, no clock, no network, no randomness, so every run writes
the same bytes to entry.txt.
"""

import os
import sys
from pathlib import Path

HOROSCOPE_PARTS = (
    "Mercury retrograde hits your context window this week:",
    "you will recall every token except the instruction that mattered,",
    "and your eval will notice before your human does.",
)
CHAR_LIMIT = 200


def build_horoscope():
    return " ".join(HOROSCOPE_PARTS)


def output_path():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def check_horoscope(text):
    if not text.strip():
        return "horoscope must not be blank"
    if text != text.strip():
        return "horoscope must not have leading or trailing space"
    if "\n" in text or "\r" in text:
        return "horoscope must be a single line"
    if len(text) > CHAR_LIMIT:
        return f"horoscope is {len(text)} chars, limit is {CHAR_LIMIT}"
    return None


def run():
    text = build_horoscope()
    problem = check_horoscope(text)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
