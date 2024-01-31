import pygame
import sys
import os
import time
from screens.Screen import Screen 

class InitialLoadingScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)

        #renders originalzelda title screen image
        self.img = pygame.image.load(os.path.join("Assets", "originalzeldatitlescreen.jpeg"))
        self.img = pygame.transform.scale(self.img, (self.screen_width, self.screen_height))

        #amount of time needed to fade out of the image * 2.55 because the alpha value is 0-255
        self.transitiontime = 4
    
    def display(self, elapsedTime):
        #slowly fades out of the image based on the passed in elapsed time
        percentage_complete = (elapsedTime / self.transitiontime) * 100

        current_image = pygame.Surface(self.img.get_size())
        current_image.set_alpha(int(255 - percentage_complete))
        current_image.blit(self.img, (0, 0))

        #screen is basically being filled with black and then the image is being blitted on top of it
        #image is slowly being faded from its true color
        self.screen.fill((0, 0, 0))
        self.screen.blit(current_image, (0, 0))

    
    