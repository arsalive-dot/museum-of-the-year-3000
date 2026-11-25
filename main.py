"""Museum of the Year 3000 — make.fun entry.

Writes the museum label a museum in the year 3000 puts beside an
ordinary object from today to /output/entry.txt, deterministically.

Craft: a real museum-label register — headword, date, definition —
with the year 3000 misreading a password as a religious rite, so
the humour is the curator's confident misunderstanding of a
perfectly ordinary habit.
"""

import os

ENTRY = (
    "Password (n., 2020s): a secret word, typed daily, forgotten "
    "instantly, reset at once. The ancients performed this rite "
    "four times a week."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
