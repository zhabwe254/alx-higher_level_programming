#!/usr/bin/python3
"""Module for saving an object to a file using JSON representation"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation."""
    import json
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
