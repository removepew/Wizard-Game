from math import sqrt


# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class baseProperties:
    
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
    def x(self, newX): # we will handle collision checks in another script lol
        if isinstance(newX, int):       # check if it's an integer
            self._x = newX

        elif isinstance(newX, float):   # check if we can change it
            self._x = round(newX)

        else:                           # explode otherwise
            raise TypeError(f"Attempted to assign {type(newX)} to x")

    @y.setter
    def y(self, newY):  # we will handle collision checks in another script lol
        if isinstance(newY, int):       # check if it's an integer
            self._y = newY

        elif isinstance(newY, float):   # check if we can change it
            self._y = round(newY)

        else:                           # explode otherwise
            raise TypeError(f"Attempted to assign {type(newY)} to y")
        
    # Custom Functions

    # Data
    def getDistance(self, otherItem):
        return sqrt(pow((otherItem.y - self.y), 2) + pow((otherItem.x - self.x), 2))

    # Default Methods

    def __str__(self):
        return f"Person({self.name}):\tsize = {self.size},\tx = {self.x}\ty = {self.y}"
