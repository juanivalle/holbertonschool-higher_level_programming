#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in (matrix):
        contador = 0
        for n in i:
            contador += 1
            if len(i) != contador:
                print("{:d}".format(n), end=" ")
            else:
                print("{:d}".format(n), end="")
        print()
