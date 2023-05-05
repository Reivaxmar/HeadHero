import pygame.sprite
import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.scale(self.image, (4*17, 4*19))
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move((-10, 0))
        if keys[pygame.K_d]:
            self.move((10, 0))
        if keys[pygame.K_s]:
            self.move((0, 10))
        if keys[pygame.K_w]:
            self.move((0, -10))

    def moveKey(self, key):
        if key == pygame.K_a:
            self.move((-10, 0))
        if key == pygame.K_d:
            self.move((10, 0))
        if key == pygame.K_s:
            self.move((0, 10))
        if key == pygame.K_w:
            self.move((0, -10))

    def move(self, pos):
        self.rect.x += pos[0]
        self.rect.y += pos[1]
