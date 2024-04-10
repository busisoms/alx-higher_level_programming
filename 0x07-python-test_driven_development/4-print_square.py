#!/usr/bin/python3

# Prints a square with the character #


def print_square(size):
    # Check if size is less than 0 or not an int

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print a square using #
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print("#", end="")
        print()
