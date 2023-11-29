import os
import pygame
from pygame.locals import *
from Constants import *
from Overworld import *
import random
from Player import *


pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
screen.fill((255,255,255))
pygame.display.update()


def init_home_screen():
    
    """
    # initialize all variables
    biomes = ["desert", "homes", "tundra", "zelda"]
    biomes_order = [0, 1, 2, 3]
    random.shuffle(biomes_order)
    """
    
    overworld = Overworld()
    curr_biome = overworld.test_room
    next_biome = overworld.test_room2
    
    player1 = Player("bheem", {}, "", 1, 1.2, 5,5,5, "str", 0, 400, 0)
    
    # curr_biome = biomes[biomes_order[0]]
    curr_screen_x_pos = 0
    # starting_filepath = curr_biome + "_biome.png"
    # img = pygame.image.load(os.path.join("Assets/biomes", starting_filepath))
    # image = pygame.transform.scale(img, (screen_width, screen_height))
    # del biomes_order[0]
    
    gameLoop = True
    attacktime = None
    pressed_left=False
    pressed_right=False
    pressed_up=False
    pressed_down=False
    
    # Establishing game loop to keep screen running
    gameLoop = True
    
    while gameLoop:
        
        overworld.obstacles_in_biome(player1, curr_biome)
        
        curr_biome.render(curr_screen_x_pos, player1, screen)
        
        if curr_biome != None:
            
            new_biome = overworld.going_to_next_biome(player1, curr_biome, next_biome, curr_screen_x_pos, screen)
            if new_biome != None:
                curr_biome = new_biome
                curr_screen_x_pos = 0
                
            dungeon = overworld.going_to_dungeon(player1, curr_biome, screen)
            if dungeon != None:
                curr_biome = dungeon
        
        
        # player controls
        
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

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameLoop=False


init_home_screen()
