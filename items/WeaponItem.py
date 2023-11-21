import pygame
from items.Item import Item

class WeaponItem(Item):
    def __init__(self, img, power, item_type) -> None:
        self.attacking = False
        super().__init__(img, power, item_type)
    
    def attack(self, player, monster):
        self.attacking = True
        if ((abs(player.x_pos - monster.x_pos) <= 100) and (abs(player.y_pos - monster.y_pos) <= 100)):
            print("attack went through")
            monster.get_hit(self.power)

    def render(self, x_pos:float, y_pos:float, height, width, screen:pygame.display):
        image = pygame.transform.scale(self.img, (height, width))
        screen.blit(image, (x_pos, y_pos))
