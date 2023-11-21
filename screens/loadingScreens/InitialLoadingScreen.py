import pygame
import sys
import os
import time
from screens.Screen import Screen 

class InitialLoadingScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)

        self.img = pygame.image.load(os.path.join("Assets", "originalzeldatitlescreen.jpeg"))
        self.img = pygame.transform.scale(self.img, (self.screen_height, self.screen_width))

        self.transitiontime = 4
    
    def display(self, elapsedTime):
        percentage_complete = (elapsedTime / self.transitiontime) * 100

        current_image = pygame.Surface(self.img.get_size())
        current_image.set_alpha(int(255 - percentage_complete))
        current_image.blit(self.img, (0, 0))

        self.screen.fill((0, 0, 0))
        self.screen.blit(current_image, (0, 0))

    
    