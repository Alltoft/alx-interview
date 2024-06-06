#!/usr/bin/python3

Open = 'opened!'


def OpenBox(boxes, n):
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
    OpenBox(boxes, n=0)
    for box in boxes:
        if Open in box:
            continue
        else:
            return False
    return True
