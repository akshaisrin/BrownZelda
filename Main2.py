import os
import sys
import time
import pygame
from screens.loadingScreens.InitialLoadingScreen import InitialLoadingScreen
from screens.loadingScreens.NewLoadingScreen import NewLoadingScreen
from screens.TestScreen import TestScreen
from screens.InstructionsScreen import InstructionsScreen
from pygame.locals import *
from Constants import *
from TestMonster import *
from TestMonsterMedium import *
from inputs import get_gamepad
from XBoxController import *
from Player2 import *
from items.Sword import Sword
from Obstacle import *

pygame.init()

# Set up screen dimensions
screen_width, screen_height = 1500, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
pygame.mixer.init()
font = pygame.font.Font('freesansbold.ttf', 32)
current_screen = None

def init_loading_screen():
    current_screen = InitialLoadingScreen(screen)
    loadingscreenstarttime = time.time()
    pygame.mixer.music.load(os.path.join("Assets", "originalzeldatitlemusic.mp3"))  
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play()
    
    gameLoop = True
    initialLoadingScreenDone = False
    newLoadingScreenDone = False
    instructionsScreenStarted = False
    firstSongSet = False
    secondSongSet = False
    thirdSongSet = False
    fourthSongSet = False
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif newLoadingScreenDone and not instructionsScreenStarted and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load(os.path.join("Assets", "echo.mp3"))  
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play()
                    loadingscreenstarttime = time.time()
                    instructionsScreenStarted = True

        if not initialLoadingScreenDone:
            elapsedTime = time.time() - loadingscreenstarttime
            if elapsedTime > 20:
                initialLoadingScreenDone = True
                current_screen = NewLoadingScreen(screen)
                loadingscreenstarttime = time.time()
                pygame.mixer.music.set_volume(0.7)
            elif elapsedTime > 18 and not thirdSongSet: 
                pygame.mixer.music.set_volume(0.55)
                thirdSongSet = True
            elif elapsedTime > 16 and not secondSongSet:
                pygame.mixer.music.load(os.path.join("Assets", "chottabheemtitlesong.mp3"))  
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)
                secondSongSet = True
            elif elapsedTime > 13 and not fourthSongSet:
                pygame.mixer.music.set_volume(0.15)
                fourthSongSet = True
            elif elapsedTime > 10 and not firstSongSet:
                pygame.mixer.music.set_volume(0.3)
                firstSongSet = True
            elif elapsedTime > 4:
                current_screen.display(elapsedTime - 4)
            else:
                current_screen.display(0)
        elif not newLoadingScreenDone:
            elapsedTime = time.time() - loadingscreenstarttime
            if elapsedTime > 6:
                newLoadingScreenDone = True
            else:
                current_screen.display(elapsedTime)    
        elif instructionsScreenStarted:
            elapsedTime = time.time() - loadingscreenstarttime
            current_screen.displayfade(elapsedTime)
            if elapsedTime > 2:
                gameLoop = False         
        pygame.display.update()


def init_instructions_screen():
    current_screen = InstructionsScreen(screen)
    instructionsscreenstarttime = time.time()

    gameLoop = True
    while gameLoop:
        elapsedTime = time.time() - instructionsscreenstarttime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
        if elapsedTime > 72:
            pygame.mixer.music.stop()
            gameLoop = False
        elif elapsedTime > 68:
            current_screen.displayfade(elapsedTime - 68)
        elif elapsedTime > 65:
            pygame.mixer.music.set_volume(.1)
        else:    
            current_screen.display(elapsedTime)
        pygame.display.update()

def init_home_screen():
    clock = pygame.time.Clock() 
    player1 = Player2("bheem", {}, "", 1, 1.2, 3,5,5, "str", 500, 500, 0)
    gameLoop = True
    direction = None
    framecounter = 0
    while gameLoop:
        clock.tick(60)
        framecounter = framecounter + 1
        screen.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:                   
                if event.key == pygame.K_LEFT: 
                    player1.current_frame = 10
                    direction = "left"
                elif event.key == pygame.K_RIGHT: 
                    player1.current_frame = 10
                    direction = "right"
                elif event.key == pygame.K_UP: 
                    player1.current_frame = 11
                    direction = "up"
                elif event.key == pygame.K_DOWN: 
                    player1.current_frame = 9
                    direction = "down"
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player1.current_frame = 10
                    direction = None
                elif event.key == pygame.K_UP:
                    player1.current_frame = 11
                    direction = None
                elif event.key == pygame.K_DOWN:
                    player1.current_frame = 9
                    direction = None
            
            if event.type == pygame.QUIT:
                gameLoop=False
                pygame.quit()
                sys.exit()

        player1.handlemove(direction, framecounter)
        player1.render(player1.player_rectangle.x, player1.player_rectangle.y, screen)

        pygame.display.update()


# init_loading_screen()
# init_instructions_screen()
init_home_screen()