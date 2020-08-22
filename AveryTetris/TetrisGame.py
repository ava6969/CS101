# NEW: Import math library
import pygame, math
from pygame.locals import *
from AveryTetris.Tetrimino import *
from AveryTetris.Board import *

pygame.init()

# Colors
black = (0, 0, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
orange = (255, 100, 10)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
purple = (160, 32, 240)
gray = (190, 190, 190)
colors = [black, cyan, blue, orange, yellow, green, purple, red]

# Variables for window and tiles
clock = pygame.time.Clock()
BASE_FPS = FPS = 60
WIDTH = 640
HEIGHT = 480
TILE_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")


# NEW: Drop time function this is standard Tetris guidelines. reference: https://tetris.fandom.com/wiki/Tetris_Guideline
def calculate_drop_time(level):
    return math.floor(math.pow((0.8 - ((level - 1) * 0.007)), level - 1) * 60)


locking = False
hit_space = False
lock_clock = 0
lock_delay = 30

# NEW: Variables for player information
level = 1
score = 0
new_level = 5 * level
drop_clock = 0
currentDropTime = baseDropTime = calculate_drop_time(level)
print(baseDropTime)

# Variables for board
ROWS = 40
COLS = 10

grid = Board(ROWS, COLS, TILE_SIZE)

# Game States
RESTART = -1
PLAYING = 0
GAME_OVER = 1
game_state = PLAYING

# Create first tetrimino
active_tetrimino = Tetrimino(grid)
# active_tetrimino.reset()

# text
title_font = pygame.font.SysFont("Verdana", 40)
large_font = pygame.font.SysFont("Verdana", 60)

score_title = title_font.render("score", True, (0, 0, 0))
score_text = large_font.render(str(0), True, (0, 0, 0))
game_over = large_font.render("Game Over", True, (0, 0, 0))

# Game Loop
while True:
    while game_state == PLAYING:
        # score_text = large_font.render(str(grid.scores), True, (0, 0, 0))
        # screen.blit(score_text, (int(WIDTH*0.75), int(HEIGHT * 0.25)))

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # NEW: Controlling the tetrinomo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    active_tetrimino.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    currentDropTime = baseDropTime // 20
                elif event.key == pygame.K_LEFT:
                    active_tetrimino.move(-1, 0)
                elif event.key == pygame.K_UP or event.key == pygame.K_x:
                    active_tetrimino.rotate(1)
                elif event.key == pygame.K_z or event.key == pygame.K_RCTRL:
                    active_tetrimino.rotate(-1)
                elif event.key == pygame.K_SPACE:
                    hit_space = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    currentDropTime = baseDropTime

        if hit_space:
            FPS = 240
            move = active_tetrimino.move(0, 1)
            if not move:
                FPS = BASE_FPS
                hit_space = False

        # NEW: Drop clock which indicates how fast the pieces will fall down
        # Increase the drop clock each frame, once we pass current_drop_time, it's time to fall.
        drop_clock += 1
        if drop_clock >= currentDropTime and not hit_space:
            move = active_tetrimino.move(0, 1)
            if not move:
                if not locking:
                    locking = True
                    lock_clock = 0
                else:
                    locking = False
            drop_clock = 0

        if locking:
            lock_clock += 1
            if lock_clock >= lock_delay:
                active_tetrimino.lock()
                drop_clock = baseDropTime
                lock_clock = 0
                locking = False
                active_tetrimino.reset()
                grid.check_and_clear_lines()

        # DELETE: active_tetrimino.move(0,1)
        screen.fill(gray)
        grid.draw_board()

        # drawing to the board
        active_tetrimino.draw_tetrimino()
        active_tetrimino.draw_next_tetrimino(screen)
        grid.draw_play_area((10, 10), screen)

        # scores
        screen.blit(score_text, (640//2, 300))
        pygame.display.update()
