import pygame.sprite
import pygame
import Hardcodes


def clamp(n, m, M):  # For the player to not get outside the window
    if n < m:
        return m
    elif n > M:
        return M
    else:
        return n


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        # Import the ship image
        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.scale(self.image, (3*17, 3*19))
        self.rect = self.image.get_rect()
        # And center it
        self.rect.move_ip((Hardcodes.windowSize[0] / 2 - self.rect.width / 2, Hardcodes.windowSize[1] - self.rect.height / 2))

        # Setup the speed variables
        self.sx = 0
        self.sy = 0

    def update(self, dt):
        # Move the ship
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.move((-Hardcodes.shipSpeed, 0))
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.move((Hardcodes.shipSpeed, 0))
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move((0, Hardcodes.shipSpeed))
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move((0, -Hardcodes.shipSpeed))

        self.updatePos(dt)
        # And make it so that it doesn't get outside the screen
        self.rect.x = clamp(self.rect.x, 0, Hardcodes.windowSize[0] - self.rect.width)
        self.rect.y = clamp(self.rect.y, 0, Hardcodes.windowSize[1] - self.rect.height)

    def updatePos(self, dt):
        self.rect.x += self.sx * dt
        self.rect.y += self.sy * dt

        self.sx *= 0.8
        self.sy *= 0.8

        self.rect.x = clamp(self.rect.x, 0, Hardcodes.windowSize[0] - self.rect.width)
        self.rect.y = clamp(self.rect.y, 0, Hardcodes.windowSize[1] - self.rect.height)

    def move(self, pos):
        self.sx += pos[0]
        self.sy += pos[1]

