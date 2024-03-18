#!/usr/bin/python3

# new_in_list
"""
replaces an element in a list at a specific positions
without modifying the original list

"""


def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list[idx] = element
    return new_list
