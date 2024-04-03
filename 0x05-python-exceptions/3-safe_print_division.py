#!/usr/bin/python3
"""
* safe_print_division - divides 2 integers and prints
* the result
* Return: value of the division, otherwise None
*
"""


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
