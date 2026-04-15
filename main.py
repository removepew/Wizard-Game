import pygame
from Constants import *
from entities.PlayerController import PlayerController
from entities.Enemy import Enemy
from systems.CollisionManager import CollisionManager
from systems.RenderManager import RenderManager
from systems.ScoreManager import ScoreManager


"""
TODO: Create a room system (each room contains an enterance and exit)
TODO: Create an enemy and playercontroller file
TODO: Create a bounding box system
TODO: Create static and dynamic entities which allow for custom behavior
TODO: Add visual elements
TODO: Add health system and attack system
"""

MAX_ENEMIES = 20

START_HEALTH = 3

ENEMY_BOUNDS = ((0, HEIGHT - 200), (0, WIDTH))

def choose_location()

def spawn_enemy(sprite):

    enemy = Enemy(None, sprite, ())

    return enemy



# Initialize pygame library and display and clock object
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

game_timer = 0

# Create a person object

wizard = pygame.image.load('assets/wizard.png')
spider = pygame.image.load('assets/spider.png')

spider = pygame.transform.scale(spider, (100, 100))

p = PlayerController(pygame.transform.scale(wizard, (75, 100)), projectileSurf=pygame.Surface((2, 2)))

colMan = CollisionManager(WIDTH, HEIGHT)
renMan = RenderManager(WIDTH, HEIGHT, screen, WHITE)
scoreMan = ScoreManager()

font = pygame.font.Font(None, 36)

text_surface = font.render(f"Score: {scoreMan.score}, Health: {scoreMan.health}", True, (255, 255, 255))

held_stuff = [p, [spawn_enemy(spider)]]


RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.

    game_timer += 1

    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    for item in held_stuff:
        item.update()

    if game_timer % 2500 == 0:
        if scoreMan.score > 5:
            held_stuff.append(spawn_enemy(spider))
            held_stuff.append(spawn_enemy(spider))
        else:
            held_stuff.append(spawn_enemy(spider))
    

    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()

    clock.tick(300)     # Throttle the loop to 300 updates a second

