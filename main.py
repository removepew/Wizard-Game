from libs.Constants import *
from libs.PlayerController import PlayerController

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
p = PlayerController()
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
            for projectile in p.projectiles:
                print(projectile)
                print(projectile.getPosition())

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    for projectile in p.projectiles:
        if not projectile.active:
            p.projectiles.remove(projectile)
        projectile.update()
        screen.blit(projectile.surf, projectile.rect)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()

    clock.tick(200)     # Throttle the loop to 200 updates a second

