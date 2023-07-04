#!/usr/bin/python3
"""A function that takes floats and/or integers and returns the sum as an int"""


def add_integer(a, b=98):
    """Adds 2 ints and/or floates
    Args:
        a: first int or float
        b: second int or float
    Raises:
        TypeError: if var is not an int or float
    Returns:
        sum of a and b as an int
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
