import random

from Pygame.Tetris.tetris_pieces import *

class Tetrimino:

    def __init__(self, grid):
        self.type = 'I'
        self.rotation = 0
        self.x, self.y = (3, 18)
        self.types = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
        self.grid_ref = grid.board

    def reset(self):
        self.type = random.choice(self.types)
        self.rotation = 0
        self.x, self.y = (3, 18)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self, dr):
        new_rotation = (self.rotation + dr) % len(pieces[self.type])
        self.rotation = new_rotation

    def draw_tetrimino(self, posX, posY, tetrimino):
        topX = posX
        topY = posY
        rows = len(tetrimino)
        cols = len(tetrimino[0])

        for row in range(rows):
            for col in range(cols):
                tile = tetrimino[row][col]
                if tile != 0:  # tile is not black
                    tileX = (topX + col) * self.grid_ref.tile_size
                    tileY = (topY + row) * self.grid_ref.tile_size
                    self.grid_ref.draw_tile( tileX, tileY, tile)