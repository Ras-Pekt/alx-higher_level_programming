#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """write json to file"""
    with open(filename, "w", encoding="utf-8") as fobj:
        data = json.dumps(my_obj)
        fobj.write(data)