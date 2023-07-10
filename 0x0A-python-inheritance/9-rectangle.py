#!usr/bin/python3
"""create rectangle subclass by inheriting basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class from BaseGeometry parent class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints the description of a rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
