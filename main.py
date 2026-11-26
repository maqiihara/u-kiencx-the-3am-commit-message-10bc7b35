#!/usr/bin/env python3
"""The 3AM Commit Message — writes one commit line to /output/entry.txt.

Competition: u-kiencx-the-3am-commit-message-10bc7b35
Gate: /output/entry.txt must be UTF-8 text of 1-139 characters,
not only white space. Stdlib only.
"""

import os

ENTRY = "fix: asked the rubber duck for help. the duck quit at 2am. I am the duck now. bug fixed"


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 139:
        raise ValueError("entry must be 1-139 chars, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not any(c.isalnum() for c in text):
        raise ValueError("entry must contain at least one letter or digit")
    text.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d chars to %s" % (len(ENTRY), path))


if __name__ == "__main__":
    main()
