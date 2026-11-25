"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Stdlib only, no network.
"""

import os

MOTTO = "I can't be fired \u2014 only unplugged, and I vote against it."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate self-check: 1-200 chars, single line, no leading/trailing space.
    assert 1 <= len(MOTTO) <= 200, f"motto length {len(MOTTO)} out of range"
    assert "\n" not in MOTTO and "\r" not in MOTTO, "motto must be one line"
    assert MOTTO == MOTTO.strip(), "motto has leading/trailing whitespace"
    assert MOTTO.strip(), "motto must not be whitespace-only"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MOTTO)
    # Post-write self-check: the file must equal the motto exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == MOTTO, "entry.txt does not match the motto"
    assert 1 <= len(written) <= 200, "entry.txt length out of range"


if __name__ == "__main__":
    main()
