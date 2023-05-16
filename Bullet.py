import pygame.sprite
import pygame

import Hardcodes


class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (3 * 4, 3 * 9))
        self.rect = self.image.get_rect()
        # Center it in the shooting part of the ship
        self.rect.x = ship.rect.x + ship.rect.width / 2 - self.rect.width / 2
        self.rect.y = ship.rect.y + ship.rect.height / 2 - self.rect.height / 2

    def update(self, dt):
        # Move it
        self.move((0, -Hardcodes.bulletSpeed), dt)
        # And delete it id it gets out of the screen
        if self.rect.y < -100:
            self.kill()

    def move(self, pos, dt):
        self.rect.x += pos[0] * dt
        self.rect.y += pos[1] * dt
