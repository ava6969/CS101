import sys

import pygame
from pygame.locals import *
from AndyJohnson.Grid import Grid
from AndyJohnson.Tetrimino import Tetrimino

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 320

# colors
white = (255, 255, 255)
gray = tuple([c//2 for c in white])

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

ROWS = 40
COLS = 10
FPS = 10
TILE_SIZE = 20

clock = pygame.time.Clock()
grid = Grid(ROWS, COLS, TILE_SIZE)
active_tetrimino = Tetrimino(grid)


while True:

    clock.tick(FPS)
    for event in pygame.event.get():

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         rect = rect2

        if event.type == pygame.QUIT:
            pygame.quit() # end pygame
            sys.exit() # end program

    screen.fill(gray)
    grid.draw_grid()
    active_tetrimino.move(0, 1)
    active_tetrimino.draw_tetrimino()
    grid.draw_play_area((30,10), screen)

    pygame.display.update()
