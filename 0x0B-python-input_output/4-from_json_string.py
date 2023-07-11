#!/usr/bin/python3
"""returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """convert obj to json string"""
    return (json.loads(my_str))
