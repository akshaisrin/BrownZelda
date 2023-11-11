from MiniBoss import *
import os

class TestMonster(MiniBoss):

    def __init__(self, attack_power:float, health:float, test_monster_name):

        img=pygame.image.load(os.path.join("Assets", "monster1.png"))
        super().__init__(attack_power, health, img, "Test Monster")
        self.test_monster_name=test_monster_name
    