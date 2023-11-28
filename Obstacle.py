import pygame

class Obstacle:
    def __init__(self, img:str, x_pos:float, y_pos:float, item_type:str) -> None:
        self.img = img
        self.item_type = item_type
        self.x = x_pos
        self.y = y_pos

    def render(self, height, width, screen:pygame.display):
        image = pygame.transform.scale(self.img, (height, width))
        screen.blit(image, (self.x, self.y))

    def is_collided(self, player_x, player_y):
        if player_x in range(self.x -15, self.x +15) and player_y in range(self.y -15, self.y + 15):
            return True
