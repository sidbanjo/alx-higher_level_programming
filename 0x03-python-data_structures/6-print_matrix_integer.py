#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in matrix[x]:
            print("{}".format(y))
            if y != matrix[-1]:
                print(" ")
        print("\n")
