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

    if x < 1 or not nums:
        return None

    maria_chances = 0
    ben_chances = 0

    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    for n in nums:
        count = sum(primes[2:n + 1])
        if count % 2 == 0:
            ben_chances += 1
        else:
            maria_chances += 1

    if maria_chances == ben_chances:
        return None

    return "Maria" if maria_chances > ben_chances else "Ben"
