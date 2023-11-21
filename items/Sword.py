import pygame
import os
from items.WeaponItem import WeaponItem

class Sword(WeaponItem):
    def __init__(self) -> None:
        img=pygame.image.load(os.path.join("Assets", "washington.jpeg"))
        super().__init__(img, 2.5, "weapon")
    
