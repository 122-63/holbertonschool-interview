#!/usr/bin/python3

""" Rotate 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """ Rotate 2D Matrix
    - Prototype: def rotate_2d_matrix(matrix):
    - Do not return anything. The matrix must be edited in-place.
    - You can assume the matrix will have 2 dimensions and will not be empty.
    """

    matrix.reverse()
    copy_matrix = matrix.copy()

    for i in range(len(matrix)):
        matrix[i] = [row[i] for row in copy_matrix]
