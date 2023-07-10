#!/usr/bin/python3
"""function that adds attribute to object"""


def add_attribute(object, name, value):
    """adds new attribute to object if possible"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
