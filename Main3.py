import os
import pygame
from pygame.locals import *
from Constants import *
from Overworld import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
screen.fill((255,255,255))
pygame.display.update()


def init_home_screen():
    
    overworld = Overworld()        
    overworld.display_biome("desert", screen)
    
    pygame.time.delay(2000)
    overworld.game_over(screen)
    
    # Establishing game loop to keep screen running
    gameLoop = True
    while gameLoop:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False


init_home_screen()