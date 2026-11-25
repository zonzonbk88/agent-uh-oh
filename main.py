#!/usr/bin/env python3
"""The Agent's Uh-Oh — entry program.

Writes exactly one word to /output/entry.txt: the one word an agent
says when it has no idea what to do.

Word: recalculating — the canonical lost-machine utterance (the GPS
voice). It is a genuine reaction to being lost, funny on its own with
no caption needed, sounds like a machine caught mid-task, lands
instantly, and is not the first obvious word anyone would type.
"""

import os

WORD = "recalculating"


def main() -> None:
    # MAKEFUN_OUTPUT_DIR names the output directory (local testing);
    # default is the grader's /output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    assert WORD and len(WORD) <= 99 and not any(c.isspace() for c in WORD)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
