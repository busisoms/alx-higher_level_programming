#!/usr/bin/python3

def remove_char_at(str, n):

    if n > len(str) or n < 0:
        return str

    ls = list(str)
    del ls[n]

    n_str = ""
    for i in ls:
        n_str += i
    return n_str
