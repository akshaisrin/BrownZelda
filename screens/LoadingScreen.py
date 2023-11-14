import pygame
import sys
from .Screen import Screen 

class LoadingScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        font = pygame.font.Font(None, 36)
        self.text = font.render("Loading...", True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))

    def display(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.text, self.text_rect)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return "test"

        return None
    
    