import math
import pygame
from Projectile import *
import os
import Constants
import time
import random
class Monster:

    def __init__(self, attack_power:float, health:float, img:pygame.image, monster_type:str, start_pos_x:int, start_pos_y:int, height:int, width:int, proj_img:str, proj_height:int, proj_width:int):

        self.attack_power=attack_power
        self.health=health
        self.height=height
        self.width=width
        self.img=img
        self.img=pygame.transform.scale(self.img, (self.height, self.width))
        self.start_pos_x=start_pos_x
        self.start_pos_y=start_pos_y
        self.monster_type=monster_type
        self.alive = True
        self.monster_rectangle=self.img.get_rect()
        self.monster_rectangle.x, self.monster_rectangle.y = start_pos_x, start_pos_y
        self.projectile = Projectile(1, self.monster_rectangle.x, self.monster_rectangle.y, proj_height, proj_width, pygame.image.load(os.path.join("Assets", proj_img)))
        self.current_increment=1
        self.total_increments=0
        self.patrol_constant=Constants.reg_patrol_constant
        self.projectile_constant=Constants.reg_projectile_constant

        # Stuff for attacks        

        self.patrol_vector=(0,0)
        self.patrol_bounds=[(self.start_pos_x,self.start_pos_y), (self.start_pos_x+100, self.start_pos_y)]
        
        self.current_path_target_coords=(0,0)
        self.path_direction="forwards"

        self.hit_wall=False

        self.stop_moving=False
    
    def realign_projectile(self):
        self.projectile.projectile_rectangle.x=self.monster_rectangle.x
        self.projectile.projectile_rectangle.y=self.monster_rectangle.y

    def move_towards_player(self, player, speed):
        

        distance = [player.player_rectangle.x - self.monster_rectangle.x, player.player_rectangle.y - self.monster_rectangle.y]
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / norm, distance[1 ] / norm]

        movement_vector = [direction[0] * speed, direction[1] * speed]
        self.monster_rectangle.move_ip(movement_vector[0], movement_vector[1])
    
    def patrol_and_shoot(self, player, x1, y1, x2, y2, speed, screen):
        # check vertical distance between player and monster to figure out if monster should shoot
        
        if (self.stop_moving):
            self.shoot_straight(self.projectile.shoot_coords[0], self.projectile.shoot_coords[1], speed, screen)

        elif abs(player.player_rectangle.centery-self.monster_rectangle.centery)<=player.player_rectangle.height/2 or abs(player.player_rectangle.centerx-self.monster_rectangle.centerx)<=self.monster_rectangle.width/2:
            self.stop_moving=True
            self.shoot_straight(player.player_rectangle.x, player.player_rectangle.y, speed, screen)
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
    
    def patrol(self, speed, distance, direction):

        if direction=='x':
            self.patrol_bounds[1]=(self.start_pos_x+distance, self.start_pos_y)

        if direction=='y':
            self.patrol_bounds[1]=(self.start_pos_x, self.start_pos_y+distance)

        recalculate_vector=False
        if (self.monster_rectangle.collidepoint(self.patrol_bounds[1][0], self.patrol_bounds[1][1])):
            distance = [self.patrol_bounds[0][0] - self.patrol_bounds[1][0], self.patrol_bounds[0][1] - self.patrol_bounds[1][1]]
            recalculate_vector=True
            
        if (self.monster_rectangle.collidepoint(self.patrol_bounds[0][0], self.patrol_bounds[0][1])):
            distance = [self.patrol_bounds[1][0] - self.patrol_bounds[0][0], self.patrol_bounds[1][1] - self.patrol_bounds[0][1]]
            recalculate_vector=True

        if recalculate_vector:
            norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
            direction = [distance[0] / norm, distance[1 ] / norm]
            self.patrol_vector = (direction[0] * speed, direction[1] * speed)
        
        self.monster_rectangle.move_ip(self.patrol_vector[0], self.patrol_vector[1])

    def follow_path(self, coords, speed):

        recalculate_vector=False

        if self.monster_rectangle.collidepoint(coords[0][0], coords[0][1]):
            self.path_direction="forwards"

        elif self.monster_rectangle.collidepoint(coords[len(coords)-1][0], coords[len(coords)-1][1]):
            self.path_direction="backwards"

        if self.path_direction=="forwards":
            if self.monster_rectangle.collidepoint(coords[len(coords)-2][0], coords[len(coords)-2][1]):
                self.current_target_path_coords=coords[len(coords)-1]
                distance=[coords[len(coords)-1][0]-coords[len(coords)-2][0], coords[len(coords)-1][1]-coords[len(coords)-2][1]]
                recalculate_vector=True

            else:
                for i in range(0,len(coords)-1):
                    
                    if self.monster_rectangle.collidepoint(coords[i][0], coords[i][1]):
                        self.current_target_path_coords=coords[i+1]
                        distance=[coords[i+1][0]-coords[i][0], coords[i+1][1]-coords[i][1]]
                        recalculate_vector=True
                        break
        
        else:
            
            if self.monster_rectangle.collidepoint(coords[1][0], coords[1][1]):
                self.current_target_path_coords=coords[0]
                distance=[coords[0][0]-coords[1][0], coords[0][1]-coords[1][1]]
                recalculate_vector=True

            else:
                for i in range(len(coords)-1, -1, -1):
                    
                    if self.monster_rectangle.collidepoint(coords[i][0], coords[i][1]):
                        self.current_target_path_coords=coords[i-1]
                        distance=[coords[i-1][0]-coords[i][0], coords[i-1][1]-coords[i][1]]
                        recalculate_vector=True
                        break

        if recalculate_vector:
            norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
            direction = [distance[0] / norm, distance[1 ] / norm]
            self.patrol_vector = (direction[0] * speed, direction[1] * speed)            

        self.monster_rectangle.move_ip(self.patrol_vector[0], self.patrol_vector[1])

    def follow_path_and_shoot(self, coords, speed, projectile_speed, player, screen):

        if (self.stop_moving):
            self.shoot_straight(self.projectile.shoot_coords[0], self.projectile.shoot_coords[1], projectile_speed, screen)

        elif abs(player.player_rectangle.centery-self.monster_rectangle.centery)<=player.player_rectangle.height/2 or abs(player.player_rectangle.centerx-self.monster_rectangle.centerx)<=self.monster_rectangle.width/2:
            self.stop_moving=True
            self.shoot_straight(player.player_rectangle.x, player.player_rectangle.y, projectile_speed, screen)
            self.projectile.shoot_coords=(player.player_rectangle.x, player.player_rectangle.y)
        
        # check to see if projectile is at edge of screen

        if self.projectile.projectile_rectangle.x<=0 or self.projectile.projectile_rectangle.x>=Constants.screen_width or self.projectile.projectile_rectangle.y<=0 or self.projectile.projectile_rectangle.y>=Constants.screen_height:
            self.stop_moving=False
            self.projectile.started_shooting=True
        
        if not self.stop_moving:
            self.follow_path(coords, speed)
        

    def shoot_straight(self, end_x, end_y, speed, screen):

        if self.projectile.started_shooting:
            self.projectile.projectile_rectangle.x=self.monster_rectangle.x
            self.projectile.projectile_rectangle.y=self.monster_rectangle.y
            self.projectile.started_shooting=False
            
        distance = [end_x - self.monster_rectangle.x, end_y - self.monster_rectangle.y]
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / norm, distance[1 ] / norm]

        movement_vector = [direction[0] * speed, direction[1] * speed]
        self.projectile.projectile_rectangle.move_ip(movement_vector[0], movement_vector[1])

        self.projectile.render(self.projectile.projectile_rectangle.x, self.projectile.projectile_rectangle.y, screen)

    
    def render(self, x_pos:float, y_pos:float, height:int, width:int, screen:pygame.display) -> None:
        
        image = pygame.transform.scale(self.img, (width, height))
        self.monster_rectangle = image.get_rect()
        self.monster_rectangle.topleft = (x_pos, y_pos)
        screen.blit(image, self.monster_rectangle)
    
    def get_hit(self, damage:float):
        
        self.health-=damage
        print("got hit")
        if self.health<=0:
            self.die()

    def die(self) -> None:  

        # Implement die here
        self.alive = False

        print(f"Monster: {self.monster_type} has been killed") 
