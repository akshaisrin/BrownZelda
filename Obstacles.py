import pygame
import os
from Constants import *

class Obstacles():
    
    def __init__(self, file_path:str):
        self.file_path = file_path
    
    def get_image(self):
        img = pygame.image.load(os.path.join("Assets/obstacles", self.file_path))
        image = pygame.transform.scale(img, (screen_width, screen_height))
        return image
    
    def render(self, screen:pygame.display):
        image = self.get_image()
        screen.blit(image, (0, 0))