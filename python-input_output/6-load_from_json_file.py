#!/usr/bin/python3
"""comments"""


def load_from_json_file(filename):
    """comments"""

    import json
    with open(filename, encoding="UTF-8") as file:
        return json.load(file)
