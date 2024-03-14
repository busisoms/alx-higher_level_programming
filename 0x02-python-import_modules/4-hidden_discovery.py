#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    defined = dir(hidden_4)

    for item in sorted(defined):
        if not item.startswith("__"):
            print(item)
