#!/usr/bin/python3

# update_dictionary
"""
replaces or adds key/value in a dictionary
"""


def update_dictionary(a_dictionary, key, value):
    new_items = {key: value}
    a_dictionary.update(new_items)
    return a_dictionary
