import pygame.sprite
import pygame
import random

import Hardcodes


class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        # Import the alien image
        self.image = pygame.image.load("alien.png")
        self.image = pygame.transform.scale(self.image, (2 * 24, 2 * 18))
        self.rect = self.image.get_rect()
        # And set its position to the ceiling with a random x position
        self.rect.x = random.randint(0, Hardcodes.windowSize[0]-3 * 24)
        self.rect.y = -4 * 18

    def update(self, dt):
        self.move((0, Hardcodes.alienSpeed), dt)
        if self.rect.y > 1700:
            self.kill()

    def move(self, pos, dt):
        self.rect.x += pos[0] * dt
        self.rect.y += pos[1] * dt
