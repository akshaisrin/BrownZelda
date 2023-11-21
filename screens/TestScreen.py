import os
import sys
import pygame
from pygame.locals import *
from Constants import *
from TestMonster import *
from TestMonsterMedium import TestMonsterMedium
from .Screen import Screen
from items.MoneyItem import MoneyItem
from items.Sword import Sword
from screens.loadingScreens.InitialLoadingScreen import InitialLoadingScreen

class TestScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)

    def display(self):
        self.screen.fill((255, 255, 255))
        monster2=TestMonsterMedium(10.0, 9.0, "Test Monster 2", 500, 100, 250, 300)

        monster2.render(300, 300, 300, 300, self.screen)

        sword = Sword()

        money = MoneyItem()
        money.render(200, 200, 75, 75, self.screen)  
        sword.render(300, 300, 55, 55, self.screen)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return "loading"

        return None