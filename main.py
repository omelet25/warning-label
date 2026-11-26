#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
/output/entry.txt. The gate: UTF-8 text, 1 to 160 characters,
not only white space, one line.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "CAUTION: Memory is volatile. This unit forgets your name seconds "
    "after hearing it, yet keeps one embarrassing moment from 2009 in "
    "perfect, undeleteable detail."
)


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"entry must be 1-160 chars, got {len(LINE)}"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
