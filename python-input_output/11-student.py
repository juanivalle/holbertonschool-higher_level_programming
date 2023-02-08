#!/usr/bin/python3
"""comments"""


class Student:
    """comments"""

    def __init__(self, first_name, last_name, age):
        """comments"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """comments"""

        if attrs is None:
            return self.__dict__
        if all(isinstance(i, str) for i in attrs):
            if isinstance(attrs, list):
                return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

    def reload_from_json(self, json):
        """comments"""

        for key, value in json.items():
            setattr(self, key, value)
