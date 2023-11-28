import pygame
import os
from Room import *
from Constants import *
from Biome import *
from Player import *
from Obstacles import *

class Overworld(Room):
    
    def __init__(self):
        super().__init__(0, 0, 0)
        
        # intialize all obstacles
        self.desert_obstacle = Obstacles("obstacle_test.png")
        
        # intialize all the biomes
        self.desert = Biome("desert", "desert_biome.png", 1200, 500, True, 500, 400)
        self.homes = Biome("homes", "homes_biome.png", 1200, 500, True, 500, 400)
        self.tundra = Biome("tundra", "tundra_biome.png", 1200, 500, True, 500, 400)
        self.zelda = Biome("zelda", "zelda_biome.png", 1200, 500, True, 500, 400)
        
    def biome_name_to_biome(self, biome_name:str):
        if biome_name == "desert":
            return self.desert
        elif biome_name == "graveyard":
            return self.graveyard
        elif biome_name == "homes":
            return self.homes
        elif biome_name == "tundra":
            return self.tundra
        else:
            return self.zelda
    
    def display_biome(self, biome_name:str, screen:pygame.display):
        biome = self.biome_name_to_biome(biome_name)
        biome.render(screen)
        pygame.display.update()
        
    def game_over(self, screen:pygame.display):
        img = pygame.image.load(os.path.join("Assets", "game_over_screen.jpg"))
        image = pygame.transform.scale(img, (screen_width, screen_height))
        screen.blit(image, (0, 0))
        pygame.display.update()
        
    # NOTE: NEED TO CHANGE THE CODE BELOW TO ACCEPT AN ACTUAL DUNGEON OBJECT AS A PARAMETER AND USE THAT OBJECT'S PICTURE & EXIT POSITIONS
    def going_to_dungeon(self, player, biome_name:str, screen:pygame.display):
        biome = self.biome_name_to_biome(biome_name)
        if biome.dungeon:
            if (player.x_pos < biome.dungeon_x + 10 and player.x_pos > biome.dungeon_x - 10) and (player.y_pos < biome.dungeon_y + 10 and player.y_pos > biome.dungeon_y - 10):
                img = pygame.image.load(os.path.join("Assets", "dungeon1.jpg"))
                image = pygame.transform.scale(img, (screen_width, screen_height))
                screen.fill((0, 0, 0))
                pygame.display.update()
                pygame.time.wait(500)
                for i in range(30, 1, -2):
                    screen.blit(image, (int((screen_width - screen_width/i)/2), 0), (int((screen_width - screen_width/i)/2), 0, int(screen_width/i), screen_height))
                    pygame.display.update()
                    pygame.time.wait(100)
                player.x_pos = 1200
                player.y_pos = 215
                player.z_pos = -1
                return image
        return None
    
    def going_to_next_biome(self, player, biomes:list, biomes_order:list, biome_name:str, curr_image, curr_screen_x_pos:int, screen:pygame.display):    
        curr_biome = self.biome_name_to_biome(biome_name)
        next_biome = self.biome_name_to_biome(biomes[biomes_order[0]])
        if (player.x_pos < curr_biome.exit_x + 10 and player.x_pos > curr_biome.exit_x - 10) and (player.y_pos < curr_biome.exit_y + 10 and player.y_pos > curr_biome.exit_y - 10):
            del biomes_order[0]
            image = next_biome.get_image()
            x_pos = screen_width
            while x_pos > 0:
                curr_screen_x_pos -= 100
                screen.blit(curr_image, (curr_screen_x_pos, 0))
                x_pos -= 100
                screen.blit(image, (x_pos, 0))
                if x_pos > 0:
                    player.x_pos -= 100
                else:
                    player.x_pos = -100
                player.render(player.x_pos, player.y_pos, 300, 300, screen)
                pygame.display.update()
                pygame.time.wait(10)
            return (image, biomes_order)
        return (None, biomes_order)
        