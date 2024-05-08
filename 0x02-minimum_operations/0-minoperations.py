#!/usr/bin/python3
"""
write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """
    Computes the fewest number of operations needed to result
    in exactly n 'H' characters.
    :param n: target number of 'H' characters.
    :return: minimum number 
    """
    if not isinstance(n, int):
        return 0
    operation_count = 0
    clipboard_contents = 0
    complet = 1
    while complet < n:
        if clipboard_contents == 0:
            clipboard_contents = complet
            complet += clipboard_contents
            operation_count += 2
        elif n - complet > 0 and (n - complet) % complet == 0:
            clipboard_contents = complet
            complet += clipboard_contents
            operation_count += 2
        elif clipboard_contents > 0:
            complet += clipboard_contents
            operation_count += 1
    return operation_count
