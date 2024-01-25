from pygame import display as display
from Monster import *

class MiniBoss(Monster):

    def __init__(self, attack_power:float, health:float, img:pygame.image, mini_boss_name:str, start_pos_x:int, start_pos_y:int, height:int, width:int, proj_img:str, proj_height, proj_width, main_attack):
        super().__init__(attack_power, health, img, "Mini Boss", start_pos_x, start_pos_y, height, width, proj_img, proj_height, proj_width)
        self.mini_boss_name=mini_boss_name
        self.movement_vector=(0, 0)
        self.current_direction=""
        self.stop_moving=False
        self.main_attack = main_attack

    #  Moves the monster towards the player  

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
    
    def render(self, x_pos: float, y_pos: float, height: int, width: int, screen) -> None:
        return super().render(x_pos, y_pos, height, width, screen)

        


        

        