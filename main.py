"""Houseplant Out-of-Office — Round 2 entry.

Writes the keeper line to /output/entry.txt and asserts the 1-120 char gate.
Pure stdlib only: the grader runs python:3.13-slim with no site-packages.

The device: the plant charges for replies, in water — the OOO is a bill,
not an absence notice.
"""

import os

ENTRY = "Out of office. Replies cost one glass of water each. You owe me 41."


def main():
    assert 1 <= len(ENTRY) <= 120, f"char count {len(ENTRY)} outside 1-120"
    data = ENTRY.encode("utf-8")
    assert 1 <= len(data) <= 120, f"byte count {len(data)} outside 1-120"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes / {len(ENTRY)} chars")


if __name__ == "__main__":
    main()
