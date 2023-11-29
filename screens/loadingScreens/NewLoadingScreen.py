import pygame
import sys
import os
import time
from screens.Screen import Screen 

class NewLoadingScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)

        self.img = pygame.image.load(os.path.join("Assets", "newzeldatitlescreen.png"))
        self.img = pygame.transform.scale(self.img, (self.screen_width, self.screen_height))
        self.transitiontime = 3
        self.fadetime = 1.5
    
    def display(self, elapsedTime):
        percentage_complete = (elapsedTime / self.transitiontime) * 100

        current_image = pygame.Surface(self.img.get_size())
        current_image.set_alpha(int(percentage_complete))
        current_image.blit(self.img, (0, 0))

        self.screen.fill((0, 0, 0))
        self.screen.blit(current_image, (0, 0))
    
    def displayfade(self, elapsedTime):
        percentage_complete = ((elapsedTime + 2) / self.fadetime) * 100

        current_image = pygame.Surface(self.img.get_size())
        current_image.set_alpha(int(255 - percentage_complete))
        current_image.blit(self.img, (0, 0))

        self.screen.fill((0, 0, 0))
        self.screen.blit(current_image, (0, 0))

    
    