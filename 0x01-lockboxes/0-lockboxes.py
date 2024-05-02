#!/usr/bin/python3
""""
    Determines if all boxes can be opened.
    
    Args:
    - boxes (list of lists): Represents the locked boxes
      and keys within each box.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
"""

def canUnlockAll(boxes):
    n = len(boxes)
    stack = [0]
    unlocked = [False] * n
    unlocked[0] = True
    while stack:
        node = stack.pop()
        for key in boxes[node]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    return all(unlocked)
