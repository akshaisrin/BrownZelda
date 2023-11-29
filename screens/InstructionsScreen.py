import pygame
import sys
import os
import time
from screens.Screen import Screen 

class InstructionsScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)

        self.img = pygame.image.load(os.path.join("Assets", "prologuescreen.png"))
        print(self.img.get_height())
        self.img = pygame.transform.scale(self.img, (self.screen_width, int(self.img.get_height())))
        

        self.img_x = 0
        self.img_y = 0
        
        self.scrolltime = 66
        self.screen_height = -2064
        self.fadetime = 1.5
    
    def display(self, elapsedTime):
        percentage_complete = elapsedTime / self.scrolltime
        self.img_y = self.screen_height * percentage_complete

        self.screen.blit(self.img, (self.img_x, self.img_y))
        
    def displayfade(self, elapsedTime):
        percentage_complete = (elapsedTime  / self.fadetime) * 100

        current_image = pygame.Surface(self.img.get_size())
        current_image.set_alpha(int(255 - percentage_complete))
        current_image.blit(self.img, (0, 0))

        self.screen.fill((0, 0, 0))
        self.screen.blit(current_image, (self.img_x, self.img_y))

    
    