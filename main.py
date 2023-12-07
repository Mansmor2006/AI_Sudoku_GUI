import pygame 
import sys
import random

class Sudoku:
    def __init__(self):
        pygame.init()

        # Define some colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)

        # Set up the display
        self.width, self.height = 570, 570
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Puzzle")

        # Set up fonts
        self.font = pygame.font.Font(None, 36)
    # Initialize puzzle
        self.puzzle = self.generate_puzzle()
        self.selected_cell = None

    # Sudoku puzzle generator function
    def generate_puzzle(self):
        """
        Generates a Sudoku puzzle with a partially filled grid.
        """
        puzzle = []
        for _ in range(9):
            row = [0] * 9
            puzzle.append(row)

        for _ in range(40):  
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
            while not self.is_valid(puzzle, row, col, num):
                row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
            puzzle[row][col] = num
        return puzzle

    # Check if placing a number in a certain position is a valid move
    def is_valid(self, board, row, col, num):
        """
        Checks if placing a number at a given position in the Sudoku grid is a valid move.
        """
        return (
            num not in board[row] and
            num not in [board[i][col] for i in range(9)] and
            num not in [board[i][j] for i in range(row - row % 3, row - row % 3 + 3) for j in range(col - col % 3, col - col % 3 + 3)]
        )

    # Draw the Sudoku grid
    def draw_grid(self):
        """
        Draws the Sudoku grid on the screen.
        """
        cell_size = self.width // 9

        for i in range(10):
            if (i % 3 == 0):
                pygame.draw.line(self.screen, self.BLACK, (0, i * cell_size), (self.width, i * cell_size), 4)
                pygame.draw.line(self.screen, self.BLACK, (i * cell_size, 0), (i * cell_size, self.height), 4)
            else:
                pygame.draw.line(self.screen, self.BLACK, (0, i * cell_size), (self.width, i * cell_size), 2)
                pygame.draw.line(self.screen, self.BLACK, (i * cell_size, 0), (i * cell_size, self.height), 2)
        
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] != 0:
                    number_text = self.font.render(str(self.puzzle[i][j]), True, self.BLACK)
                    self.screen.blit(number_text, (j * cell_size + 20, i * cell_size + 10))

        if self.selected_cell:
            pygame.draw.rect(self.screen, self.RED, (self.selected_cell[1] * cell_size, self.selected_cell[0] * cell_size, cell_size, cell_size), 3) 

    def event_handler(self): 
            """
            Handles events and updates the display.
            """  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    selected_cell = (event.pos[1] // (self.width // 9), event.pos[0] // (self.height // 9))
                elif event.type == pygame.KEYDOWN and selected_cell:
                    
                    if event.unicode.isdigit() and 1 <= int(event.unicode) <= 9:
                        if self.is_valid(self.puzzle, selected_cell[0], selected_cell[1], int(event.unicode)):
                            self.puzzle[selected_cell[0]][selected_cell[1]] = int(event.unicode)

    def main(self):
        while True:
            self.event_handler()        
            
            self.screen.fill(self.WHITE)
            self.draw_grid()
            pygame.display.flip()
        

        

if __name__ == "__main__":
    sudoku_game = Sudoku()
    sudoku_game.main()