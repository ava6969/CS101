import pygame, sys
from pygame.locals import *

BLACK = (0,0,0)
CYAN = (0,255,255)
BLUE = (0,0,255)
ORANGE = (255,100,10)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
PURPLE = (160,32,240)
GRAY = (190, 190, 190)
colors = [BLACK, CYAN, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED]

ROWS = 40
COLS = 10

def draw_board(board, TILE_SIZE, board_surface):
    for row in range(ROWS):
        for col in range(COLS):
            tile = board[row][col]
            tile_x = col * TILE_SIZE
            tile_y = row * TILE_SIZE
            draw_tile((tile_x, tile_y), TILE_SIZE, tile, board_surface)


def draw_tile(pos, TILE_SIZE, tile, surface):
    tile_color = colors[tile]
    rect = Rect(pos, (TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(surface, tile_color, rect)
    pygame.draw.rect(surface, GRAY, rect.inflate(1, 1), 1)

def main():
    TILE_SIZE = 20
    pygame.init()
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    board_surface = pygame.Surface((COLS * TILE_SIZE, ROWS * TILE_SIZE))
    # colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # windows vars
    clock = pygame.time.Clock()
    FPS = 60
    WIDTH = 640
    HEIGHT = 480
    TILE_SIZE = 20

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(BLACK)
        pygame.draw.rect(window, WHITE, (WIDTH/4, HEIGHT/2, TILE_SIZE, TILE_SIZE))
        pygame.display.update()


main()