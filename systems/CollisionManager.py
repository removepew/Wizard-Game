from pygame import sprite, Rect


class CollisionManager:

    def __init__(self, MAX_WIDTH, MAX_HEIGHT):
        self.MAX_WIDTH = MAX_WIDTH
        self.MAX_HEIGHT = MAX_HEIGHT
        self.bounds = Rect(0, 0, self.MAX_WIDTH, self.MAX_HEIGHT)
        

    def check_player_collide(self, player_sprite, enemy_group):
        
        if player_sprite.invincible:    # we can't do damage so no need
            return

        # something touched the player?
        for enemy in enemy_group:
            if player_sprite.getDistance(enemy) <= player_sprite.size[0]:
                player_sprite.invincibility()       # make the player invincible
                return True     # tell the program to deduct a health point
            
    def check_projectile_collide(self, player_sprite, enemy_group):

        thingsToHurt = [] # list of enemies to delete after being hit

        
        # any player projectiles touch anything?
        for projectile in player_sprite.projectile_list:

            if self.check_bounds(projectile, player_sprite.projectile_list):
                projectile = None
                continue

            for enemy in enemy_group:
                if projectile.getDistance(enemy) <= enemy.size[0]:
                    thingsToHurt.append(enemy)

        if player_sprite.invincible:    # we can't do damage so no need
            return thingsToHurt
        
        # any projectiles touch anything?
        for enemy in enemy_group:
            if enemy.projectile_list:
                
                for projectile in enemy.projectile_list:

                    if self.check_bounds(projectile, enemy.projectile_list):
                        projectile = None
                        continue


                    if projectile.getDistance(player_sprite) <= player_sprite.size[0]:
                        return thingsToHurt, True     # tell the program to deduct a health point
            
        
    def check_bounds(self, thing, list):
        if thing.x > self.MAX_WIDTH or thing.x < 0:
            return True
        elif thing.y > self.MAX_HEIGHT or thing.y < 0:
            return True
        
    def boundary_restrict(self, things):
        for thing in things:
            if thing.x > self.MAX_WIDTH:
                thing.x = self.MAX_WIDTH
            elif thing.x < 0:
                thing.x = 0

            if thing.y > self.MAX_HEIGHT:
                thing.y = self.MAX_HEIGHT
            elif thing.y < 0:
                thing.y = 0
        

