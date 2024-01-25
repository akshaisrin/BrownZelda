import os
import sys
import pygame
from pygame.locals import *
from Constants import *
from .Screen import Screen
from items.Sword import Sword
from screens.loadingScreens.InitialLoadingScreen import InitialLoadingScreen

#class not in use anymore - was used during testing period
class TestScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)

    def display(self):
        self.screen.fill((255, 255, 255))

        sword = Sword()

        sword.render(300, 300, 55, 55, self.screen)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return "loading"

        return None