import pygame
from Projectile import *
import os
import Constants
import time
import random
class Monster:

    def __init__(self, attack_power:float, health:float, img:pygame.image, monster_type:str, start_pos_x:int, start_pos_y:int, height:int, width:int):

        self.attack_power=attack_power
        self.health=health
        self.height=height
        self.width=width
        self.img=img
        self.img=pygame.transform.scale(self.img, (self.height, self.width))
        self.x_pos=start_pos_x
        self.y_pos=start_pos_y
        self.monster_type=monster_type
        self.alive = True
        self.monster_rectangle=self.img.get_rect()
        self.monster_rectangle.x, self.monster_rectangle.y = start_pos_x, start_pos_y
        self.projectile = Projectile(1, self.monster_rectangle.x, self.monster_rectangle.y, 50, 50, pygame.image.load(os.path.join("Assets", "flappybird.png")))
        self.current_increment=1
        self.total_increments=0
        
    
    def realign_projectile(self):
        self.projectile.projectile_rectangle.x=self.monster_rectangle.x
        self.projectile.projectile_rectangle.y=self.monster_rectangle.y

    def start_moving(self, player):
        
        self.movement_vector=Constants.mini_boss_movement_vector[random.choice(["left", "right", "up", "down"])]
        self.monster_rectangle.move_ip(self.movement_vector[0], self.movement_vector[1])
        



    def shoot(self, screen, player):
        

        # Returning projectile back to monster
        
        if (self.projectile.projectile_rectangle.x>=Constants.screen_width or self.projectile.projectile_rectangle.x<=0 or self.projectile.projectile_rectangle.y>=Constants.screen_height or self.projectile.projectile_rectangle.y<=0):
            self.realign_projectile()
            
        if (self.monster_rectangle.colliderect(self.projectile.projectile_rectangle)):
            offset_x=self.projectile.projectile_rectangle.x+Constants.medium_boss_projectile_offset_x
            offset_y=self.projectile.projectile_rectangle.y+Constants.medium_boss_projectile_offset_y

            self.projectile_change_x=(player.player_rectangle.x-offset_x)/Constants.medium_boss_velocity_constant
            self.projectile_change_y=(player.player_rectangle.y-offset_y)/Constants.medium_boss_velocity_constant


        self.projectile.projectile_rectangle.x+=self.projectile_change_x
        self.projectile.projectile_rectangle.y+=self.projectile_change_y

        self.projectile.render(self.projectile.projectile_rectangle.x, self.projectile.projectile_rectangle.y, screen)
    
          
    def render(self, x_pos:float, y_pos:float, height:int, width:int, screen:pygame.display) -> None:
        # self.x_pos=x_pos
        # self.y_pos=y_pos

        image = pygame.transform.scale(self.img, (width, height))
        self.monster_rectangle = image.get_rect()
        self.monster_rectangle.topleft = (x_pos, y_pos)
        #pygame.draw.rect(screen, (0, 0, 255), self.monster_rectangle)
        screen.blit(image, self.monster_rectangle)
    
    def get_hit(self, damage:float):
        
        self.health-=damage

        if self.health<=0:
            self.die()

    def die(self) -> None:  

        # Implement die here
        self.alive = False

        print(f"Monster: {self.monster_type} has been killed") 
