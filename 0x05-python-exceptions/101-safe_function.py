#!/usr/bin/python3
import sys
"""
* safe_function - executes a function safely
* Returns: the result of the function
*
"""


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
