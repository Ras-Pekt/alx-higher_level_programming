#!/usr/bin/python3
"""base class"""


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if (id is None):
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id
