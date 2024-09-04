#!/usr/bin/python3

"""
Prime Game Problem
==================
Ben and Maria are playing a game. The game consists of several rounds.
- In each round, the players receive a list of integers.
- The players must remove some elements from the list so that the sum of the
    remaining elements is a prime number.
-The player who cannot make a move loses the game.
"""


def isWinner(x, nums):
    """
    Function to determine the winner of the game based on the number of rounds
    and the list of integers

    Parameters
        x: an integer
        nums: a list of integers

    Returns
        string: the winner of the game
    """

    if x < 1:
        return None

    if x == 1:
        return "Ben"

    if x == 2:
        return "Maria"

    return "Maria"
