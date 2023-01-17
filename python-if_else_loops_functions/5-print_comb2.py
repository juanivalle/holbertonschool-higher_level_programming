#!/usr/bin/python3
for j in range(0, 100):
    if j < 99:
        print("{num:02d}".format(num = j), end=", ")
    else:
        print("{}".format(j))
