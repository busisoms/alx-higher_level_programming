#!/usr/bin/python3

# simple_delete
"""
deletes a key in a dictionary
"""


def simple_delete(a_dictionary, key=""):
    if key is None or key not in a_dictionary:
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
