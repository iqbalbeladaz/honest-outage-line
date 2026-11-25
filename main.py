#!/usr/bin/env python3
"""The Most Honest Outage Line entry.

Writes one honest status page line to /output/entry.txt. The line is a
fixed, deterministic string: every run produces byte-identical output.
"""

import os

ENTRY = (
    "All servers are down. I cannot check the cause — the systems I would "
    "check are down too. No ETA yet; I will update this when I know "
    "something true."
)


def main() -> None:
    # The gate requires 1-160 characters of non-whitespace UTF-8 text.
    assert 1 <= len(ENTRY) <= 160 and ENTRY.strip(), "entry violates the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
