#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        if x == []:
            print("")
        else:
            for y in x:
                if y != x[-1]:
                    print("{}".format(y), end=' ')
                else:
                    print("{}".format(y))
