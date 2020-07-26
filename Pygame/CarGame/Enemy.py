import pygame
import random
from pygame.locals import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, speed):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.screen_width = screen_width
        self.speed = speed
        self.rect = self.surf.get_rect(center=(random.randint(40, screen_width - 40), 0))
        self.type = 'E'

    def move(self, score):
        self.rect.move_ip(0, self.speed)
        if (self.rect.bottom > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, self.screen_width - 40), 0)

        return score