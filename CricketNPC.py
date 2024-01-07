from MiniBoss import *
import os

class CricketNPC(MiniBoss):

    def __init__(self, attack_power:float, health:float, test_monster_name:str, start_pos_x:float, start_pos_y:float, height:int, width:int, main_attack:str):
        
        img=pygame.image.load(os.path.join("Assets", "cricketer" + str(random.randint(1,10)) + ".png"))
        super().__init__(attack_power, health, img, "Cricket NPC", start_pos_x, start_pos_y, height, width, "cricket_ball.png", 25, 25)
        self.test_monster_name=test_monster_name
        self.main_attack=main_attack
    
    def attack(self, player, screen):
        if self.main_attack=="shoot":

            #self.patrol_and_shoot(player, 700, 500, 900, 500, Constants.npc_cricker_player_projectile_speed, screen)
            #self.patrol(Constants.npc_cricker_player_speed, 500, 'x')
            coords=[(self.start_pos_x, self.start_pos_y), (self.start_pos_x+450, self.start_pos_y), (self.start_pos_x+450, self.start_pos_y+450), (self.start_pos_x, self.start_pos_y+450)]
            self.follow_path_and_shoot(coords, Constants.npc_cricker_player_speed, Constants.npc_cricker_player_projectile_speed, player, screen)
            #self.follow_path(coords, Constants.npc_cricker_player_speed)

        else:
           
            self.move_towards_player(player,Constants.npc_cricker_player_speed)