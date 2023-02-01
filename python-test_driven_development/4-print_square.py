#!/usr/bin/python3
"""Write a class Square that defines a square"""


def print_square(size):
    """With a given number this function prints a square"""
    if not size:
        return
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
