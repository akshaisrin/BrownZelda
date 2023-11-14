import pygame
from Item import Item

class HealingItem(Item):
    def __init__(self, img, power, item_type) -> None:
        super().__init__(img, power, item_type)
    
    def use(self, player):
        player.health += self.power
    
    
    
