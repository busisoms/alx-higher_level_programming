#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    import sys

    n_args = len(sys.argv)

    if n_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        print("{0} + {1} = {2}".format(a, b, cal.add(a, b)))

    elif operator == '-':
        print("{0} - {1} = {2}".format(a, b, cal.sub(a, b)))

    elif operator == '*':
        print("{0} * {1} = {2}".format(a, b, cal.mul(a, b)))

    elif operator == '/':
        if b == 0:
            print("Error: Division by zero is not allowed.")
            sys.exit(1)
        print("{0} / {1} = {2}".format(a, b, cal.div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
