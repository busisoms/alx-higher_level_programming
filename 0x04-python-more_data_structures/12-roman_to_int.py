#!/usr/bin/python3

# roman_to_int
"""
converts a Roman numeral to an integer
"""


def roman_to_int(roman_string):
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman_string)):
        if i > 0 and r[roman_string[i]] > r[roman_string[i - 1]]:
            result += r[roman_string[i]] - 2 * r[roman_string[i - 1]]
        else:
            result += r[roman_string[i]]

    return result
