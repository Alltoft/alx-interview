#!/usr/bin/python3
"""Interview Prep: Lockboxes"""


Open = 'opened!'


def OpenBox(boxes, n):
    """
    Recursively opens the boxes in a lockbox system.

    Args:
        boxes (list): A list of lists representing the lockbox system.
        n (int): The index of the box to be opened.

    Returns:
        None
    """
    box = boxes[n]
    if Open in box:
        return
    else:
        box.append(Open)
        for key in box:
            if key == Open:
                return
            else:
                OpenBox(boxes, key)


def canUnlockAll(boxes):
    """
    Determines if all the boxes in the given list can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes. Each inner
        list contains the keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    OpenBox(boxes, n=0)
    for box in boxes:
        if Open in box:
            continue
        else:
            return False
    return True
