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
            solver.solve_puzzle(self.puzzle)

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
