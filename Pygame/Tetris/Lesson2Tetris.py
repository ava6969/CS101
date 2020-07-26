import pygame, sys
from pygame.locals import *
from Pygame.Tetris.Grid import Grid

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
gray = (255//2, 255//2, 255//2)

colors = [gray, black, white]

clock = pygame.time.Clock()
FPS = 60
WIDTH = 640
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# attributes of board
ROWS = 40
COLS = 10
TILE_SIZE = 20
grid = Grid(ROWS, COLS, TILE_SIZE, gray)

while True:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    grid.draw_play_area((10, 10), screen)

    pygame.display.update()




