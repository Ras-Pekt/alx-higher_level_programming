#!/usr/bin/python3
"""A class with 2 public instance methods"""


class BaseGeometry:
    """a class with 2 public methods"""
    def area(self):
        """a function that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
