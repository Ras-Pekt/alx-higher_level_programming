#!/usr/bin/python3
"""
A funtion that finds peak in a list
"""


def find_peak(list_of_integers):
    """
    Finds peak in a list
    Args:
        list_of_integers: unsorted list of ints
    Returns:
        peak value. None otherwise
    """
    if not isinstance(list_of_integers, list) or not list_of_integers:
        return None

    start = 0
    end = len(list_of_integers) - 1

    while start < end:
        middle = (start + end) // 2

        if list_of_integers[middle] > list_of_integers[middle + 1]:
            end = middle
        else:
            start = middle + 1

    return list_of_integers[start]
