import pygame
import os
from Room import *
from Constants import *
from Biome import *
from Player import *

class Overworld(Room):
    
    def __init__(self):
        super().__init__(0, 0, 0)
        
        # intialize all the biomes
        self.desert = Biome("desert", "desert_biome.png", 1210, 300)
        self.graveyard = Biome("graveyard", "graveyard_biome.jpg", 1210, 300)
        self.homes = Biome("homes", "homes_biome.png", 1210, 300)
        self.tundra = Biome("tundra", "tundra_biome.png", 1165, 225)
        self.zelda = Biome("zelda", "zelda_biome.png", 1210, 300)
        
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
        
    # def going_to_dungeon(self, player:Player, biome_name:str, screen:pygame.display):
    #     biome = self.biome_name_to_biome(biome_name)
    #     if (player.x_pos < biome.exit_x + 10 and player.x_pos > biome.exit_x - 10) and (player.y_pos < biome.exit_y + 10 and player.y_pos > biome.exit_y - 10):
    #         img = pygame.image.load(os.path.join("Assets", "dungeon1.jpg"))
    #         image = pygame.transform.scale(img, (screen_width, screen_height))
    #         screen.blit(image, (0, 0))
    #         pygame.display.update()
    #         player.x_pos = 0 # change to location of dungeon
    #         player.y_pos = 0 # change to location of dungeon
    #         player.z_pos = -1
    #         print(image)
    #         return image
    #     return None
    
    # def going_to_next_biome(self, player:Player, screen_end_x_pos:float, screen_end_y_pos:float, biomes:list, biomes_order:list, screen:pygame.display):
    #     if player.x_pos == screen_end_x_pos and player.y_pos == screen_end_y_pos:
    #         player.x_pos = 0 # change to location of next room
    #         player.y_pos = 0 # change to location of room
    #         self.display_biome(biomes[biomes_order[0]], screen)
    #         del biomes_order[0]
    #     return biomes_order        
        