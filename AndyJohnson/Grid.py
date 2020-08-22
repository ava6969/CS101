import pygame
from pygame.locals import *

class Grid:

    def __init__(self, ROWS, COLS, TILESIZE):

        self.rows = ROWS
        self.cols = COLS
        self.board = [[0] * COLS] * ROWS
        self.tile_size = TILESIZE
        self.tile_tuple = (TILESIZE, TILESIZE)
        self.board_surface = pygame.Surface((COLS * TILESIZE, ROWS * TILESIZE))

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col*self.tile_size
                y = row*self.tile_size
                self.draw_tile((x, y), (0, 0, 0))

    def draw_tile(self, pos, tile_color, bkgColor=(255//2, 255//2, 255//2)):
        rect = Rect(pos, self.tile_tuple)
        pygame.draw.rect(self.board_surface, tile_color, rect)
        pygame.draw.rect(self.board_surface, bkgColor, rect.inflate(1, 1), 1)

    def draw_play_area(self, screen_pos, screen_surface):
        rows_to_show = 20.5
        topY = self.board_surface.get_height() - rows_to_show*self.tile_size
        screen_surface.blit(self.board_surface, screen_pos, Rect((0, topY),
                                                             (self.board_surface.get_width(),
                                                              rows_to_show*self.tile_size)))


