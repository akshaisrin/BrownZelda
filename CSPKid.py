from MiniBoss import *
import os

class CSP_Kid(MiniBoss):

    def __init__(self, attack_power:float, health:float, start_pos_x:float, start_pos_y:float, main_attack:str):
        
        img=pygame.image.load(os.path.join("Assets", "csp_kid_" + str(random.randint(1,3)) + ".png"))
        super().__init__(attack_power, health, img, "CSP Kid", start_pos_x, start_pos_y, 125, 75, "cricket_ball.png", 25, 25, main_attack)
        #self.main_attack=main_attack
    
    def attack(self, player, screen):
        # if not self.in_hit_cooldown:
            
        #     self.move_towards_player(player,Constants.npc_cricker_player_speed, screen)
        
        # if self.in_hit_cooldown:
        #     now = pygame.time.get_ticks()
            
        #     if now - self.last_hit>= self.hit_cooldown_count:
        #         self.in_hit_cooldown=False
        
    
        self.move_towards_player(player,Constants.csp_kid_speed, screen, 0.5)
    
    def check_player_collision(self, player, screen):
        if self.alive:
            if player.player_rectangle.colliderect(self.monster_rectangle) and not player.attacking:
                now = pygame.time.get_ticks()
                if now -self.last_damage >= self.attack_cooldown or self.first_time_attacking:
                    if not self.in_hit_cooldown:
                        self.last_damage = now
                        player.get_attacked(self.current_attack_damage, screen)
                        self.first_time_attacking=False
            elif player.player_rectangle.colliderect(self.monster_rectangle) and player.attacking:
                self.get_hit(player.currentitem.power)                    
                if not self.in_hit_cooldown:
                    self.in_hit_cooldown=True
                    self.last_hit=pygame.time.get_ticks()