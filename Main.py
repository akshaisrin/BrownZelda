import os
import pygame
from pygame.locals import *
from Constants import *
from TestMonster import *
from inputs import get_gamepad
import math
import threading
from XBoxController import *

pygame.init()


screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
screen.fill((255,255,255))
pygame.display.update()

def test_x_box_controller():
    joystick = XboxController()
    while True:
        print(joystick.get_a_button())

def init_home_screen():

    monster1=TestMonster(10.0, 9.0, "Test Monster 1", 800, 100, 250, 300)

    # Establishing game loop to keep screen running

    gameLoop = True
    
    while gameLoop:
        screen.fill((255,255,255))
        monster1.render(800, 100, 250, 300, screen)
        monster1.shoot(screen)
        pygame.display.update()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameLoop=False

#init_home_screen()
test_x_box_controller()