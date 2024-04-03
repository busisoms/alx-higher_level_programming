#!/usr/bin/python3

"""
* safe_print_integer - prints an integer
* Return: True if value is correctly printed
* else False
*
"""


def safe_print_integer(value):
    try:
        print("{:d}". format(value))
        return True
    except ValueError:
        return False
