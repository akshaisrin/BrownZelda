from MediumBoss import *
import os
import Constants
from AuntieClone import *
class Auntieji(MediumBoss):
    def __init__(self, attack_power:float, health:float, test_monster_name:str, height:int, width:int, start_pos_x:float, start_pos_y:float):

        img=pygame.image.load(os.path.join("Assets", "auntiji_mediumBoss.png"))
        super().__init__(attack_power, health, img, "Auntie Ji", start_pos_x, start_pos_y, height, width, ["charge_and_hit", "shoot_attack"])
        self.test_monster_name=test_monster_name

        # Fields for charge attack

        self.charge_speed=2.25

        # Post-charge attack cooldown duration

        self.cooldown=Constants.cooldown
        self.in_cooldown=False
        self.started_charging=True

        # Coords monster will charge towards

        self.charge_coords=(0, 0)

        #self.patrol_constant=Constants.kohli_patrol_constant

        self.projectile.damage=2
        self.projectile_constant=Constants.kohli_projectile_constant
        self.current_attack=""
        self.exclamation=pygame.image.load(os.path.join("Assets", "exclamationmark.png"))
        self.exclamation=pygame.transform.scale(self.exclamation, (25, 25))

        self.are_clones = False

def clone(self, player, screen):
    #there are now clones
    self.are_clones = True
    #determine auntie clones locations 100 px away from player.
    ac1_x, ac1_y = float(player.player_rectangle.x), float(player.player_rectangle.y - 100)
    ac2_x, ac2_y = player.player_rectangle.x + 100, player.player_rectangle.y
    ac3_x, ac3_y = player.player_rectangle.x -100, player.player_rectangle.y
    self.monster_rectangle.x, self.monster_rectangle.y = player.player_rectangle.x, player.player_rectangle.y + 100


    clone1 = AuntieClone(5.0, 35.0, "auntieclone1.png", "auntie_clone1", ac1_x, ac1_y, 100, 100)
    clone1.render(ac1_x, ac1_y, 100, 100, screen)

