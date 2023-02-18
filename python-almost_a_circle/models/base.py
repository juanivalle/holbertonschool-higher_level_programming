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
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """comments"""

        if list_dictionaries is None:
            return("[]")
        else:
            return json.dumps(list_dictionaries)   
    
    @classmethod
    def save_to_file(cls, list_objs):
        """comments"""

        if list_objs is None:
            new_list = []
        else:
            new_list = [cls.to_dictionary(obj) for obj in list_objs]

        filename = cls.__name__ + ".json"

        with open(filename, mode="w") as file:
            file.write(cls.to_json_string(new_list))
