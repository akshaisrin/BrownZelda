import pygame
import os
from items.WeaponItem import WeaponItem

#this class is for the sword weapon - not in use anymore, feature scrapped for time
class Sword(WeaponItem):
    def __init__(self, item_type= None) -> None:
        image = pygame.image.load(os.path.join("Assets", "sword.jpg"))
        super().__init__(image, 2.5, "weapon")

