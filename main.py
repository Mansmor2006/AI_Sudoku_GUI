import pygame
import sys
import copy

from generate_sudoku import *
from solver_backtracking import SolverBacktracking
from solver_forward_checking import SolverForwardChecking


class Sudoku:
    def __init__(self):
        pygame.init()

        # Define some colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.PURPLE = (50, 0, 155)

        # Width and height attributes
        self.width, self.height = 570, 670

        self.selected_difficulty = None

        self.show_splash_screen()

    def show_splash_screen(self):
        # Set up the display for splash screen
        self.splash_screen = pygame.display.set_mode(( self.width, self.height))
        pygame.display.set_caption("Sudoku Puzzle")

        # Set up fonts for splash screen
        self.splash_font = pygame.font.Font(None, 36)

        # Add a start button to the splash screen
        self.start_button_rect = pygame.Rect(230, 600, 100, 40)
        self.start_button_color = self.RED
        self.start_button_hover_color = (255, 50, 50)  # Highlight color when hovering
        self.start_button_text = self.splash_font.render("Start", True, self.WHITE)

        # Add radio buttons for difficulty levels
        self.radio_buttons = [
            {"rect": pygame.Rect(50, 400, 80, 30), "label": "Easy", "value": "easy", "color": self.RED, "selected": False},
            {"rect": pygame.Rect(230, 400, 110, 30), "label": "Medium", "value": "medium", "color": self.RED, "selected": False},
            {"rect": pygame.Rect(450, 400, 80, 30), "label": "Hard", "value": "hard", "color": self.RED, "selected": False},   
        ]
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
                    for button in self.radio_buttons:
                        if button["rect"].collidepoint(event.pos):
                            self.handle_radio_button_selection(button)
            # Check if the mouse is over the start button
            if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
                button_color = self.start_button_hover_color
            else:
                button_color = self.start_button_color
                       
            self.splash_screen.fill(self.BLACK)

            # Draw splash screen content
            splash_text = self.splash_font.render("welcome to my Sudoku Puzzle", True, self.GREEN)
            self.splash_screen.blit(splash_text, (100, 100))

            pygame.draw.rect(self.splash_screen, self.start_button_color, self.start_button_rect)
            self.splash_screen.blit(self.start_button_text, (self.start_button_rect.x + 10, self.start_button_rect.y + 10))

            # Draw radio buttons
            for button in self.radio_buttons:
                pygame.draw.rect(self.splash_screen, button.get("color", self.RED), button["rect"], 2)
                button_text = self.splash_font.render(button["label"], True, self.GREEN)
                self.splash_screen.blit(button_text, (button["rect"].x + 10, button["rect"].y + 5))

            pygame.display.flip()

    def setup_game(self):
        # Set up the display
        self.width, self.height = 570, 670
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Puzzle")

        # Set up fonts
        self.font = pygame.font.Font(None, 36)
        
        # Add a solve button
        self.solve_button_rect = pygame.Rect(20, self.height - 70, 100, 40)
        self.solve_button_color = self.RED
        self.solve_button_text = self.font.render("Solve", True, self.WHITE)

        # Add a Reset button
        self.reset_button_rect = pygame.Rect(self.width - 130, self.height - 70, 110, 40)
        self.reset_button_color = self.RED
        self.reset_button_text = self.font.render("Reset", True, self.WHITE)

        # Add a New Game button
        self.newgame_button_rect = pygame.Rect(210, self.height - 70, 150, 40)
        self.newgame_button_color = self.PURPLE
        self.newgame_button_text = self.font.render("New Game", True, self.WHITE)

        # Message area to display Solved or Unsolved
        self.message_area_rect = pygame.Rect(250, self.height - 97, self.width - 320, 27)
        self.message_area_color =  self.WHITE
        self.message_font = pygame.font.Font(None, 24)
        self.solving_message = " "

        # Initialize puzzle and solver
        self.puzzle = generate_puzzle(self.selected_difficulty)
        self.puzzle_for_reset = copy.deepcopy(self.puzzle)
        self.selected_cell = None
        #self.solver = SolverBacktracking()
        self.solver = SolverForwardChecking()

        self.main()  # Start the main game loop

    # Draw the Sudoku grid and buttons
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
                
        
        # Drawing of puzzle numbers
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] != 0:
                    number_text = self.font.render(
                        str(self.puzzle[i][j]), True, self.BLACK
                    )
                    self.screen.blit(
                        number_text, (j * cell_size + 20, i * cell_size + 10)
                    )

        # Draw selected red bordered square to type in
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

        # Draw the solve button in the expanded area
        pygame.draw.rect(self.screen, self.solve_button_color, self.solve_button_rect)
        self.screen.blit(self.solve_button_text, (self.solve_button_rect.x + 10, self.solve_button_rect.y + 10))

        # Draw the reset button in the expanded area
        pygame.draw.rect(self.screen, self.reset_button_color, self.reset_button_rect)
        self.screen.blit(self.reset_button_text, (self.reset_button_rect.x + 10, self.reset_button_rect.y + 10))

        # Draw the new game button in the expanded area
        pygame.draw.rect(self.screen, self.newgame_button_color, self.newgame_button_rect)
        self.screen.blit(self.newgame_button_text, (self.newgame_button_rect.x + 10, self.newgame_button_rect.y + 10))

        # Draw the message area that shows solved or unsolved after solve button clicked
        pygame.draw.rect(self.screen, self.message_area_color, self.message_area_rect)
        message_text = self.message_font.render(self.solving_message, True, self.BLACK)
        self.screen.blit(message_text, (self.message_area_rect.x + 10, self.message_area_rect.y + 5))

    # All Handlers for mouse and keyboard input
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
        
        # Add an additional condition to check if the click is within the button area
        elif (self.solve_button_rect.collidepoint(event.pos) or
            self.reset_button_rect.collidepoint(event.pos) or
            self.newgame_button_rect.collidepoint(event.pos)):
            # Clicking on buttons, handle button actions
            if self.solve_button_rect.collidepoint(event.pos):
                self.solving_message = "Solving..."
                solving_successful = self.solver.solve_game(self.puzzle)
                if solving_successful:
                    self.solving_message = "Solved"
                else:
                    self.solving_message = "No solution found"
            elif self.reset_button_rect.collidepoint(event.pos):
                self.reset_game()
            elif self.newgame_button_rect.collidepoint(event.pos):
                self.new_game()
    
    def keyboard_handler(self, event):
        if event.unicode.isdigit() and 1 <= int(event.unicode) <= 9:
            if SolverBacktracking.is_valid(
                self.puzzle,
                self.selected_cell[0],
                self.selected_cell[1],
                int(event.unicode),
            ):
            # Only allow changing if the cell is not part of the initial puzzle
                if self.puzzle[self.selected_cell[0]][self.selected_cell[1]] == 0:
                    self.puzzle[self.selected_cell[0]][self.selected_cell[1]] = int(event.unicode)

    def handle_radio_button_selection(self, selected_button):
        for button in self.radio_buttons:
            button["selected"] = False  # Deselect all buttons
            button["color"] = self.RED  # Reset colors

        selected_button["selected"] = True
        selected_button["color"] = self.GREEN
        self.selected_difficulty = selected_button["value"]

    def new_game(self):
        self.puzzle = generate_puzzle(self.selected_difficulty)
        self.puzzle_for_reset = copy.deepcopy(self.puzzle)
        self.solving_message = " "

    def reset_game(self):
        self.puzzle = copy.deepcopy(self.puzzle_for_reset)
        self.solving_message = " "

    def main(self):
        while True:
            self.event_handler()

            self.screen.fill(self.WHITE)
            self.draw_grid()

            pygame.display.flip()


if __name__ == "__main__":
    sudoku_game = Sudoku()
    pygame.quit()
