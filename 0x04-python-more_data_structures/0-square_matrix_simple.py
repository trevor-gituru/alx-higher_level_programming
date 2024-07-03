#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    a function that computes the square value of all integers in a matrix
    """
    if matrix is not None:
        return list(map(lambda row: list(map(lambda element: element**2, row)) , matrix))
