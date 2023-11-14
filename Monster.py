import pygame
from Projectile import *
import os
import time
class Monster:

    def __init__(self, attack_power:float, health:float, img:pygame.image, monster_type:str, start_pos_x:int, start_pos_y:int):

        self.attack_power=attack_power
        self.health=health
        self.img=img
        self.x_pos=start_pos_x
        self.y_pos=start_pos_y
        self.monster_type=monster_type
    
    def shoot(self, screen) -> None:
        
        img=pygame.image.load(os.path.join("Assets", "fireball.png"))
        projectile = Projectile(10, self.x_pos+2, self.y_pos, img)
        projectile.render(50, 50, self.x_pos+4, self.y_pos, screen)
        
          
    def render(self, x_pos:float, y_pos:float, height:int, width:int, screen:pygame.display) -> None:
        self.x_pos=x_pos
        self.y_pos=y_pos

        image = pygame.transform.scale(self.img, (height, width))
        screen.blit(image, (x_pos, y_pos))

        print(f"Monster: {self.monster_type} has been rendered at position ({x_pos}, {y_pos})")

    def start_moving(self) -> None:
        
        # Implement start_moving here

        print(f"Monster: {self.monster_type} has been begun moving")
    
    def get_hit(self, damage:float):
        
        self.health-=damage

        if self.health<=0:
            self.die()

    def die(self) -> None:  

        # Implement die here

        print(f"Monster: {self.monster_type} has been killed") 


