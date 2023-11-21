import pygame
import os
from Room import *
from Constants import *

class Biome(Room):
    
    def __init__(self, name:str, file_path:str, exit_x, exit_y):
        super().__init__(0, 0, 0)
        self.name = name
        self.file_path = file_path
        self.exit_x = exit_x
        self.exit_y = exit_y
        
    def render(self, screen:pygame.display):
        img = pygame.image.load(os.path.join("Assets/biomes", self.file_path))
        image = pygame.transform.scale(img, (screen_width, screen_height))
        screen.blit(image, (0, 0))
    
    # need to implement function below to ensure the player can't go beyond screen or on places it shouldn't be able to go for each biome
    def borders():
        pass