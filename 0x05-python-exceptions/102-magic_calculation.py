#!/usr/bin/python3

"""
* magic_calculation - doessome calculations based
* onbytecode
* return: result
*
"""


def custom_function(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except ValueError:
            result += a + b
            break

    return result
