import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
width, height = 570, 570
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Puzzle")

# Set up fonts
font = pygame.font.Font(None, 36)

puzzle = []
for _ in range(9):
    row = []
    for _ in range(9):
        row.append(0)
    puzzle.append(row)

# Sudoku puzzle generator function
def generate_puzzle():

    puzzle = []
    for _ in range(9):
        row = []
        for _ in range(9):
            row.append(0)
        puzzle.append(row)

    for _ in range(40):  
        row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        while not is_valid(puzzle, row, col, num):
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        puzzle[row][col] = num
    return puzzle

# Check if placing a number in a certain position is a valid move
def is_valid(board, row, col, num):
    return (
        num not in board[row] and
        num not in [board[i][col] for i in range(9)] and
        num not in [board[i][j] for i in range(row - row % 3, row - row % 3 + 3) for j in range(col - col % 3, col - col % 3 + 3)]
    )

# Draw the Sudoku grid
def draw_grid(board, selected_cell):
    cell_size = width // 9

    for i in range(10):
        if (i % 3 == 0):
            pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size), 4)
            pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height), 4)
        else:
            pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size), 2)
            pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height), 2)
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                number_text = font.render(str(board[i][j]), True, BLACK)
                screen.blit(number_text, (j * cell_size + 20, i * cell_size + 10))

    if selected_cell:
        pygame.draw.rect(screen, RED, (selected_cell[1] * cell_size, selected_cell[0] * cell_size, cell_size, cell_size), 3)

# Main game loop
def main():
    puzzle = generate_puzzle()
    selected_cell = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected_cell = (event.pos[1] // (width // 9), event.pos[0] // (height // 9))
            elif event.type == pygame.KEYDOWN and selected_cell:
                if event.unicode.isdigit() and 1 <= int(event.unicode) <= 9:
                    if is_valid(puzzle, selected_cell[0], selected_cell[1], int(event.unicode)):
                        puzzle[selected_cell[0]][selected_cell[1]] = int(event.unicode)
        
            

        

        screen.fill(WHITE)
        draw_grid(puzzle, selected_cell)
        pygame.display.flip()
        

        

if __name__ == "__main__":
    main()