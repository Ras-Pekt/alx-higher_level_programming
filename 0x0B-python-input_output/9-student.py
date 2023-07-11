#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """
    A Student class with public instance attributes;
    first_name
    last_name
    age
    """
    def __init__(self, first_name, last_name, age):
        """initialize object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve dict representation"""
        return vars(self)
