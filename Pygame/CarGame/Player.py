import pygame

from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center=(160, 520))
        self.screen_width = screen_width
        self.type = 'P'

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        # self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < self.screen_width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)