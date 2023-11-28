import pygame
import os

class Obstacles():
    
    def __init__(self, file_path:str):
        self.file_path = file_path
    
    def get_image(self):
        image = pygame.image.load(os.path.join("Assets/obstacles", self.file_path))
        return image
    
    def render(self, screen:pygame.display):
        image = self.get_image()
        screen.blit(image, (0, 0))