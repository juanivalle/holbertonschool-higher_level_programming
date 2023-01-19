#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = 0
    for i in range(1, len(argv)):
        if len(argv) == 0:
            print("{}".format(a))
        else:
            a += int(argv[i])
    print("{}".format(a))
