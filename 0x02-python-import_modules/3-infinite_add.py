#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    def infinite_add():
        n_args = len(sys.argv)

        if n_args < 2:
            print("0")
        else:
            sum_all = 0
            for num in range(1, n_args):
                sum_all += int(sys.argv[num])
            print(sum_all)

    infinite_add()
