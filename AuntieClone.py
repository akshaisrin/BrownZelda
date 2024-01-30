from pygame import display as display, image as image
from MiniBoss import *
import os
import Constants

class AuntieClone(MiniBoss):
    
    def __init__(self, attack_power: float, health: float, img: pygame.image.load(os.path.join("Assets", "auntieclone1.png")), mini_boss_name: str, height: int, width: int, start_pos_x: int, start_pos_y: int, is_clone: bool, main_attack:str = None):
        super().__init__(attack_power, health, img, "AuntieClone", start_pos_x, start_pos_y, height, width, "auntie_chapal (2).png", 30, 40, main_attack)
        self.is_clone = is_clone

    def attack(self, player, screen):
        # check if the mini boss is a clone, if it is it only has the one clone attack
        if self.is_clone:
          self.close_range_attack(player, Constants.auntie_clone_speed, screen)

        # if its not, it has a variety of attacks for funsies
        if not self.is_clone:
            if not self.in_hit_cooldown:
                if self.main_attack=="shoot and follow path":
                    
                    self.follow_path_and_shoot(self.path_coords, Constants.auntie_clone_speed, Constants.auntie_projectile_speed, player, screen)

                elif self.main_attack=="shoot and patrol":
                    self.patrol_and_shoot(player, Constants.auntie_clone_speed, Constants.auntie_projectile_speed, self.patrol_distance, self.patrol_direction, screen)
               
                else:
                    
                    self.move_towards_player(player,Constants.csp_kid_walk_towards_player_speed, screen)
        
            if self.in_hit_cooldown:
                now = pygame.time.get_ticks()
                
                if now - self.last_hit>= Constants.hit_cooldown_count:
                    self.in_hit_cooldown=False

    #auntie mini dies
    def die(self) -> None:
        return super().die()
    
    #auntie renders on screen
    def render(self, x_pos: float, y_pos: float, height: int, width: int, screen) -> None:
        return super().render(x_pos, y_pos, height, width, screen)
