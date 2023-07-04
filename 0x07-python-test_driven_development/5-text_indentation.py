#!/usr/bin/python3
"""a function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    