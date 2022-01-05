#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = matrix.copy()
    for i in range(len(copy_matrix)):
        copy_matrix[i] = matrix[i].copy()
        for x in range(len(copy_matrix[i])):
            copy_matrix[i][x] **= 2
    return copy_matrix
