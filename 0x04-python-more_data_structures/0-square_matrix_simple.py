#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    dup_matrix = matrix.copy()
    for i in range(len(matrix)):
        dup_matrix[i] = list(map((lambda x: x**2), matrix[i]))
    return(dup_matrix)
