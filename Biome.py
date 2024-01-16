import pygame
import os
from Room import *
from Constants import *
from Obstacles import *
from Player2 import *
from Monster import *
from items.Ladoo import *
from items.Ingredient import *

class Biome(Room):
    
    def __init__(self, name:str, file_path:str, exits:list, text:list, last_room:bool=False, new_level_x:int=None, new_level_y:int=None):
        super().__init__(0, 0, 0)
        self.name = name
        self.file_path = file_path
        self.exits = exits # list of exit objects
        self.last_room = last_room # whether the room is the last in the level
        self.new_level_x = new_level_x # where the player should start after transitioning to next level (x position)
        self.new_level_y = new_level_y # where the player should start after transitioning to next level (y position)
        self.obstacles = []
        self.obstacles_rect = []
        self.monsters = []
        self.items = []
        self.keys = []
        self.text = text
    
    def get_image(self):
        img = pygame.image.load(os.path.join("Assets/rooms", self.file_path))
        image = pygame.transform.scale(img, (screen_width, screen_height))
        return image
    
    def render(self, x_pos:int, y_pos:int, player:Player2, screen:pygame.display):
        # render the screen
        image = self.get_image()
        screen.blit(image, (x_pos, y_pos))
        # render the obstacles
        #for o in self.obstacles:
            #screen.blit(o.get_image(), (o.x, x_pos + o.y))
        # render the player
        # render the monsters
        for m in self.monsters:
            if m.alive:
                m.attack(player, screen)
                #m.patrol_and_shoot(player, 500, 300, 500, 500, screen)
                #m.charge_and_hit(player)
                #m.start_moving(player)
                m.render(m.monster_rectangle.x, m.monster_rectangle.y, m.height,m.width, screen)

                #m.shoot(screen, player)
            else:
                if random.randint(0, 9) > 5:
                    self.add_items(1, m.monster_rectangle.x, m.monster_rectangle.y)
                self.monsters.remove(m)

        for i in self.items:
            i.render(screen)

        for i in self.keys:
            i.render(screen)

        player.render(player.player_rectangle.topleft[0],player.player_rectangle.topleft[1], screen)
        
    def add_obstacles(self, obstacles:list):
        for o in obstacles:
            self.obstacles.append(o)
            rect = o.get_image().get_rect()
            rect[0] = o.x
            rect[1] = o.y
            self.obstacles_rect.append(rect)
            
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
    
    def add_ingredient(self, x_pos, y_pos):
        self.items.append(Ingredient(x_pos, y_pos))

    def is_valid_spawn(self, x_pos, y_pos):
        for obstacle in self.obstacles_rect:
            if obstacle.colliderect((x_pos, y_pos, 100, 100)):
                return False
        return True
    
    def add_key(self, key):
        self.keys.append(key)