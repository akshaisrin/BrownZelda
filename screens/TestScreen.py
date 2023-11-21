import os
import sys
import pygame
from pygame.locals import *
from Constants import *
from TestMonster import *
from .Screen import Screen
from items.MoneyItem import MoneyItem
from screens.loadingScreens.InitialLoadingScreen import InitialLoadingScreen

class TestScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)

    def display(self):
        self.screen.fill((255, 255, 255))
        monster1=TestMonster(10.0, 9.0, "Test Monster 1", 300, 300)
        monster2=TestMonster(10.0, 9.0, "Test Monster 2", 100, 100)

        monster1.render(100, 100, 200, 200, self.screen)
        monster2.render(300, 300, 300, 300, self.screen)

        money = MoneyItem()
        money.render(200, 200, 75, 75, self.screen)  

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return "loading"

        return None