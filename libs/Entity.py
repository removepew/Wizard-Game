#####################################################################
#   File which is the basis for all entities within the game
#   Contains the positional data and size for an entity
#   Additionally contains pass-through data
#####################################################################

from math import sqrt
from libs.Constants import HEIGHT, WIDTH

# global Constants to restrict the maximum x and y values that an entity object
# can have.
MAX_X = WIDTH
MAX_Y = HEIGHT

# A class representing an entity. An entity can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). An entity
# also has a size which is set to 1 by default. An entity can go left, 
# go right, go up and go down. An entity also has a string function 
# that prints out their name location, and size. An entity also has a 
# function that calculates the euclidean distance from another entity 
# object.
class Entity:
    
    def __init__(self, name: str="", x: int=0, y: int=0, canPass: bool=False):
        self.name = name
        self.size = (1,1)
        self.x = x
        self.y = y
        self.canPass = canPass

    # Accessors

    @property
    def name(self) -> str:
        return self._name

    @property
    def size(self) -> float:
        return self._size

    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y 
    
    @property
    def canPass(self) -> bool:
         return self._canPass
    
    # Mutators / Setters

    @name.setter
    def name(self, newName):
        if isinstance(newName, str) and len(newName) > 2:
            self._name = newName
        else:
            self._name = "player 1"     # Default

    @size.setter
    def size(self, newSize):
        if newSize[0] >= 1 and newSize[1] >= 1:    # check if it is greater than or equal to 1, otherwise do nothing
            self._size = newSize
    
    @x.setter
    def x(self, newX):
        if isinstance(newX, int) and newX >= 0:       # check if it's an integer- if so, check if it isn't negative

            if newX > MAX_X:                          # check if the new value is greater than what is allowed- if so, max it out
                self._x = MAX_X
            else:
                self._x = newX

        else:
            self._x = 0     # Default

    @y.setter
    def y(self, newY):
        if isinstance(newY, int) and newY >= 0:       # check if it's an integer- if so, check if it isn't negative

            if newY > MAX_Y:                          # check if the new value is greater than what is allowed- if so, max it out
                self._y = MAX_Y
            else:
                self._y = newY

        else:
            self._y = 0     # Default

    @canPass.setter
    def canPass(self, newValue):
         self._canPass = newValue

    # Custom Functions

    # Movement
    def goLeft(self, distance:int = 1):
        
            self.x = self.x - distance

    def goRight(self, distance:int = 1):
        
            self.x = self.x + distance

    def goUp(self, distance:int = 1):
        
            self.y = self.y - distance

    def goDown(self, distance:int = 1):
        
            self.y = self.y + distance

    # Data
    def getDistance(self, otherEntity: 'Entity') -> int:
        return sqrt(pow((otherEntity.y - self.y), 2) + pow((otherEntity.x - self.x), 2))
    
    def getPosition(self) -> tuple:
        """
        Calculates the appropriate coordinates using 
        x, y and size and returns the result as a tuple.
        """

        # Take the current position, subtract from the size divided by 2 for both x and y

        return (self.x - (self.size / 2), self.y - (self.size / 2))

    # Default Methods

    def __str__(self):
        return f"Entity({self.name}):\tsize = {self.size},\tx = {self.x}\ty = {self.y}\tcanPass = {self.canPass}"
