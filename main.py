import pygame
import sys
from grid import Grid
from simulation import Simulation


pygame.init()

GREY = (29, 29, 29)
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
FPS = 12
CELL_SIZE = 25



window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game Of Life")

clock = pygame.time.Clock()

simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
simulation.grid.cells[5][29] = 1




# Simulation Loop

while True:

    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Updating State

    # 3. Drawing the Grid
    window.fill(GREY)

    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS)
