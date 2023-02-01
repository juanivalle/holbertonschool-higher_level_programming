#!/usr/bin/python3
def text_indentation(text):
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
        i = i.strip("., ?, :")
        print("{}".format(i), end="")
