#!/usr/bin/python3

def uppercase(str):
    lower_case = range(97, 123)
    result_str = ""
    for i in str:
        if ord(i) in lower_case:
            lower = (ord(i) - 32)
            result_str += "{}".format(chr(lower))
        else:
            result_str += "{}".format(i)

    print(result_str, end="\n")
