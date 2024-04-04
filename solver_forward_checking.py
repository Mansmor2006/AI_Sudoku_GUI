class SolverForwardChecking:
    # Returns True when sudoku fully solved otherwise False
    def solve_game(self, board):
        if self.is_not_empty(board):
            return True
        
        row, col = self.select_first_empty_cell(board)
        
        # Filter out inconsistent values from cell domain,
        # so that consistent values (that align with  constraints) remain,
        # instead of using inconsistent values which can lead to dead ends.
        for value in self.get_possible_domain_values(board, row, col): 
            if self.is_value_valid(board, row, col, value):
                
                # Add number value to the cell
                board[row][col] = value 
                
                if self.solve_game(board):
                    return True  
                
                # Backtrack when dead end
                board[row][col] = 0  
        
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
    
    def get_block_start(self, row, col):
        block_start_row = row - (row % 3)
        block_start_col = col - (col % 3)
        return block_start_row, block_start_col
    
    # Function forward checks to not choose domain values that are already existing in neighbouring cell domain
    # Instead of initializing domains for each cell as a global variable then update/delete a value from the domains when assigning,
    # we check only current cell domains and see if its available in other cells, then delete it from current cell domain on the go.
    def get_possible_domain_values(self, board, row, col):
        # Initialize domain with all possibilities 
        possible_values = set(range(1, 10))  
        
        # Delete values that are already used in the same row
        for c in range(9):
            possible_values.discard(board[row][c])
        
        # Delete values that are already used in the same column
        for r in range(9):
            possible_values.discard(board[r][col])
        
        # Delete values that are already used in the same 3x3 block
        block_start_row, block_start_col = self.get_block_start(row, col)
        block_end_row, block_end_col = (block_start_row + 3, block_start_col + 3)
        for r in range(block_start_row, block_end_row):
            for c in range(block_start_col, block_end_col):
                possible_values.discard(board[r][c])
        
        return possible_values

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
        block_start_row, block_start_col = self.get_block_start(row, col)
        for r in range(block_start_row, block_start_row + 3):
            for c in range(block_start_col, block_start_col + 3):
                if board[r][c] == value:
                    return False
        
        return True
    
