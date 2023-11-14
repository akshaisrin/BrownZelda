import os
import sys
import pygame
from screens.LoadingScreen import LoadingScreen
from screens.TestScreen import TestScreen

pygame.init()

# Set up screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brown Zelda (But Not Garbage)")

def init_home_screen():
    current_screen = LoadingScreen(screen)

    gameLoop = True
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 0 <= x <= 800 and 0 <= y <= 600:
                    current_screen = TestScreen(screen)

        current_screen.display()
        pygame.display.update()

    pygame.quit()
    sys.exit()


init_home_screen()