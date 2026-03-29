from libs.DynamicEntity import DynamicEntity
from libs.Constants import *

class Projectile(DynamicEntity):

    def __init__(self, name, x, y, color, surf, direction):

        DynamicEntity.__init__(self, name, x, y, False, color, surf)
        
        
        self.velocity = direction  # e.g. (5, 0)

        self.active = True

    

    def update(self):
        self.goDown(self.velocity[0])
        self.goUp(self.velocity[1])

        # If we are off screen, we are no longer active

        if self.x - (self.size[0] / 2) < 0 or self.x + (self.size[0] / 2) > WIDTH:
            self.active = False
        if self.y - (self.size[1] / 2) < 0 or self.y + (self.size[1] / 2) > HEIGHT:
            self.active = False