from pygame import image as image
from MediumBoss import *
import os
import Constants
import Overworld
from Obstacles import *

class SRK(MediumBoss):
    def __init__(self, attack_power: float, health: float, img, medium_boss_name: str, start_pos_x: int, start_pos_y: int, height: int, width: int, attacks, proj_img, proj_height, proj_width):
        img=pygame.image.load(os.path.join("Assets", "SRK_sprite.png"))
        super().__init__(attack_power, health, img, "SRK", start_pos_x, start_pos_y, height, width, attacks, proj_img, proj_height, proj_width)
        self.paralyze_cooldown_started=False
        self.in_paralyze_cooldown=False
        self.paralyze_cooldown_timer = pygame.time.get_ticks()
        self.paralyze_cooldown_count = 5000
        self.start_paralyze = True
        self.paralyzing = False
        self.post_paralyze_cooldown_count = 3000
        self.post_paralyze_cooldown_timer = pygame.time.get_ticks()
        self.in_post_paralyze_cooldown = False
        self.last_charged = pygame.time.get_ticks()
        self.add_burnie = False
        self.burnies_added = False
        self.og_health = health
        self.shoot_count = 0

    def paralyze_cooldown_over(self):
        now = pygame.time.get_ticks()
        if now - self.paralyze_cooldown_timer >= self.paralyze_cooldown_count:
            self.in_paralyze_cooldown=False
            return True
        return False

    def post_paralyze_cooldown_over(self):
        now = pygame.time.get_ticks()
        if now - self.post_paralyze_cooldown_timer >= self.post_paralyze_cooldown_count:
            self.in_post_paralyze_cooldown=False
            return True
        return False
    
    def paralyze(self, player:Player2):
        player.is_paralyzed = True
        if self.paralyze_cooldown_over():
            player.is_paralyzed = False
            self.in_post_paralyze_cooldown = True
            self.paralyzing = False
            self.post_paralyze_cooldown_timer = pygame.time.get_ticks()


    def attack(self, player, screen):
        if not self.in_paralyze_cooldown and not self.in_post_paralyze_cooldown and not self.paralyzing:
            self.walk_towards_player_and_shoot(player, Constants.SRK_speed, Constants.SRK_projectile_speed, screen)

        if self.health== self.og_health//2 and self.burnies_added == False:
            self.add_burnie = True
            print("add_burnie is True")
            self.burnies_added = True

        if self.start_paralyze and self.check_player_in_line(player):
            self.paralyze_cooldown_timer = pygame.time.get_ticks()
            self.start_paralyze = False
            self.paralyzing = True
            self.shoot_count = 0
        if self.paralyzing:
            self.paralyze(player)
            self.shoot_in_paralyze(player, screen)
        if self.in_post_paralyze_cooldown:
            if self.post_paralyze_cooldown_over():
                self.start_paralyze = True
                self.in_post_paralyze_cooldown = False
                print("post paralyze cooldown is False")
        


    def check_player_in_line(self, player):
        if (abs(player.player_rectangle.centery-self.monster_rectangle.centery)<=player.player_rectangle.height//1.85 or abs(player.player_rectangle.centerx-self.monster_rectangle.centerx)<=self.monster_rectangle.width//1.85) and not self.stop_moving:
            return True
        
    def shoot_in_paralyze(self, player, screen):
        if self.paralyzing:
            if self.walk_towards_player_and_shoot(player, Constants.SRK_speed, Constants.SRK_projectile_speed, screen, True):
                self.shoot_count += 1

            if self.shoot_count >= 2:
                pass

        
        

    