import pygame
import os
from items.Item import Item

#standard item class - just renders ingredients, most of functionality taken care of elsewhere
class Ingredient(Item):
    def __init__(self, file_path, x_pos, y_pos) -> None:
        ingredientimg=pygame.image.load(os.path.join("Assets", file_path))
        self.x_pos = x_pos
        self.y_pos = y_pos
        #adjust the item rectangle to the xpos and ypos
        self.item_rectangle = ingredientimg.get_rect()
        self.item_rectangle[0] = self.x_pos
        self.item_rectangle[1] = self.y_pos
        self.used = False
        super().__init__(ingredientimg, 1, "ingredient")

    def render(self, screen:pygame.display) -> None:
        if self.used:
            return
        image = pygame.transform.scale(self.img, (48, 48))
        screen.blit(image, (self.x_pos, self.y_pos))
    
    
    
