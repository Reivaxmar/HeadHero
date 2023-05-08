import pygame.sprite
import pygame
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
        self.image = pygame.transform.scale(self.image, (4*17, 4*19))
        self.rect = self.image.get_rect()
        # Centra la nau
        self.move((1600 / 2 - self.rect.width / 2, 900 - self.rect.height / 2))

    def update(self):
        # Mou la nau
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move((-10, 0))
        if keys[pygame.K_d]:
            self.move((10, 0))
        if keys[pygame.K_s]:
            self.move((0, 10))
        if keys[pygame.K_w]:
            self.move((0, -10))

        # I fa que no es surti
        self.rect.x = clamp(self.rect.x, 0, 1600 - self.rect.width)
        self.rect.y = clamp(self.rect.y, 0, 900 - self.rect.height)



    def move(self, pos):
        self.rect.x += pos[0]
        self.rect.y += pos[1]

