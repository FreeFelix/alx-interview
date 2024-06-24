#!/usr/bin/python3
"""
Defines island perimeter finding function.
"""

def island_perimeter(grid):
    """
    Return the perimeter of an island.
    
    The grid represents water by 0 and land by 1.
    
    Args:
        grid (list): A list of list of integers representing an island.
        
    Returns:
        int: The perimeter of the island defined in grid.
    """
    # Determine the dimensions of the grid
    width = len(grid[0])
    height = len(grid)
    
    edges = 0  # Initialize edge count
    size = 0   # Initialize island size count
    
    # Traverse through each cell in the grid
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:  # Found land cell
                size += 1  # Increment island size count
                # Check adjacent cells to count shared edges
                if j > 0 and grid[i][j - 1] == 1:
                    edges += 1
                if i > 0 and grid[i - 1][j] == 1:
                    edges += 1
    
    # Calculate perimeter using the formula: total perimeter = 4 * island size - 2 * shared edges
    return size * 4 - edges * 2
