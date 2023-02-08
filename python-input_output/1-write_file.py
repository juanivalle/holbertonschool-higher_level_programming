#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """function that write"""

    a = 0
    with open(filename, mode="r", encoding="utf-8") as f:
        for i in f:
            for n in i:
                a = a + 1
        return a
