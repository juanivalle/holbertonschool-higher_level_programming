#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """function that write"""

    with open(filename, encoding="utf-8") as f:
        s = str(text)
        print(f.write(s), end="")
