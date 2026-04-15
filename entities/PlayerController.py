from pygame import sprite, Surface, transform
# keys from pygame
from pygame.locals import (     # just the inputs we want to read
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE
)
from random import randint, choice
from .baseProperties import baseProperties
from .Projectile import Projectile


class PlayerController(sprite.Sprite, baseProperties):
    
    def __init__(self, surf:Surface = Surface((1, 1)), position=(0,0), projectileSurf:Surface = Surface((1,1))):

        # Initialize parent classes

        sprite.Sprite.__init__(self)
        baseProperties.__init__(self, "Wizard", position[0], position[1])

        # Store the surface object for later editing

        self.surf = surf
        self.size = (self.surf.get_rect().width, self.surf.get_rect().height)

        self.projectileSurf = projectileSurf


        # Create a place to store created projectiles (for later rendering)

        self.projectile_list = []
        self.projectile_timer = 0

    # Custom Methods

    def shootProjectile(self, direction):
        newProjectile = Projectile(self, self.projectileSurf, (self.x,self.y), direction)

        self.projectile_list.append(newProjectile)

    def setSize(self) -> None:
        """
        Changes the size of the Person/Item to a random value 
        between 10 and 100, and then changes the size of the 
        surf to match that size
        """

        # Generate a new, random size

        newSize = (randint(10, 100), randint(10, 100))

        # Set the stored values to the new value

        self.size = newSize

        # Change the surface object to match new values and store it

        self.surf = transform.scale(self.surf, newSize)
        
    def invincibility(self):
        self.invincible = True
        self.invincibility_timer = 800
    
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

        # Process projectile press

        self.projectile_timer += 1

        if self.invincibility_timer and self.invincibility_timer > 0:
            self.invincibility_timer -= 1
        elif self.invincibility_timer and self.invincibility <= 0:
            self.invincible = False

        if keyLogs[K_SPACE]:

            if self.projectile_timer >= 1000:
                self.shootProjectile((0, 1))
                self.projectile_timer = 0

        for projectile in self.projectile_list:
            projectile.update()

    def setRandomPosition(self, bounds: tuple) -> None:
        """
        Updates the Person’s x and y coordinates to a randomly selected
        value within the provided bounds (point1, point2)
        """

        # Find a random position within the two points

        newX = randint(bounds[0][0], bounds[1][0])  # x values from both points
        newY = randint(bounds[0][1], bounds[1][1])  # y values from both points

        # Set the positional data to the new, randomized data

        self.x = newX
        self.y = newY
        

    def getPosition(self) -> tuple:
        """
        Calculates the appropriate coordinates using 
        x, y and size and returns the result as a tuple.
        """

        # Take the current position, subtract from the size divided by 2 for both x and y

        return (self.x - (self.size[0] / 2), self.y - (self.size[1] / 2))

    # Default Methods

    def __str__(self) -> str:

        # Take and append the stored color value from the parent class's default __str__ function

        return f"{baseProperties.__str__(self)},\tPosition = ({self.x}, {self.y})"
