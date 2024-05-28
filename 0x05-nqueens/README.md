# N Queens Puzzle

## Overview

This project involves solving the N Queens puzzle using Python and the backtracking algorithm. The N Queens puzzle is a classic problem in which N queens must be placed on an N×N chessboard in such a way that no two queens threaten each other. In other words, no two queens should share the same row, column, or diagonal.

## Files

- `nqueens.py`: Python script containing the implementation of the N Queens puzzle solver.
- `README.md`: This file, providing an overview of the project and instructions for usage.

## How to Use

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Run the `nqueens.py` script with the desired value of N (size of the chessboard):

    ```bash
    ./nqueens.py 8
    ```

    Replace `8` with the desired value of N. Ensure that N is at least 4, as the puzzle is not solvable for N less than 4.

4. The script will output all valid solutions to the N Queens puzzle for the given value of N.

## Example

```bash
$ ./nqueens.py 4
[1, 3, 0, 2]
[2, 0, 3, 1]


Resources

Wikipedia - N Queens puzzle
Wikipedia - Backtracking

Requirements

Python 3.4.3 or higher
PEP 8 compliant code
Executable files
README.md file

Author

Your Name - @freefelix


Feel free to customize it further to include additional information or instructions specific to your project.
