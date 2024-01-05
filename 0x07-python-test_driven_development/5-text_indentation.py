#!/usr/bin/python3
"""
This module contains a function that prints text with 2 new lines after '.', '?', and ':' characters.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    for char in text:
        print(char, end="")
        if char in separators:
            print("\n")
