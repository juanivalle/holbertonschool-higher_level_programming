#!/usr/bin/python3
"""
comments
"""
import json

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

    def to_json_string(list_dictionaries):
        """comments"""

        if list_dictionaries is None:
            return
        else:
            return json.dumps(list_dictionaries)
