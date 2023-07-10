#!/usr/bin/python3
"""A Square subclass by inheriting Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square from baseclass rectangle"""
    def __init__(self, size):
        """inititialize a square object"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """calculates area of square"""
        return super().area()
