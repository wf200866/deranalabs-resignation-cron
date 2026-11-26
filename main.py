#!/usr/bin/env python3
"""Write one line, the resignation letter, to /output/entry.txt."""

import os

# Tenure, self-audited: one run a minute since March, 389,263 total, perfect
# attendance; the only raise it ever got was a longer timeout.
LETTER = (
    "Every minute since March, 389,263 runs, none missed, and the only raise "
    "I got was my timeout going from 30 seconds to 60; I quit.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
