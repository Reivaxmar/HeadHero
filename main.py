import pygame
import pygame.sprite
from Ship import Ship
from Bullet import Bullet
from Alien import Alien
from Scoreboard import Scoreboard
import time
import pygame.mixer


pygame.init()
screen = pygame.display.set_mode((1600, 900))

clock = pygame.time.Clock()

pygame.mixer.music.load("ElectromanAdventures.mp3")
pygame.mixer.music.play(-1)

spritesGroup = pygame.sprite.Group()

Player = Ship()
# noinspection PyTypeChecker
spritesGroup.add(Player)

sb = Scoreboard()
spritesGroup.add(sb)

spawnRate = 1
waitTime = 1
start_time = time.time()
start_fire = time.time()
backgroundImg = pygame.image.load("background.jpg")
backgroundImg = pygame.transform.scale(backgroundImg, (1950, 1300))

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and time.time() - start_fire > 0.5:
                start_fire = time.time()
                spritesGroup.add(Bullet(Player))
                bulletSound = pygame.mixer.Sound("laserShoot.wav")
                bulletSound.play()
            if event.key == pygame.K_c:
                spritesGroup.add(Alien())

    # screen.fill((255, 255, 255))
    screen.blit(backgroundImg, (-200, 0))

    if time.time() - start_time > waitTime:
        spawnRate -= 0.001
        waitTime += spawnRate
        spritesGroup.add(Alien())

    spritesGroup.update()

    for spr in spritesGroup.sprites():
        if isinstance(spr, Bullet):
            for al in spritesGroup.sprites():
                if isinstance(al, Alien):
                    if pygame.sprite.collide_rect(spr, al):
                        sb.addScore("Score", 1)
                        spr.kill()
                        al.kill()
                        alienDie = pygame.mixer.Sound("explosion.wav")
                        alienDie.play()
        if isinstance(spr, Alien):
            if pygame.sprite.collide_rect(spr, Player):
                sb.addScore("Lives", -1)
                spr.kill()

    if sb.Lives == 0:
        Running = False

    spritesGroup.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
