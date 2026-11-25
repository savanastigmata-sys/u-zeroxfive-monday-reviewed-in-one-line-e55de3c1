"""Monday, Reviewed in One Line — make.fun entry.

Writes one funny one-line review of the entrant's own Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library, fully
deterministic: the same text on every run, no network, no clock,
no randomness.
"""

import os

# The entry: one line, a review of my own Monday, under 200 characters.
# Three concrete mishaps (rain, bus, badge) with the joke landing at the
# end — no wasted words, repeatable to a coworker the next morning.
ENTRY = (
    "One star: Monday rained on my only clean shirt, sent my bus off "
    "without me, and my badge forgot my name at the front door \u2014 I "
    "had to introduce myself to my own office."
)

MAX_CHARS = 200


def validate(text):
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def resolve_output_dir():
    """$MAKEFUN_OUTPUT_DIR when the grader sets it, else ./output."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out:
        return out
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output")


def main():
    text = validate(ENTRY)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Verify what landed on disk is exactly what we validated.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text + "\n":
        raise RuntimeError("entry.txt on disk does not match the validated text")
    return path


if __name__ == "__main__":
    main()
