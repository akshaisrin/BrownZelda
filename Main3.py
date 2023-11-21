import os
import pygame
from pygame.locals import *
from Constants import *
from Overworld import *
import json
import random

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
screen.fill((255,255,255))
pygame.display.update()


def init_home_screen():
    
    # initialize all variables
    biomes = ["desert", "homes", "tundra", "zelda"]
    biomes_order = [0, 1, 2, 3]
    random.shuffle(biomes_order)
    overworld = Overworld()
    img = pygame.image.load(os.path.join("Assets", "player_sprite_test.png"))
    player1 = Player("bheem", {}, "", 1, 1.2, 5,5,5, "str", 500, 500, 0)
    
    curr_biome = biomes[biomes_order[0]]
    starting_filepath = curr_biome + "_biome.png"
    img = pygame.image.load(os.path.join("Assets/biomes", starting_filepath))
    image = pygame.transform.scale(img, (screen_width, screen_height))
    del biomes_order[0]
    
    
    # Establishing game loop to keep screen running
    gameLoop = True
    
    while gameLoop:

        screen.blit(image, (0, 0))
        player1.render(player1.x_pos,player1.y_pos, 300, 300, screen)
        
        new_image = overworld.going_to_dungeon(player1, curr_biome, screen)
        if new_image != None:
            print(new_image)
            image = new_image
            

            
        #biomes_order = overworld.going_to_next_biome(player1, 650, 500, biomes, biomes_order, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
         
            # checking if keydown event happened or not, updating direction accordingly, and then calling move function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("move left")
                    player1.direction = "left"
                    player1.move()

                elif event.key == pygame.K_RIGHT:
                    print("right")
                    player1.direction = "right"
                    player1.move()

                elif event.key == pygame.K_UP:
                    print("up")
                    player1.direction = "up"
                    player1.move()

                elif event.key == pygame.K_DOWN:
                    print("down")
                    player1.direction = "down"
                    player1.move()
                print(player1.x_pos)
                print(player1.y_pos)
        
        pygame.display.update()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameLoop=False


init_home_screen()