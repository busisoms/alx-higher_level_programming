#!/usr/bin/python3

# replace_in_list
# replaces an element of a list at a specific postion

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
    return my_list
