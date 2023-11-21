from Monster import *
from Constants import *
import Constants

class MediumBoss(Monster):

    def __init__(self, attack_power:float, health:float, img:pygame.image, medium_boss_name:str, start_pos_x:int, start_pos_y:int, height:int, width:int):
        super().__init__(attack_power, health, img, "Medium Boss", start_pos_x, start_pos_y, height, width)
        
        self.medium_boss_name=medium_boss_name
        self.projectile_change_x=0.0
        self.projectile_change_y=0.0
    
    def shoot(self, screen, player):
        

        # Returning projectile back to monster
        
        if (self.projectile.x_pos>=Constants.screen_width or self.projectile.x_pos<=0 or self.projectile.y_pos>=Constants.screen_height or self.projectile.y_pos<=0):
            self.projectile.x_pos=self.x_pos
            self.projectile.y_pos=self.y_pos

        if (abs(self.x_pos-self.projectile.x_pos)<=Constants.med_boss_projectile_bounds and abs(self.y_pos-self.projectile.y_pos)<=Constants.med_boss_projectile_bounds):
            offset_x=self.projectile.x_pos+Constants.medium_boss_projectile_offset_x
            offset_y=self.projectile.y_pos+Constants.medium_boss_projectile_offset_y

            self.projectile_change_x=(player.x_pos-offset_x)/Constants.medium_boss_velocity_constant
            self.projectile_change_y=(player.y_pos-offset_y)/Constants.medium_boss_velocity_constant


        self.projectile.x_pos+=self.projectile_change_x
        self.projectile.y_pos+=self.projectile_change_y

        self.projectile.render(self.projectile.x_pos, self.projectile.y_pos, screen)

        
        