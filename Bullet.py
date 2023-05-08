import pygame.sprite
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (4 * 4, 4 * 9))
        self.rect = self.image.get_rect()
        self.rect.x = ship.rect.x + ship.rect.width / 2 - self.rect.width / 2
        self.rect.y = ship.rect.y + ship.rect.height / 2 - self.rect.height / 2

    def update(self):
        self.move((0, -20))
        if self.rect.y < -100:
            self.kill()

    def move(self, pos):
        self.rect.x += pos[0]
        self.rect.y += pos[1]
