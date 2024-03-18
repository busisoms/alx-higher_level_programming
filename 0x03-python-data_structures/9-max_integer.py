#!/usr/bin/python3

# max_integer
"""
finds the biggest integer of a list

"""


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    my_list.sort()
    return my_list[-1]
