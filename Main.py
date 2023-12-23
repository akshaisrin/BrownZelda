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
from Obstacle import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
screen.fill((255,255,255))
pygame.display.update()
font = pygame.font.Font('freesansbold.ttf', 32)

def init_home_screen():
    controller_detected=True
    monster2=TestMonster(10.0, 9.0, "Test Monster 1", 800, 100, 250, 300)
    #monster2=TestMonsterMedium(10.0, 9.0, "Test Monster 2", 500, 100, 250, 300)

    player1 = Player("bheem", {}, "", 1, 1.2, 3,5,5, "str", 500, 500, 0)
   
    sword = Sword()

    try:
        joystick=XboxController()
    except:
        controller_detected=False
    # Establishing game loop to keep screen running

    gameLoop = True
    attacktime = None
    pressed_left=False
    pressed_right=False
    pressed_up=False
    pressed_down=False

    while gameLoop:
        
        screen.fill((255,255,255))
        #pygame.draw.rect(screen, (255, 0, 255), player1.player_rectangle)
        health_bar_display = font.render('Player Health: ' + str(player1.health_bar), True, Color(0, 0, 0))
        screen.blit(health_bar_display, (1200, 100))

        lives_display = font.render('Lives Remaining: ' + str(player1.lives_remaining), True, Color(0, 0, 0))
        screen.blit(lives_display, (1200, 150))
        # monster1.render(800, 100, 250, 300, screen)        
        # monster1.shoot(screen)
        
        if monster2.alive:
            #monster2.patrol(player1, 500, 200, 500, 500)
            
            monster2.render(monster2.monster_rectangle.x, monster2.monster_rectangle.y, 250, 300, screen)
            
            #monster2.shoot(screen, player1)
            if (player1.player_rectangle.colliderect(monster2.projectile.projectile_rectangle)):
                print("player got hit")
                #monster2.realign_projectile()
                player1.get_attacked(monster2.projectile.damage, screen)
            
            if sword.attacking:
                elaspedTime = time.time() - attacktime
                if elaspedTime > 0.5:
                    sword.attacking = False
                elif elaspedTime > 0.25:
                    sword.render(player1.player_rectangle.x + 75 + (100 * elaspedTime), player1.player_rectangle.y + 75 + (100 * elaspedTime), 50, 50, screen)
                else:
                    sword.render(player1.player_rectangle.x + 100 - (100 * elaspedTime), player1.player_rectangle.y + 100 - (100 * elaspedTime), 50, 50, screen)

            # obj1 = Obstacle("washington.jpeg", 0, 0,"irrelevant")
            # obj1.render(200, 200, screen)  
        player1.render(player1.player_rectangle.x,player1.player_rectangle.y, 300, 300, screen)
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

            if event.type == pygame.KEYDOWN:                   
                if event.key == pygame.K_LEFT:        
                    pressed_left = True
                elif event.key == pygame.K_RIGHT:     
                    pressed_right = True
                elif event.key == pygame.K_UP:        
                    pressed_up = True
                elif event.key == pygame.K_DOWN:     
                    pressed_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pressed_left = False
                elif event.key == pygame.K_RIGHT:
                    pressed_right = False
                elif event.key == pygame.K_UP: 
                    pressed_up = False
                elif event.key == pygame.K_DOWN:
                     pressed_down = False
                elif (event.key == pygame.K_SPACE) and not sword.attacking:
                     print("attack")
                     attacktime = time.time()
                     sword.attack(monster2)
            
            if event.type == pygame.QUIT:
                gameLoop=False
                pygame.quit()
                sys.exit()

        if pressed_left:
            player1.direction = "left"
            player1.move() 

        if pressed_right:
            player1.direction = "right"
            player1.move() 

        if pressed_up:
            player1.direction = "up"
            player1.move()
        
        if pressed_down:
            player1.direction = "down"
            player1.move() 
        
        pygame.display.update()

init_home_screen()




