#!/usr/bin/python3

# print_reversed_list_integer
# print all integers of a list, in reverse order

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
