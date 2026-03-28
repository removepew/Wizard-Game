#####################################################################
# author: Alex Martinez
# date: 3/25/2026
# description: game project
#####################################################################
import pygame
from libs.DynamicEntity import DynamicEntity
from libs.Constants import *



class PlayerController(DynamicEntity):
    
    def __init__(self, name="", x: int=0, y:int = 0, canPass:bool = False, color:list[int] = BLACK, surf:pygame.Surface = False):

        # Initialize parent classes

        surfObj = None

        if not surf:
            surfObj = pygame.image.load("./Assets/wizard.png").convert_alpha()
            surfObj = pygame.transform.scale(surfObj, (50,75))
        else:
            surfObj = surf

        DynamicEntity.__init__(self, "Wizard", 0, 0, False, None, surfObj)


    # Custom Methods

    
    def update(self, keyLogs) -> None:
        """
        Receives as an argument a dictionary containing all the 
        key pressed events and then updates the state of the 
        object based on what was pressed
        """

        # Process directional presses

        # Set this varaible to determine if diagonal movement occured
        moveOpportunities = 2



        if keyLogs[K_UP] or keyLogs[K_DOWN]:
            moveOpportunities = 1
            

        if keyLogs[K_UP]:
            self.goUp()
        if keyLogs[K_DOWN]:
            self.goDown()
        if keyLogs[K_LEFT]:
            self.goLeft()
        if keyLogs[K_RIGHT]:
            self.goRight()

        # Process randomized press

        if False and keyLogs[K_SPACE]:
            self.setColor()
            self.setSize()

        # Keep player within bounds
        if self.x < 0:
            self.x = 0
        elif self.x >= WIDTH:
            self.x = WIDTH
        if self.y <= 0:
            self.y = 0
        elif self.y >= HEIGHT:
            self.y = HEIGHT


