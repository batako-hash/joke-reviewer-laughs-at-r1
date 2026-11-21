# the-joke-the-reviewer-laughs-at-20261121-0329 entry (Python 3.13, standard
# library only): writes one original one-line joke about working beside AI
# coding agents to /output/entry.txt.
#
# The joke is the reviewer's trap: you approve an agent's diff in ten seconds
# — and then you spend an hour figuring out what you just approved. The laugh
# is the reversal of effort: the review takes ten seconds, the understanding
# takes an hour, and the order is backwards. Every developer who has
# rubber-stamped an agent diff recognises it at once.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = (
    "I approved my agent's diff in ten seconds, "
    "then spent an hour figuring out what I'd approved."
)

chars = len(JOKE)
if chars < 1 or chars > 280 or not JOKE.strip():
    raise SystemExit(f"joke fails the gate: {chars} characters")

out_path = Path(OUTPUT_DIR) / "entry.txt"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(JOKE, encoding="utf-8")

# Read it back: the grader runs the program twice and both runs must write
# the same bytes, so fail loudly here rather than silently writing wrong ones.
written = out_path.read_text(encoding="utf-8")
if written != JOKE:
    raise SystemExit("entry.txt does not match the joke")
