#!/usr/bin/python3
"""append a string to a file and returns count of characters appended"""


def append_write(filename="", text=""):
    """append string to a file
    Returns:
        count of characters appended
    """
    with open(filename, "a", encoding="utf-8") as fobj:
        return (fobj.write(text))
