#!/usr/bin/python3
"""create a rectangle class"""
from .rectangle import Rectangle


class Square(Rectangle):
    """a class Square with dimension attributes, x-y cordinates and an id"""
    def __init__(self, size, x=0, y=0, id=None):
        """square class constructor"""
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """prints string representation of the object"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """getter for square size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for square size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns args to attr using *args"""
        if args is not None and len(args) > 0:
            arg_list = ["id", "size", "x", "y"]
            for arg in range(len(args)):
                setattr(self, arg_list[arg], args[arg])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().update(id=value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dict rep of square object"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
