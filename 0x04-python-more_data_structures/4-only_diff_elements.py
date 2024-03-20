#!/usr/bin/python3

# only_diff_elements
"""
returns a set of all elements present in only one set
"""


def only_diff_elements(set_1, set_2):

    diff = set_1 ^ set_2
    return diff
