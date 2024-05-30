#!/usr/bin/python3
"""This module divides all elements of a matrix by a given divisor"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of list of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of list of float: A new matrix with all elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
                   If the rows of the matrix are not of the same size.
                   If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    
    # Check if matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row of the matrix is the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements by div and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    
    return new_matrix
