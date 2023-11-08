import os
import pygame
from pygame.locals import *
from Constants import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
screen.fill((255,255,255))
pygame.display.update()

background_img=pygame.image.load(os.path.join("Images", "title_screen.jpg"))

def init_home_screen():

    gameLoop = True

    # Establishing game loop to keep screen running

    while gameLoop:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameLoop=False

init_home_screen()