import sys

import pygame
from pygame.locals import *
# NEW: Import assets from tetris_pieces4.py
# IMPORTANT NOTE 1: depending on how your Pycharm is set up you might need to add this directory as a path in the project interpreter settings
from Pygame.Tetris.tetris_pieces import *

pygame.init()

# Colors
black = (0,0,0)
cyan = (0,255,255)
blue = (0,0,255)
orange = (255,100,10)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
purple = (160,32,240)
gray = (190, 190, 190)

colors = [black, cyan, blue, orange, yellow, green, purple, red]

#Variables for window and tiles
clock = pygame.time.Clock()
FPS = 60
WIDTH = 640
HEIGHT = 480
TILE_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Game States
RESTART = -1
PLAYING = 0
GAME_OVER = 1
game_state = PLAYING

ROWS = 20
COLS = 20
board = []

for _ in range(ROWS):
    column = []
    for _ in range(COLS):
        column.append(0)
    board.append(column)

board_surface = pygame.Surface((COLS*TILE_SIZE, ROWS*TILE_SIZE))


def draw_board(board, board_surface):
    for row in range(ROWS):
        for col in range(COLS):
            current_tile = board[row][col]
            tile_x =  col * TILE_SIZE
            tile_y = row * TILE_SIZE
            draw_tile(tile_x, tile_y, current_tile, board_surface)


def draw_tile(posX, posY, tile, surface):
    tile_color = colors[tile]
    rect = Rect((posX, posY), (TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(surface, tile_color, rect)
    pygame.draw.rect(surface, gray, rect.inflate(1, 1), 1)


def draw_play_area(screen_position, screen_surface, board_surface, rows_to_show=20.5):

    topY = board_surface.get_height() - rows_to_show*TILE_SIZE
    screen_surface.blit(board_surface, screen_position, Rect((0, topY),
                                                             (board_surface.get_width(), rows_to_show * TILE_SIZE)))


# Game Loop
while True:
   while game_state == PLAYING:
       clock.tick(FPS)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()


       screen.fill(gray)
       draw_board(board,board_surface)
       draw_play_area((50,50), screen, board_surface, 20.5)
       pygame.display.update()
