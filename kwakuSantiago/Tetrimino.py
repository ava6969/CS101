import random

from kwakuSantiago.Grid import Grid
from kwakuSantiago.utlis import *


class Tetrimino:

    def __init__(self, grid_ref:Grid):
        self.type = 'I'
        self.rotation = 0
        self.position = (3, 18)
        self.grid = grid_ref

    def move(self, dx, dy):
        x, y = self.position
        dest = (x+dx, y+dy)
        if not self.collided(dest):
            self.position = dest
            return True
        return False

    def rotate(self, dr):
        new_rot = (self.rotation + dr) % len(pieces[self.type])
        prev_rot = self.rotation
        self.rotation = new_rot
        if not self.collided(self.position):
            return
        self.rotation = prev_rot

    def reset(self):
        self.type = random.choice(types)
        self.rotation = 0
        self.position = (3, 18)

    def collided(self, pos):
        topx, top_y = pos
        tet = pieces[self.type][self.rotation]
        h = len(tet)
        w = len(tet[0])

        for y in range(h):
            for x in range(w):
                if tet[y][x] != 0:
                    if topx + x < 0 or topx + x >= len(self.grid.grid[0]) or \
                            top_y + y >= len(self.grid.grid) or top_y + y < 0:
                        return True
                    # if  self.grid is not None and self.grid.grid[top_y+y][topx + x] != 0:
                    #     return True

        return False

    def get_current_tet(self):
        tet = pieces[self.type][self.rotation]
        rows = len(tet)
        cols = len(tet[0])
        return tet, (rows, cols)

    def draw_tetrimino(self):
        tet = pieces[self.type][self.rotation]
        rows = len(tet)
        cols = len(tet[0])
        x, y = self.position

        for row in range(rows):
            for col in range(cols):
                tile = tet[row][col]
                if tile != 0:
                    tile_x = (x + col) * self.grid.tile_size
                    tile_y = (y + row) * self.grid.tile_size
                    self.grid.draw_tile(tile_x, tile_y, tile)

    def lock(self):
        tetrimino, (rows, cols) = self.get_current_tet()

        for y in range(rows):
            for x in range(cols):
                tile = tetrimino[y][x]
                if tile != 0:
                    x_, y_ = self.position
                    self.grid.grid[y_+y][x_ + x] = tile
