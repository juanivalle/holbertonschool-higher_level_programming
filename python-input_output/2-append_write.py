#!/usr/bin/python3
"""comments"""


def append_write(filename="", text=""):
    """comments"""
    
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        a = 0
        for i in text:
            a = a + 1
        return a
