from pygame import sprite


class RenderManager():

    def __init__(self, MAX_WIDTH, MAX_HEIGHT, screen, defaultColor):
        self.MAX_WIDTH = MAX_WIDTH
        self.MAX_HEIGHT = MAX_HEIGHT
        self.screen = screen
        self.defaultColor = defaultColor

    def flatten(self, lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result

    def render_step(self, stuff_to_render:list):

         # fill the screen with a color
        self.screen.fill(self.defaultColor)

        for thing in stuff_to_render:
            if thing.x > self.MAX_WIDTH or thing.x < 0:
                continue
            elif thing.y > self.MAX_HEIGHT or thing.y < 0:  # don't render if they arent on the screen
                continue
            
            self.screen.blit(thing.surf, (thing.getPosition()))

            if thing.projectile_list:
                for projectile in thing.projectile_list:
                    self.screen.blit(projectile.surf, (projectile.x, projectile.y))


            
