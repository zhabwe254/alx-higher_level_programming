#!/usr/bin/python3
"""Module for reading a text file and printing its content to stdout"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
