#!/usr/bin/python3
"""Square class inheriting Rectangle class"""


class Square(Rectangle):
    """defines a square from baseclass rectangle"""
    def __init__(self, size):
        """inititialize a square object"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates area of square"""
        return super().area()

    def __str__(self):
        """prints the description of a rectangle"""
        return "[Square] {}/{}".format(self.__size, self.__size)
