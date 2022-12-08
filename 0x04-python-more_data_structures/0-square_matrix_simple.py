#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for mtx in matrix:
        for i in range(0, len(mtx)):
            mtx[i] = mtx[i] ** 2
    return matrix
