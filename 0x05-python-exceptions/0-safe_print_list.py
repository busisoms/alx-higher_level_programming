#!/usr/bin/python3

"""
* safe_print_list - prints (x) elements of a list
* Return:  number of elements printed
*
"""


def safe_print_list(my_list=[], x=0):
    real_printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            real_printed += 1
    except IndexError:
        pass
    print()
    return real_printed
