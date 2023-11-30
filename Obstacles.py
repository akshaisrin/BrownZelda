import pygame
import os
from Constants import *

class Obstacles():
    
    def __init__(self, file_path:str, x_pos:int, y_pos:int, width:int, height:int):
        self.file_path = file_path
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height
    
    def get_image(self):
        img = pygame.image.load(os.path.join("Assets/obstacles", self.file_path))
        image = pygame.transform.scale(img, (self.width, self.height))
        return image
    
    def render(self, screen:pygame.display):
        image = self.get_image()
        screen.blit(image, (self.x, self.y))
        