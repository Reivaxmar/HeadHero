import pygame.sprite
import pygame

import Hardcodes

class ScrollBG(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ScrollBackground.png")
        self.image = pygame.transform.scale(self.image, (Hardcodes.windowSize[0], 2*Hardcodes.windowSize[0]))
        self.rect = self.image.get_rect()
        self.rect.y = -Hardcodes.windowSize[0]

    def update(self, dt):
        self.rect.y += Hardcodes.bgscrollspeed * dt
        if self.rect.y >= 0:
            self.rect.y = -Hardcodes.windowSize[0]
