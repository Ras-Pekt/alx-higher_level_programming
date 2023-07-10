#!/usr/bin/python3
"""
A class that inherits the attributes and methods of list.
Contains a public method that prints a sorted list
 """


class MyList(list):
    """
    A class that inherits the attributes and methods of list
    """

    def print_sorted(self):
        """
        prints a sorted list in ascending order
        """
        print(sorted(self))
