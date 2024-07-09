#!/usr/bin/python3

"""
Function calculates the fewest number of operations needed to result in exactly
`n` `H` characters in the file
"""

import math


def factors(number):
    """
    Calculates the factors of a given number

    Parameters
        number (int): The number for which factors need to be calculated

    Return
        list: A list of factors of the given number
    """

    factors_list = []
    while number % 2 == 0:
        factors_list.append(2)
        number //= 2

    for i in range(3, math.isqrt(number) + 1, 2):
        while number % i == 0:
            factors_list.append(i)
            number //= i
    if number > 2:
        factors_list.append(number)

    return factors_list


def minOperations(n):
    """
    Calculates the minimum number of operations required to
    transform a given number into 1.

    Parameters
        n (int): The number to be transformed.

    Return
        int: The minimum number of operations required.
    """

    if not isinstance(n, int) or n < 2:
        return 0
    else:
        number_of_operations = sum(factors(n))
        return int(number_of_operations)
