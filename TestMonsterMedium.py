from MediumBoss import *
import os

class TestMonsterMedium(MediumBoss):

    def __init__(self, attack_power:float, health:float, test_monster_name:str, start_pos_x:float, start_pos_y:float, height:int, width:int):

        img=pygame.image.load(os.path.join("Assets", "enemy2.png"))
        super().__init__(attack_power, health, img, "Test Monster Medium", start_pos_x, start_pos_y, height, width)
        self.test_monster_name=test_monster_name
    