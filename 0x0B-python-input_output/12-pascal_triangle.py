#!/usr/bin/python3
"""
a function that returns a list of lists
of integers representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """returns a list of lists"""
    if n <= 0:
        return []

    list = [[1]]

    for i in range(1, n):
        last_row = list[-1]

        new_row = [1]

        for j in range(1, i):
            new_row.append(last_row[j-1] + last_row[j])

        new_row.append(1)
        list.append(new_row)

    return list
