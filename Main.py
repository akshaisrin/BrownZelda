import os
import pygame
import sys
from pygame.locals import *
from Constants import *
from TestMonster import *
from Player import *
from Overworld import *

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
        player1.render(player1.x_pos,player1.y_pos, 300, 300, screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
         
            # checking if keydown event happened or not, updating direction accordingly, and then calling move function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("move left")
                    player1.direction = "left"
                    player1.move()

                elif event.key == pygame.K_RIGHT:
                    print("right")
                    player1.direction = "right"
                    player1.move()

                elif event.key == pygame.K_UP:
                    print("up")
                    player1.direction = "up"
                    player1.move()

                elif event.key == pygame.K_DOWN:
                    print("down")
                    player1.direction = "down"
                    player1.move()

        pygame.display.update()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameLoop=False

init_home_screen()