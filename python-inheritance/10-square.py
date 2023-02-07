#!/usr/bin/python3
"""class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class"""

    def __init__(self, size):
        """initialization"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area"""

        return(self.__size ** 2)
