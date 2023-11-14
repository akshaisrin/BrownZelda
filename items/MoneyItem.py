import pygame
import os
from .Item import Item

class MoneyItem(Item):
    def __init__(self) -> None:
        img=pygame.image.load(os.path.join("Assets", "indianruppee.jpeg"))
        super().__init__(img, 1, "Money")
    
    def pickedup(self, player):
        player.money += self.power