import pygame

class Projectile:

    def __init__(self,damage:float, x_pos:float, y_pos:float, height:int, width:int, img:pygame.image):
        self.damage=damage
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height=height
        self.width=width
        self.img=img
        self.img=pygame.transform.scale(self.img, (self.height, self.width))
        self.projectile_rectangle=self.img.get_rect()
        self.projectile_rectangle.topleft = (x_pos, y_pos)

    def render(self, x:float, y:float, screen:pygame.display):
        # self.x_pos=x
        # self.y_pos=y
        
        # screen.blit(self.img, (self.x_pos, self.y_pos))
    
        # screen.blit(image, (x_pos, y_pos))
        self.projectile_rectangle.x = x
        self.projectile_rectangle.y = y
        #pygame.draw.rect(screen, (0, 255, 0), self.projectile_rectangle)
        screen.blit(self.img, self.projectile_rectangle)


    