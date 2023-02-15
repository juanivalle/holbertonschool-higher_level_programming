#!/usr/bin/python3
"""
comments
"""

class Base:
    """
    comments
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        comments
        """

        if id is not None:
            self.id = id

        else:
           Base.__nb_objects += 1
           self.id = self.__nb_objects

