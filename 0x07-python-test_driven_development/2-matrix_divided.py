#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with elements divided by div.

    Raises:
        TypeError: If the matrix contains non-integer/float elements,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not all(isinstance(row, list) and all(isinstance(i, (int, float)) for i in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
