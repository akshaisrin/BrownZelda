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
from Player import *
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
    controller_detected=True
    #monster1=TestMonster(10.0, 9.0, "Test Monster 1", 800, 100, 250, 300)

    player1 = Player("bheem", {}, "", 1, 1.2, 3,5,5, "str", 0, 400, 0)
   
    sword = Sword()
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
    pressed_left=False 
    pressed_right=False
    pressed_up=False
    pressed_down=False

    while gameLoop:
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
                sword.render(player1.player_rectangle.x + 75 + (100 * elaspedTime), player1.player_rectangle.y + 75 + (100 * elaspedTime), 50, 50, screen)
            else:
                sword.render(player1.player_rectangle.x + 100 - (100 * elaspedTime), player1.player_rectangle.y + 100 - (100 * elaspedTime), 50, 50, screen)
        
        
        # player contorls
        if controller_detected:        
            new_state=(joystick.get_x_axis(), joystick.get_y_axis())

            # player movement with x box controller

        if (new_state[0]<-1*Constants.controller_threshold):
            player1.direction = "left"
            player1.move()
            
        if (new_state[0]>Constants.controller_threshold):
            player1.direction = "right"
            player1.move()
        
        if (new_state[1]<-1*Constants.controller_threshold):
            player1.direction = "down"
            player1.move()

        if (new_state[1]>controller_threshold):
            player1.direction = "up"
            player1.move()   

        if (joystick.X) and not sword.attacking:
            attacktime = time.time()
            sword.attack(curr_biome.monsters[0])
    
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
                     attacktime = time.time()
                     sword.attack(curr_biome.monsters[0])
            
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
        
init_loading_screen()
init_instructions_screen()
init_home_screen()