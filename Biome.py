import pygame
import os
from Constants import *
from Obstacles import *
from Player2 import *
from Monster import *
from items.Ladoo import *
from items.Ingredient import *
from Auntieji import *
from items.Key import *

class Biome():
    
    def __init__(self, name:str, file_path:str, exits:list, text:list, last_room:bool=False, new_level_x:int=None, new_level_y:int=None):
        self.name = name
        self.file_path = file_path
        self.exits = exits # list of exit objects
        self.last_room = last_room # whether the room is the last in the level
        self.new_level_x = new_level_x # where the player should start after transitioning to next level (x position)
        self.new_level_y = new_level_y # where the player should start after transitioning to next level (y position)
        self.obstacles = [] # store obstacles that you don't want shown on screen (just used for collision with player)
        self.obstacles_rect = []
        self.obstacles_with_img = [] # store obstacles that you want to show on the screen
        self.key_obstacles = []
        self.key_obstacles_rect = []
        self.combined_obstacle_rects = []
        self.monsters = []
        self.monstersremoved = []
        self.items = []
        self.keys = []
        self.text = text
    
    
    # get the image for the room (which is needed for rendering)
    def get_image(self):
        if self.name != "game_over":
            img = pygame.image.load(os.path.join("Assets/rooms", self.file_path))
        else:
            img = pygame.image.load(os.path.join("Assets", self.file_path))
        image = pygame.transform.scale(img, (screen_width, screen_height))
        return image
    
    
    # render the image, items, keys, and obstacles for the room
    def render(self, x_pos:int, y_pos:int, player:Player2, screen:pygame.display):
        
        # render the room image
        image = self.get_image()
        screen.blit(image, (x_pos, y_pos))
        
        # render the obstacles
        for o in self.obstacles_with_img:
            screen.blit(o.get_image(), (o.x, o.y))
            
        # render the items
        for i in self.items:
            i.render(screen)
            
        # render the keys
        for i in self.keys:
            i.render(screen)
            
    
    # render the player and monsters for the room
    def render_characters(self, player:Player2, screen:pygame.display):
        
        # render the monsters
        for m in self.monsters:
            if m.alive:
                # if isinstance(m, Auntieji):
                #     if m.are_clones:       
                m.attack(player, screen)
                #m.patrol_and_shoot(player, 500, 300, 500, 500, screen)
                #m.charge_and_hit(player)
                #m.start_moving(player)
                m.render(m.monster_rectangle.x, m.monster_rectangle.y, m.height,m.width, screen)
                #m.shoot(screen, player)
            else:
                if m not in self.monstersremoved:
                    continue
                if random.randint(0, 9) > 5:
                    self.add_items(1, m.monster_rectangle.x, m.monster_rectangle.y)
                self.monstersremoved.remove(m)
                
        # render player
        if self.name != "game_over":
            player.render(player.player_rectangle.topleft[0], player.player_rectangle.topleft[1], screen)

    
    # get obstacle rect
    def get_obstacle_rect(self, o):
        rect = o.get_image().get_rect()
        rect[0] = o.x
        rect[1] = o.y
        return rect        
    
    # add obstacles and their rects that don't want to be shown to the room
    def add_obstacles(self, obstacles:list):
        for o in obstacles:
            self.obstacles.append(o)
            rect = self.get_obstacle_rect(o)
            self.obstacles_rect.append(rect) 
        self.combined_obstacle_rects = self.obstacles_rect
            
    # add obstacles and their rects that should be shown to the room
    def add_obstacles_with_img(self, obstacles_with_img:list, screen):
        for o in obstacles_with_img:
            self.obstacles_with_img.append(o)
            rect = self.get_obstacle_rect(o)
            self.obstacles_rect.append(rect)
        self.combined_obstacle_rects = self.obstacles_rect
    
    # add obstacles for places where there is a lock preventing the player from exiting the room
    def add_key_obstacles(self, obstacles:list):
        for o in obstacles:
            self.key_obstacles.append(o)
            rect = self.get_obstacle_rect(o)
            self.key_obstacles_rect.append(rect)
        self.combined_obstacle_rects = self.obstacles_rect + self.key_obstacles_rect   
            
    def add_monsters(self, monsters:list):
        self.monsters += monsters
        
    def add_exits(self, exits:list):
        # Combines the list of exits
        self.exits += exits
        

    def add_items(self, amount, x_pos = None, y_pos = None):
        for i in range(amount):
            if x_pos == None and y_pos == None or not self.is_valid_spawn(x_pos, y_pos):
                while True:
                    x_pos = random.randint(0, 1500)
                    y_pos = random.randint(0, 800)
                    if self.is_valid_spawn(x_pos, y_pos):
                        self.items.append(Ladoo(x_pos, y_pos))
                        break
            self.items.append(Ladoo(x_pos, y_pos))
    
    def add_ingredient(self, ingredient):
        self.items.append(ingredient)

    def is_valid_spawn(self, x_pos, y_pos):
        for obstacle in self.obstacles_rect:
            if obstacle.colliderect((x_pos, y_pos, 100, 100)):
                return False
        return True
    
    def add_key(self, key):
        print("Added a key")
        self.keys.append(key)
        