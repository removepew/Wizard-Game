from pygame import sprite, Surface
from .baseProperties import baseProperties

class Projectile(sprite.Sprite, baseProperties):

    def __init__(self, parent_ref, surface, position, velocity):
        # Initialize parent classes

        sprite.Sprite.__init__(self)
        baseProperties.__init__(self, "projectile", position[0], position[1])

        self.parent = parent_ref        # so we can keep track who owns which projectiles
        

