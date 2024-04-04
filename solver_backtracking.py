import random
"""
    Made Methods static to use some functions on their own.
    for example in generating sudoku puzzle.
"""
class SolverBacktracking:
    @staticmethod
    def solve_game(board):
        empty_cell = SolverBacktracking.find_empty_cell(board)
        if not empty_cell:
            return True  # Puzzle is solved

        row, col = empty_cell

        nums = list(range(1, 10))
        random.shuffle(nums)
        for num in nums:
            if SolverBacktracking.is_valid(board, row, col, num):
                board[row][col] = num

                if SolverBacktracking.solve_game(board):
                    return True  # Recursive call successful

                board[row][col] = 0  # Backtrack if the current path doesn't lead to a solution

        return False  # No valid number found

    @staticmethod
    def find_empty_cell(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return(i,j)
        return None
         
    @staticmethod
    def is_valid(board, row, col, num):
        # Check if num is not present in the current row
        if num in board[row]:
            return False

        # Check if num is not present in the current column
        for i in range(9):
            if num == board[i][col]:
                return False

        # Check if num is not present in the 3x3 subgrid
        subgrid_start_row, subgrid_start_col = row - row % 3, col - col % 3
        for i in range(subgrid_start_row, subgrid_start_row + 3):
            for j in range(subgrid_start_col, subgrid_start_col + 3):
                if num == board[i][j]:
                    return False

        # If all checks pass, the move is valid
        return True