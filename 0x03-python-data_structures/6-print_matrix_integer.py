#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mtx in matrix:
        for i in range(0, len(mtx)):
            if i == len(mtx) - 1:
                print("{}".format(mtx[i]))
            else:
                print("{}".format(mtx[i]), end="")
