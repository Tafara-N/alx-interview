#!/usr/bin/python3

"""
Function that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Parameters
        boxes (list): A list of lists representing the boxes and their keys

    Return
        bool: True if all the boxes can be unlocked, otherwise False
    """

    if not boxes:
        return False

    number_of_boxes = len(boxes)
    visited = set()
    visited.add(0)  # The first box is unlocked

    box_stack = [0]  # Start with the first box
    while box_stack:
        current_box = box_stack.pop()

        for key in boxes[current_box]:
            if key < number_of_boxes and key not in visited:
                visited.add(key)
                box_stack.append(key)

    return len(visited) == number_of_boxes
