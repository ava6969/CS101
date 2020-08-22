import math
import sys
import pygame
from LucasTetris.Board import Board
from LucasTetris.util import *
from LucasTetris.Tetrimino import Tetrimino
pygame.init()

# variables for windows and tiles
clock = pygame.time.Clock()
FPS = 60
WIDTH = 640
HEIGHT = 480
TILE_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris game')


def calculate_drop_time(level):
   return math.floor(math.pow((0.8 - ((level - 1) * 0.007)), level-1) * 60)

# level
grid = Board(40, 10, 20)
active_tetrimino = Tetrimino(grid)

# droptime
level = 1
lock_clock = 0
locking = False
lock_delay = 4
drop_clock = 0
current_drop_time = base_drop_time = calculate_drop_time(level)

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                active_tetrimino.move(1, 0)
            if event.key == pygame.K_LEFT:
                active_tetrimino.move(-1, 0)

    drop_clock += 1
    if drop_clock >= current_drop_time:
        have_moved = active_tetrimino.move(0, 1)
        if not have_moved:
            if not locking:
                locking = True
                lock_clock = 0
            else:
                locking = False
        drop_clock = 0

    if locking:
        lock_clock += 1
        if lock_clock >= lock_delay:
            active_tetrimino.lock()
            drop_clock = base_drop_time
            lock_clock = 0
            locking = False
            active_tetrimino.reset()


    screen.fill(gray)
    grid.draw_board()
    active_tetrimino.draw_tetrimino()
    grid.draw_play_area((10, 10), screen)


    pygame.display.update()

