import sys

import pygame
from pygame.locals import *

# initialize pygame
from kwakuSantiago.Grid import Grid
from kwakuSantiago.utlis import *
from kwakuSantiago.Tetrimino import Tetrimino

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (155, 155, 155)

colors = [black, ]

FPS = 60
clock = pygame.time.Clock()
ROWS = 40
COLS = 10
TILESIZE = 20
grid = Grid(ROWS, COLS, TILESIZE)
active_tet = Tetrimino(grid)

level = 1
current_drop_delay = base_drop_delay = calculate_drop_delay(level)
drop_timer = 0

locking = False
lock_delay = 30
lock_counter = 0
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                active_tet.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                active_tet.move(1, 0)
            elif event.key == pygame.K_DOWN:
                active_tet.move(0, 1)
            elif event.key == pygame.K_UP:
                active_tet.rotate(1)
            elif event.key == pygame.K_z:
                active_tet.rotate(-1)
    screen.fill(gray)

    drop_timer += 1
    if drop_timer >= current_drop_delay:
        move = active_tet.move(0, 1)
        drop_timer = 0
    #     if not move:
    #         if not locking:
    #             locking = True
    #             lock_counter = 0
    #         else:
    #             locking = False
    #     drop_timer = 0
    #
    # if locking:
    #     lock_counter += 1
    #     if lock_counter >= lock_delay:
    #         active_tet.lock()
    #         drop_timer = base_drop_delay
    #         lock_counter = 0
    #         locking = False
    #         active_tet.reset()


    grid.draw_board()
    active_tet.draw_tetrimino()
    grid.draw_play_area((10, 10), screen)
    pygame.display.update()

