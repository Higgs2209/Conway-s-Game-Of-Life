import pygame
import sys
from grid import Grid
from simulation import Simulation


pygame.init()

GREY = (29, 29, 29)
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
FPS = 12
CELL_SIZE = 4

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game Of Life")

clock = pygame.time.Clock()

simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation Loop
while True:

    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Game Of Life is Running")
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of Life Has Stopped")
            elif event.key == pygame.K_f:
                FPS += 2
            elif event.key == pygame.K_s:
                if FPS > 5:
                    FPS -= 2
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            elif event.key == pygame.K_c:
                simulation.clear()

    # 2. Updating State
    simulation.update()

    # 3. Drawing the Grid
    window.fill(GREY)

    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS)
