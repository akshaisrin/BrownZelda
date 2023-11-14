import os
import sys
import pygame
from pygame.locals import *
from Constants import *
from TestMonster import *
from items.MoneyItem import MoneyItem
from screens.LoadingScreen import LoadingScreen

class TestScreen:
    def __init__(self):
        super().__init__()

    def display(self):
        monster1=TestMonster(10.0, 9.0, "Test Monster 1")
        monster2=TestMonster(10.0, 9.0, "Test Monster 2")

        monster1.render(100, 100, 200, 200, self.screen)
        monster2.render(300, 300, 300, 300, self.screen)

        money = MoneyItem()
        money.render(200, 200, 75, 75, self.screen)
    
    def get_screen(self):
        return self.screen        
