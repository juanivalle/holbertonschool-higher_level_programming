#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
   for i in (matrix):
        for n in i:
            if n != matrix[-1]:
                print("{}".format(n), end=" ")
            else:
                print("{}".format(n))
        print()
