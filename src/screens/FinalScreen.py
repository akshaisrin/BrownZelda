import pygame
import sys
import os
import time
from screens.Screen import Screen 

class FinalScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)

        self.img = pygame.image.load(os.path.join("Assets", "endingscreen.png"))
        self.img = pygame.transform.scale(self.img, (self.screen_width, int(self.img.get_height())))
        

        self.img_x = 0
        self.img_y = 0
        
        #time needed to scroll through the image        
        self.scrolltime = 66
        self.screen_height = -2064
        #time needed to fade in and out of image * 2.55 because the alpha value is 0-255
        self.fadetime = 1.5
    
    #slowlly scrolls through the image based on the passed in elapsed time
    def display(self, elapsedTime):
        percentage_complete = elapsedTime / self.scrolltime
        self.img_y = self.screen_height * percentage_complete

        self.screen.blit(self.img, (self.img_x, self.img_y))
    
    #slowly fades out of the image based on the passed in elapsed time
    def displayfade(self, elapsedTime):
        percentage_complete = (elapsedTime  / self.fadetime) * 100

        current_image = pygame.Surface(self.img.get_size())
        current_image.set_alpha(int(255 - percentage_complete))
        current_image.blit(self.img, (0, 0))

        self.screen.fill((0, 0, 0))
        self.screen.blit(current_image, (self.img_x, self.img_y))
    
    #slowly fades into the image based on the passed in elapsed time
    def displayfadein(self, elapsedTime):
        percentage_complete = (elapsedTime  / self.fadetime) * 100

        current_image = pygame.Surface(self.img.get_size())
        current_image.set_alpha(int(percentage_complete))
        current_image.blit(self.img, (0, 0))

        self.screen.fill((0, 0, 0))
        self.screen.blit(current_image, (self.img_x, self.img_y))

    
    