from Monster import *

class MiniBoss(Monster):

    def __init__(self, attack_power:float, health:float, img:pygame.image, mini_boss_name:str, start_pos_x:int, start_pos_y:int):
        super().__init__(attack_power, health, img, "Mini Boss", start_pos_x, start_pos_y)
        self.mini_boss_name=mini_boss_name