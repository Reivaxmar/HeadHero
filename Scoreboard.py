import pygame.sprite
import pygame

import Hardcodes


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # Initcialitza les vides i la puntuació
        self.Lives = Hardcodes.startLives
        self.Score = 0

        # Importa la font i ho posa per sobre de tot
        self.font = pygame.font.Font("Singkong.ttf", 40)
        self.layer = 1

        self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
        self.image.fill(pygame.Color(0, 0, 0, 0))
        self.rect = self.image.get_rect()

    def update(self, dt):
        # Un programa molt llarg per juntar dues imatges
        image1 = self.font.render(f"Lives: {self.Lives}", True, (255, 0, 0))
        image2 = self.font.render(f"Score: {self.Score}", True, (0, 0, 255))
        height = image1.get_height() + image2.get_height()
        width = max(image1.get_width(), image2.get_width())
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill(pygame.Color(0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.image.blit(image1, (0, 0))
        self.image.blit(image2, (0, image1.get_height()))

    def addScore(self, t, num): # No serveix, però l'utilitzo :)
        if t == "Score":
            self.Score += num
        elif t == "Lives":
            self.Lives += num
