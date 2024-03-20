#!/usr/bin/python3

# search_replace
"""
replaces all occurences of an element
by another in a new list
"""


def search_replace(my_list, search, replace):

    if search not in my_list:
        return my_list
    else:
        modified_list = my_list[:]
        for i in range(len(modified_list)):
            if modified_list[i] == search:
                modified_list[i] = replace
                break
    return modified_list
