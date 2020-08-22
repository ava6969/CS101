
import random

import pygame
from pygame.locals import *
from AveryTetris.utils import *

class Tetrimino:

   def __init__(self, grid_ref):
       self.type = "I"
       self.next_type = random.choice(types)
       self.rotation = 0
       self.x, self.y = (3,18)
       self.tile_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
       # Set grid_ref manually - if left as none, blocks will fall and ignore the grid.
       self.grid_ref = grid_ref
       self.next_tet_surface = pygame.Surface((4 * self.grid_ref.TILE_SIZE, 4 * self.grid_ref.TILE_SIZE))

   def reset(self):
       self.tile_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
       self.type = self.next_type
       self.next_type = random.choice(types)
       self.rotation = 0 # possible tweak random
       self.x, self.y = (3, 18) # possible tweak random

 # NEW: redefine move function to check for collision
   def move(self, dx, dy):
       destination_x = self.x + dx
       destination_y = self.y + dy
       if not self.collision_check(destination_x, destination_y):
           self.x = destination_x
           self.y = destination_y
           return True
       return False

   def rotate(self, dr):
       new_rotation = (self.rotation + dr) % len(pieces[self.type])
       #NEW: Redefined rotation now that we have a collision check
       prev_rotation = self.rotation
       self.rotation = new_rotation
       if not self.collision_check(self.x,self.y):
            # rotate succeeded
            return
       #rotate failed
       self.rotation = prev_rotation


   # NEW: Define a collision check function
   def collision_check(self,xPos,yPos):
       top_x, top_y = xPos, yPos
       tetrimino = pieces[self.type][self.rotation]
       tetrimino_height = len(tetrimino)
       tetrimino_width = len(tetrimino[0])

       for y in range(tetrimino_height):
           for x in range(tetrimino_width):
               # No need to check blank spaces of the tetrimino for collision.
               if tetrimino[y][x] != 0:
                   # out of bounds (walls or floor)
                   if top_x + x < 0 or top_x + x >= len(self.grid_ref.board[0]) or top_y + y < 0 or top_y + y >= len(self.grid_ref.board):
                       return True
                   # Check vs grid
                   if self.grid_ref is not None and self.grid_ref.board[top_y + y][top_x + x] != 0:
                       return True
       # If you make it out of this loop without returning True, you're in the clear.
       return False

   def lock(self):
       tetrimino = pieces[self.type][self.rotation]
       h = len(tetrimino)
       w = len(tetrimino[0])

       for y in range(h):
           for x in range(w):
               tile = tetrimino[y][x]
               if tile != 0:
                   self.grid_ref.board[self.y + y][self.x + x] = tile

   def draw_tetrimino(self):
       tetrimino = pieces[self.type][self.rotation]
       rows = len(tetrimino)
       cols = len(tetrimino[0])

       for row in range(rows):
           for col in range(cols):
               tile = tetrimino[row][col]
               if tile != 0:  # tile is not black
                   tileX = (self.x + col) * self.grid_ref.TILE_SIZE
                   tileY = (self.y + row) * self.grid_ref.TILE_SIZE
                   self.grid_ref.draw_tile(tileX, tileY, self.tile_color)

   def draw_next_tetrimino(self, screen):

       tetrimino = pieces[self.next_type][0]
       rows = len(tetrimino)
       cols = len(tetrimino[0])
       startingPos = (480, 120)
       TS = self.grid_ref.TILE_SIZE
       for row in range(rows):
           for col in range(cols):
               tile = tetrimino[row][col]
               if tile != 0:  # tile is not black
                   tileX = startingPos[0] + (col * TS)
                   tileY = startingPos[1] + (row * TS)
                   rect = Rect((tileX, tileY), (TS, TS))
                   pygame.draw.rect(screen, black, rect)
                   pygame.draw.rect(screen, gray, rect.inflate(1, 1), 1)


