#!/usr/bin/python3

"""
Given a pile of coins of different values, determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total

    Parameters
        coins: list of integers
        total: integer

    Return
        fewest number of coins needed to meet a given amount
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if total <= 0:
            break

        num_coins += total // coin
        total %= coin

    if total != 0:
        return -1

    return num_coins
