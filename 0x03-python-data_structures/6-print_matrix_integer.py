#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for mtx in matrix:
            for i in range(0, len(mtx)):
                if i == len(mtx) - 1:
                    print("{:d}".format(mtx[i]))
                else:
                    print("{:d}".format(mtx[i]), end="")
    else:
        return (None)
