#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to entry.txt.

Stdlib only, no network, fully deterministic: every run writes the
exact same bytes.
"""

import os

LINE = "I'm away until Monday. Gary is covering my inbox. Gary doesn't work here \u2014 but he seemed confident."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
