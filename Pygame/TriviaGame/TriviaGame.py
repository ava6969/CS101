import random
import time

import pygame, sys
from pygame.locals import *
from Trivia import Trivia


# Create Trivia object
trivia = Trivia('dewe', 'questions.txt', 10)

pygame.init()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 1200
HEIGHT = 600
FPS = 60
# Create Windows
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAYSURF.fill(GREEN)
pygame.display.set_caption("Trivia Game")

# create input box
input_box = pygame.Rect(WIDTH//2, HEIGHT//2, 140, 32)

# create fonts
font_large = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
font_italic_medium = pygame.font.SysFont("Verdana", 40, italic=True)
active = False
trivia.generate_question()

answer = ''
clock = pygame.time.Clock()
points = 0
while True:
    question_text = font_italic_medium.render(trivia.question, True, BLACK)
    point_text = font_large.render(str(points), True, WHITE)
    DISPLAYSURF.blit(question_text, (WIDTH//4, HEIGHT//3))
    DISPLAYSURF.blit(point_text, (WIDTH*3//4, HEIGHT//10))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(*event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    correct, point = trivia.validate_answer(answer)
                    points += point
                    trivia.generate_question()
                    input_box = pygame.Rect(WIDTH // 2, HEIGHT // 2, 140, 32)
                    print(correct)
                    answer = ''
                elif event.key == pygame.K_BACKSPACE:
                    answer = answer[:-1]
                else:
                    answer += event.unicode
        if points >= trivia.max_point:
            DISPLAYSURF.fill(BLACK)
            TEXT = font_large.render('YOU WON', True, WHITE)
            DISPLAYSURF.blit(TEXT, (WIDTH // 3, HEIGHT // 3))
            time.sleep(3)
            pygame.quit()
            sys.exit()

    # DISPLAYSURF.fill(GREEN)
    txt_surface = font_small.render(answer, True, WHITE)
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    DISPLAYSURF.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(DISPLAYSURF, WHITE, input_box, 5)
    pygame.display.flip()
    clock.tick(FPS)

    DISPLAYSURF.fill(GREEN)
    pygame.display.update()