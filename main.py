import Hardcodes
from Ship import Ship
from Bullet import Bullet
from Alien import Alien
from Scoreboard import Scoreboard
import time
import pygame.mixer

# Inicialitza Pygame i la pantalla
pygame.init()
screen = pygame.display.set_mode(Hardcodes.windowSize)
# Inicialitza el rellotge per fer el framerate constant (60 fps)
clock = pygame.time.Clock()

# Posa en bucle la musica de fons
pygame.mixer.music.load("ElectromanAdventures.mp3")
pygame.mixer.music.play(-1)

# Crea el grup de Sprites
spritesGroup = pygame.sprite.Group()

# Crea el jugador
Player = Ship()
spritesGroup.add(Player)

# Crea el Scoreboard
sb = Scoreboard()
spritesGroup.add(sb)

# Spawnrate -> Disminueix en 0.001 cada vegada que un alien apareix, per així fer que els aliens apareguin cada
# vegada més ràpid
spawnRate = 1
waitTime = 1
# Timers per saber quan pot apareixer un alien i quan pots disparar
start_time = time.time()
start_fire = time.time()
# La imatge de fons escalada per a que es vegi millor
backgroundImg = pygame.image.load("background.jpg")
backgroundImg = pygame.transform.scale(backgroundImg, (1950, 1300))
dt = 0

# Bucle principal
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            # Si has disparat i es pot disparar
            if event.key == pygame.K_SPACE and time.time() - start_fire > Hardcodes.fireDelay:
                # Resetea el timer
                start_fire = time.time()
                # Crea la bala
                spritesGroup.add(Bullet(Player))
                # I fa un so
                bulletSound = pygame.mixer.Sound("laserShoot.wav")
                bulletSound.play()

    # Dibuixa el fons
    screen.blit(backgroundImg, (-200, 0))

    # Crea els aliens
    if time.time() - start_time > waitTime:
        spawnRate -= 0.001
        waitTime += spawnRate
        spritesGroup.add(Alien())

    spritesGroup.update(dt)

    # Colisions
    for spr in spritesGroup.sprites():
        if isinstance(spr, Bullet):
            for al in spritesGroup.sprites():
                if isinstance(al, Alien):
                    # Colisió alien <-> bala
                    if pygame.sprite.collide_rect(spr, al):
                        # Afegeix 1 a Score
                        sb.addScore("Score", 1)
                        # Elimina la bala i l'alien
                        spr.kill()
                        al.kill()
                        # I fa un so
                        alienDie = pygame.mixer.Sound("explosion.wav")
                        alienDie.play()
        if isinstance(spr, Alien):
            # Colisió alien <-> jugador
            if pygame.sprite.collide_rect(spr, Player):
                # Quita una vida i elimina l'alien
                sb.addScore("Lives", -1)
                spr.kill()

    # Para el programa si et quedes sense vides
    if sb.Lives == 0:
        Running = False

    spritesGroup.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000.0 * 60
    dt = round(dt * 10) / 10
    print(dt)

pygame.quit()
