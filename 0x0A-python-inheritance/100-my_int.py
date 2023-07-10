#!/usr/bin/pyhton3
"""MyInt class that inherits from int"""


class MyInt(int):
    """rebel class with inverted == and !="""
    def __eq__(self, other):
        """returns false if equal"""
        if int.__eq__(self, other):
            return False
        return True

    def __ne__(self, other):
        """returns false is not equal"""
        if int.__ne__(self, other):
            return False
        return True
