#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """define a square"""
    def __init__(self, size=0):
        """initialize"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
