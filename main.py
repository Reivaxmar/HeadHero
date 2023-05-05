import pygame
import pygame.sprite
from pygame import mixer
from Ship import Ship

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1600, 900))

spritesGroup = pygame.sprite.Group()

Player = Ship()
# noinspection PyTypeChecker
spritesGroup.add(Player)

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spritesGroup.add(Ship())

    screen.fill((255, 255, 255))

    spritesGroup.update()
    spritesGroup.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
