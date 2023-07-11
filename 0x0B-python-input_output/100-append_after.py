#!/usr/bin/python3
"""
a function that inserts a line of text to a file
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file"""
    file = []

    with open(filename, "r+", encoding="utf-8") as fobj:
        file = fobj.readlines()

        for f in file:
            fobj.write(f)

            if search_string in f:
                fobj.write(new_string)
