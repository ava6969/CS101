import pygame
from pygame.locals import *
from LucasTetris.util import *


class Board:
    def __init__(self, ROWS, COLS, TILE_SIZE):
        self.TILE_SIZE = TILE_SIZE
        self.ROWS = ROWS
        self.COLS = COLS
        self.board = []
        self.board_surface = pygame.Surface((COLS * TILE_SIZE, ROWS * TILE_SIZE))

        for r in range(ROWS):
            column_of_colors = []
            for c in range(COLS):
                column_of_colors.append(0)
            self.board.append(column_of_colors)

    def draw_board(self):
        for r in range(self.ROWS):
            for c in range(self.COLS):
                tile = self.board[r][c]
                x = c * self.TILE_SIZE
                y = r * self.TILE_SIZE
                self.draw_tile(x, y, tile)

    def draw_tile(self, posX, posY, tile):
        tile_color = colors[tile]
        rect = Rect((posX, posY), (self.TILE_SIZE, self.TILE_SIZE))
        pygame.draw.rect(self.board_surface, tile_color, rect)
        pygame.draw.rect(self.board_surface, gray, rect.inflate(1, 1), 1)

    def draw_play_area(self, start_position, screen_surface, rows_to_show=20.5):

        topY = self.board_surface.get_height() - rows_to_show*self.TILE_SIZE
        screen_surface.blit(self.board_surface, start_position,
                            Rect((0, topY), (self.board_surface.get_width(), rows_to_show*self.TILE_SIZE)))


# game loop
