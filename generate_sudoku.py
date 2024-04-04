import random
from solver_backtracking import SolverBacktracking

# difficulty arguments (1,2,3) or (easy, medium, hard)
def generate_puzzle(difficulty):
    """
    Generates a Sudoku puzzle with a partially filled grid.
    """
    puzzle = []
    for _ in range(9):
        row = [0] * 9
        puzzle.append(row)

    num_of_initial_cells = 0
    if difficulty == "easy" or difficulty == 0:
        num_of_initial_cells = 30
    elif difficulty == "medium" or difficulty == 1:
        num_of_initial_cells = 25
    elif difficulty == "hard" or difficulty == 2:
        num_of_initial_cells = 20

    SolverBacktracking.solve_game(puzzle)

    # Randomly remove numbers to create a puzzle
    empty_cells = random.randint(71-num_of_initial_cells, 81-num_of_initial_cells)
    for _ in range(empty_cells):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0

    return puzzle