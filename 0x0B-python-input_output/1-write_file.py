#!/usr/bin/python3
"""writes a string to a file and returns the count of characters written"""


def write_file(filename="", text=""):
    """writes a string to a file
    Return:
        count of characters written
    """
    with open(filename, "w", encoding="utf-8") as fobj:
        count = fobj.write(text)
    return count
