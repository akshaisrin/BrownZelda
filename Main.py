import os
import pygame
import sys
from pygame.locals import *
from Constants import *
from TestMonster import *
from TestMonsterMedium import *
from inputs import get_gamepad
from XBoxController import *
from Player import *
from items.Sword import Sword
import time

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
screen.fill((255,255,255))
pygame.display.update()

def init_home_screen():
    controller_detected=True
    #monster1=TestMonster(10.0, 9.0, "Test Monster 1", 800, 100, 250, 300)
    monster2=TestMonsterMedium(10.0, 9.0, "Test Monster 2", 500, 100, 250, 300)


    player1 = Player("bheem", {}, "", 1, 1.2, 5,5,5, "str", 500, 500, 0)

    sword = Sword()

    try:
        joystick=XboxController()
    except:
        controller_detected=False

    # Establishing game loop to keep screen running

    gameLoop = True
    attacktime = None
    
    while gameLoop:
        
        screen.fill((255,255,255))
        #monster1.render(800, 100, 250, 300, screen)
        #monster1.shoot(screen)
        if monster2.alive:
            monster2.render(500, 100, 250, 300, screen)
        # monster2.shoot(screen, player1)

        player1.render(player1.x_pos,player1.y_pos, 300, 300, screen)
        if sword.attacking:
            elaspedTime = time.time() - attacktime
            if elaspedTime > 0.5:
                sword.attacking = False
            elif elaspedTime > 0.25:
                sword.render(player1.x_pos + 75 + (100 * elaspedTime), player1.y_pos + 75 + (100 * elaspedTime), 50, 50, screen)      
            else:
                sword.render(player1.x_pos + 100 - (100 * elaspedTime), player1.y_pos + 100 - (100 * elaspedTime), 50, 50, screen)      
            


        if controller_detected:
            new_state=(joystick.get_x_axis(), joystick.get_y_axis())
            
            # player movement with x box controller

            if (new_state[0]<-1*Constants.controller_threshold):
                print("move left")
                player1.direction = "left"
                player1.move()
                
            if (new_state[0]>Constants.controller_threshold):
                print("move right")
                player1.direction = "right"
                player1.move()

            if (new_state[1]<-1*Constants.controller_threshold):
                print("move down")
                player1.direction = "down"
                player1.move()
            
            if (new_state[1]>controller_threshold):
                print("move up")
                player1.direction = "up"
                player1.move()   
     
        for event in pygame.event.get():

            # checking if keydown event happened or not, updating direction accordingly, and then calling move function (arrow keys)
            
            if (event.type == pygame.KEYDOWN):
                print("button pressed")
                if (event.key == pygame.K_LEFT):
                    print("move left")
                    player1.direction = "left"
                    player1.move()   
                    
                elif (event.key == pygame.K_RIGHT):
                    print("right")
                    player1.direction = "right"
                    player1.move()   
                    
                elif (event.key == pygame.K_UP):
                    print("up")
                    player1.direction = "up"
                    player1.move()   
                
                elif (event.key == pygame.K_DOWN):
                    print("down")
                    player1.direction = "down"
                    player1.move()   
                elif (event.key == pygame.K_SPACE) and not sword.attacking:
                    print("attack")
                    attacktime = time.time()
                    sword.attack(player1, monster2)
            
            if event.type == pygame.QUIT:
                gameLoop=False
                pygame.quit()
                sys.exit()
            
        pygame.display.update()

init_home_screen()