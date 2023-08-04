#!/usr/bin/python3
"""base class"""
import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if (id is None):
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """
        converts a python dict object into a JSON array object
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)