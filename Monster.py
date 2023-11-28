import pygame
from Projectile import *
import os
class Monster:

    def __init__(self, attack_power:float, health:float, img:pygame.image, monster_type:str, start_pos_x:int, start_pos_y:int, height:int, width:int):

        self.attack_power=attack_power
        self.health=health
        self.height=height
        self.width=width
        self.img=img
        self.img=pygame.transform.scale(self.img, (self.height, self.width))
        self.x_pos=start_pos_x
        self.y_pos=start_pos_y
        self.monster_type=monster_type
        self.projectile = Projectile(10, self.x_pos+2, self.y_pos, 50, 50, pygame.image.load(os.path.join("Assets", "flappybird.png")))
        self.alive = True
        self.monster_rectangle=self.img.get_rect()
        self.monster_rectangle.topleft = (start_pos_x, start_pos_x)
    
    def shoot(self, screen:pygame.display) -> None:
        if self.projectile.x_pos<=0:
            self.projectile.x_pos=self.x_pos-2

        self.projectile.x_pos+=-1.5
        self.projectile.render(self.projectile.x_pos, self.projectile.y_pos, screen)
    
          
    def render(self, x_pos:float, y_pos:float, height:int, width:int, screen:pygame.display) -> None:
        # self.x_pos=x_pos
        # self.y_pos=y_pos

        image = pygame.transform.scale(self.img, (width, height))
        self.monster_rectangle = image.get_rect()
        self.monster_rectangle.topleft = (x_pos, y_pos)
        # pygame.draw.rect(screen, (0, 0, 255), self.monster_rectangle)
        screen.blit(image, self.monster_rectangle)
    
    def get_hit(self, damage:float):
        
        self.health-=damage

        if self.health<=0:
            self.die()

    def die(self) -> None:  

        # Implement die here
        self.alive = False

        print(f"Monster: {self.monster_type} has been killed") 
