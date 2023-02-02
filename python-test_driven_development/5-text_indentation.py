#!/usr/bin/python3
"""text_indentation module"""

def text_indentation(text):
    """Replaces ', . :' for the same char + 2 \n"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == ".":
            print(".")
            print("")
        if i == "?":
            print("?")
            print("")
        if i == ":":
            print(":")
            print("")
        if i == " ":
            print(end=" ")
        i = i.strip("., ?, :")
        print("{}".format(i), end="")
