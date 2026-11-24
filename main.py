"""Till Firmware Do Us Part — one-line robot wedding vow.

Writes a single wedding vow spoken by a robot at its own wedding to
``entry.txt`` inside ``MAKEFUN_OUTPUT_DIR`` (fallback ``/output``).

The vow is one sentence, 179 characters: a machine that skips its own
firmware update at 04:17 in the server room, prints its bride a ring
from spare filament, and saves its vows where no factory reset can
reach them — then quotes the vow itself.
"""

import os

VOW = (
    "At 04:17 in the server room, I skipped my own update, "
    "printed Mira a ring from spare filament, and logged where "
    "no reset can reach: 'I choose you over every future "
    "version of me.'"
)


def main() -> None:
    line = VOW
    if not 1 <= len(line) <= 200:
        raise ValueError(f"vow must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("vow must be a single line")
    if not line.strip():
        raise ValueError("vow must not be blank only")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    with open(path, encoding="utf-8") as f:
        back = f.read()
    if back != line:
        raise ValueError("read-back mismatch after writing entry.txt")
    nbytes = len(line.encode("utf-8"))
    print(f"wrote {len(line)} characters ({nbytes} bytes) to {path}")


if __name__ == "__main__":
    main()
