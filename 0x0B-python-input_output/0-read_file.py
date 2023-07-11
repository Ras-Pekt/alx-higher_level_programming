#!/usr/bin/python3
"""a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """reads file and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as f_obj:
        print(f_obj.read(), end="")
