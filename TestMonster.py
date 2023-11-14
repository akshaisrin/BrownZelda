from MiniBoss import *
import os

class TestMonster(MiniBoss):

    def __init__(self, attack_power:float, health:float, test_monster_name:str, start_pos_x, start_pos_y):

        img=pygame.image.load(os.path.join("Assets", "monster1.png"))
        super().__init__(attack_power, health, img, "Test Monster", start_pos_x, start_pos_y)
        self.test_monster_name=test_monster_name
    