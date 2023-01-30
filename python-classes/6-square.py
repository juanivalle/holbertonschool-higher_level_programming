#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """define a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize"""
        self.__position = position
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        self.__position = value
        for i in (value):
            if i < 0:
                raise TypeError("positionmustbeatuple of 2 positive integers")

    def area(self):
        """method that returns the square area"""
        area = self.__size * self.__size
        return(area)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print()
                print(end="")
            for i in range(self.__size):
                print("-" * self.__position[0], end="")
                print("#" * self.__size)
