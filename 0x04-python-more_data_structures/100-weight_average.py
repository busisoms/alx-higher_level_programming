#!/usr/bin/python3

# weight_average
"""
returns the weighted average of all integers tuple
"""


def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_score = sum(i * j for i, j in my_list)
    total_weight = sum(j for x, j in my_list)

    return total_score / total_weight
