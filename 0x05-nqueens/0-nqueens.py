#!/usr/bin/python3

'''
N queens puzzle
'''

from sys import argv, exit

def is_NQueen(cell: list) -> bool:
    '''
    Check if the latest queen placement is valid in the current configuration.
    
    Args:
        cell (list): List of column indices for each row where queens are placed.
    
    Returns:
        bool: True if the latest queen placement is valid, False otherwise.
    '''
    row_number = len(cell) - 1
    # Iterate through each previously placed queen
    for index in range(row_number):
        # Calculate the absolute difference in column indices
        difference = abs(cell[index] - cell[row_number])
        # Check if queens are placed in the same column or on diagonals
        if difference == 0 or difference == row_number - index:
            return False
    return True

def solve_NQueens(dimension: int, row: int, current_solution: list, solutions: list):
    """
    Recursively solve the N Queens problem.
    
    Args:
        dimension (int): Size of the chessboard (number of rows/columns).
        row (int): Current row being processed.
        current_solution (list): Current partial solution (list of column indices for each row).
        solutions (list): List to store all valid solutions.
    """
    if row == dimension:
        # If all rows are filled, add the current solution to the list of solutions
        solutions.append(current_solution[:])
    else:
        # Try placing a queen in each column of the current row
        for col in range(dimension):
            current_solution.append(col)
            # Check if the placement of the queen is valid
            if is_NQueen(current_solution):
                # If valid, recursively solve for the next row
                solve_NQueens(dimension, row + 1, current_solution, solutions)
            current_solution.pop()

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    N = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if N < 4:
    print('N must be at least 4')
    exit(1)

# List to store all valid solutions to the N Queens problem
solutions = []

# Solve the N Queens problem
solve_NQueens(N, 0, [], solutions)

# Print all valid solutions
for solution in solutions:
    print(solution)
