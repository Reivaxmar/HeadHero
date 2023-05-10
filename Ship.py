import pygame.sprite
import pygame
import Hardcodes


def clamp(n, min, max): # Per a que el jugador no es surti de la pantalla.
    if n < min:
        return min
    elif n > max:
        return max
    else:
        return n

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        # Importa l'imatge de la nau i la fa gran
        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.scale(self.image, (3*17, 3*19))
        self.rect = self.image.get_rect()
        # Centra la nau
        self.move((Hardcodes.windowSize[0] / 2 - self.rect.width / 2, Hardcodes.windowSize[1] - self.rect.height / 2), 1)

    def update(self, dt):
        # Mou la nau
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move((-Hardcodes.shipSpeed, 0), dt)
        if keys[pygame.K_d]:
            self.move((Hardcodes.shipSpeed, 0), dt)
        if keys[pygame.K_s]:
            self.move((0, Hardcodes.shipSpeed), dt)
        if keys[pygame.K_w]:
            self.move((0, -Hardcodes.shipSpeed), dt)

        # I fa que no es surti
        self.rect.x = clamp(self.rect.x, 0, Hardcodes.windowSize[0] - self.rect.width)
        self.rect.y = clamp(self.rect.y, 0, Hardcodes.windowSize[1] - self.rect.height)

    def move(self, pos, dt):
        self.rect.x += pos[0] * dt
        self.rect.y += pos[1] * dt

