#!/usr/bin/python3
""" Module for Prime Game """


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    
    Parameters:
    x (int): Number of rounds.
    nums (list of int): List of integers for each round.

    Returns:
    str: Name of the winner ("Maria" or "Ben"). If there is no winner, returns None.
    """
    if not nums or x < 1:
        return None

    # Create a sieve list to determine prime numbers
    n = max(nums)
    sieve = [True for _ in range(max(n + 1, 2))]
    
    # Implement the Sieve of Eratosthenes
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i * i, n + 1, i):
            sieve[j] = False

    sieve[0] = sieve[1] = False

    # Compute the cumulative count of prime numbers
    c = 0
    for i in range(len(sieve)):
        if sieve[i]:
            c += 1
        sieve[i] = c

    player1 = 0
    
    # Determine the number of rounds Maria wins
    for n in nums:
        player1 += sieve[n] % 2 == 1

    # Determine the winner based on the number of rounds won
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
