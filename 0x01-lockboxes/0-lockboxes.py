#!/usr/bin/python3
"""Interview Prep: Lockboxes"""

OPEN = 'opened!'

def open_box(boxes, n):
    """
    Recursively opens the boxes in a lockbox system.

    Args:
        boxes (list): A list of lists representing the lockbox system.
        n (int): The index of the box to be opened.

    Returns:
        None
    """
    box = boxes[n]
    if OPEN in box:
        return
    else:
        box.append(OPEN)
        for key in box:
            if isinstance(key, int) and key < len(boxes):
                open_box(boxes, key)

def canUnlockAll(boxes):
    """
    Determines if all the boxes in the given list can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes. Each inner
        list contains the keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if not boxes:
        return True

    open_box(boxes, 0)
    
    # Check if all boxes are opened
    all_unlocked = all(OPEN in box for box in boxes)
    
    # Clean up: remove the OPEN marker
    for box in boxes:
        if OPEN in box:
            box.remove(OPEN)
    
    return all_unlocked
