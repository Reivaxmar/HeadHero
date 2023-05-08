import pygame.sprite
import pygame
import random


class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("alien.png")
        self.image = pygame.transform.scale(self.image, (3 * 24, 3 * 18))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1600-3 * 24)
        self.rect.y = -4 * 18

    def update(self):
        self.move((0, 5))
        if self.rect.y > 1700:
            self.kill()

    def move(self, pos):
        self.rect.x += pos[0]
        self.rect.y += pos[1]
