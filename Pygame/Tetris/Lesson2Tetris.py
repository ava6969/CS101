import pygame, sys
from pygame.locals import *

from Pygame.Tetris.Tetrimino import *
from Pygame.Tetris.Grid import Grid

pygame.init()

# Game States
RESTART = -1
PLAYING = 0
GAME_OVER = 1
game_state = PLAYING

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
grid = Grid(ROWS, COLS, TILE_SIZE, gray, colors)

# tetrimono
active_tetrimino = Tetrimino(grid)
active_tetrimino.reset()

while True:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    active_tetrimino.move(0, 1)
    grid.draw_board()
    active_tetrimino.draw_tetrimino(3, 30, pieces["I"][0])
    # active_tetrimino.draw_tetrimino(active_tetrimino.x, active_tetrimino.y, pieces[active_tetrimino.type][active_tetrimino.rotation])
    grid.draw_play_area((10, 10), screen)

    pygame.display.update()




