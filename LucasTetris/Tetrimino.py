import random

from LucasTetris.util import pieces
from LucasTetris.util import *

class Tetrimino:

    def __init__(self, grid_ref):
        self.type = 'J'
        self.rotation = 0
        self.x = 3
        self.y = 18

        self.grid_ref = grid_ref

    def reset(self):
        self.type = random.choice(types)
        self.rotation = random.randint(0, len(pieces[self.type])-1)
        self.x, self.y = (3, 18)

    def move(self, dx, dy):
        dest_x = self.x + dx
        dest_y = self.y + dy
        if not self.collision_check(dest_x, dest_y):
            self.x = dest_x
            self.y = dest_y
            return True
        return False

    def draw_tetrimino(self):
        tetrimino = pieces[self.type][self.rotation]
        rows = len(tetrimino)
        cols =len(tetrimino[0])

        for row in range(rows):
            for col in range(cols):
                tile = tetrimino[row][col]
                if tile != 0:
                    tileX = (self.x + col) * self.grid_ref.TILE_SIZE
                    tileY = (self.y + row) * self.grid_ref.TILE_SIZE
                    self.grid_ref.draw_tile(tileX, tileY, tile)

    def collision_check(self, xPos, yPos):
        tetrimino = pieces[self.type][self.rotation]
        h = len(tetrimino)
        w = len(tetrimino[0])

        for row in range(h):
            for col in range(w):

                if tetrimino[row][col] != 0:
                    if xPos + col < 0 or xPos + col >= len(self.grid_ref.board[0]) or yPos + row >= len(self.grid_ref.board):
                        return True

                    if self.grid_ref.board[yPos+ row][xPos + col] != 0:
                        return True
        return False

    def lock(self):
        tetrimino = pieces[self.type][self.rotation]
        rows = len(tetrimino)
        cols = len(tetrimino[0])

        for row in range(rows):
            for col in range(cols):
                tile = tetrimino[row][col]
                if tile != 0:
                    self.grid_ref.board[self.y + row][self.x + col] = tile