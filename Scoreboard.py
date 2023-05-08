import pygame.sprite
import pygame


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # Initcialitza les vides i la puntuació
        self.Lives = 3
        self.Score = 0

        # Importa la font i ho posa per sobre de tot
        self.font = pygame.font.Font("Singkong.ttf", 60)
        self.layer = 1

    def update(self):
        # Un programa molt llarg per juntar dues imatges
        self.image1 = self.font.render(f"Lives: {self.Lives}", True, (255, 0, 0))
        self.image2 = self.font.render(f"Score: {self.Score}", True, (0, 0, 255))
        height = self.image1.get_height() + self.image2.get_height()
        width = max(self.image1.get_width(), self.image2.get_width())
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill(pygame.Color(0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.image.blit(self.image1, (0, 0))
        self.image.blit(self.image2, (0, self.image1.get_height()))

    def addScore(self, type, num): # No serveix, però l'utilitzo :)
        if type == "Score":
            self.Score += num
        elif type == "Lives":
            self.Lives += num
