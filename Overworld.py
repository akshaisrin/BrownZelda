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
        self.desert = Biome("desert", "desert_biome.png", 1200, 500)
        self.graveyard = Biome("graveyard", "graveyard_biome.jpg", 1200, 500)
        self.homes = Biome("homes", "homes_biome.png", 1200, 500)
        self.tundra = Biome("tundra", "tundra_biome.png", 1200, 500)
        self.zelda = Biome("zelda", "zelda_biome.png", 1200, 500)
        
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
<<<<<<< HEAD
        
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
=======
    
    def going_to_dungeon(self, player:Player, biome_name:str, screen:pygame.display):
        biome = self.biome_name_to_biome(biome_name)
        if (player.x_pos < biome.exit_x + 10 and player.x_pos > biome.exit_x - 10) and (player.y_pos < biome.exit_y + 10 and player.y_pos > biome.exit_y - 10):
            img = pygame.image.load(os.path.join("Assets", "dungeon1.jpg"))
            image = pygame.transform.scale(img, (screen_width, screen_height))
            screen.blit(image, (0, 0))
            pygame.display.update()
            player.x_pos = 0 # change to location of dungeon
            player.y_pos = 0 # change to location of dungeon
            player.z_pos = -1
            return image
        return None
    
    def going_to_next_biome(self, player:Player, biomes:list, biomes_order:list, biome_name:str, curr_image, curr_screen_x_pos:int, screen:pygame.display):    
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
                    player.x_pos = 0
                player.render(player.x_pos, player.y_pos, 300, 300, screen)
                pygame.display.update()
                pygame.time.wait(100)
            return (image, biomes_order)
        return (None, biomes_order)
>>>>>>> 5f2cb67 (Transition between biomes - screen loads slowly. #29)
        