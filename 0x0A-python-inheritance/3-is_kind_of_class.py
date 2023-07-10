#!/usr/bin/python3
"""
checks for an instance of a class or a subclass

"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance of a class or subclass"""
    if isinstance(obj, a_class):
        return True
    return False
