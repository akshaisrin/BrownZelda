import pygame

class Monster:

    def __init__(self, attack_power:float, health:float, img:str, monster_type):

        self.attack_power=attack_power
        self.health=health
        self.img=img
        self.monster_rectangle=self.img.get_rect()
        self.monster_rectangle.x=0
        self.monster_rectangle.y=0
        self.monster_type=monster_type
    
    def attack(self) -> None:
    
        # Implement once player object has been created

        print("Attacking player")
    
    def render(self, x_pos:float, y_pos:float, height, width, screen:pygame.display) -> None:

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


