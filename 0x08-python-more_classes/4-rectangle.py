#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """Define a rectangle with width and height attributes"""
    def __init__(self, width=0, height=0):
        """initialize new rectangle
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width
        Args:
            value (int): rectangle width
        Raises:
            TypeError: if width is not int
            ValueError: if width < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height
        Args:
            value (int): rectangle height
        Raises:
            TypeError: if height is not int
            ValueError: if height < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectanlge"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns and informal string of the object"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            if i != self.__height - 1:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """returns a formal string of the object"""
        return "Rectangle ({:d}, {:d})".format(self.width, self.height)
