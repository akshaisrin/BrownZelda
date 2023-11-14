import os
import sys
import pygame
from pygame.locals import *
from Constants import *
from TestMonster import *
from items.MoneyItem import MoneyItem
from screens.LoadingScreen import LoadingScreen

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
screen.fill((255,255,255))
pygame.display.update()


image = pygame.image.load("./Assets/washington.jpeg")

def init_home_screen():

    monster1=TestMonster(10.0, 9.0, "Test Monster 1", 100, 100)

    monster1.render(100, 100, 200, 200, screen)
    monster2.render(300, 300, 300, 300, screen)

    # item1 = Item(image)
    # item1.render(400, 400, 50, 50, screen)

    money = MoneyItem()
    money.render(200, 200, 75, 75, screen)

    pygame.display.update()

    # Establishing game loop to keep screen running

    gameLoop = True
    
    while gameLoop:
        #monster1.shoot(screen)
        #pygame.display.update()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameLoop=False

        pygame.display.update()

    pygame.quit()
    sys.exit()


init_home_screen()