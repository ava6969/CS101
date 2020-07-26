#Imports
import pygame, sys
from pygame.locals import *
import random, time
from Pygame.CarGame.Player import Player
from Pygame.CarGame.Enemy import Enemy

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

class CarGame:
    def __init__(self):
        # Initialzing
        pygame.init()



        self.SPEED = 5
        self.SCORE = 0
        # Setting up Sprites
        self.P1 = Player(SCREEN_WIDTH)
        self.E1 = Enemy(SCREEN_WIDTH, self.SPEED)

        # Creating Sprites Groups
        self.enemies = pygame.sprite.Group()
        self.enemies.add(self.E1)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.P1)
        self.all_sprites.add(self.E1)

        # Adding a new User event
        self.INC_SPEED = pygame.USEREVENT + 1
        pygame.time.set_timer(self.INC_SPEED, 1000)

        # Setting up Fonts
        font = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 20)
        font_medium = pygame.font.SysFont("Verdana", 40, bold=True, italic=True)
        self.game_over = font.render("Game Over", True, BLACK)

        self.background = pygame.image.load("AnimatedStreet.png")

        # Create a white screen
        self.DISPLAYSURF = pygame.display.set_mode((400, 600))
        self.DISPLAYSURF.fill(WHITE)
        pygame.display.set_caption("Game")

    def run(self):
        # Game Loop
        while True:
            # Cycles through all events occuring
            events = pygame.event.get()
            for event in events:
                if event.type == self.INC_SPEED:
                    self.SPEED += 0.5
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.DISPLAYSURF.blit(self.background, (0, 0))
            scores = self.font_small.render(str(self.SCORE), True, BLACK)
            self.DISPLAYSURF.blit(scores, (10, 10))

            # Moves and Re-draws all Sprites
            for entity in self.all_sprites:
                self.DISPLAYSURF.blit(entity.image, entity.rect)
                if entity.type == 'E':
                    self.SCORE = entity.move(self.SCORE)
                else:
                    entity.move()

            # To be run if collision occurs between Player and Enemy
            if pygame.sprite.spritecollideany(self.P1, self.enemies):
                pygame.mixer.Sound('crash.wav').play()
                time.sleep(1)

                self.DISPLAYSURF.fill(RED)
                self.DISPLAYSURF.blit(self.game_over, (30, 250))

                pygame.display.update()
                for entity in self.all_sprites:
                    entity.kill()
                time.sleep(2)
                pygame.quit()
                sys.exit()

            pygame.display.update()
            FramePerSec.tick(FPS)


def main():
    game = CarGame()
    game.run()




main()

