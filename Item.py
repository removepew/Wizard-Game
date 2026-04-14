#####################################################################
# author: Alex Martinez
# date: 3/12/2026
# description: Item class
#####################################################################

from math import sqrt
from Constants import HEIGHT, WIDTH

# global Constants to restrict the maximum x and y values that a person object
# can have.
# Lazy
MAX_X = WIDTH
MAX_Y = HEIGHT

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Item:
    
    def __init__(self, name: str="", x: int=0, y: int=0):
        self.name = name
        self.size = 1
        self.x = x
        self.y = y

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
    
    # Mutators / Setters

    @name.setter
    def name(self, newName):
        if isinstance(newName, str) and len(newName) > 2:
            self._name = newName
        else:
            self._name = "player 1"     # Default

    @size.setter
    def size(self, newSize):
        if newSize >= 1:    # check if it is greater than or equal to 1, otherwise do nothing
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
    def getDistance(self, otherItem: 'Item'):
        return sqrt(pow((otherItem.y - self.y), 2) + pow((otherItem.x - self.x), 2))

    # Default Methods

    def __str__(self):
        return f"Person({self.name}):\tsize = {self.size},\tx = {self.x}\ty = {self.y}"
