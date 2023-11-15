import os
import pygame
from pygame.locals import *
from Constants import *
from TestMonster import *
from Player import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
screen.fill((255,255,255))
pygame.display.update()


def init_home_screen():

    monster1=TestMonster(10.0, 9.0, "Test Monster 1", 800, 100)
    player1 = Player("bheem", {}, "", 1, 1.2, 5,5,5, "str", 500, 500, 0)

    # Establishing game loop to keep screen running

    gameLoop = True
    
    while gameLoop:
        screen.fill((255,255,255))
        monster1.render(800, 100, 200, 200, screen)
        monster1.shoot(screen)
        player1.render(player1.x_pos,player1.y_pos, 100, 100, screen)
        
        pygame.display.update()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameLoop=False

init_home_screen()