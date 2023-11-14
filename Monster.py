import pygame
from Projectile import *
import os
class Monster:

    def __init__(self, attack_power:float, health:float, img:pygame.image, monster_type:str, start_pos_x:int, start_pos_y:int):

        self.attack_power=attack_power
        self.health=health
        self.img=img
        self.x_pos=start_pos_x
        self.y_pos=start_pos_y
        self.monster_type=monster_type
        self.projectile = Projectile(10, self.x_pos+2, self.y_pos, 50, 50, pygame.image.load(os.path.join("Assets", "flappybird.png")))

    
    def shoot(self, screen:pygame.display) -> None:
        if self.projectile.x_pos<=0:
            self.projectile.x_pos=self.x_pos-2

        self.projectile.x_pos+=-1.5
        self.projectile.render(self.projectile.x_pos, self.projectile.y_pos, screen)
    
          
    def render(self, x_pos:float, y_pos:float, height:int, width:int, screen:pygame.display) -> None:
        self.x_pos=x_pos
        self.y_pos=y_pos

        image = pygame.transform.scale(self.img, (height, width))
        screen.blit(image, (x_pos, y_pos))

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


