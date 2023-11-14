import pygame
import sys

class Screen:
    def __init__(self, screen):
        self.screen_height = 800
        self.screen_width = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
    
