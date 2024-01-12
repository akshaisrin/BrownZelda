import pygame
import os

class Key:
    def __init__(self, biomeunlock, x_pos, y_pos, k_x_pos, k_y_pos) -> None:
        self.img = pygame.image.load(os.path.join("Assets", "key.png"))
        self.biomeunlock = biomeunlock
        self.start_x_pos = x_pos
        self.start_y_pos = y_pos
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.k_x_pos = k_x_pos
        self.k_y_pos = k_y_pos
        self.key_rectangle = self.img.get_rect()
        self.key_rectangle[0] = x_pos
        self.key_rectangle[1] = y_pos
        self.pickedup = False
        self.used = False

    def render(self, screen:pygame.display):
        if self.pickedup:
            return
        image = pygame.transform.scale(self.img, (64, 64))
        screen.blit(image, (self.x_pos, self.y_pos))