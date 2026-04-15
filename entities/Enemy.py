from pygame import sprite, Surface, transform
from random import randint, choice
from .baseProperties import baseProperties
from .Projectile import Projectile


class Enemy(sprite.Sprite, baseProperties):
    
    def __init__(self, color:list[int] = [0xe3, 0x1b, 0x23], surf:Surface = Surface((1, 1)), position=(0,0), projectileSurf:Surface = Surface((1,1)), restriction_area=None, projectile_based=False):

        # Initialize parent classes

        sprite.Sprite.__init__(self)
        baseProperties.__init__(self, "Enemy", position[0], position[1])

        # Store the surface object for later editing

        self.surf = surf
        self.size = self.surf.get_rect()

        # Set preset values

        self.color = color
        self.surf.fill(color)

        self.projectile_list = []
        self.projectile_timer = 0

        self.restriction_area = restriction_area

    # Custom Methods

    def setColor(self, colorList:list):
        """
        Randomly selects the value to be stored in the color 
        instance variable, and then changes the color of the 
        surf to match that color
        """
        chosenColor = choice(colorList)

        self.color = chosenColor

        self.surf.fill(chosenColor)


    def setSize(self, square=True) -> None:
        """
        Changes the size of the Person/Item to a random value 
        between 10 and 100, and then changes the size of the 
        surf to match that size
        """

        # Generate a new, random size

        newSize = (1, 1)

        if square:
            generatedNum = randint(10, 100)
            newSize = (generatedNum, generatedNum)
        else:
            newSize = (randint(10, 100), randint(10, 100))

        # Set the stored values to the new value

        self.size = newSize

        # Change the surface object to match new values and store it

        self.surf = transform.scale(self.surf, newSize)
        

    
    def update(self) -> None:
        if self.restriction_area:   # are we restricted somewhere?
            
            x1_restriction = min((self.restriction_area[0][0], self.restriction_area[1][0]))    # always the largest
            x2_restriction = max((self.restriction_area[0][0], self.restriction_area[1][0]))    # always the smallest

            y1_restriction = min((self.restriction_area[0][1], self.restriction_area[1][1]))    # same
            y2_restriction = max((self.restriction_area[0][1], self.restriction_area[1][1]))

            if y1_restriction >= self.y:
                self.goDown()
            else:
                self.goUp()

            if x1_restriction < self.x:
                self.goRight()
            else:
                self.goLeft()
        
        if self.projectile_based:
            self.projectile_timer += 1

            for projectile in self.projectile_list:
                projectile.update()

            if self.projectile_timer >= 2000:
                self.shootProjectile((0, 1))
                self.projectile_timer = 0
        

    def shootProjectile(self, direction):
        newProjectile = Projectile(self, self.projectileSurf, (self.x,self.y), direction)

        self.projectile_list.append(newProjectile)

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

        return self.surf.get_rect().topleft # (self.x - (self.size / 2), self.y - (self.size / 2)) )

    # Default Methods

    def __str__(self) -> str:

        # Take and append the stored color value from the parent class's default __str__ function

        return f"{baseProperties.__str__(self)},\tPosition = ({self.x}, {self.y})"
