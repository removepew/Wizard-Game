#####################################################################
# author: Alex Martinez
# date: 3/13/2026
# description: game project
#####################################################################
import pygame
from random import randint, choice
from Item import *
from Constants import *


class Person(pygame.sprite.Sprite, Item):
    
    def __init__(self, color:list[int] = RED, surf:pygame.Surface = pygame.Surface((1, 1))):

        # Initialize parent classes

        pygame.sprite.Sprite.__init__(self)
        Item.__init__(self)

        # Store the surface object for later editing

        self.surf = surf

        # Set preset values

        self.color = color
        self.surf.fill(color)
        self.rect = self.surf.get_rect()

    # Custom Methods

    def setColor(self) -> None:
        """
        Randomly selects the value to be stored in the color 
        instance variable, and then changes the color of the 
        surf to match that color
        """
        chosenColor = choice(COLORS)

        self.color = chosenColor

        self.surf.fill(chosenColor)

        return # Signify we are done

    def setSize(self) -> None:
        """
        Changes the size of the Person/Item to a random value 
        between 10 and 100, and then changes the size of the 
        surf to match that size
        """

        # Generate a new, random size

        newSize = randint(10, 100)

        # Set the stored values to the new value

        self.size = newSize

        # Change the surface object to match new values and store it

        self.surf = pygame.transform.scale(self.surf, (newSize, newSize))

        self.rect = self.surf.get_rect()
        

        return # Signify we are done
    
    def update(self, keyLogs) -> None:
        """
        Receives as an argument a dictionary containing all the 
        key pressed events and then updates the state of the 
        object based on what was pressed
        """

        # Process directional presses

        if keyLogs[K_UP]:
            self.goUp()
        if keyLogs[K_DOWN]:
            self.goDown()
        if keyLogs[K_LEFT]:
            self.goLeft()
        if keyLogs[K_RIGHT]:
            self.goRight()

        # Process randomized press

        if keyLogs[K_SPACE]:
            self.setColor()
            self.setSize()

        # Keep player within bounds
        if self.x < 0:
            self.x = 0
        if self.x >= WIDTH:
            self.x = WIDTH
        if self.y <= 0:
            self.y = 0
        if self.y >= HEIGHT:
            self.y = HEIGHT

        return # Signify we are done

    def setRandomPosition(self) -> None:
        """
        Updates the Person’s x and y coordinates to a randomly selected
        value within the appropriate range 
        """

        # Find a random position with the maximum value from the constant values

        newX = randint(0, WIDTH)
        newY = randint(0, HEIGHT)

        # Set the positional data to the new, randomized data

        self.x = newX
        self.y = newY
        
        return  # Signify we are done

    def getPosition(self) -> tuple:
        """
        Calculates the appropriate coordinates using 
        x, y and size and returns the result as a tuple.
        """

        # Take the current position, subtract from the size divided by 2 for both x and y

        return (self.x - (self.size / 2), self.y - (self.size / 2))

    # Default Methods

    def __str__(self) -> str:

        # Take and append the stored color value from the parent class's default __str__ function

        return f"{Item.__str__(self)},\tcolor = {self.color}"





########################### main game################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
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
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()

