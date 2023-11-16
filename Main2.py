import os
import sys
import time
import pygame
from screens.LoadingScreen import LoadingScreen
from screens.TestScreen import TestScreen

pygame.init()

# Set up screen dimensions
screen_width, screen_height = 1500, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brown Zelda (But Not Garbage)")

pygame.mixer.music.load(os.path.join("Assets", "originalzeldatitlemusic.mp3"))  
pygame.mixer.music.set_volume(0.5)

def init_home_screen():
    current_screen = LoadingScreen(screen)
    loadingscreenstarttime = time.time()

    pygame.mixer.music.play(-1)
    
    gameLoop = True
    loadingScreenDone = False
    testScreenStarted = False
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif loadingScreenDone and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 0 <= x <= 1500 and 0 <= y <= 800:
                    current_screen = TestScreen(screen)
                    testScreenStarted = True

        if not loadingScreenDone:
            elapsedTime = time.time() - loadingscreenstarttime
            if elapsedTime > 5:
                loadingScreenDone = True
            current_screen.display(elapsedTime)
        if testScreenStarted:
            current_screen.display()
        pygame.display.update()

    pygame.quit()
    sys.exit()


init_home_screen()