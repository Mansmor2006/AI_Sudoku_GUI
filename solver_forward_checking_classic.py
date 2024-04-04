class SolverForwardCheckingClassic:
    def __init__(self):
        self.domains = self.initialize_domains()

    # Returns True when sudoku fully solved otherwise False
    def solve_game(self, board):
        if self.is_not_empty(board):
            return True
        
        cell = self.select_first_empty_cell(board)
        row, col = cell
        
        for value in self.domains[cell]: 
            if self.is_value_valid(board, row, col, value):
                
                # Add number value to the cell
                board[row][col] = value 
                self.update_domains(cell, value)
                if self.solve_game(board):
                    return True  
                
                # Backtrack when dead end
                board[row][col] = 0 
                self.restore_domains(cell, value) 
        
        return False 

    def is_not_empty(self, board):
        for row in board:
            for cell in row:
                if cell == 0:
                    return False
        return True

    def select_first_empty_cell(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return -1, -1
    
    def is_value_valid(self, board, row, col, value):
        # Check if the value is already used in the same row
        for c in range(9):
            if board[row][c] == value:
                return False
        
        # Check if the value is already used in the same column
        for r in range(9):
            if board[r][col] == value:
                return False
        
        # Check if the value is already used in the same 3x3 block
        block_start_row = row - (row % 3)
        block_start_col = col - (col % 3)
        for r in range(block_start_row, block_start_row + 3):
            for c in range(block_start_col, block_start_col + 3):
                if board[r][c] == value:
                    return False
        
        return True
    
    def initialize_domains(self):
        domains = {}
        for row in range(9):
            for col in range(9):
                domains[(row, col)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return domains
    
    def update_domains(self, cell, value):
        # Removes the assigned value from the domains of rows, columns, and boxes.
 
        row, col = cell
        # Remove value from the row
        for i in range(9):
            if value in self.domains[(row, i)]:
                self.domains[(row, i)].remove(value)
        # Remove value from the column
        for i in range(9):
            if value in self.domains[(i, col)]:
                self.domains[(i, col)].remove(value)
        # Remove value from the box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if value in self.domains[(i, j)]:
                    self.domains[(i, j)].remove(value)

    def restore_domains(self, cell, value):
        # Restores the assigned value to the domains of rows, columns, and boxes.
        
        row, col = cell
        # Restore value to the row
        for i in range(9):
            if value not in self.domains[(row, i)]:
                self.domains[(row, i)].append(value)
        # Restore value to the column
        for i in range(9):
            if value not in self.domains[(i, col)]:
                self.domains[(i, col)].append(value)
        # Restore value to the box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if value not in self.domains[(i, j)]:
                    self.domains[(i, j)].append(value)


