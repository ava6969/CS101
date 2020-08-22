import pygame
from pygame.locals import *
from kwakuSantiago.utlis import *

class Grid:

    def __init__(self, n_rows, n_cols, tilesz):
        self.grid = [[0] * n_cols] * n_rows
        self.grid_surface = pygame.Surface((n_cols * tilesz, n_rows * tilesz))
        self.tile_size = tilesz
        self.n_rows = n_rows
        self.n_cols = n_cols

    def draw_tile(self, x, y, tile):
        color = colors[tile]
        rectangle = Rect((x, y), (self.tile_size, self.tile_size))
        pygame.draw.rect(self.grid_surface, color, rectangle)
        pygame.draw.rect(self.grid_surface, gray, rectangle.inflate(1, 1), 1)

    # game loop
    def draw_board(self):
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                currentTile = self.grid[row][col]
                if currentTile == 0:
                    tile_x = col * self.tile_size
                    tile_y = row * self.tile_size
                    self.draw_tile(tile_x, tile_y, 0)

    def draw_play_area(self, screen_position, screen_surface):
        rows_to_show = 20.5
        topY = self.grid_surface.get_height() - rows_to_show * self.tile_size
        screen_surface.blit(self.grid_surface, screen_position,
                            Rect((0, topY), (self.grid_surface.get_width(), rows_to_show * self.tile_size)))

