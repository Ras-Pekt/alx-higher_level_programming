#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """adds all args to python list"""
    file = "add_item.json"

    try:
        items = load_from_json_file(file)
    except Exception:
        items = []

    for item in range(1, len(argv)):
        items.append(argv[item])

    save_to_json_file(items, file)


add_item()
