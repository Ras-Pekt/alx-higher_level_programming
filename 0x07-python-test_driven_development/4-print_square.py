#!/usr/bin/python3
"""a function that prints a square with the character #"""


def print_square(size):
    """prints a square using #
    Args:
        size: size of the sqaure
    Raises:
        TypeError: if size is not int 
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        print("#" * size)