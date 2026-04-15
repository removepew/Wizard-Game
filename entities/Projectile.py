from pygame import sprite, Surface
from .baseProperties import baseProperties

class Projectile(sprite.Sprite, baseProperties):

    def __init__(self, parent_ref, surface, position, velocity):
        # Initialize parent classes

        sprite.Sprite.__init__(self)
        baseProperties.__init__(self, "projectile", position[0], position[1])

        self.surf = surface
        self.parent = parent_ref        # so we can keep track who owns which projectiles
        self.x = position[0]
        self.y = position[1]
        self.velocity = velocity
        
    def update(self):
        self.x += self.velocity[0]      # could use inherented functions
        self.y += self.velocity[1]      # but it unnecessarily complicates these two lines

    
        

