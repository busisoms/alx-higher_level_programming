#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("{} argument:".format(n - 1))
    else:
        print("{} arguments:".format(n - 1))

    for arg in range(1, n):
        print("{0}: {1}".format(arg, sys.argv[arg]))
