#!/usr/bin/python3

# best_score
"""
returns a key with the biggest integer value
"""


def best_score(a_dictionary):
    if a_dictionary:
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    return None
