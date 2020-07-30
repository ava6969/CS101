import random

black = (0, 0, 0)
white = (255, 255, 255)
gray = (255//2, 255//2, 255//2)
cyan = (0,255,255)
blue = (0,0,255)
orange = (255,100,10)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
purple = (160,32,240)
colors = [gray, cyan, blue, orange, yellow, green, purple, red]

# Piece shapes
types = ["I", "J", "L", "O", "S", "T", "Z"]

pieces = {
   # IMPORTANT NOTE 3: Have the student only do one of these and give them the rest!
   # see IMPORTANT NOTE 2 for a debug / check code to make sure their pieces work
   "I": [
       [[0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],
       [[0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0]],
       [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]],
       [[0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
        ]
   ],
   "J": [
       [[2, 0, 0],
        [2, 2, 2],
        [0, 0, 0]],
       [[0, 2, 2],
        [0, 2, 0],
        [0, 2, 0]],
       [[0, 0, 0],
        [2, 2, 2],
        [0, 0, 2]],
       [[0, 2, 0],
        [0, 2, 0],
        [2, 2, 0]]
   ],
    "L": [
        [[0, 0, 3],
         [3, 3, 3],
         [0, 0, 0]],
        [[0, 3, 0],
         [0, 3, 0],
         [0, 3, 3]],
        [[0, 0, 0],
         [3, 3, 3],
         [3, 0, 0]],
        [[3, 3, 0],
         [0, 3, 0],
         [0, 3, 0]]
    ],
    "O": [
        [[0, 4, 4, 0],
         [0, 4, 4, 0],
         [0, 0, 0, 0]]
    ],
    "S": [
        [[0, 5, 5],
         [5, 5, 0],
         [0, 0, 0]],
        [[0, 5, 0],
         [0, 5, 5],
         [0, 0, 5]],
        [[0, 0, 0],
         [0, 5, 5],
         [5, 5, 0]],
        [[5, 0, 0],
         [5, 5, 0],
         [0, 5, 0]]
    ],
    "T": [
        [[0, 6, 0],
 [6, 6, 6],
        [0, 0, 0]],
       [[0, 6, 0],
        [0, 6, 6],
        [0, 6, 0]],
       [[0, 0, 0],
        [6, 6, 6],
        [0, 6, 0]],
       [[0, 6, 0],
        [6, 6, 0],
        [0, 6, 0]]
   ],
   "Z": [
       [[7, 7, 0],
        [0, 7, 7],
        [0, 0, 0]],
       [[0, 0, 7],
        [0, 7, 7],
        [0, 7, 0]],
       [[0, 0, 0],
        [7, 7, 0],
        [0, 7, 7]],
       [[0, 7, 0],
        [7, 7, 0],
        [7, 0, 0]]
   ]
}

# IMPORTANT NOTE 4 : Do this after you know the student can draw a tetrimino onto the board with no issues
# NEW: Tetrimino class

class Tetrimino:

   def __init__(self):
       self.type = "I"
       self.rotation = 0
       self.x, self.y = (3,18)

       # Set grid_ref manually - if left as none, blocks will fall and ignore the grid.
       self.grid_ref = None

   def reset(self):
       self.type = random.choice(types)
       self.rotation = 0
       self.x, self.y = (3,18)

   def move(self, dx, dy):
       self.x += dx
       self.y += dy

   def rotate(self, dr):
       new_rotation = (self.rotation + dr) % len(pieces[self.type])
       self.rotation = new_rotation
