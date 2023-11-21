import pygame
import sys
import os
import time
from screens.Screen import Screen 

class InstructionsScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)

        self.img = pygame.image.load(os.path.join("Assets", "tempinstructionspage.png"))
        self.img = pygame.transform.scale(self.img, (int(self.img.get_height()), self.screen_width))

        self.img_x = 0
        self.img_y = 0
        
        self.scroll_speed = -0.5
    
    def display(self):
        self.img_y += self.scroll_speed

        self.screen.blit(self.img, (self.img_x, self.img_y))
        

    
    