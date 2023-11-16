import os
import pygame
from pygame.locals import *
from Constants import *
from TestMonster import *
<<<<<<< HEAD
from Player import *
=======
from Overworld import *
>>>>>>> ef3b685 (Added code for testing Overworld & Biome class #15)

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
screen.fill((255,255,255))
pygame.display.update()


def init_home_screen():

<<<<<<< HEAD
    monster1=TestMonster(10.0, 9.0, "Test Monster 1", 800, 100)
    player1 = Player("bheem", {}, "", 1, 1.2, 5,5,5, "str", 500, 500, 0)
=======
    monster1=TestMonster(10.0, 9.0, "Test Monster 1", 100, 100)

    monster1.render(100, 100, 200, 200, screen)
    #monster1.shoot(screen)
    pygame.display.update()
    
    """
    # testing Overworld class
    overworld = Overworld()
    overworld.display_biome("desert", screen)
    pygame.display.update()
    """
>>>>>>> ef3b685 (Added code for testing Overworld & Biome class #15)

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