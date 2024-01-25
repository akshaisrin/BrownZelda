from MiniBoss import *
import os

class CricketNPC(MiniBoss):

    def __init__(self, attack_power:float, health:float, test_monster_name:str, start_pos_x:float, start_pos_y:float, main_attack:str):
        
        img=pygame.image.load(os.path.join("Assets", "cricketer" + str(random.randint(1,10)) + ".png"))
        super().__init__(attack_power, health, img, "Cricket NPC", start_pos_x, start_pos_y, 125, 75, "cricket_ball.png", 25, 25, "shoot and follow path")
        self.test_monster_name=test_monster_name
        self.main_attack=main_attack
    
    # Main attack function for mini boss

    def attack(self, player, screen):

        # Monster can only attack if it is not in a cooldown

        if not self.in_hit_cooldown:

            # There are three main attacks a typical monster can have, each corresponding to a different function
            # A mini boss is only assigned one of the three attacks

            if self.main_attack=="shoot and follow path":
                
                self.follow_path_and_shoot(self.path_coords, Constants.npc_cricker_player_speed, Constants.npc_cricker_player_projectile_speed, player, screen)

            elif self.main_attack=="shoot and patrol":
                self.patrol_and_shoot(player, Constants.npc_cricker_player_speed, Constants.npc_cricker_player_projectile_speed, self.patrol_distance, self.patrol_direction, screen)
            else:
                
                self.move_towards_player(player,Constants.npc_cricker_player_speed, screen)
        
        # This manages the hit cooldown and sets it to false if the timer is up

        if self.in_hit_cooldown:
            now = pygame.time.get_ticks()
            
            if now - self.last_hit>= self.hit_cooldown_count:
                self.in_hit_cooldown=False