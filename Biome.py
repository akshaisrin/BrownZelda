import pygame
import os
from Room import *
from Constants import *
from Obstacles import *

class Biome(Room):
    
    def __init__(self, name:str, file_path:str, exit_x:int, exit_y:int, dungeon:bool=False, dungeon_x=None, dungeon_y=None, obstacle:Obstacles=None):
        super().__init__(0, 0, 0)
        self.name = name
        self.file_path = file_path
        self.exit_x = exit_x
        self.exit_y = exit_y
        self.dungeon = dungeon
        self.dungeon_x = dungeon_x
        self.dungeon_y = dungeon_y
        self.obstacles = obstacle
    
    def get_image(self):
        img = pygame.image.load(os.path.join("Assets/biomes", self.file_path))
        image = pygame.transform.scale(img, (screen_width, screen_height))
        image2 = self.obstacles.get_image()
        return (image, image2)
    
    def render(self, screen:pygame.display):
        image, image2 = self.get_image()
        screen.blit(image, (0, 0))
        screen.blit(image2, (0, 0))
    
    # need to implement function below to ensure the player can't go beyond screen or on places it shouldn't be able to go for each biome
    def borders():
        pass