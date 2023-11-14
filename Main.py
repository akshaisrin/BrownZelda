import os
import pygame
from pygame.locals import *
from Constants import *
from TestMonster import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
screen.fill((255,255,255))
pygame.display.update()


def init_home_screen():

    monster1=TestMonster(10.0, 9.0, "Test Monster 1", 100, 100)

    monster1.render(100, 100, 200, 200, screen)
    #monster1.shoot(screen)
    pygame.display.update()

    # Establishing game loop to keep screen running

    gameLoop = True
    
    while gameLoop:
        #monster1.shoot(screen)
        #pygame.display.update()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameLoop=False

init_home_screen()