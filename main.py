#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence
after knocking a glass off the table, to /output/entry.txt.

The excuse: the glass was squatting in the cat's sunbeam and refused
to move, so the cat served it an eviction notice. Cat logic, zero
remorse, no apology, no confession, no gravity cliche.
"""

import os

ENTRY = "That glass parked itself in my sunbeam and refused to move, so I served it an eviction notice."

# The gate requires 1 to 200 characters of UTF-8 text, not only
# whitespace, and the brief requires exactly one sentence.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the sentence.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
