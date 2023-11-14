import pygame

class Projectile:

    def __init__(self,damage:float, x_pos:float, y_pos:float, img:pygame.image):
        self.damage=damage
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.img=img
    

    def render(self, height:int, width:int, x:float, y:float, screen:pygame.display):
        self.x_pos=x
        self.y_pos=y
        
        image = pygame.transform.scale(self.img, (height, width))
        screen.blit(image, (self.x_pos, self.y_pos))