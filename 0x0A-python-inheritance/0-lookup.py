#!/usr/bin/python3
"""a function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """print a list of availble attributes and methods
    Args:
        obj: a class object
    Returns:
        list of availble attributes and methods
    """
    return dir(obj)
