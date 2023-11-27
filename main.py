import pygame
import sys

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)
pygame.display.set_caption("Sudoku Puzzle")



# Draw the Sudoku grid
def draw_grid():
    cell_size = width // 9

    for i in range(10):
        if (i % 3 == 0):
            pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size), 4)
            pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height), 4)

        pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size), 2)
        pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height), 2)

# Main game loop
def main():
    # Initialize Pygame
    pygame.init()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_grid()
        pygame.display.update()
        
if __name__ == "__main__":
    main()