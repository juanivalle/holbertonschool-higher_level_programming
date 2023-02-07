#!/usr/bin/python3
"""class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class"""

    def __init__(self, width, height):
        """initialization"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return("[Rectangle] " + str(self.__width) + "/" + str(self.__height))


    def area(self):
        area = self.__width * self.__height
        return(area)
