from random import randint, choice
from libs.Constants import *
from libs.Entity import Entity

class DynamicEntity(pygame.sprite.Sprite, Entity):

    def __init__(self, name, x, y, canPass, color, surf, damageOnTouch = False):
        # Initialize parent classes

        pygame.sprite.Sprite.__init__(self)
        Entity.__init__(self, name, x, y, canPass)

        # Store the surface object for later editing

        self.size  = surf.get_size()

        self.surf = surf

        # Set preset values
        self.color = color
        if color != None:

            self.surf.fill(color)
    
        self.rect = self.surf.get_rect()


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
    
    def setRandomPosition(self) -> None:
        """
        Updates the Person's x and y coordinates to a randomly selected
        value within the appropriate range 
        """

        # Find a random position with the maximum value from the constant values

        newX = randint(0, WIDTH)
        newY = randint(0, HEIGHT)

        # Set the positional data to the new, randomized data

        self.x = newX
        self.y = newY
        
        return  # Signify we are done
    
    def setSize(self) -> None:
        """
        Changes the size of the Person/Item to a random value 
        between 10 and 100, and then changes the size of the 
        surf to match that size
        """

        # Generate a new, random size

        newSize = randint(10, 100)

        # Set the stored values to the new value

        self.size = (newSize, newSize)

        # Change the surface object to match new values and store it

        self.surf = pygame.transform.scale(self.surf, (newSize, newSize))

        self.rect = self.surf.get_rect()
        

        return # Signify we are done
    
    def getPosition(self) -> tuple:
        """
        Calculates the appropriate coordinates using 
        x, y and size and returns the result as a tuple.
        """

        # Take the current position, subtract from the size divided by 2 for both x and y

        return (self.x - (self.size[0] / 2), self.y - (self.size[1] / 2))
    
    def __str__(self) -> str:

        # Take and append the stored color value from the parent class's default __str__ function

        return f"{Entity.__str__(self)},\tcolor = {self.color}"