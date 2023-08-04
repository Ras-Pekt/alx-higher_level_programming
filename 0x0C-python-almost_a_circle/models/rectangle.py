#!/usr/bin/python3
"""create a rectangle class"""
from .base import Base


class Rectangle(Base):
    """a class Rectangle with dimension attributes, x-y cordinates and an id"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter function"""
        return self.__width

    @property
    def height(self):
        """height getter function"""
        return self.__height

    @property
    def x(self):
        """x getter function"""
        return self.__x

    @property
    def y(self):
        """y getter function"""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter function"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """height setter function"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """x setter function"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """y setter function"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """displayes a rectangles based on width-height attributes"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """prints string representation of the object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """assigns args to attr using *args"""
        if args is not None and len(args) > 0:
            arg_list = ["id", "width", "height", "x", "y"]
            for arg in range(len(args)):
                setattr(self, arg_list[arg], args[arg])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dict rep of rectangle object"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
