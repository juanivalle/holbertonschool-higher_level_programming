#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """function that write"""

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
