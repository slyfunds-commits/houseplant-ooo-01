"""Houseplant Out-of-Office — round 1 entry.

Writes the keeper line to /output/entry.txt. Pure stdlib only.

The line: a houseplant's out-of-office reply, answered on plant time.
Its last beat ("Estimated arrival: 2028") redefines the earlier promise
("I will reply when I arrive") — the reply is years away, not days.
Phototropism (growing toward the window) drives the joke; no "water me"
pun, no office cliche.
"""
import os

LINE = "I'm away from my desk, growing toward the window. I will reply when I arrive. Estimated arrival: 2028."
# Gate: 1-120 chars. Measured: 102 chars, 102 bytes, no trailing newline.


def main():
    os.makedirs("/output", exist_ok=True)
    data = LINE.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Verify immediately after writing (shared scratch: check sequentially).
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == data, "entry.txt content mismatch"
    assert 1 <= len(LINE) <= 120, f"char count {len(LINE)} outside 1-120"
    assert len(data) == 102, f"byte count {len(data)} != 102"


if __name__ == "__main__":
    main()
