from MediumBoss import *
import os
import Constants

class Kohli(MediumBoss):

    def __init__(self, attack_power:float, health:float, test_monster_name:str, start_pos_x:float, start_pos_y:float, height:int, width:int):

        img=pygame.image.load(os.path.join("Assets", "enemy2.png"))
        super().__init__(attack_power, health, img, "Virat Kohli", start_pos_x, start_pos_y, height, width)
        self.test_monster_name=test_monster_name
        self.charge_speed=2.25
        self.cooldown=Constants.cooldown
        self.in_cooldown=False
        self.started_charging=True
        self.charge_coords=(0, 0)
        self.patrol_constant=Constants.kohli_patrol_constant
        self.projectile.damage=2
        self.projectile_constant=Constants.kohli_projectile_constant
        self.current_attack=""
        self.exclamation=pygame.image.load(os.path.join("Assets", "exclamationmark.png"))
        self.exclamation=pygame.transform.scale(self.exclamation, (25, 25))
        self.initial_cooldown=Constants.kohli_initial_cooldown
        self.in_initial_cooldown=False


    def charge(self):

        change=((self.charge_coords[0]-self.monster_rectangle.x)/self.charge_speed, (self.charge_coords[1]-self.monster_rectangle.y)/self.charge_speed)
        self.monster_rectangle.move_ip(change[0], change[1])
        #self.charge_speed-=5
    
    def charge_and_hit(self, player, screen):

        # Checking if monster is touching player to tell the monster when to stop charging and when to start the cooldown

        if self.monster_rectangle.colliderect(player.player_rectangle) or (abs(self.monster_rectangle.x-self.charge_coords[0])<=5 and abs(self.monster_rectangle.y-self.charge_coords[1])<=5):

            self.in_cooldown=True
        
        # Checking if cooldown is over to know when the monster can start moving

        if self.in_cooldown:
            self.cooldown-=1

        if self.cooldown==0:
           
            self.cooldown=Constants.cooldown
            self.in_cooldown=False
            self.stop_moving=False
    
        # Checking if monster is currently already attacking

        if (self.stop_moving) and not self.in_cooldown and not self.in_initial_cooldown:
            
            self.charge()
            
        # Checking if monster is not already charging and the player is in the monster's radius
        elif self.in_initial_cooldown:
            screen.blit(self.exclamation, (player.player_rectangle.centerx-(player.player_rectangle.width/2)-10, player.player_rectangle.centery))
            screen.blit(self.exclamation, (player.player_rectangle.centerx+(player.player_rectangle.width/2)+10, player.player_rectangle.centery))
            self.initial_cooldown-=1
            if self.initial_cooldown==0:
                self.initial_cooldown=Constants.kohli_initial_cooldown
                self.in_initial_cooldown=False

        elif (abs(player.player_rectangle.centery-self.monster_rectangle.centery)<=self.monster_rectangle.height/2 or abs(player.player_rectangle.centerx-self.monster_rectangle.centerx)<=self.monster_rectangle.width/2) and not self.in_cooldown and not self.in_initial_cooldown:
            
            self.stop_moving=True
            self.charge_coords=(player.player_rectangle.x, player.player_rectangle.y)
            self.in_initial_cooldown=True
        
        
            
    
    def shoot_attack(self, player, screen):
        # check vertical distance between player and monster to figure out if monster should shoot
        
        if (self.stop_moving):
            self.shoot_straight(self.projectile.shoot_coords[0], self.projectile.shoot_coords[1], screen)

        elif (abs(player.player_rectangle.centery-self.monster_rectangle.centery)<=self.monster_rectangle.height/2 or abs(player.player_rectangle.centerx-self.monster_rectangle.centerx)<=self.monster_rectangle.width/2):
            self.stop_moving=True
            self.shoot_straight(player.player_rectangle.x, player.player_rectangle.y, screen)
            self.projectile.shoot_coords=(player.player_rectangle.x, player.player_rectangle.y)
        
        # check to see if projectile is at edge of screen

        if (self.projectile.projectile_rectangle.x<=0 or self.projectile.projectile_rectangle.x>=Constants.screen_width or self.projectile.projectile_rectangle.y<=0 or self.projectile.projectile_rectangle.y>=Constants.screen_height):
            self.stop_moving=False
            self.projectile.started_shooting=True
            
    
    

    def shoot_straight(self, end_x, end_y, screen):

        if self.projectile.started_shooting:
            self.projectile.projectile_rectangle.x=self.monster_rectangle.x
            self.projectile.projectile_rectangle.y=self.monster_rectangle.y
            self.projectile.started_shooting=False

        change=((end_x-self.monster_rectangle.x)/self.projectile_constant, (end_y-self.monster_rectangle.y)/self.projectile_constant)
        self.projectile.projectile_rectangle.move_ip(change[0], change[1])
        self.projectile.render(self.projectile.projectile_rectangle.x, self.projectile.projectile_rectangle.y, screen)
    
    def walk_towards_player(self, player, screen):

        if not self.stop_moving:

            change=((player.player_rectangle.x-self.monster_rectangle.x)/(Constants.kohli_speed), (player.player_rectangle.y-self.monster_rectangle.y)/(Constants.kohli_speed))
            self.monster_rectangle.move_ip(change[0], change[1])    
        
        if self.stop_moving:
            if self.current_attack=="shoot":
                self.shoot_attack(player, screen)
            else:

                self.charge_and_hit(player, screen)  


        if (abs(player.player_rectangle.centery-self.monster_rectangle.centery)<=self.monster_rectangle.height/2 or abs(player.player_rectangle.centerx-self.monster_rectangle.centerx)<=self.monster_rectangle.width/2) and not self.stop_moving:
            attack=random.choice(["charge", "shoot", "shoot"])
            self.current_attack=attack
            if self.current_attack=="shoot":
                print("shoot")
                self.shoot_attack(player, screen)
            else:
                print("charge")
                self.charge_and_hit(player, screen)
            
            