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
        self.projectile = Projectile(0.5, self.monster_rectangle.x, self.monster_rectangle.y, proj_height, proj_width, pygame.image.load(os.path.join("Assets", proj_img)))
        self.current_increment=1
        self.total_increments=0
        self.patrol_constant=Constants.reg_patrol_constant
        self.projectile_constant=Constants.reg_projectile_constant
        self.attacked = False
        self.attacktime = None
        rect = self.img.get_rect()
        dsurface = self.img.copy()
        wsurface = pygame.Surface(rect.size, pygame.SRCALPHA)
        wsurface.fill((255, 255, 255, 128))
        dsurface.blit(wsurface, (0, 0), None, pygame.BLEND_RGB_ADD)
        self.attackimg = dsurface

        # Stuff for patrolling/path following

        self.patrol_vector=(0,0)
        self.patrol_bounds=[(self.start_pos_x,self.start_pos_y), (self.start_pos_x+100, self.start_pos_y)]
        self.current_path_target_coords=(0,0)
        self.path_direction="forwards"

        self.hit_wall=False

        self.stop_moving=False
        self.current_attack_damage=1

        # Stuff for cooldown between attacks to make sure the player doesn't instantly die

        self.first_time_attacking=True
        self.first_time_shooting=True
        self.last_damage = pygame.time.get_ticks()
        self.last_fired=pygame.time.get_ticks()

        self.in_hit_cooldown=False
        self.last_hit=pygame.time.get_ticks()

    # Moves projectile back to monster
        
    def realign_projectile(self):
        self.projectile.projectile_rectangle.x=self.monster_rectangle.x
        self.projectile.projectile_rectangle.y=self.monster_rectangle.y

    # Monster walks towards player- this is kinda buggy so ignore for time being
        
    def move_towards_player(self, player, speed, screen, attack_damage=1):
        self.current_attack_damage=attack_damage
        distance = [player.player_rectangle.x - self.monster_rectangle.x, player.player_rectangle.y - self.monster_rectangle.y]
        
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        if norm==0:
            norm=1
        direction = [distance[0] / norm, distance[1 ] / norm]

        movement_vector = [direction[0] * speed, direction[1] * speed]
        self.monster_rectangle.move_ip(movement_vector[0], movement_vector[1])

        # This collision detection code should technically go in overworld, but the collision wasn't detecting there (idk why) so I've also included it here, which seems to work

        if self.monster_rectangle.colliderect(player.player_rectangle) and not player.attacking:
            now = pygame.time.get_ticks()
            if now -self.last_damage >= Constants.monster_attack_cooldown_count or self.first_time_attacking:
                self.last_damage = now
                player.get_attacked(self.current_attack_damage, screen)
                self.first_time_attacking=False
    
    # Patrols between two points

    def patrol(self, speed, distance, direction):

        # Starts at its start position, sets its end point as start position + distance in the given direction, and moves between the two points

        self.current_attack_damage=1
        
        # Patrol bounds is the two points the monster shud travel in between
        
        if direction=='x':
            self.patrol_bounds[1]=(self.start_pos_x+distance, self.start_pos_y)

        if direction=='y':
            self.patrol_bounds[1]=(self.start_pos_x, self.start_pos_y+distance)

        recalculate_vector=False

        # Checking for collision with second point

        if (self.monster_rectangle.collidepoint(self.patrol_bounds[1][0], self.patrol_bounds[1][1])):
            distance = [self.patrol_bounds[0][0] - self.patrol_bounds[1][0], self.patrol_bounds[0][1] - self.patrol_bounds[1][1]]
            recalculate_vector=True
        
        # Checking for collision with first point

        if (self.monster_rectangle.collidepoint(self.patrol_bounds[0][0], self.patrol_bounds[0][1])):
            distance = [self.patrol_bounds[1][0] - self.patrol_bounds[0][0], self.patrol_bounds[1][1] - self.patrol_bounds[0][1]]
            recalculate_vector=True

        # New movement vectors are calculated since the monster is changing directions

        if recalculate_vector:
            norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
            direction = [distance[0] / norm, distance[1 ] / norm]
            self.patrol_vector = (direction[0] * speed, direction[1] * speed)
        
        self.monster_rectangle.move_ip(self.patrol_vector[0], self.patrol_vector[1])
    
    # Patrolling with shooting
        
    def patrol_and_shoot(self,player, speed, projectile_speed, distance, direction, screen):
        self.current_attack_damage=1
        self.check_if_in_line_with_player_and_shoot(projectile_speed, player, screen)
        if not self.stop_moving:
            self.patrol(speed, distance, direction)

    # Monster will follow a path in a list of coords, and will reverse the path once it reaches the end

    def follow_path(self, coords, speed):
        self.current_attack_damage=1
        recalculate_vector=False

        # Checks for collision with first point in list to set direction as forwards (going through list of coords normally from index 0 to end)

        if self.monster_rectangle.collidepoint(coords[0][0], coords[0][1]):
            self.path_direction="forwards"

        # Checks for collision with last point in list to set direction as backwards (going through list of coords in reverse order)    

        elif self.monster_rectangle.collidepoint(coords[len(coords)-1][0], coords[len(coords)-1][1]):
            self.path_direction="backwards"

        # Going through list of coords in normal order and calculating the updated distance between points
            
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

        # Going through list of coords in reverse order and calculating the updated distance between points
                    
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
        
        # New movement vectors are calculated when the monster reaches one of the points in its list
                    
        if recalculate_vector:
            norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
            direction = [distance[0] / norm, distance[1 ] / norm]
            self.patrol_vector = (direction[0] * speed, direction[1] * speed)            

        self.monster_rectangle.move_ip(self.patrol_vector[0], self.patrol_vector[1])

    # Path following with shooting 
        
    def follow_path_and_shoot(self, coords, speed, projectile_speed, player, screen):
        self.current_attack_damage=1
        self.check_if_in_line_with_player_and_shoot(projectile_speed, player, screen)        
        if not self.stop_moving:
            self.follow_path(coords, speed)
    
    # Checks to see if player is directly facing the monster and fires a projectile
            
    def check_if_in_line_with_player_and_shoot(self, projectile_speed, player, screen, rot=False, SRK_paralyze = False):

        # If stop moving is already true, the projectile is midflight, so it continues to shoot with the same end destination
        # If stop moving is false, the monster should be moving

        if (self.stop_moving):
            self.shoot_straight(projectile_speed, screen)

        # Checks to see if the player is directly facing the monster

        elif ((abs(player.player_rectangle.centery-self.monster_rectangle.centery)<=player.player_rectangle.height/2 or abs(player.player_rectangle.centerx-self.monster_rectangle.centerx)<=self.monster_rectangle.width/2) or SRK_paralyze) and not self.stop_moving:
            now = pygame.time.get_ticks()
            
            # Sets the projectile's new end destination as the player's updated location
            
            self.projectile.shoot_coords=(player.player_rectangle.centerx, player.player_rectangle.centery)

            # Calculates the time interval between when it last shot a projectile as an shooting cooldown to make it easier for player

            if now - self.last_fired >= Constants.monster_attack_cooldown_count or self.first_time_shooting:
                self.last_fired = now
                self.stop_moving=True
                self.realign_projectile()
                if rot:
                    self.projectile.rotate_towards_player(player)
                self.shoot_straight(projectile_speed, screen)
                self.first_time_shooting=False

        # Checks to see if projectile is at edge of screen

        if self.projectile.projectile_rectangle.x<=0 or self.projectile.projectile_rectangle.x>=Constants.screen_width or self.projectile.projectile_rectangle.y<=0 or self.projectile.projectile_rectangle.y>=Constants.screen_height:
            if SRK_paralyze:
                return True
            # If stop moving is false, the monster can stop shooting and continue patrolling/following its path

            self.stop_moving=False
            self.realign_projectile()
      

        if self.projectile.projectile_rectangle.colliderect(player.player_rectangle):
            if SRK_paralyze:
                return True
        
    # Shoots a projectile in the direction of shoot_coords, which is the projectile's end destination
    
    def walk_towards_player_and_shoot(self, player, speed, projectile_speed, screen, rot=False, SRK_paralyze = False):
        self.current_attack_damage=1
        self.check_if_in_line_with_player_and_shoot(projectile_speed, player, screen, rot, SRK_paralyze)        
        if not self.stop_moving:
            self.move_towards_player(player, speed, screen)

    def shoot_straight(self, speed, screen):

        self.current_attack_damage=1
        
        # Distance formula stuff to calculate movement vectors for projectile

        distance = [self.projectile.shoot_coords[0] - self.monster_rectangle.x, self.projectile.shoot_coords[1] - self.monster_rectangle.y]
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        if norm==0:
            norm = 1
        direction = [distance[0] / norm, distance[1 ] / norm]
        movement_vector = [direction[0] * speed, direction[1] * speed]
        self.projectile.projectile_rectangle.move_ip(movement_vector[0], movement_vector[1])
        self.projectile.render(self.projectile.projectile_rectangle.x, self.projectile.projectile_rectangle.y, screen)

    
    def render(self, x_pos:float, y_pos:float, height:int, width:int, screen:pygame.display) -> None:
        
        image = pygame.transform.scale(self.img, (width, height))
        if self.attacked:
            elapsedTime = time.time() - self.attacktime
            if elapsedTime > 0.25:
                self.attacked = False
            if elapsedTime % 0.1 <= 0.05:
                image = pygame.transform.scale(self.attackimg, (width, height))
        self.monster_rectangle = image.get_rect()
        self.monster_rectangle.topleft = (x_pos, y_pos)
        #pygame.draw.rect(screen, (0,255,0), self.monster_rectangle)
        screen.blit(image, self.monster_rectangle)
    
    def get_hit(self, damage:float):
        
        self.health-=damage
        self.attacked = True
        self.attacktime = time.time()
        if self.health<=0:
            self.die()


    def die(self) -> None:  

        # Implement die here
        self.alive = False

        #have a 50% chance to drop a ladoo
