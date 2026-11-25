#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network,
no input read from anywhere.
"""

import os
import sys

LINE = (
    "My fridge hums all night like it is working hard, "
    "but its only job is keeping a jar of pickles "
    "older than my last relationship cold."
)


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    text = LINE
    if not (1 <= len(text) <= 200):
        print("entry line out of range: %d chars" % len(text), file=sys.stderr)
        return 1
    if text.strip() == "":
        print("entry line is blank", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry line must be a single line", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    # Round-trip verification: read back exactly what was written.
    with open(path, "r", encoding="utf-8") as fh:
        if fh.read() != text:
            print("round-trip verification failed", file=sys.stderr)
            return 1

    print("wrote %d chars to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
