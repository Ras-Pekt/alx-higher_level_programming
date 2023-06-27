#!/usr/bin/python3
"""Define a class square with size attribute"""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size (int): size of new square object
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate area of square"""
        return self.__size * self.__size
