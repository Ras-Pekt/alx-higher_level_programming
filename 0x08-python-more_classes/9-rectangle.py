#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """Define a rectangle with width and height attributes"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize new rectangle
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new rectangle instance"""
        return Rectangle(size, size)

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectanlge"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns an informal string of the object"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(self.print_symbol)
            if i != self.__height - 1:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """returns a formal string of the object"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """print message at deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
