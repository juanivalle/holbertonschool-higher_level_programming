#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
   for fila in (matrix):
        for valor in fila:
            print("{:d}".format(valor), end=" ")
        print() 
