#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """dict description for JSON serialization"""
    return vars(obj)
