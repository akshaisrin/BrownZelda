from pygame import *
import os
from Room import *
from Constants import *
from Biome import *
from Player import *
from Obstacles import *
from Monster import *
from TestMonsterMedium import *

class Overworld(Room):
    
    def __init__(self):
        super().__init__(0, 0, 0)
        
        # intialize all obstacles
        self.obstacle = Obstacles("obstacle_test.png", 500, 200, 100, 100)
        
        self.test_obstacle1 = Obstacles("test_object1.png", screen_width-680, 0, 680, 380)
        self.test_obstacle2 = Obstacles("test_object2.png", 0, screen_height-355, 190, 355)
        self.test_obstacle3 = Obstacles("test_object2.png", screen_width-190, screen_height-355, 190, 355)
        self.test_obstacle4 = Obstacles("test_object3.png", 200, screen_height-150, screen_width-400, 150)
        self.test_obstacle5 = Obstacles("test_object4.png", 480, 0, 200, 150)
        self.test_obstacle6 = Obstacles("test_object5.png", 0, 0, 150, 380)
        self.test_obstacle7 = Obstacles("test_object5.png", 150, 0, 110, 350)
        self.test_obstacle8 = Obstacles("test_object5.png", 260, 0, 130, 250)
        
        self.test2_o1 = Obstacles("room2_object_1.png", 0, 0, screen_width, 120)
        self.test2_o2 = Obstacles("room2_object_1.png", 0, screen_height-100, int((screen_width-200)/2), 100)
        self.test2_o3 = Obstacles("room2_object_3.png", 350, 250, 80, 80)
        self.test2_o4 = Obstacles("room2_object_3.png", 350, 480, 80, 80)
        self.test2_o5 = Obstacles("room2_object_3.png", 750, 250, 80, 80)
        self.test2_o6 = Obstacles("room2_object_3.png", 750, 480, 80, 80)
        self.test2_o7 = Obstacles("room2_object_3.png", 1150, 250, 80, 80)
        self.test2_o8 = Obstacles("room2_object_3.png", 1150, 480, 80, 80)
        self.test2_o9 = Obstacles("room2_object_1.png", int(screen_width/2+100), screen_height-100, int((screen_width-200)/2), 100)
        
        # intialize all the biomes
        #self.desert = Biome("desert", "desert_biome.png", [(1200, 500, self.desert, "up")], True, 500, 400)
        #self.homes = Biome("homes", "homes_biome.png", [(1200, 500, self.homes, "up")], True, 500, 400)
        #self.tundra = Biome("tundra", "tundra_biome.png", [(1200, 500, self.homes, "up")], True, 500, 400)
        #self.zelda = Biome("zelda", "zelda_biome.png", [(1200, 500, self.homes, "up")], True, 500, 400)
        #self.dungeon = Biome("dungeon", "dungeon1_copy.jpg", [(-1000, -1000, self.homes, "up")], False)
        self.test_room = Biome("test_room", "background.jpg", [], False)
        self.test_room2 = Biome("test_room", "test_room.png", [(500, 0, self.test_room, "up")], True, 290, 0)
        self.test_room.add_exits([(650, 600, self.test_room2, "down"), (1200, 500, self.test_room2, "right")])
                
        # add obstacles to each Biome
        #self.desert.add_obstacles([self.obstacle])
        #self.homes.add_obstacles([self.obstacle])
        #self.tundra.add_obstacles([self.obstacle])
        #self.zelda.add_obstacles([self.obstacle])
        self.test_room.add_obstacles([self.test2_o1, self.test2_o2, self.test2_o3, self.test2_o4, self.test2_o5, self.test2_o6, self.test2_o7, self.test2_o8, self.test2_o9])
        self.test_room2.add_obstacles([self.test_obstacle1, self.test_obstacle2, self.test_obstacle3, self.test_obstacle4, self.test_obstacle5, self.test_obstacle6, self.test_obstacle7, self.test_obstacle8])
        
        # add monster
        self.monster=TestMonsterMedium(10.0, 9.0, "Test Monster 2", 500, 100, 250, 300)
        self.test_room.add_monsters([self.monster])
        self.test_room2.add_monsters([self.monster])
        
        # set font
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        
    def biome_name_to_biome(self, biome_name:str):
        if biome_name == "desert":
            return self.desert
        elif biome_name == "graveyard":
            return self.graveyard
        elif biome_name == "homes":
            return self.homes
        elif biome_name == "tundra":
            return self.tundra
        else:
            return self.zelda
    
    """
    def display_biome(self, biome_name:str, x_pos:int, screen:pygame.display):
        biome = self.biome_name_to_biome(biome_name)
        biome.render(x_pos, screen)
        for o in biome.obstacles:
            screen.blit(o.get_image(), (x_pos + o.x, o.y))
        pygame.display.update()
    """
        
    def game_over(self, screen:pygame.display):
        img = pygame.image.load(os.path.join("Assets", "game_over_screen.jpg"))
        image = pygame.transform.scale(img, (screen_width, screen_height))
        screen.blit(image, (0, 0))
        pygame.display.update()
        
    # NOTE: NEED TO CHANGE THE CODE BELOW TO ACCEPT AN ACTUAL DUNGEON OBJECT AS A PARAMETER AND USE THAT OBJECT'S PICTURE & EXIT POSITIONS
    def going_to_dungeon(self, player, biome:Biome, screen:pygame.display):
        if biome.dungeon:
            if (player.player_rectangle.topleft[0] < biome.dungeon_x + 10 and player.player_rectangle.topleft[0] > biome.dungeon_x - 10) and (player.player_rectangle.topleft[1] < biome.dungeon_y + 10 and player.player_rectangle.topleft[1] > biome.dungeon_y - 10):
                image = self.dungeon.get_image()
                screen.fill((0, 0, 0))
                pygame.display.update()
                pygame.time.wait(500)
                for i in range(30, 1, -2):
                    screen.blit(image, (int((screen_width - screen_width/i)/2), 0), (int((screen_width - screen_width/i)/2), 0, int(screen_width/i), screen_height))
                    pygame.display.update()
                    pygame.time.wait(100)
                # player.player_rectangle.topleft(dungeon_x_pos, dungeon_y_pos)
                player.player_rectangle.topleft = (1200, 250)
                return self.dungeon
        return None
    
    # change code so that there can be multiple exits in a room and not just one, also order of rooms will be predetermined
    def going_to_next_biome(self, player:Player, biome:Biome, curr_screen_x_pos:int, curr_screen_y_pos:int, screen:pygame.display):    
        curr_biome = biome
        for exit in curr_biome.exits:
            exit_x = exit[0]
            exit_y = exit[1]
            if (player.player_rectangle.topleft[0] < exit_x + 40 and player.player_rectangle.topleft[0] > exit_x - 40) and (player.player_rectangle.topleft[1] < exit_y + 40 and player.player_rectangle.topleft[1] > exit_y - 40):
                next_biome = exit[2]
                # moving down or up
                if (exit[3] == "down" or exit[3] == "up"):
                    if exit[3] == "down":
                        change = -100
                    else:
                        change = 100
                    y_pos = screen_height
                    while y_pos > 0:
                        curr_screen_y_pos += change
                        curr_biome.render(curr_screen_x_pos, curr_screen_y_pos, player, screen)
                        y_pos += change
                        next_biome.render(curr_screen_x_pos, y_pos, player, screen)
                        new_y = player.player_rectangle.topleft[1] + change
                        player.player_rectangle.topleft = (player.player_rectangle.topleft[0], new_y)
                        player.render(player.player_rectangle.topleft[0], player.player_rectangle.topleft[1], screen)
                        pygame.display.update()
                        pygame.time.wait(10)
                # moving left or right
                else:
                    if exit[3] == "right":
                        change = -100
                    else:
                        change = 100
                    x_pos = screen_width
                    while x_pos > 0:
                        curr_screen_x_pos += change
                        curr_biome.render(curr_screen_x_pos, curr_screen_y_pos, player, screen)
                        x_pos += change
                        next_biome.render(x_pos, curr_screen_y_pos, player, screen)
                        new_x = player.player_rectangle.topleft[1] + change
                        player.player_rectangle.topleft = (new_x, player.player_rectangle.topleft[1])
                        player.render(player.player_rectangle.topleft[0], player.player_rectangle.topleft[1], screen)
                        pygame.display.update()
                        pygame.time.wait(10)
                next_biome.render(0, 0, player, screen)
                #player.player_rectangle.topleft = (player.player_rectangle.topleft[0], -100)
                return next_biome
        return None
    
    def obstacles_in_biome(self, player:Player, biome:Biome):
        obstacle_rects = biome.obstacles_rect
        for obstacle_rect in obstacle_rects:
            if player.player_rectangle.colliderect(obstacle_rect):
                if player.direction == "left":
                    x_pos = obstacle_rect[0] + obstacle_rect[2]
                    player.player_rectangle.topleft = (x_pos, player.player_rectangle.topleft[1])
                elif player.direction == "right":
                    x_pos = obstacle_rect[0] - player.player_rectangle[2]
                    player.player_rectangle.topleft = (x_pos, player.player_rectangle.topleft[1])
                elif player.direction == "up":
                    y_pos = obstacle_rect[1] + obstacle_rect[3]
                    player.player_rectangle.topleft = (player.player_rectangle.topleft[0], y_pos)
                else:
                    y_pos = obstacle_rect[1] - player.player_rectangle[3]
                    player.player_rectangle.topleft = (player.player_rectangle.topleft[0], y_pos)
    
    def monster_attack(self, curr_biome:Biome, player:Player, screen:pygame.display):
        monsters = curr_biome.monsters
        mon_alive = 0
        for m in monsters:
            if m.alive:
                mon_alive += 1
                if (player.player_rectangle.colliderect(m.projectile.projectile_rectangle)):
                    print("player got hit")
                    m.realign_projectile()
                    player.get_attacked(m.projectile.damage, screen)
        if mon_alive == 0:
            return False
        else:
            return True
        
    def display_text(self, words:str, curr_biome:Biome, player:Player, start_x:int, start_y:int, screen:pygame.display):
        """
        # displaying the text in the center always - so letters already displayed continue to shift
        for i in range(1, len(words) + 1):
            curr_biome.render(0, player, screen)
            text = self.font.render(words[0:i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (screen_width//2, screen_height//2)
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.wait(500)
            #arcadegamer font used in instructions
        """
        for i in range(1, len(words) + 1):
            curr_biome.render(0, 0, player, screen)
            text = self.font.render(words[0:i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect = (start_x, start_y)
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.wait(500)
        return (text, text_rect)
        
        