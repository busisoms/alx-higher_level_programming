#!/usr/bin/python3

# add_tuple
"""
adds 2 tuples

"""


def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    idx_0 = a[0] + b[0]
    idx_1 = a[1] + b[1]
    return (idx_0, idx_1)
