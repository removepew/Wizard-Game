import pygame
from Constants import *
from entities.PlayerController import PlayerController
from entities.Enemy import Enemy

"""
TODO: Create a room system (each room contains an enterance and exit)
TODO: Create an enemy and playercontroller file
TODO: Create a bounding box system
TODO: Create static and dynamic entities which allow for custom behavior
TODO: Add visual elements
TODO: Add health system and attack system
"""


# Initialize pygame library and display and clock object
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create a person object

wizard = pygame.image.load('assets/wizard.png')

p = PlayerController(WHITE, pygame.transform.scale(wizard, (100, 100)), projectileSurf=pygame.Surface((2, 2)))
RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
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


    # fill the screen with a color
    screen.fill(RED)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()

    clock.tick(200)     # Throttle the loop to 200 updates a second

