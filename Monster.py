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
        self.projectile = Projectile(1, self.monster_rectangle.x, self.monster_rectangle.y, 40, 40, pygame.image.load(os.path.join("Assets", "flappybird.png")))
        self.current_increment=1
        self.total_increments=0
        self.patrol_constant=Constants.reg_patrol_constant
        self.projectile_constant=Constants.reg_projectile_constant

        # Stuff for attacks        

        self.patrol_vector=(0,0)
        self.hit_wall=False

        self.stop_moving=False
        
    
    def realign_projectile(self):
        self.projectile.projectile_rectangle.x=self.monster_rectangle.x
        self.projectile.projectile_rectangle.y=self.monster_rectangle.y

    def start_moving(self, player):
        
        self.movement_vector=Constants.mini_boss_movement_vector[random.choice(["left", "right", "up", "down"])]
        self.monster_rectangle.move_ip(self.movement_vector[0], self.movement_vector[1])
    
    def patrol_and_shoot(self, player, x1, y1, x2, y2, screen):
        # check vertical distance between player and monster to figure out if monster should shoot
        
        if (self.stop_moving):
            self.shoot_straight(self.projectile.shoot_coords[0], self.projectile.shoot_coords[1], screen)

        elif abs(player.player_rectangle.centery-self.monster_rectangle.centery)<=player.player_rectangle.height/2 or abs(player.player_rectangle.centerx-self.monster_rectangle.centerx)<=self.monster_rectangle.width/2:
            self.stop_moving=True
            self.shoot_straight(player.player_rectangle.x, player.player_rectangle.y, screen)
            self.projectile.shoot_coords=(player.player_rectangle.x, player.player_rectangle.y)
        
        # check to see if projectile is at edge of screen

        if self.projectile.projectile_rectangle.x<=0 or self.projectile.projectile_rectangle.x>=Constants.screen_width or self.projectile.projectile_rectangle.y<=0 or self.projectile.projectile_rectangle.y>=Constants.screen_height:
            self.stop_moving=False
            self.projectile.started_shooting=True


        # check to see if monster at new coords

        if not self.stop_moving:

            if (self.monster_rectangle.collidepoint(x2, y2)):
                self.patrol_vector=((x1-x2)/self.patrol_constant, (y1-y2)/self.patrol_constant)
            
            if (self.monster_rectangle.collidepoint(x1, y1)):
                self.patrol_vector=((x2-x1)/self.patrol_constant, (y2-y1)/self.patrol_constant)
            
            self.monster_rectangle.move_ip(self.patrol_vector[0], self.patrol_vector[1])
    
    

    def shoot_straight(self, end_x, end_y, screen):

        if self.projectile.started_shooting:
            self.projectile.projectile_rectangle.x=self.monster_rectangle.x
            self.projectile.projectile_rectangle.y=self.monster_rectangle.y
            self.projectile.started_shooting=False

        change=((end_x-self.monster_rectangle.x)/self.projectile_constant, (end_y-self.monster_rectangle.y)/self.projectile_constant)
        self.projectile.projectile_rectangle.move_ip(change[0], change[1])
        self.projectile.render(self.projectile.projectile_rectangle.x, self.projectile.projectile_rectangle.y, screen)
    

    
    def render(self, x_pos:float, y_pos:float, height:int, width:int, screen:pygame.display) -> None:
        
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
