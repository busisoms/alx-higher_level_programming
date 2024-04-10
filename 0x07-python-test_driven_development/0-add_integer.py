#!/usr/bin/python3

# adds 2 integers


def add_integer(a, b=98):

    # check if a and b are int or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # returns addition of a and b
    return int(a) + int(b)
