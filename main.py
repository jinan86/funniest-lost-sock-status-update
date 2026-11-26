#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry.

Writes exactly one status update, in the voice of a lost sock that
ended up inside a guitar, to /output/entry.txt. Deterministic: the
same bytes on every run.
"""

ENTRY = "I'm inside a guitar. Every strum, I scream. He calls it music."


def main() -> None:
    import os

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
