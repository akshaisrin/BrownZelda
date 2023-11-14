import pygame

class Item:
    def __init__(self, img:str, power:float, item_type:str) -> None:
        self.img = img
        self.power = power
        self.item_type = item_type

    def render(self, x_pos:float, y_pos:float, height, width, screen:pygame.display):
        image = pygame.transform.scale(self.img, (height, width))
        screen.blit(image, (x_pos, y_pos))



