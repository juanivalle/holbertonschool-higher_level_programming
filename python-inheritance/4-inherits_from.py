#!/usr/bin/python3
"""class MyList that inherits from list"""


def inherits_from(obj, a_class):
    """function"""

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
