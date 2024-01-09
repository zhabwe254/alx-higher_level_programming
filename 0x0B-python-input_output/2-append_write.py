#!/usr/bin/python3
"""Module for appending a string to the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8) and returns the number of characters added."""
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
