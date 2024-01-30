from pygame import display as display, image as image
from MiniBoss import *
import os
import Constants

class Paparazzi(MiniBoss):
    
    def __init__(self, attack_power: float, health: float, img: pygame.image.load(os.path.join("Assets", "auntieclone1.png")), mini_boss_name: str, height: int, width: int, start_pos_x: int, start_pos_y: int):
        super().__init__(attack_power, health, img, "Paparazzi", start_pos_x, start_pos_y, height, width, "camera_projectile.png", 40, 40, "none")
    
    #paparazzi has two attacks
    def attack(self, player, screen):
       self.close_range_attack(player, Constants.auntie_clone_speed, screen)
       self.walk_towards_player_and_shoot(player, Constants.paparazzi_speed, Constants.paparazzi_proj_speed, screen)
    
    def die(self) -> None:  
        return super().die()
    
    def render(self, x_pos: float, y_pos: float, height: int, width: int, screen) -> None:
        return super().render(x_pos, y_pos, height, width, screen)
