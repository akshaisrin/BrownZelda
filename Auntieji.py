from MediumBoss import *
import os
from Constants import *
from AuntieClone import *
class Auntieji(MediumBoss):
    def __init__(self, attack_power:float, health:float, test_monster_name:str, height:int, width:int, start_pos_x:float, start_pos_y:float):

        img=pygame.image.load(os.path.join("Assets", "auntiji_mediumBoss.png"))
        super().__init__(attack_power, health, img, "Auntie Ji", start_pos_x, start_pos_y, height, width, ["charge_and_hit", "shoot_attack"], "auntie_chapal (2).png", 50, 60)
        self.test_monster_name=test_monster_name
        self.og_health = health

        #cooldown variables
        self.cooldown=Constants.auntieji_cooldown
        self.in_cooldown=False
        self.started_charging=True

        self.projectile.damage=2
        self.projectile_constant=Constants.auntie_projectile_speed
        self.are_clones = False
        self.clone_happened = False
    
    #auntie has one main attack, other being cloning ability
    def attack(self, player, screen):
        self.walk_towards_player_and_shoot(player, Constants.auntie_speed, Constants.auntie_projectile_speed, screen)

        #turn on clones when auntie is half dead
        if self.health== self.og_health//2 and self.clone_happened == False:
            self.are_clones = True
            self.clone_happened = True


