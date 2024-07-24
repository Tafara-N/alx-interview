#!/usr/bin/python3

"""
A method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Parameters
        data: list of integers

    Return
        True if data is a valid UTF-8 encoding, else False
    """

    bytes = 0
    for byte in data:
        mask = 1 << 7
        if bytes == 0:
            while mask & byte:
                bytes += 1
                mask = mask >> 1
            if bytes == 0:
                continue
            if bytes == 1 or bytes > 4:
                return False
        else:
            if not (byte & 1 << 7 and not (byte & 1 << 6)):
                return False

        bytes -= 1

    return bytes == 0
