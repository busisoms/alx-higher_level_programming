#!/usr/bin/python

# matrix_divided - divides all elements of a matrix


def matrix_divided(matrix, div):
    # Returns a new matrix
    new_matrix = []

    for row in matrix:
        # Check if each row is a list of integers or floats
        if not isinstance(row, list) or \
                not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
        # Check if each row has the same size
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for elem in row:
            # Check if div is a number
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")

            # Check if div is not zero
            if div == 0:
                raise ZeroDivisionError("division by zero")

            new_row.append(round(elem / div, 2))

        new_matrix.append(new_row)

    return new_matrix
