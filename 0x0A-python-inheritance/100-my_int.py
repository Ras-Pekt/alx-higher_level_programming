#!/usr/bin/python3
"""MyInt class that inherits from int"""


class MyInt(int):
    """rebel class with inverted == and !="""
    def __eq__(self, other):
        """returns false if equal"""
        if super().__eq__(other):
            return False
        return True

    def __ne__(self, other):
        """returns false is not equal"""
        if super().__ne__(other):
            return False
        return True
