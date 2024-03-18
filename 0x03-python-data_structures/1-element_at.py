#!/usr/bin/python3

# element_at
# retrieves an element from list

def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return None
    elif idx >= length:
        return None
    return my_list[idx]
