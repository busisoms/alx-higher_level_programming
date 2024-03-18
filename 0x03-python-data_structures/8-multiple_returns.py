#!/usr/bin/python3

# multiple_returns
"""
returns a tuple with the length of a
string and its first character

"""


def multiple_returns(sentence):

    length = len(sentence)

    if length == 0:
        first = None
        return (length, first)
    else:
        first = sentence[0]
    return (length, first)
