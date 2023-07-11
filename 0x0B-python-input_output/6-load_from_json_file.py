#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """reads json to create python object"""
    with open(filename, "r", encoding="utf-8") as fobj:
        data = fobj.read()
        return json.loads(data)
