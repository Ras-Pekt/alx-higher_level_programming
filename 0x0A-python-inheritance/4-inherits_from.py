#!/usr/bin/python3
"""
checks if object is an instance of a class
that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """checks if obj inherited from derived a_class"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
