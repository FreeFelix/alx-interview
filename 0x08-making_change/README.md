# 0x19. Making Change projects#1221

## Resources:books:
Read or watch:

---
## Learning Objectives:bulb:
What you should learn from this project:

---

### [0. Change comes from within](./0-making_change.py)
* Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

---

# Repo:
GitHub repository: alx-interview
Directory: 0x08-making_change

It seems like you're working on a project related to making change using Python. To achieve the goal of determining the fewest number of coins needed to meet a given amount total, you typically use a dynamic programming approach known as the "coin change problem". Here’s a breakdown of how you can approach and structure your project:

Project Structure
1. Problem Statement
The task is to implement a function in Python that calculates the minimum number of coins required to make up a given amount using a provided set of coin denominations.

2. Project Files
0-making_change.py: This file will contain the implementation of the makeChange function that solves the coin change problem.
README.md: This file will provide an overview of the project, instructions on how to use the code, and any other relevant information.
3. Learning Objectives
Understand dynamic programming concepts, specifically related to the coin change problem.
Implement an efficient algorithm to find the minimum number of coins required for a given amount using a set of coin denominations.
Steps to Implement
1. Define Function makeChange
Use dynamic programming to efficiently compute the minimum number of coins.
Use a list to store the minimum number of coins required for each amount from 0 to the target amount (total).
2. Test the Function
Create test cases to validate the correctness of the makeChange function.
Test edge cases such as negative amounts, zero amount, and large amounts.
3. README.md
Provide an overview of the project.
Include instructions on how to run the code and how the makeChange function works.
Discuss the approach used to solve the problem and any assumptions made.
Example Implementation (0-making_change.py)
python
Copy code
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
    if total < 0:
        return 0
    
    coins.sort(reverse=True)  # Sort coins in descending order
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1

# Example usage:
if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    total = 37
    result = makeChange(coins, total)
    print(f"The minimum number of coins to make {total} cents is: {result}")
Explanation
Function makeChange: Implements the dynamic programming approach to solve the coin change problem. It initializes a dp array where dp[i] represents the minimum number of coins needed to make amount i.
Sorting Coins: Ensures that the coins list is sorted in descending order to facilitate the greedy approach in dynamic programming.
Edge Case Handling: Returns 0 if the total amount is negative, assuming no coins are needed.
Example Usage: Demonstrates how to use the makeChange function with a sample set of coin denominations (coins) and a target total (total).
