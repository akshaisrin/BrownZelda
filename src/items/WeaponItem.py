import pygame
from items.Item import Item

class WeaponItem(Item):
    def __init__(self, img, power, item_type) -> None:
        self.attacking = False
        super().__init__(img, power, item_type)
        self.weapon_rectangle=self.img.get_rect()
        self.weapon_rectangle.topleft = (0, 0)
    
    def attack(self, monster):
        self.attacking = True
        if (self.weapon_rectangle.colliderect(monster.monster_rectangle)):
            #print("attack went through")
            monster.get_hit(self.power)

    def render(self, x_pos:float, y_pos:float, height, width, screen:pygame.display):
        image = pygame.transform.scale(self.img, (height, width))    
        self.weapon_rectangle = image.get_rect()
        self.weapon_rectangle.topleft = (x_pos, y_pos)
        # pygame.draw.rect(screen, (255, 255, 0), self.player_rectangle)
        screen.blit(image, self.weapon_rectangle)

