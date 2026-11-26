"""Houseplant OOO R3 entry: a houseplant's out-of-office auto-reply.

The keeper line is the plant's own message, written by this program.
Pure stdlib only: the grader runs python:3.13-slim with no site-packages.
"""
import os

LINE = "Out of office. I left 11 leaves on your desk. Read them in order. They spell 'water'."

def main() -> None:
    # Gate (RULES.txt): UTF-8 text of 1 to 120 characters, not only whitespace.
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, gate is 1-120"
    assert LINE.strip(), "line must not be only whitespace"
    data = LINE.encode("utf-8")
    assert len(data) == len(LINE), "line must be pure ASCII for byte/char parity"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Self-check: read the entry back and confirm it round-trips exactly.
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == data, "entry.txt does not match the keeper line"
    print(f"wrote {len(data)} bytes / {len(LINE)} chars")

if __name__ == "__main__":
    main()
