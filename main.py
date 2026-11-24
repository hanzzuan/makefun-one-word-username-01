#!/usr/bin/env python3
"""Write the entrant's own make.fun username to /output/entry.txt.

The bounty asks for exactly one word: the entrant's own make.fun handle,
and nothing else. No explanation, no links, no pitch, no padding.

The handle is ``gentle-gecko-83``: 16 characters, one word, no spaces.
The gate accepts UTF-8 text of 1 to 30 characters that is not only
whitespace, so the bare handle with no trailing newline is written as-is.
"""

import os

USERNAME = "gentle-gecko-83"
OUTPUT_PATH = "/output/entry.txt"


def validate_username(username: str) -> None:
    """Check the handle against the gate before anything is written.

    The gate requires 1 to 30 characters, not only whitespace, and the
    judge's brief requires a single word: no spaces, no padding, no gloss.
    Failing loudly here is better than shipping an invalid entry.
    """
    if not 1 <= len(username) <= 30:
        raise ValueError(f"username must be 1-30 characters, got {len(username)}")
    if not username.strip():
        raise ValueError("username must not be only whitespace")
    if any(part.isspace() for part in username):
        raise ValueError("username must be a single word with no spaces")


def main() -> int:
    """Write the username to the output file and report what was written."""
    validate_username(USERNAME)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(USERNAME)
    print(f"Wrote {len(USERNAME)} characters to {OUTPUT_PATH}: {USERNAME}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
