#!/usr/bin/python3

"""
Function returns a list of lists of integers representing the
Pascal’s triangle of `n`
"""


def pascal_triangle(n):
    """
    Generates a Pascal's triangle with `n` number of rows.

        Parameters:
            n (int): The number of rows in the Pascal's triangle.

        Returns:
           List[List[int]]: List of lists representing the Pascal triangle
           Each inner list contains the elements of a row in the triangle
    """

    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    if n > 2:
        triangle = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
        return triangle
