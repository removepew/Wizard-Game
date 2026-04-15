
from pygame import sprite, Surface
from .baseProperties import baseProperties


class Text(sprite.Sprite, baseProperties):
    
    def __init__(self, color:list[int] = [0x00, 0x00, 0x00], surf:Surface = Surface((1, 1)), position=(0,0)):

        # Initialize parent classes

        sprite.Sprite.__init__(self)
        baseProperties.__init__(self, "Text", position[0], position[1])

        # Store the surface object for later editing

        self.surf = surf

        # Set preset values

        self.color = color


    # Custom Methods

    # Default Methods

    def __str__(self) -> str:

        # Take and append the stored color value from the parent class's default __str__ function

        return f"{baseProperties.__str__(self)},\tPosition = ({self.x}, {self.y})"
