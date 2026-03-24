"""General functions (sorted alphabetically) to analyze data."""

import re


def count_words(text: str):
    """Counts the number of words text.

    Considering a given text (with any type of characters), the function counts all alphanumeric
    words and prints the total count. Numbers (only numeric characters) are also considered as words.
    """
    words = re.findall(r"\w+", text)
    print(f"Total word count: {len(words)}")
