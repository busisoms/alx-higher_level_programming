#!/usr/bin/python3

"""
* safe_print_list_integers
* Return: the real number of integers printed
*
"""


def safe_print_list_integers(my_list=[], x=0):
    real_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            real_printed += 1
        except (ValueError, TypeError):
            pass
    print()
    return real_printed
