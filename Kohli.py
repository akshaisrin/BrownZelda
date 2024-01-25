from MediumBoss import *
import os
import Constants

class Kohli(MediumBoss):

    def __init__(self, attack_power:float, test_monster_name:str, start_pos_x:float, start_pos_y:float):

        img=pygame.image.load(os.path.join("Assets", "kohli_beard.png"))
        super().__init__(attack_power, 10, img, "Virat Kohli", start_pos_x, start_pos_y, 175, 100, ["charge_and_hit", "shoot_attack"], "cricket_ball.png", 25, 25)
        self.test_monster_name=test_monster_name

        # Fields for charge attack

        self.charge_speed=10

        # Post-charge attack cooldown durations

        self.in_cooldown=False
        self.started_charging=True
        self.currently_charging=False

        # Coords monster will charge towards

        self.charge_coords=(0, 0)

        self.projectile.damage=2
        self.projectile_constant=Constants.kohli_projectile_speed
        self.current_attack="shoot"
        self.exclamation=pygame.image.load(os.path.join("Assets", "exclamation_point.png"))
        self.exclamation=pygame.transform.scale(self.exclamation, (25, 35))

        # Variables to handle the initial cooldown (when it has locked in on a point and is about to charge towards the player)

        self.initial_cooldown_started=True
        self.in_initial_cooldown=True
        self.initial_cooldown_timer = pygame.time.get_ticks()
        self.initial_cooldown_count=2000

        # Variables to handle the post attack cooldown (which is when the player is supposed to hit the monster)

        self.post_attack_cooldown_started=False
        self.in_post_attack_cooldown=False
        self.post_attack_cooldown_timer = pygame.time.get_ticks()
        self.post_attack_cooldown_count=4000

        self.last_charged = pygame.time.get_ticks()
        self.shoot_attack_cooldown_count=4000

        self.first_time_in_room=True
        self.die_speech_bubble=pygame.image.load(os.path.join("Assets", "die_speech_bubble.png"))
        self.die_speech_bubble=pygame.transform.scale(self.die_speech_bubble, (150, 50))

    # This handles the inital cooldown, which gives time for the player to get out of the way before kohli charges towards them

    def initial_cooldown(self, player, screen):

        # This is right when the initial cooldown begins

        if self.initial_cooldown_started:
          
            self.initial_cooldown_timer = pygame.time.get_ticks()
            self.initial_cooldown_started=False

            # This sets the monster's charge coordinates and charge movement vector by calculting the distance between the player and monster

            self.charge_coords=[player.player_rectangle.centerx, player.player_rectangle.centery]
            distance = [self.charge_coords[0] - self.monster_rectangle.x, self.charge_coords[1] - self.monster_rectangle.y]
            norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
            direction = [distance[0] / norm, distance[1 ] / norm]
            self.charge_movement_vector = [direction[0] * Constants.kohli_charge_speed, direction[1] * kohli_charge_speed]

            self.adjust_charge_coords()

        # This is if the initial cooldown is ongoing    

        if self.in_initial_cooldown:
            now = pygame.time.get_ticks()
            if now - self.initial_cooldown_timer >= self.initial_cooldown_count:
                self.in_initial_cooldown=False
                self.currently_charging=True
                
            else:
                
                # Rendering exclamation points to give the player a warning

                screen.blit(self.exclamation, (player.player_rectangle.centerx-(player.player_rectangle.width/2)-15, player.player_rectangle.centery-10))
                screen.blit(self.exclamation, (player.player_rectangle.centerx+(player.player_rectangle.width/2)+2, player.player_rectangle.centery-10))

    # Handles the post attack cooldown when the player is supposed to attack the monster since it can't move

    def post_attack_cooldown(self) -> bool:
        now = pygame.time.get_ticks()
        if now - self.post_attack_cooldown_timer >= self.post_attack_cooldown_count:
            self.in_post_attack_cooldown=False
            self.realign_projectile()
            return True
        return False
    
    # Sometimes, the monster needs to go slightly farther than the original charge coordinates to detect a proper collision- this function adjusts the charge coordinates

    def adjust_charge_coords(self):
        if self.charge_movement_vector[0]>=0:
            self.charge_coords[0]+=Constants.kohli_adjusted_charge_coords_const
        
        if self.charge_movement_vector[0]<0:
            self.charge_coords[0]-=Constants.kohli_adjusted_charge_coords_const

        if self.charge_movement_vector[1]>=0:
            self.charge_coords[1]+=Constants.kohli_adjusted_charge_coords_const
        
        if self.charge_movement_vector[1]<0:
            self.charge_coords[1]-=Constants.kohli_adjusted_charge_coords_const
    
    # Sometimes, because the x and y increments are so large, the monster overshoots where it's supposed to be charging to. This function checks if this is true

    def check_for_overshooting(self):
        x,y=False, False

        # Compares the monster's position to the target destination based on the current direction it's travelling in

        if (self.charge_movement_vector[0]>=0 and self.monster_rectangle.x>=self.charge_coords[0]) or (self.charge_movement_vector[0]<0 and self.monster_rectangle.x<=self.charge_coords[0]):
            x=True
        if (self.charge_movement_vector[1]>=0 and self.monster_rectangle.y>=self.charge_coords[1]) or (self.charge_movement_vector[1]<0 and self.monster_rectangle.y<=self.charge_coords[1]):
            y=True
        
        return (x==True and y==True)

    # Moves the monster towards the monster's charge coordinates

    def charge(self, player):
        
        self.monster_rectangle.move_ip(self.charge_movement_vector[0], self.charge_movement_vector[1])

        # Checks to see if the monster is at its target destination or has overshot

        if self.monster_rectangle.collidepoint(self.charge_coords[0], self.charge_coords[1]) or self.monster_rectangle.colliderect(player.player_rectangle) or self.check_for_overshooting():
            self.currently_charging=False
            self.in_post_attack_cooldown=True
            self.post_attack_cooldown_timer=pygame.time.get_ticks()


    # This function handles all components of the charge attack

    def charge_attack(self, player, screen):
        if self.in_initial_cooldown:
            screen.blit(self.die_speech_bubble, (self.monster_rectangle.topright[0]-10, self.monster_rectangle.topright[1]+5))
            self.initial_cooldown(player, screen)
        
        elif self.currently_charging:
            screen.blit(self.die_speech_bubble, (self.monster_rectangle.topright[0]-10, self.monster_rectangle.topright[1]+5))
            self.charge(player)
            self.current_attack_damage=1

        elif self.in_post_attack_cooldown:
            post_attack_cooldown_over=self.post_attack_cooldown()
            if post_attack_cooldown_over:
                
                # Switches attack back to shoot

                self.current_attack="shoot"
                now = pygame.time.get_ticks()
                self.last_charged=now

    # Main attack function to switch between shooting and charging

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
