#!/usr/bin/python3
"""read a text file"""


def read_file(filename=""):
    """function that read the file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

