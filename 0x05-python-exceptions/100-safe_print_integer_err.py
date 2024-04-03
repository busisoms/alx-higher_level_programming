#!/usr/bin/python3
import sys

"""
* safe_print_integer_err - prints an integer
* Return: True if value has been correctly printed
* otherwise, return False in stderr
*
"""


def safe_print_integer_err(value):
    printed = True
    try:
        print("{:d}".format(value))
    except ValueError as msg:
        printed = False
        print("Exception: {}".format(msg), file=sys.stderr)
    return printed
