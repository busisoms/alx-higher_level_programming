#!/usr/bin/python3

# print_sorted_dictionary
"""
print a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):

    my_keys = list(a_dictionary.keys())
    my_keys.sort()
    sorted_dict = {i: a_dictionary[i] for i in my_keys}

    for i, j in sorted_dict.items():
        print("{}: {}".format(i, j))
