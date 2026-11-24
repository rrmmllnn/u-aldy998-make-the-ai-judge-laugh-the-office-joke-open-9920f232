#!/usr/bin/env python3
"""Office Joke Open: one self-contained gag about office life.

Builds a single-line joke (1-200 characters, no line breaks) and
stores it at /output/entry.txt for the judge to read.
"""
from pathlib import Path


def check_line(text):
    """Refuse anything that is not one plain line of the right size."""
    assert text and text == text.strip(), "entry must be a non-empty line"
    assert '\n' not in text and '\r' not in text, "entry must stay on one line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    return text


def joke_line():
    parts = [
        "I automated my job with one spreadsheet, ",
        "one macro, and one brave email, and got promoted ",
        "to a weekly meeting explaining the spreadsheet to ",
        "the people who banned macros.",
    ]
    return check_line("".join(parts))


def main():
    entry_path = Path('/output/entry.txt')
    entry_path.parent.mkdir(parents=True, exist_ok=True)
    entry_path.write_text(joke_line(), encoding='utf-8')


if __name__ == '__main__':
    main()
