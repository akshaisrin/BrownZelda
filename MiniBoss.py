from Monster import *

class MiniBoss(Monster):

    def __init__(self, attack_power:float, health:float, img:str, mini_boss_name):
        super().__init__(attack_power, health, img, "Mini Boss")
        self.mini_boss_name=mini_boss_name
        

    