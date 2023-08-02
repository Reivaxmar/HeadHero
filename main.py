import Hardcodes
from Ship import Ship
from Bullet import Bullet
from Alien import Alien
from Scoreboard import Scoreboard
from ScrollBG import ScrollBG
from FaceDetector import FaceInterface
import time
import pygame.mixer

# Initialize Pygame and the screen
pygame.init()
screen = pygame.display.set_mode(Hardcodes.windowSize)
pygame.display.set_caption("Head Hero")
# Init the clock for constant fps
clock = pygame.time.Clock()

# Create the Face Interface object and wait for it to start
mFI = FaceInterface()
while not mFI.hasStarted:
    pass

# Import and start the background music
pygame.mixer.music.load("ElectromanAdventures.mp3")
pygame.mixer.music.play(-1)

# Create the sprite group
spritesGroup = pygame.sprite.Group()

# Create the player object
Player = Ship()
spritesGroup.add(Player)

# Create the scoreboard object
sb = Scoreboard()
spritesGroup.add(sb)


# spawnrate -> it decreases in 0.001 every time an enemy spawns, so that they spawn faster
spawnRate = 1
waitTime = 1
# Timers to know when an enemy spawns and when you can fire a bullet
start_time = time.time()
start_fire = time.time()
# Import the background image and make it smaller so that it looks better
bg = ScrollBG()

dt = 0

# Main loop
Running = True
while Running:
    # Calculate delta time
    dt = clock.tick(60) / 1000.0 * 60
    dt = round(dt * 100) / 100

    # If quitting or pressing escape
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Running = False

    # Draw the background
    screen.blit(bg.image, bg.rect)
    bg.update(dt)

    # Update the camera window
    mFI.getImage()

    # If you shoot and you can shoot
    if (pygame.key.get_pressed()[pygame.K_SPACE] or mFI.info[1]) and time.time() - start_fire > Hardcodes.fireDelay:
        # Reset the shoot timer
        start_fire = time.time()
        # Create a bullet
        spritesGroup.add(Bullet(Player))
        # And make a sound
        bulletSound = pygame.mixer.Sound("laserShoot.wav")
        bulletSound.play()

    # Create the enemies
    if time.time() - start_time > waitTime:
        spawnRate -= 0.005
        waitTime += spawnRate
        spritesGroup.add(Alien())

    # Update the face info in the player object
    Player.updateFaceInfo(mFI.info)
    # And update the objects
    spritesGroup.update(dt)

    # Collisions
    for spr in spritesGroup.sprites():
        if isinstance(spr, Bullet):
            for al in spritesGroup.sprites():
                if isinstance(al, Alien):
                    # enemy <-> bullet
                    if pygame.sprite.collide_rect(spr, al):
                        # Add 1 to "Score"
                        sb.addScore("Score", 1)
                        # Delete the bullet and the enemy
                        spr.kill()
                        al.kill()
                        # And make a sound
                        alienDie = pygame.mixer.Sound("explosion.wav")
                        alienDie.play()
        if isinstance(spr, Alien):
            # enemy <-> player
            if pygame.sprite.collide_rect(spr, Player):
                # Remove 1 from "Lives" and delete the enemy
                sb.addScore("Lives", -1)
                spr.kill()
                # And make a sound
                alienDie = pygame.mixer.Sound("explosion.wav")
                alienDie.play()

    # Stop the program if you get out of lives
    if sb.Lives == 0:
        Running = False
        pygame.mixer.music.stop()
        gameOver = pygame.mixer.Sound("game-over.wav")
        gameOver.play()
        st = time.time()
        et = 0
        while et < 2:
            et = time.time() - st
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False
            pygame.display.flip()
        break

    spritesGroup.draw(screen)

    pygame.display.flip()

mFI.closeCam()
pygame.quit()
