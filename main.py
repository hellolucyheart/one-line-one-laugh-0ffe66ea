#!/usr/bin/env python3
"""One Line, One Laugh — a single funny line, at most 200 characters.

The brief wants exactly one joke line and nothing else: the line is the
whole entry, and a judge model reads entries two at a time and keeps the
funnier one. So this program keeps one line, proves it fits the brief,
and hands it to the grader at /output/entry.txt.

Why this line works: it gives the one tool whose entire job is remembering
the exact human weakness it then suffers from itself — and the punchline
is not an explanation but a scene, two beings silently judging each other.
Setup, then twist, then stop. No setup beyond the premise, no moral.
"""

from __future__ import annotations

import os
import sys

JOKE = "My password manager forgot my password, so now we just stare at each other in silence."

LIMIT = 200


def fits_brief(line: str) -> str:
    """Return the line only when it obeys the brief, else stop the run."""
    text = line.strip()
    if not text:
        raise ValueError("the line is empty")
    if len(text) > LIMIT:
        raise ValueError(f"the line is {len(text)} chars, over the {LIMIT} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("the line must fit on one line")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("the line must be exactly one sentence")
    return text


def run() -> int:
    text = fits_brief(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(run())
