#!/usr/bin/python3

"""
Change comes from within
"""

def makeChange(coins, total):
    """
    Return the fewest number of coins needed to meet total

    Args:
    - coins (list of int): Available coin denominations, sorted in descending order.
    - total (int): The target amount to make up using the coins.

    Returns:
    - int: Minimum number of coins needed, or -1 if it's not possible to meet the total.

    """
    temp_value = 0
    coins.sort(reverse=True)  # Sort coins in descending order

    if total < 0:
        return 0  # If total is negative, return 0 (assuming no coins are needed)

    for coin in coins:
        if total % coin <= total:  # Check if using this coin does not exceed total
            temp_value += total // coin  # Add number of coins of this denomination
            total = total % coin  # Update total amount remaining

    return temp_value if total == 0 else -1  # Return result or -1 if total cannot be met
