import pygame
import os
from Room import *
from Constants import *
from Obstacles import *
from Player import *
from Monster import *

class Biome(Room):
    
    def __init__(self, name:str, file_path:str, exit_x:int, exit_y:int, dungeon:bool=False, dungeon_x=None, dungeon_y=None):
        super().__init__(0, 0, 0)
        self.name = name
        self.file_path = file_path
        self.exit_x = exit_x
        self.exit_y = exit_y
        self.dungeon = dungeon
        self.dungeon_x = dungeon_x
        self.dungeon_y = dungeon_y
        self.obstacles = []
        self.obstacles_rect = []
        self.monsters = []
    
    def get_image(self):
        img = pygame.image.load(os.path.join("Assets/biomes", self.file_path))
        image = pygame.transform.scale(img, (screen_width, screen_height))
        return image
    
    def render(self, x_pos:int, player:Player, screen:pygame.display):
        # render the screen
        image = self.get_image()
        screen.blit(image, (0, x_pos))
        # render the obstacles
        # for o in self.obstacles:
        #     screen.blit(o.get_image(), (o.x, x_pos + o.y))
        # render the player
        # render the monsters
        for m in self.monsters:
            if m.alive:
                m.render(500, 100, 250, 300, screen)
                m.shoot(screen, player)
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
            