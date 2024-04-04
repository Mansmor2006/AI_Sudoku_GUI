import copy
import unittest
# from generate_sudoku import *
from solver_backtracking import SolverBacktracking
from solver_forward_checking import SolverForwardChecking


class TestBacktrackingSolver(unittest.TestCase):
    
    empty_board = [[0 for _ in range(9)] for _ in range(9)]


    easy_puzzle = [[0, 0, 0, 7, 2, 0, 4, 9, 0],
        [0, 0, 8, 0, 0, 0, 3, 0, 1],
        [0, 9, 0, 0, 4, 0, 0, 0, 8],
        [0, 7, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 1, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 2, 8, 5, 9, 4, 0],
        [0, 0, 9, 3, 0, 0, 0, 7, 0],
        [2, 0, 0, 4, 0, 9, 0, 0, 0]]
    
    

    easy_puzzle_solution = [
            [3, 1, 5, 7, 2, 8, 4, 9, 6],
            [7, 4, 8, 9, 5, 6, 3, 2, 1],
            [6, 9, 2, 1, 4, 3, 7, 5, 8],
            [8, 7, 6, 5, 3, 4, 2, 1, 9],
            [9, 3, 4, 6, 1, 2, 5, 8, 7],
            [5, 2, 1, 8, 9, 7, 6, 3, 4],
            [1, 6, 7, 2, 8, 5, 9, 4, 3],
            [4, 5, 9, 3, 6, 1, 8, 7, 2],
            [2, 8, 3, 4, 7, 9, 1, 6, 5]
        ]


    medium_puzzle = [
        [0, 7, 0, 0, 0, 0, 0, 4, 3],
       [0, 4, 0, 0, 0, 9, 6, 1, 0],
       [8, 0, 0, 6, 3, 4, 9, 0, 0],
       [0, 9, 4, 0, 5, 2, 0, 0, 0],
       [3, 5, 8, 4, 6, 0, 0, 2, 0],
       [0, 0, 0, 8, 0, 0, 5, 3, 0],
       [0, 8, 0, 0, 7, 0, 0, 9, 1],
       [9, 0, 2, 1, 0, 0, 0, 0, 5],
       [0, 0, 7, 0, 4, 0, 8, 0, 2]
       ]


    medium_puzzle_solution = [[6, 7, 9, 5, 1, 8, 2, 4, 3],
            [5, 4, 3, 7, 2, 9, 6, 1, 8],
            [8, 2, 1, 6, 3, 4, 9, 5, 7],
            [7, 9, 4, 3, 5, 2, 1, 8, 6],
            [3, 5, 8, 4, 6, 1, 7, 2, 9],
            [2, 1, 6, 8, 9, 7, 5, 3, 4],
            [4, 8, 5, 2, 7, 6, 3, 9, 1],
            [9, 6, 2, 1, 8, 3, 4, 7, 5],
            [1, 3, 7, 9, 4, 5, 8, 6, 2]]


    hard_puzzle =   [[0, 0, 3, 4, 0, 6, 0, 8, 9],
                [0, 0, 0, 0, 0, 9, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 5, 0],
                [0, 0, 4, 3, 0, 0, 8, 0, 0],
                [3, 6, 0, 0, 0, 7, 0, 0, 4],
                [8, 9, 0, 0, 0, 0, 3, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [6, 0, 2, 0, 7, 0, 0, 0, 0],
                [9, 7, 8, 0, 0, 0, 0, 0, 2]]

    hard_puzzle_solution = [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 1, 4, 3, 6, 5, 8, 9, 7],
                [3, 6, 5, 8, 9, 7, 2, 1, 4],
                [8, 9, 7, 2, 1, 4, 3, 6, 5],
                [5, 3, 1, 6, 4, 2, 9, 7, 8],
                [6, 4, 2, 9, 7, 8, 5, 3, 1],
                [9, 7, 8, 5, 3, 1, 6, 4, 2]]
    
    def test_solve_empty_sudoku_puzzle(self):
        SolverBacktracking.solve_game(self.empty_board)
        is_empty = lambda board: next(((i, j) for i in range(9) for j in range(9) if board[i][j] == 0), False)
        self.assertFalse(is_empty(self.empty_board))
        #print(self.empty_board)
    
    def test_solve_easy_sudoku_puzzle(self):
        success = False
        # Try out max combinations
        for _ in range(1000):
            try:
                easy_puzzle = copy.deepcopy(self.easy_puzzle)
                SolverBacktracking.solve_game(easy_puzzle)
                self.assertEqual(easy_puzzle, self.easy_puzzle_solution)
                success = True  # Set success flag to True if assert is successful
                break  # Exit the loop if assert is successful
            except AssertionError as e:
                last_error_message = str(e)
                continue

        if not success and last_error_message is not None:
            raise AssertionError(last_error_message)
        
    def test_solve_medium_sudoku_puzzle(self):
        success = False
        # Try out max combinations
        for _ in range(1000):
            try:
                medium_puzzle = copy.deepcopy(self.medium_puzzle)
                SolverBacktracking.solve_game(medium_puzzle)
                self.assertEqual(medium_puzzle, self.medium_puzzle_solution)
                success = True  # Set success flag to True if assert is successful
                break  # Exit the loop if assert is successful
            except AssertionError as e:
                last_error_message = str(e)
                continue

        if not success and last_error_message is not None:
            raise AssertionError(last_error_message)
    
    def test_solve_hard_sudoku_puzzle(self):
        success = False
        # Try out max combinations
        for _ in range(1000):
            try:
                hard_puzzle = copy.deepcopy(self.hard_puzzle)
                SolverBacktracking.solve_game(hard_puzzle)
                self.assertEqual(hard_puzzle, self.hard_puzzle_solution)
                success = True  # Set success flag to True if assert is successful
                break  # Exit the loop if assert is successful
            except AssertionError as e:
                last_error_message = str(e)
                continue

        if not success and last_error_message is not None:
            raise AssertionError(last_error_message)
   

class TestForwardCheckingSolver(unittest.TestCase):
    solver = SolverForwardChecking()
    empty_board = [[0 for _ in range(9)] for _ in range(9)]


    easy_puzzle = [[0, 0, 0, 7, 2, 0, 4, 9, 0],
        [0, 0, 8, 0, 0, 0, 3, 0, 1],
        [0, 9, 0, 0, 4, 0, 0, 0, 8],
        [0, 7, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 1, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 2, 8, 5, 9, 4, 0],
        [0, 0, 9, 3, 0, 0, 0, 7, 0],
        [2, 0, 0, 4, 0, 9, 0, 0, 0]]
    
    

    easy_puzzle_solution = [
            [3, 1, 5, 7, 2, 8, 4, 9, 6],
            [7, 4, 8, 9, 5, 6, 3, 2, 1],
            [6, 9, 2, 1, 4, 3, 7, 5, 8],
            [8, 7, 6, 5, 3, 4, 2, 1, 9],
            [9, 3, 4, 6, 1, 2, 5, 8, 7],
            [5, 2, 1, 8, 9, 7, 6, 3, 4],
            [1, 6, 7, 2, 8, 5, 9, 4, 3],
            [4, 5, 9, 3, 6, 1, 8, 7, 2],
            [2, 8, 3, 4, 7, 9, 1, 6, 5]
        ]


    medium_puzzle = [
        [0, 7, 0, 0, 0, 0, 0, 4, 3],
       [0, 4, 0, 0, 0, 9, 6, 1, 0],
       [8, 0, 0, 6, 3, 4, 9, 0, 0],
       [0, 9, 4, 0, 5, 2, 0, 0, 0],
       [3, 5, 8, 4, 6, 0, 0, 2, 0],
       [0, 0, 0, 8, 0, 0, 5, 3, 0],
       [0, 8, 0, 0, 7, 0, 0, 9, 1],
       [9, 0, 2, 1, 0, 0, 0, 0, 5],
       [0, 0, 7, 0, 4, 0, 8, 0, 2]
       ]


    medium_puzzle_solution = [[6, 7, 9, 5, 1, 8, 2, 4, 3],
            [5, 4, 3, 7, 2, 9, 6, 1, 8],
            [8, 2, 1, 6, 3, 4, 9, 5, 7],
            [7, 9, 4, 3, 5, 2, 1, 8, 6],
            [3, 5, 8, 4, 6, 1, 7, 2, 9],
            [2, 1, 6, 8, 9, 7, 5, 3, 4],
            [4, 8, 5, 2, 7, 6, 3, 9, 1],
            [9, 6, 2, 1, 8, 3, 4, 7, 5],
            [1, 3, 7, 9, 4, 5, 8, 6, 2]]


    hard_puzzle =   [[0, 0, 3, 4, 0, 6, 0, 8, 9],
                [0, 0, 0, 0, 0, 9, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 5, 0],
                [0, 0, 4, 3, 0, 0, 8, 0, 0],
                [3, 6, 0, 0, 0, 7, 0, 0, 4],
                [8, 9, 0, 0, 0, 0, 3, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [6, 0, 2, 0, 7, 0, 0, 0, 0],
                [9, 7, 8, 0, 0, 0, 0, 0, 2]]

    hard_puzzle_solution = [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 1, 4, 3, 6, 5, 8, 9, 7],
                [3, 6, 5, 8, 9, 7, 2, 1, 4],
                [8, 9, 7, 2, 1, 4, 3, 6, 5],
                [5, 3, 1, 6, 4, 2, 9, 7, 8],
                [6, 4, 2, 9, 7, 8, 5, 3, 1],
                [9, 7, 8, 5, 3, 1, 6, 4, 2]]
    
    def test_solve_empty_sudoku_puzzle(self):
        self.solver.solve_game(self.empty_board)
        is_empty = lambda board: next(((i, j) for i in range(9) for j in range(9) if board[i][j] == 0), False)
        self.assertFalse(is_empty(self.empty_board))
        #print(self.empty_board)
    
    def test_solve_easy_sudoku_puzzle(self):
        success = False
        # Try out max combinations
        for _ in range(1000):
            try:
                easy_puzzle = copy.deepcopy(self.easy_puzzle)
                self.solver.solve_game(easy_puzzle)
                self.assertEqual(easy_puzzle, self.easy_puzzle_solution)
                success = True  # Set success flag to True if assert is successful
                break  # Exit the loop if assert is successful
            except AssertionError as e:
                last_error_message = str(e)
                continue

        if not success and last_error_message is not None:
            raise AssertionError(last_error_message)
        
    def test_solve_medium_sudoku_puzzle(self):
        success = False
        # Try out max combinations
        for _ in range(1000):
            try:
                medium_puzzle = copy.deepcopy(self.medium_puzzle)
                self.solver.solve_game(medium_puzzle)
                self.assertEqual(medium_puzzle, self.medium_puzzle_solution)
                success = True  # Set success flag to True if assert is successful
                break  # Exit the loop if assert is successful
            except AssertionError as e:
                last_error_message = str(e)
                continue

        if not success and last_error_message is not None:
            raise AssertionError(last_error_message)
    
    def test_solve_hard_sudoku_puzzle(self):
        success = False
        # Try out max combinations
        for _ in range(1000):
            try:
                hard_puzzle = copy.deepcopy(self.hard_puzzle)
                self.solver.solve_game(hard_puzzle)
                self.assertEqual(hard_puzzle, self.hard_puzzle_solution)
                success = True  # Set success flag to True if assert is successful
                break  # Exit the loop if assert is successful
            except AssertionError as e:
                last_error_message = str(e)
                continue

        if not success and last_error_message is not None:
            raise AssertionError(last_error_message)
   
# If the script is run directly, run the tests
if __name__ == '__main__':
    unittest.main()
