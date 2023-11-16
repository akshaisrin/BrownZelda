import pygame
import os
from Room import *
from Constants import *
from Biome import *

class Overworld(Room):
    
    def __init__(self):
        super().__init__(0, 0, 0)
        
        # intialize all the biomes
        self.desert = Biome("desert", "desert_biome.png")
        self.graveyard = Biome("graveyard", "graveyard_biome.jpg")
        self.homes = Biome("homes", "homes_biome.png")
        self.tundra = Biome("tundra", "tundra_biome.png")
        self.zelda = Biome("zelda", "zelda_biome.png")
    
    def display_biome(self, biome_name:str, screen:pygame.display):
        if biome_name == "desert":
            self.desert.render(screen)
        elif biome_name == "graveyard":
            self.graveyard.render(screen)
        elif biome_name == "homes":
            self.homes.render(screen)
        elif biome_name == "tundra":
            self.tundra.render(screen)
        else:
            self.zelda.render(screen)
        pygame.display.update()
        
    def game_over(self, screen:pygame.display):
        img = pygame.image.load(os.path.join("Assets", "game_over_screen.jpg"))
        image = pygame.transform.scale(img, (screen_width, screen_height))
        screen.blit(image, (0, 0))
        pygame.display.update()