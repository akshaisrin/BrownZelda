import pygame
import os
from items.Item import Item

#healing item class - just renders ladoos, most of functionality taken care of elsewhere
class Ladoo(Item):
    def __init__(self, x_pos, y_pos) -> None:
        ladooimg=pygame.image.load(os.path.join("Assets", "ladoo.png"))
        self.x_pos = x_pos
        self.y_pos = y_pos
        #adjust the item rectangle to the xpos and ypos
        self.item_rectangle = ladooimg.get_rect()
        self.item_rectangle[0] = self.x_pos
        self.item_rectangle[1] = self.y_pos
        self.used = False
        super().__init__(ladooimg, 1, "healing")
    
    def use(self, player):
        self.used = True
        player.health += self.power

    def render(self, screen:pygame.display) -> None:
        if self.used:
            return
        image = pygame.transform.scale(self.img, (48, 48))
        screen.blit(image, (self.x_pos, self.y_pos))
    
    
    
