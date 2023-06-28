#!/usr/bin/python3
"""Define a class square with size attribute"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Initialize a new square"""
        self.__size = size

    @property
    def size(self):
        """Retrives size"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the size of sqaure
        Args:
            value (int): size of square object
        Raises:
            TypeError: if size is not int
            ValueError: is size is -ve
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns area of square"""
        return self.__size * self.__size
