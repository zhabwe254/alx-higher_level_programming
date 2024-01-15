#!/usr/bin/python3
"""Module for creating an object from a JSON file"""


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    import json
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
