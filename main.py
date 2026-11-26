"""Green Tests, Nothing Works: The Excuse Contest.

Writes the one-line excuse to MAKEFUN_OUTPUT_DIR/entry.txt.
One line, 99 characters, no trailing newline. Stdlib only.
"""

import os

ENTRY = "All tests pass. Unfortunately, they test the version of the app that exists only in my imagination."


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
