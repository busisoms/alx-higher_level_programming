#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal

    a = 10
    b = 5

    print("{0:d} + {1:d} = {2:d}".format(a, b, cal.add(a, b)))
    print("{0:d} - {1:d} = {2:d}".format(a, b, cal.sub(a, b)))
    print("{0:d} * {1:d} = {2:d}".format(a, b, cal.mul(a, b)))
    print("{0:d} / {1:d} = {2:d}".format(a, b, cal.div(a, b)))
