from MediumBoss import *
import os
import Constants

class Kohli(MediumBoss):

    def __init__(self, attack_power:float, test_monster_name:str, start_pos_x:float, start_pos_y:float):

        img=pygame.image.load(os.path.join("Assets", "kohli.png"))
        super().__init__(attack_power, 30, img, "Virat Kohli", start_pos_x, start_pos_y, 150, 125, ["charge_and_hit", "shoot_attack"], "cricket_ball.png", 25, 25)
        self.test_monster_name=test_monster_name

        # Fields for charge attack

        self.charge_speed=10

        # Post-charge attack cooldown duration

        self.cooldown=Constants.cooldown
        self.in_cooldown=False
        self.started_charging=True

        # Coords monster will charge towards

        self.charge_coords=(0, 0)

        #self.patrol_constant=Constants.kohli_patrol_constant

        self.projectile.damage=2
        self.projectile_constant=Constants.kohli_projectile_speed
        self.current_attack="shoot"
        self.exclamation=pygame.image.load(os.path.join("Assets", "exclamationmark.png"))
        self.exclamation=pygame.transform.scale(self.exclamation, (25, 25))

        # Initial cooldown for charge attack gives time for the player to get out of the way before the monster charges

        #self.initial_cooldown=Constants.kohli_initial_cooldown
        #self.in_initial_cooldown=False

        self.wait_for_player_to_enter_room_cooldown_timer=pygame.time.get_ticks()
        self.wait_for_player_to_enter_room_cooldown_count=500

        self.initial_cooldown_started=True
        self.in_initial_cooldown=True
        self.initial_cooldown_timer = pygame.time.get_ticks()
        self.initial_cooldown_count=2000


        self.currently_charging=False

        self.post_attack_cooldown_started=False
        self.in_post_attack_cooldown=False
        self.post_attack_cooldown_timer = pygame.time.get_ticks()
        self.post_attack_cooldown_count=4000

        self.last_charged = pygame.time.get_ticks()
        self.shoot_attack_cooldown_count=4000

        self.first_time_in_room=True

    def initial_cooldown(self, player, screen):
        if self.initial_cooldown_started:
          
            self.initial_cooldown_timer = pygame.time.get_ticks()
            self.initial_cooldown_started=False
            self.charge_coords=(player.player_rectangle.x, player.player_rectangle.y)
            distance = [self.charge_coords[0] - self.monster_rectangle.x, self.charge_coords[1] - self.monster_rectangle.y]
            norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
            direction = [distance[0] / norm, distance[1 ] / norm]
            self.charge_movement_vector = [direction[0] * Constants.kohli_charge_speed, direction[1] * kohli_charge_speed]
            

        if self.in_initial_cooldown:
            now = pygame.time.get_ticks()
            
            if now - self.initial_cooldown_timer >= self.initial_cooldown_count:
                self.in_initial_cooldown=False
                self.currently_charging=True
                
                
            else:

                screen.blit(self.exclamation, (player.player_rectangle.centerx-(player.player_rectangle.width/2)-10, player.player_rectangle.centery))
                screen.blit(self.exclamation, (player.player_rectangle.centerx+(player.player_rectangle.width/2)+10, player.player_rectangle.centery))

    
    def post_attack_cooldown(self):
        now = pygame.time.get_ticks()
        if now - self.post_attack_cooldown_timer >= self.post_attack_cooldown_count:
            self.in_post_attack_cooldown=False
            return True
        return False
    
    def charge(self, player):
        
        self.monster_rectangle.move_ip(self.charge_movement_vector[0], self.charge_movement_vector[1])

        if self.monster_rectangle.collidepoint(self.charge_coords[0], self.charge_coords[1]) or self.monster_rectangle.colliderect(player.player_rectangle) or (abs(self.monster_rectangle.x-self.charge_coords[0])<=20 and abs(self.monster_rectangle.y-self.charge_coords[1])<=20):
            self.currently_charging=False
            self.in_post_attack_cooldown=True
            self.post_attack_cooldown_timer=pygame.time.get_ticks()


    def charge_attack(self, player, screen):
        if self.in_initial_cooldown:
            self.initial_cooldown(player, screen)
        
        elif self.currently_charging:
            self.charge(player)
            self.current_attack_damage=2

        elif self.in_post_attack_cooldown:
            post_attack_cooldown_over=self.post_attack_cooldown()
            if post_attack_cooldown_over:

                self.current_attack="shoot"
                now = pygame.time.get_ticks()
                self.last_charged=now

                # Change Attack

    def attack(self,player, screen):
        if self.current_attack=="shoot":
            if self.first_time_in_room:
                self.shoot_attack_cooldown_count+=4000
                self.first_time_in_room=False

            self.walk_towards_player_and_shoot(player, Constants.kohli_speed, Constants.kohli_projectile_speed, screen)
            now = pygame.time.get_ticks()
            
            if now - self.last_charged>= self.shoot_attack_cooldown_count:
                self.current_attack="charge"
                self.in_initial_cooldown=True
                self.initial_cooldown_started=True
                
        
        elif self.current_attack=="charge":
            self.charge_attack(player, screen)
