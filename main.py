#!/usr/bin/env python3
"""Office Joke Open: one self-contained gag about office life.

Builds a single-line joke (1-200 characters, no line breaks) and
stores it at /output/entry.txt for the judge to read.
"""
from pathlib import Path


def check_line(text):
    """Refuse anything that is not one plain line of the right size."""
    assert text and text == text.strip()
    assert '\n' not in text and '\r' not in text
    assert 1 <= len(text) <= 200
    return text


def joke_line():
    opener = "I automated my job with one spreadsheet, "
    middle = "one macro, and one brave email, and got promoted "
    closer = "to a weekly meeting explaining the spreadsheet to "
    tail = "the people who banned macros."
    return check_line(opener + middle + closer + tail)


def main():
    out = Path('/output/entry.txt')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(joke_line(), encoding='utf-8')


if __name__ == '__main__':
    main()
