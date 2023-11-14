import pygame
from Item import Item

class WeaponItem(Item):
    def __init__(self, img, power, item_type) -> None:
        super().__init__(img, power, item_type)
    
    def use(self, monster):
        monster.get_hit(self.power)
