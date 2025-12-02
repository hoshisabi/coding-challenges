import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
BOX_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game grid with X symbols randomly assigned to 75% of the squares
grid = [[random.choice([True, False]) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Game")

font = pygame.font.Font(None, 36)

def draw_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(j * BOX_SIZE, i * BOX_SIZE, BOX_SIZE, BOX_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

            if grid[i][j]:
                text = font.render("X", True, RED)
                screen.blit(text, rect.move(BOX_SIZE // 3, BOX_SIZE // 4))
    
            # Display row and column labels
            if j == 0:
                text = font.render(str(i), True, BLACK)
                screen.blit(text, rect.move(5, 5))  # Draw near top-left of cell
            if i == 0:
                text = font.render(chr(ord('A') + j), True, BLACK)
                screen.blit(text, rect.move(BOX_SIZE // 2, 5))  # Draw near top of cell

def update_grid(row, col):
    for i in range(GRID_SIZE):
        # Toggle the value of the selected row
        grid[row][i] = not grid[row][i]
        # Toggle the value of the selected column
        grid[i][col] = not grid[i][col]

    # Toggle the value of the selected square
    grid[row][col] = not grid[row][col]


def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // BOX_SIZE
                col = x // BOX_SIZE
                if event.button == 1:  # Left click
                    update_grid(row, col)
                elif event.button == 3:  # Right click
                    grid[row][col] = not grid[row][col]
        screen.fill(WHITE)
        draw_grid()

        pygame.display.flip()
        clock.tick(60) # Limit frames per second

if __name__ == "__main__":
 main()
 pygame.quit()
 sys.exit()