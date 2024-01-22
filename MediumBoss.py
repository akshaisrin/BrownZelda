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
    
    def realign_projectile(self):
        self.projectile.projectile_rectangle.x=self.monster_rectangle.x
        self.projectile.projectile_rectangle.y=self.monster_rectangle.y

    # def shoot(self, screen, player):
        

    #     # Returning projectile back to monster
        
    #     if (self.projectile.projectile_rectangle.x>=Constants.screen_width or self.projectile.projectile_rectangle.x<=0 or self.projectile.projectile_rectangle.y>=Constants.screen_height or self.projectile.projectile_rectangle.y<=0):
    #         self.realign_projectile()
            
    #     if (self.monster_rectangle.colliderect(self.projectile.projectile_rectangle)):
    #         offset_x=self.projectile.projectile_rectangle.x+Constants.medium_boss_projectile_offset_x
    #         offset_y=self.projectile.projectile_rectangle.y+Constants.medium_boss_projectile_offset_y

    #         self.projectile_change_x=(player.player_rectangle.x-offset_x)/Constants.medium_boss_velocity_constant
    #         self.projectile_change_y=(player.player_rectangle.y-offset_y)/Constants.medium_boss_velocity_constant


    #     self.projectile.projectile_rectangle.x+=self.projectile_change_x
    #     self.projectile.projectile_rectangle.y+=self.projectile_change_y

    #     self.projectile.render(self.projectile.projectile_rectangle.x, self.projectile.projectile_rectangle.y, screen)
    

    

        
        