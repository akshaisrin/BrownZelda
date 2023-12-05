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
from Overworld import *


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
    
    # first, start default music and loading screen
    # then, have it start fading to black, and cut the music
    # then, pause for a second, and start the chotta bheem music
    # then, quickly have it come to the new screen

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
                    pygame.mixer.music.set_volume(0.2)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
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
    controller_detected=True
    player1 = Player2("bheem", {}, "", 1, 1.2, 3,5,5, "str", 0, 400, 0)
   
    sword = Sword()
    
    overworld = Overworld()
    curr_biome = overworld.test_room
    next_biome = overworld.test_room2
    curr_screen_x_pos = 0

    try:
        joystick=XboxController()
    except:
        controller_detected=False
    # Establishing game loop to keep screen running

    gameLoop = True
    attacktime = None

    direction = None
    framecounter = 0
    firstchange = False
    while gameLoop:
        clock.tick(60)
        framecounter = framecounter + 1
        overworld.obstacles_in_biome(player1, curr_biome)
        
        curr_biome.render(curr_screen_x_pos, player1, screen)
        health_bar_display = font.render('Player Health: ' + str(player1.health_bar), True, Color(0, 0, 0))
        screen.blit(health_bar_display, (1000, 150))
        lives_display = font.render('Lives Remaining: ' + str(player1.lives_remaining), True, Color(0, 0, 0))
        screen.blit(lives_display, (1000, 200))
        
        if curr_biome != None:
            new_biome = overworld.going_to_next_biome(player1, curr_biome, next_biome, curr_screen_x_pos, screen)
            if new_biome != None:
                curr_biome = new_biome
                curr_screen_x_pos = 0
                
            dungeon = overworld.going_to_dungeon(player1, curr_biome, screen)
            if dungeon != None:
                curr_biome = dungeon
                
        monsters_alive = overworld.monster_attack(curr_biome, player1, screen)
        
        
        if sword.attacking:
            elaspedTime = time.time() - attacktime
            if elaspedTime > 0.5:
                sword.attacking = False
            elif elaspedTime > 0.25:
                sword.render(player1.player_rectangle.x + 10 + (100 * elaspedTime), player1.player_rectangle.y + 10 + (100 * elaspedTime), 50, 50, screen)
            else:
                sword.render(player1.player_rectangle.x + 25 - (100 * elaspedTime), player1.player_rectangle.y + 25 - (100 * elaspedTime), 50, 50, screen)
        
        
        # player contorls
        if controller_detected:        
            new_state=(joystick.get_x_axis(), joystick.get_y_axis())

            # player movement with x box controller

        if (new_state[0]<-1*Constants.controller_threshold):
            direction = "left"
            player1.current_frame = 10
        elif (new_state[0]>Constants.controller_threshold):
            direction = "right"
            player1.current_frame = 10
        if (new_state[1]<-1*Constants.controller_threshold):
            direction = "down"
            player1.current_frame = 11
        if (new_state[1]>controller_threshold):
            direction = "up"
            player1.current_frame = 9
        if (joystick.X) and not sword.attacking:
            attacktime = time.time()
            sword.attack(curr_biome.monsters[0])
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:                   
                if event.key == pygame.K_LEFT: 
                    direction = "left"
                    firstchange = True
                elif event.key == pygame.K_RIGHT: 
                    direction = "right"
                    firstchange = True
                elif event.key == pygame.K_UP: 
                    direction = "up"
                    firstchange = True
                elif event.key == pygame.K_DOWN: 
                    direction = "down"
                    firstchange = True
            
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
                elif (event.key == pygame.K_SPACE) and not sword.attacking:
                     attacktime = time.time()
                     sword.attack(curr_biome.monsters[0])
            
            if event.type == pygame.QUIT:
                gameLoop=False
                pygame.quit()
                sys.exit()

        player1.handlemove(direction, framecounter, firstchange)
        firstchange = False
        
        pygame.display.update()
        
# init_loading_screen()
# init_instructions_screen()
init_home_screen()