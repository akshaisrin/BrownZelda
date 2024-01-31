import pygame
import sys
import os
import time
from screens.Screen import Screen 

class NewLoadingScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)

        #renders new title screen image
        self.img = pygame.image.load(os.path.join("Assets", "newzeldatitlescreen.png"))
        self.img = pygame.transform.scale(self.img, (self.screen_width, self.screen_height))
        #sets amount of time needed to fade in and out of image * 2.55 because the alpha value is 0-255
        self.transitiontime = 3
        self.fadetime = 1.5
    
    #slowly fades into the image based on the passed in elapsed time
    def display(self, elapsedTime):
        percentage_complete = (elapsedTime / self.transitiontime) * 100

        current_image = pygame.Surface(self.img.get_size())
        current_image.set_alpha(int(percentage_complete))
        current_image.blit(self.img, (0, 0))

        self.screen.fill((0, 0, 0))
        self.screen.blit(current_image, (0, 0))
    
    #slowly fades out of the image based on the passed in elapsed time
    def displayfade(self, elapsedTime):
        percentage_complete = ((elapsedTime + 2) / self.fadetime) * 100

        current_image = pygame.Surface(self.img.get_size())
        current_image.set_alpha(int(255 - percentage_complete))
        current_image.blit(self.img, (0, 0))

        self.screen.fill((0, 0, 0))
        self.screen.blit(current_image, (0, 0))

    
    