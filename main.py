import pygame
import sys
import random
from solver import Solver

class Sudoku:
    def __init__(self):
        pygame.init()

        # Define some colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)

         # Set up the display for splash screen
        self.splash_width, self.splash_height = 570, 670
        self.splash_screen = pygame.display.set_mode((self.splash_width, self.splash_height))
        pygame.display.set_caption("Sudoku Puzzle")

        # Set up fonts for splash screen
        self.splash_font = pygame.font.Font(None, 36)

        # Add a start button to the splash screen
        self.start_button_rect = pygame.Rect(230, 600, 100, 40)
        self.start_button_color = self.RED
        self.start_button_text = self.splash_font.render("Start", True, self.WHITE)

        self.show_splash_screen()

    def show_splash_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.start_button_rect.collidepoint(event.pos):
                        self.setup_game()  # Call a method to set up the game screen
                        pygame.quit()
                        return
                    
            self.splash_screen.fill(self.WHITE)

            # Draw splash screen content
            splash_text = self.splash_font.render("Sudoku Puzzle", True, self.BLACK)
            self.splash_screen.blit(splash_text, (200, 100))

            pygame.draw.rect(self.splash_screen, self.start_button_color, self.start_button_rect)
            self.splash_screen.blit(self.start_button_text, (self.start_button_rect.x + 10, self.start_button_rect.y + 10))

            pygame.display.flip()

    def setup_game(self):
        # Set up the display
        self.width, self.height = 570, 670
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Puzzle")

        # Set up fonts
        self.font = pygame.font.Font(None, 36)
        # Initialize puzzle
        self.puzzle = self.generate_puzzle()
        self.selected_cell = None

        # Add a solve button
        self.solve_button_rect = pygame.Rect(20, self.height - 70, 100, 40)
        self.solve_button_color = self.RED
        self.solve_button_text = self.font.render("Solve", True, self.WHITE)

        # Add a Reset button
        self.reset_button_rect = pygame.Rect(self.width - 130, self.height - 70, 110, 40)
        self.reset_button_color = self.RED
        self.reset_button_text = self.font.render("Reset", True, self.WHITE)

        self.main()  # Start the main game loop

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
            row, col, num = (
                random.randint(0, 8),
                random.randint(0, 8),
                random.randint(1, 9),
            )
            while not self.is_valid(puzzle, row, col, num):
                row, col, num = (
                    random.randint(0, 8),
                    random.randint(0, 8),
                    random.randint(1, 9),
                )
            puzzle[row][col] = num
        return puzzle

    # Check if placing a number in a certain position is a valid move
    def is_valid(self, board, row, col, num):
        """
        Checks if placing a number at a given position in the Sudoku grid is a valid move.
        """
        return (
            num not in board[row]
            and num not in [board[i][col] for i in range(9)]
            and num
            not in [
                board[i][j]
                for i in range(row - row % 3, row - row % 3 + 3)
                for j in range(col - col % 3, col - col % 3 + 3)
            ]
        )

    # Draw the Sudoku grid
    def draw_grid(self):
        """
        Draws the Sudoku grid on the screen.
        """
        cell_size = self.width // 9

        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(
                    self.screen,
                    self.BLACK,
                    (0, i * cell_size),
                    (self.width, i * cell_size),
                    4,
                )
                pygame.draw.line(
                    self.screen,
                    self.BLACK,
                    (i * cell_size, 0),
                    (i * cell_size, self.height-100),
                    4,
                )
            else:
                pygame.draw.line(
                    self.screen,
                    self.BLACK,
                    (0, i * cell_size),
                    (self.width, i * cell_size),
                    2,
                )
                pygame.draw.line(
                    self.screen,
                    self.BLACK,
                    (i * cell_size, 0),
                    (i * cell_size, self.height-100),
                    2,
                )
        # Draw the solve button in the expanded area
        pygame.draw.rect(self.screen, self.solve_button_color, self.solve_button_rect)
        self.screen.blit(self.solve_button_text, (self.solve_button_rect.x + 10, self.solve_button_rect.y + 10))

        # Draw the solve button in the expanded area
        pygame.draw.rect(self.screen, self.reset_button_color, self.reset_button_rect)
        self.screen.blit(self.reset_button_text, (self.reset_button_rect.x + 10, self.reset_button_rect.y + 10))

        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] != 0:
                    number_text = self.font.render(
                        str(self.puzzle[i][j]), True, self.BLACK
                    )
                    self.screen.blit(
                        number_text, (j * cell_size + 20, i * cell_size + 10)
                    )

        if self.selected_cell:
            pygame.draw.rect(
                self.screen,
                self.RED,
                (
                    self.selected_cell[1] * cell_size,
                    self.selected_cell[0] * cell_size,
                    cell_size,
                    cell_size,
                ),
                3,
            )

    def event_handler(self):
        """
        Handles events and updates the display.
        """
        events = {
            pygame.QUIT: self.quit_handler,
            pygame.MOUSEBUTTONDOWN: self.mouse_click_handler,
            pygame.KEYDOWN: self.keyboard_handler,
        }

        for event in pygame.event.get():
            handler = events.get(event.type)
            if handler:
                handler(event)

    def quit_handler(self, event):
        pygame.quit()
        sys.exit()

    def mouse_click_handler(self, event):
        # Check if the click is within the board
        if 0 <= event.pos[0] <= self.width and 0 <= event.pos[1] <= self.height - 100:
            cell_size = self.width // 9
            self.selected_cell = (event.pos[1] // cell_size, event.pos[0] // cell_size)
    
        # Check if the solve button is clicked
        elif self.solve_button_rect.collidepoint(event.pos):
            solver = Solver()
            solver.solve_game(self.puzzle)
        # Check if the reset button is clicked
        elif self.reset_button_rect.collidepoint(event.pos):
            self.puzzle = self.generate_puzzle()

    def keyboard_handler(self, event):
        if event.unicode.isdigit() and 1 <= int(event.unicode) <= 9:
            if self.is_valid(
                self.puzzle,
                self.selected_cell[0],
                self.selected_cell[1],
                int(event.unicode),
            ):
            # Only allow changing if the cell is not part of the initial puzzle
                if self.puzzle[self.selected_cell[0]][self.selected_cell[1]] == 0:
                    self.puzzle[self.selected_cell[0]][self.selected_cell[1]] = int(event.unicode)

    def main(self):
        while True:
            self.event_handler()

            self.screen.fill(self.WHITE)
            self.draw_grid()
            pygame.display.flip()


if __name__ == "__main__":
    sudoku_game = Sudoku()
    sudoku_game.main()
