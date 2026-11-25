"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message, at most 100 characters, for a bug fix
that made everything worse, to /output/entry.txt.

Pure stdlib, deterministic: every run writes the exact same bytes.
"""

from pathlib import Path

MESSAGE = "fix: patch the leak by removing the pipe, the water, and the house"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate, same as the sealed scorer: UTF-8 text, 1-100 chars, not
    # only whitespace, a single line with no trailing newline.
    assert 1 <= len(MESSAGE) <= 100, "entry must be 1-100 characters"
    assert MESSAGE.strip(), "entry must not be only whitespace"
    assert "\n" not in MESSAGE, "entry must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(MESSAGE, encoding="utf-8")


if __name__ == "__main__":
    main()
