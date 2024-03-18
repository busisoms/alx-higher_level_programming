#!/usr/bin/python3

# print_matrix_integer
"""
prints a matrix of integers

"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end="")
            else:
                print("{:d} ".format(row[i]), end="")
        print()
