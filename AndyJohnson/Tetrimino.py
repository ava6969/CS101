import random
from tetris_pieces import *

class Tetrimino:

    def __init__(self, grid):

        self.grid_ref = grid
        self.reset()

    def reset(self):
        self.tile_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.type = random.choice(list(pieces.keys()))
        self.rotation = random.randint(0, len(pieces[self.type])-1)
        tetrimino = pieces[self.type][self.rotation]

        self.x, self.y = random.randint(0, self.grid_ref.cols - len(tetrimino[0])), 18

    def move(self, dx, dy):
        dest_x = self.x + dx
        dest_y = self.y + dy

        self.x = dest_x
        self.y = dest_y

    def draw_tetrimino(self):
        tetrimino = pieces[self.type][self.rotation]
        rows = len(tetrimino)
        cols = len(tetrimino[0])

        for row in range(rows):
            for col in range(cols):
                x = (self.x + col) * self.grid_ref.tile_size
                y = (self.y + row) * self.grid_ref.tile_size
                self.grid_ref.draw_tile((x, y), self.tile_color)