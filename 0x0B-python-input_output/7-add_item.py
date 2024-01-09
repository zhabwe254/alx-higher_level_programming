#!/usr/bin/python3
"""Script for adding arguments to a Python list and saving them to a file"""


if __name__ == "__main__":
    import sys
    import os.path

    filename = "add_item.json"

    if not os.path.exists(filename):
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write("[]")

    try:
        data = load_from_json_file(filename)
    except:
        data = []

    data.extend(sys.argv[1:])
    save_to_json_file(data, filename)
