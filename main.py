#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline to entry.txt."""

import os

LINE = "The deadline was inside the part of my context I summarized away to make room for the deadline."


def output_path():
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"), "entry.txt")


def validate(path):
    data = open(path, "rb").read()
    text = data.decode("utf-8")
    assert b"\r" not in data, "entry.txt must not contain carriage returns"
    assert len(data) == len(LINE.encode("utf-8")), "entry byte length mismatch"
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert text == LINE, "entry text does not match LINE"
    return len(data)


def main():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    size = validate(path)
    print(f"wrote {size} bytes to {path}")


if __name__ == "__main__":
    main()
