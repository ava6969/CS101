
types = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

pieces = {
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
class Tetrimino:
    def __init__(self, type):
        self.type = type
        self.rot = 0
        self.x, self.y = (3, 18)
        self.bottom_flag = False
        self.grid_ref = None

    def move(self, dx, dy):

        dest_x, dest_y = self.x + dx, self.y + dy
        if not self.check_collision(dest_x, dest_y):
            self.x = dest_x
            self.y = dest_y

    def rotate(self, dr):
        new_r = (self.rot + dr) % len(pieces[self.type])
        prev_r = self.rot
        self.rot = new_r
        if self.check_collision(self.x, self.y):
           self.rot = prev_r

    def check_collision(self, xPos, yPos):
        top_x, top_y = xPos, yPos
        tetrimino = pieces[self.type][self.rot]
        tet_h = len(tetrimino)
        tet_w = len(tetrimino[0])

        for y in range(tet_h):
            for x in range(tet_w):
                if tetrimino[y][x] != 0:
                    if top_x + x < 0 or top_x + x >= len(self.grid_ref[0]) or top_y + y >= len(self.grid_ref):
                        return True
        return False



