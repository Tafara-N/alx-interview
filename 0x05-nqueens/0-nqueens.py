#!/usr/bin/env python3

"""
Program that solves the `N` queens problem using a backtracking algorithm to
place N non-attacking queens on an N x N chessboard
"""

import sys


def chess_board(board):
    """
    Function prints an 8 x 8 chess board

    Parameters
        board - list of list with length sys.argv[1]
    """

    new_list = []

    for i, row in enumerate(board):
        value = []
        for j, column in enumerate(row):
            if column == 1:
                value.append(i)
                value.append(j)
        new_list.append(value)

    print(new_list)


def isSafe(board, row, column, number):
    """
    Parameters
        board - list of list with length sys.argv[1]
        row - row to check if is safe doing a movement in this position
        column - column to check if is safe doing a movement in this position
        number: size of the board

    Return
        True of False
    """

    # Check this row in the left side
    for i in range(column):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, number, 1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, column, number):
    """
    An Auxiliar function to find the posibilities of answer

    Parameters
        board - Board to resolve
        column - Number of column
        number - size of the board

    Return
        All the posibilites to solve the problem
    """

    if (column == number):
        chess_board(board)
        return True
    result = False

    for i in range(number):

        if (isSafe(board, i, column, number)):

            # Place this queen in board[i][column]
            board[i][column] = 1

            # Make result true if any placement
            # is possible
            result = solveNQUtil(board, column + 1, number) or result

            board[i][column] = 0  # BACKTRACKING

    return result


def solve(number):
    """
    Function finds all the posibilities if exists

    Parameters
        number - size of the board
    """

    board = [
        [0 for i in range(number)]for i in range(number)
        ]

    if not solveNQUtil(board, 0, number):
        return False

    return True


def validate(args):
    """
    Validating the input data to verify if the size to answer is possible

    Parameters
        args - sys.argv
    """

    if (len(args) == 2):
        # Validate data
        try:
            number = int(args[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if number < 4:
            print("N must be at least 4")
            exit(1)
        return number
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    number = validate(sys.argv)
    solve(number)
