import pygame
import sys
import os
import time
from .Screen import Screen 

class LoadingScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)

        self.originaltitlescreenimg = pygame.image.load(os.path.join("Assets", "originalzeldatitlescreen.jpeg"))
        self.newtitlescreenimg = pygame.image.load(os.path.join("Assets", "newzeldatitlescreen.png"))

        self.originaltitlescreenimg = pygame.transform.scale(self.originaltitlescreenimg, (self.screen_height, self.screen_width))
        self.newtitlescreenimg = pygame.transform.scale(self.newtitlescreenimg, (self.screen_height, self.screen_width))

        self.transitiontime = 5
    
    def display(self, elapsedTime):
        percentage_complete = (elapsedTime / self.transitiontime) * 100

        current_image = pygame.Surface(self.originaltitlescreenimg.get_size())
        current_image.set_alpha(int(255 - percentage_complete))
        current_image.blit(self.originaltitlescreenimg, (0, 0))

        self.screen.fill((255, 255, 255))
        self.screen.blit(current_image, (0, 0))

    
    