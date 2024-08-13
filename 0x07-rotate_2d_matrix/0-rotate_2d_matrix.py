#!/usr/bin/python3

"""
Program to rotate a 2D matrix by 90 degrees
Edit the matrix in-place and does not return anything
"""


def rotate_2d_matrix(matrix):
    """
    Function to rotate a 2D matrix by 90 degrees
    """

    number = len(matrix)
    for i in range(number // 2):
        for j in range(i, number - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[number - j - 1][i]
            matrix[number - j - 1][i] = matrix[number - i - 1][number - j - 1]
            matrix[number - i - 1][number - j - 1] = matrix[j][number - i - 1]
            matrix[j][number - i - 1] = temp
