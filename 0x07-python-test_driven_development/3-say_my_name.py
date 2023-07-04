#!/usr/bin/python3
"""a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """prints out first name last name
    Args:
        firsr_name: first input string
        last_name: second input string
    Raises:
        TypeError: if either input is not a string
    Returns:
        combined string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
    