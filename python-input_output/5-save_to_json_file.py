#!/usr/bin/python3
"""module save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """comments"""

    import json
    with open(filename, 'w', encoding="UTF-8") as file:
        file.write(json.dumps(my_obj))
