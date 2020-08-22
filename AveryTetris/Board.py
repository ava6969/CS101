import pygame
from pygame.locals import *
from AveryTetris.utils import *


class Tile:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = color


class Board:

    def __init__(self, ROWS, COLS, TILE_SIZE):
        self.ROWS = ROWS
        self.COLS = COLS
        self.TILE_SIZE = TILE_SIZE
        self.scores = 0
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.board_surface = pygame.Surface((COLS * TILE_SIZE, ROWS * TILE_SIZE))

    def draw_board(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                currentTile = self.board[row][col]
                if currentTile == 0:
                    tile_x = col * self.TILE_SIZE
                    tile_y = row * self.TILE_SIZE
                    self.draw_tile(tile_x, tile_y, (0, 0, 0))

    def draw_tile(self, posX, posY, tile_color):
        rect = Rect((posX, posY), (self.TILE_SIZE, self.TILE_SIZE))
        pygame.draw.rect(self.board_surface, tile_color, rect)
        pygame.draw.rect(self.board_surface, gray, rect.inflate(1, 1), 1)

    def draw_play_area(self, screen_position, screen_surface):
        rows_toShow = 20.5
        topY = self.board_surface.get_height() - rows_toShow * self.TILE_SIZE
        screen_surface.blit(self.board_surface, screen_position,
                            Rect((0, topY), (self.board_surface.get_width(), rows_toShow * self.TILE_SIZE)))

    def check_and_clear_lines(self):
        lines_cleared = 0
        full_lines = []

        for y, line in enumerate(self.board):
            if 0 not in line:
                lines_cleared += 1
                full_lines.append(y)

        if lines_cleared > 0:
            for y in full_lines:
                self.board.pop(y)
                self.scores += 1
                print('new score == ', self.scores)
                self.board.insert(0, [0 for _ in range(self.COLS)])
