#!/usr/bin/python3

# uniq_add
"""
adds all unique integers in a list
"""


def uniq_add(my_list=[]):
    a = set(my_list)
    return sum(a)
