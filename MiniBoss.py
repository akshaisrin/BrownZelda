from Monster import *

class MiniBoss(Monster):

    def __init__(self, attack_power:float, health:float, img:pygame.image, mini_boss_name:str, start_pos_x:int, start_pos_y:int, height:int, width:int):
        super().__init__(attack_power, health, img, "Mini Boss", start_pos_x, start_pos_y, height, width)
        self.mini_boss_name=mini_boss_name
        self.movement_vector=(0, 0)
        self.projectile_change_x=0.0
        self.projectile_change_y=0.0
        self.current_direction=""
        self.patrol_vector=(0,0)

        self.stop_moving=False
    
    def change_direction_patrol(self, x, y):
        self.end_patrol=(x, y)

    def patrol_and_shoot(self, player, x1, y1, x2, y2, screen):
        change_direction=False

        # check vertical distance between player and monster to figure out if monster should shoot
        
        if (self.stop_moving):
            self.shoot_straight(self.projectile.shoot_coords[0], self.projectile.shoot_coords[1], screen)

        elif abs(player.player_rectangle.centery-self.monster_rectangle.centery)<=player.player_rectangle.height/2 or abs(player.player_rectangle.centerx-self.monster_rectangle.centerx)<=self.monster_rectangle.width/2:
            self.stop_moving=True
            self.shoot_straight(player.player_rectangle.x, player.player_rectangle.y, screen)
            self.projectile.shoot_coords=(player.player_rectangle.x, player.player_rectangle.y)
        

        
        # check to see if projectile is at edge of screen

        if self.projectile.projectile_rectangle.x<=0 or self.projectile.projectile_rectangle.x>=Constants.screen_width or self.projectile.projectile_rectangle.y<=0 or self.projectile.projectile_rectangle.y>=Constants.screen_height:
            self.stop_moving=False
            self.projectile.started_shooting=True




        # first check to see if monster at new coords

        if not self.stop_moving:

            if (self.monster_rectangle.collidepoint(x2, y2)):
                self.patrol_vector=((x1-x2)/Constants.mini_boss_patrol_constant, (y1-y2)/Constants.mini_boss_patrol_constant)
            
            if (self.monster_rectangle.collidepoint(x1, y1)):
                self.patrol_vector=((x2-x1)/Constants.mini_boss_patrol_constant, (y2-y1)/Constants.mini_boss_patrol_constant)
            
            self.monster_rectangle.move_ip(self.patrol_vector[0], self.patrol_vector[1])



    def start_moving(self, player):

        pass
        # check to see if touching an obstacle

        # if not, pick



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


    def shoot(self, screen, player):
        

        # Returning projectile back to monster
        
        if (self.projectile.projectile_rectangle.x>=Constants.screen_width or self.projectile.projectile_rectangle.x<=0 or self.projectile.projectile_rectangle.y>=Constants.screen_height or self.projectile.projectile_rectangle.y<=0):
            self.shooting=False

        else:    
            self.projectile.projectile_rectangle.x+=self.projectile_change_x
            self.projectile.projectile_rectangle.y+=self.projectile_change_y

            self.projectile.render(self.projectile.projectile_rectangle.x, self.projectile.projectile_rectangle.y, screen)
        


        

        