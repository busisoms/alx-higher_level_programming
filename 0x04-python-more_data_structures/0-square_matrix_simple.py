#!/usr/bin/python3

# square_matrix_simple
"""
computes the square value of all integers of a matrix
"""


def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    matrixSquare = [[col ** 2 for col in row] for row in matrix]
    return matrixSquare
