import sys

import random
import pygame
from pygame.locals import *

# for loops


# counting


# grid = []
# grid = [1, 2223, 133, 444] # list
#
# print(grid)
# print(grid[3])
#
# grid.append(454)
# print(grid)
#
# grid = [0] * 4
# print(grid)

# for row in range(ROWS):
#     grid.append([0]*COLS)
# ROWS = 5
# COLS = 2
# grid = [[0] * COLS] * ROWS
#
# print(grid)

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

FPS = 120
clock = pygame.time.Clock()

# game loop
while True:
    # type everything you want to draw
    #
    # pygame.draw.rect()
    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    pygame.display.update()