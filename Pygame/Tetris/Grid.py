
import pygame, sys
from pygame.locals import *

black = (0, 0, 0)
white = (255, 255, 255)
gray = (255 // 2, 255 // 2, 255 // 2)


class Grid:

    def __init__(self, n_rows, n_cols, tile_size, grid_color):

        self.n_rows= n_rows
        self.n_cols = n_cols
        self.grid_color = grid_color
        self.tile_size = tile_size
        self.board = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        self.board_surface = pygame.Surface((n_cols * tile_size, n_rows * tile_size))

    def draw_board(self):

        for row in range(self.n_rows):
            for col in range(self.n_cols):
                currentTile = self.board[row][col]
                tile_x = col * self.tile_size
                tile_y = row * self.tile_size
                self.draw_tile((tile_x, tile_y), currentTile)

    def draw_tile(self, position, tile):
        tile_color = gray
        rect = Rect(position, (self.tile_size, self.tile_size))
        pygame.draw.rect(self.board_surface, tile_color, rect)
        pygame.draw.rect(self.board_surface, black, rect.inflate(1, 1), 1)

    def draw_play_area(self, screen_position, screen_surface):
        self.draw_board()
        rows_toshow = 20
        topY = self.board_surface.get_height() - rows_toshow * self.tile_size
        screen_surface.blit(self.board_surface, screen_position,
                            Rect((0, topY), (self.board_surface.get_width(), rows_toshow * self.tile_size)))
