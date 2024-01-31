from Monster import *
from Constants import *
from Player2 import *
import Constants

class MediumBoss(Monster):

    def __init__(self, attack_power:float, health:float, img:pygame.image, medium_boss_name:str, start_pos_x:int, start_pos_y:int, height:int, width:int, attacks, proj_img, proj_height, proj_width):
        super().__init__(attack_power, health, img, "Medium Boss", start_pos_x, start_pos_y, height, width, proj_img, proj_height, proj_width)
        
        self.medium_boss_name=medium_boss_name
        self.projectile_change_x=0.0
        self.projectile_change_y=0.0

        self.attacks=attacks
        self.main_attack_timer = pygame.time.get_ticks()
        self.main_attack_cooldown=5000
    
    # Realigns projectile back to monster

    def realign_projectile(self):
        self.projectile.projectile_rectangle.x=self.monster_rectangle.x
        self.projectile.projectile_rectangle.y=self.monster_rectangle.y


    

    

        
        