import pygame
import sys





# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Initialize Pygame
pygame.init()

# Main game loop
def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    width, height = 600, 600
    screen = pygame.display.set_mode((width, height))
    screen.fill(WHITE)
    pygame.display.set_caption("Sudoku Puzzle")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for i in range(10):
        # Draw horizontal lines
            cell_size = width // 9
        # Draw horizontal lines
            pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size), 2)
        # Draw vertical lines
            pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height), 2)

        pygame.display.update()
if __name__ == "__main__":
    main()