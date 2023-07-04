#!/usr/bin/python3
"""a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix with a div
    Args:
        matrix: a list of lists
        div: divisor
    Raises:
        TypeError: if matrix is not list of lists of ints or floats
    Returns:
        new_matrix
    """

    new_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    
    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    length = len(matrix[0])

    
    for r in matrix:
        row = []
        
        if not isinstance(r, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        if len(r) != length:
            raise TypeError("Each row of the matrix must have the same size")
        
        for i in r:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            
            row.append(round((i / div), 2))
        
        new_matrix.append(row)

    return new_matrix
