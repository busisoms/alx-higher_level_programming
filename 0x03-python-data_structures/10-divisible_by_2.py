#!/usr/bin/python3

# divisible_by_2
"""
finds all multiples of 2 in a list

"""


def divisible_by_2(my_list=[]):
    div = []
    for i in my_list:
        if i % 2 == 0:
            i = True
            div.append(i)
        else:
            i = False
            div.append(i)
    return div
