#!/usr/bin/python3
"""Define a class square with size and position attribute"""


class Square:
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets size"""
        return self.__size

    @property
    def position(self):
        """Gets position"""
        return self.__position

    @size.setter
    def size(self, value):
        """sets the size of sqaure
        Args:
            value (int): size of square object
        Raises:
            TypeError: if size is not int
            ValueError: is size is -ve
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, position):
        """sets the size of sqaure
        Args:
            value (int): size of square object
            posittion (tuple): position of the square
        Raises:
            TypeError: if tuple is not int
        """
        if not (isinstance(position[0], int) or isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise ValueError
        else:
            self.__position = position

    def area(self):
        """returns area of square"""
        return self.__size * self.__size

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
