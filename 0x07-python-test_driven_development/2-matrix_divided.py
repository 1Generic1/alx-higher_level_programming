#!/usr/bin/python3
""" This module defines a function that divides all elements of a matrix """

def matrix_divided(matrix, div):
    """
    divides two numbers.

    Args:
        matix : The input matrix of integers or floats.
        div (int or float): the divisor
    
    returns: new matrix with elements divided by div

    """
    new_matrix = []
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
