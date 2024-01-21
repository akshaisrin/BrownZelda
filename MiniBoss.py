from pygame import display as display
from Monster import *

class MiniBoss(Monster):

    def __init__(self, attack_power:float, health:float, img:pygame.image, mini_boss_name:str, start_pos_x:int, start_pos_y:int, height:int, width:int, proj_img:str, proj_height, proj_width, main_attack):
        super().__init__(attack_power, health, img, "Mini Boss", start_pos_x, start_pos_y, height, width, proj_img, proj_height, proj_width)
        self.mini_boss_name=mini_boss_name
        self.movement_vector=(0, 0)
        self.projectile_change_x=0.0
        self.projectile_change_y=0.0
        self.current_direction=""
        self.stop_moving
        self.main_attack = main_attack
        

    def start_moving(self, player):
               # Checking if monster in movement mode, and moving the monster if it is

        if not self.stop_moving:

            change=((player.player_rectangle.x-self.monster_rectangle.x)/(Constants.mini_boss_speed), (player.player_rectangle.y-self.monster_rectangle.y)/(Constants.mini_boss_speed))
            self.monster_rectangle.move_ip(change[0], change[1])


    def get_attacked(self, player):
        if player.attacking and self.monster_rectangle.colliderect(player.player_rectangle):
            self.get_hit(3.0) #arbitrary clone damage value


    def close_range_attack(self, player, speed, screen):
        self.move_towards_player(player, speed, screen)


    def long_range_attack(self, player, speed, screen):
        if self.main_attack=="shoot and follow path":
            self.follow_path_and_shoot(self.path_coords, Constants.npc_cricker_player_speed, Constants.npc_cricker_player_projectile_speed, player, screen)
        elif self.main_attack=="shoot and patrol":
            self.patrol_and_shoot(player, Constants.npc_cricker_player_speed, Constants.npc_cricker_player_projectile_speed, self.patrol_distance, self.patrol_direction, screen)
        else:
            pass
    
    def render(self, x_pos: float, y_pos: float, height: int, width: int, screen) -> None:
        return super().render(x_pos, y_pos, height, width, screen)

        # change_direction=False
        # if self.monster_rectangle.left < 0:
        #     self.monster_rectangle.left = 0
        #     change_direction=True
        # if self.monster_rectangle.right > Constants.screen_width:
        #     self.monster_rectangle.right = Constants.screen_width
        #     change_direction=True
        # if self.monster_rectangle.top <= 0:
        #     self.monster_rectangle.top = 0
        #     change_direction=True
        # if self.monster_rectangle.bottom >= Constants.screen_height:
        #     self.monster_rectangle.bottom = Constants.screen_height
        #     change_direction=True
        # if (change_direction):
        #     if self.current_direction=="left":
        #         new_direction="right"
        #     elif self.current_direction=="right":
        #         new_direction="left"
        #     elif self.current_direction=="up":
        #         new_direction="down"
        #     else:
        #         new_direction="up"

        #     self.change_directions(new_direction)
        # # if (self.monster_rectangle.left<0 or self.monster_rectangle.right>Constants.screen_width or self.monster_rectangle.bottom>=Constants.screen_height or self.monster_rectangle.top<=Constants.screen_height):
            
        # #     new_direction=""
        # #     if self.current_direction=="left":
        # #         new_direction="right"
        # #     elif self.current_direction=="right":
        # #         new_direction="left"
        # #     elif self.current_direction=="up":
        # #         new_direction="down"
        # #     else:
        # #         new_direction="up"

        # #     self.change_directions(new_direction)
        
        # if (self.current_increment<=self.total_increments):
        #     self.current_increment+=1
        #     self.monster_rectangle.move_ip(self.movement_vector[0], self.movement_vector[1])
        #     if abs(player.player_rectangle.centerx-self.monster_rectangle.centerx)<=2 or abs(player.player_rectangle.centery-self.monster_rectangle.centery)<=2:
        #         self.shooting=True
            
        #     if (self.shooting):
        #         offset_x=self.projectile.projectile_rectangle.x+Constants.medium_boss_projectile_offset_x
        #         offset_y=self.projectile.projectile_rectangle.y+Constants.medium_boss_projectile_offset_y

        #         self.projectile_change_x=(player.player_rectangle.x-offset_x)/Constants.medium_boss_velocity_constant
        #         self.projectile_change_y=(player.player_rectangle.y-offset_y)/Constants.medium_boss_velocity_constant
        #         #self.shoot(screen, player)
            
        # else:
        #     self.change_directions(random.choice(["left", "right", "up", "down"]))    
            
    


    # def change_directions(self, direction):
    #     self.current_direction=direction
    #     self.current_increment=0
    #     self.total_increments=random.randint(5, 15)*10
    #     self.movement_vector=Constants.mini_boss_movement_vector[direction]

        


        

        