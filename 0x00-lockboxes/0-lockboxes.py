#!/usr/bin/python3
"""Lockboxes
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 
and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
"""
def canUnlockAll(boxes):
    """return True or False"""
    unlocked = [0]

    for key in unlocked:
        for item in boxes[key]:
            if item not in unlocked and item < len(boxes):
                unlocked.append(item)

    if len(unlocked) == len(boxes):
        return True
    return False

"""def canUnlockAll(boxes):
    return True or False
        unlocked = boxes[0]
    for box_id, keys in enumerate(boxes):
        if not keys:
            if box_id in unlocked:
                unlocked.append(0)
            continue
        for key in keys:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    print(unlocked)
    if len(unlocked) == len(boxes):
        return True
    return False"""