from pygame import *
import os
from Room import *
from Constants import *
from Biome import *
from Player2 import *
from Obstacles import *
from Monster import *
from TestMonsterMedium import *

class Overworld(Room):
    
    def __init__(self):
        super().__init__(0, 0, 0)
        
        # intialize all obstacles
        """
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
        """
        
        # intialize all biomes with their respective obstacles
        self.room1 = Biome("room1", "room1.png", [], [("USE ARROW KEYS TO MOVE AROUND.", (screen_width - 612) // 2, 235), ("PRESS SPACE TO ATTACK.", (screen_width - 421) // 2, 535)], False)
        self.obstacle1 = Obstacles("test_object1.png", 0, 0, screen_width, 290)
        self.obstacle2 = Obstacles("test_object1.png", 0, 500, screen_width, 300)
        self.obstacle3 = Obstacles("test_object1.png", 0, 0, 50, screen_height)
        self.room1.add_obstacles([self.obstacle1, self.obstacle2, self.obstacle3])
        
        self.room2 = Biome("room2", "room2.png", [(-100, 380, self.room1, "left", 100, 100)], [("THE FIRST INGREDIENT IS IN THE EDEN GARDENS.", 15, 235), ("UNFORTUNATELY, THE INDIAN CRICKET TEAM IS VALIANTLY DEFENDING IT.", 15, 535)], False)
        self.obstacle4 = Obstacles("test_object1.png", 0, 0, 925, 290)
        self.obstacle5 = Obstacles("test_object1.png", 1200, 0, 400, screen_height)
        self.obstacle6 = Obstacles("test_object1.png", 0, 0, screen_width, 200)
        self.room2.add_obstacles([self.obstacle2, self.obstacle4, self.obstacle5, self.obstacle6])
        
        self.cricketroom1 = Biome("cricketroom1", "cricketroom1.png", [(1000, 895, self.room2, "down", 100, 100)], [], False)
        self.obstacle7 = Obstacles("test_object1.png", 0, 0, 705, 150)
        self.obstacle8 = Obstacles("test_object1.png", 935, 0, screen_width-935, 150)
        self.obstacle9 = Obstacles("test_object1.png", screen_width-150, 0, 150, screen_height)
        self.obstacle10 = Obstacles("test_object1.png", screen_width-340, screen_height-155, 340, 155)
        self.obstacle11 = Obstacles("test_object1.png", 0, 305, 600, 195)
        self.obstacle12 = Obstacles("test_object1.png", 0, screen_height-155, 905, 155)
        self.cricketroom1.add_obstacles([self.obstacle7, self.obstacle8, self.obstacle9, self.obstacle10, self.obstacle11, self.obstacle12])
        
        self.cricketroom2 = Biome("cricketroom2", "cricketroom2.png", [(800, 895, self.cricketroom1, "down", 100, 100)], [], False)
        self.obstacle13 = Obstacles("test_object1.png", 0, 0, screen_width, 150)
        self.obstacle14 = Obstacles("test_object1.png", 950, screen_height-150, screen_width-950, 150)
        self.obstacle15 = Obstacles("test_object1.png", 0, screen_height-160, 700, 160)
        self.obstacle16 = Obstacles("test_object1.png", 0, 0, 150, screen_height)
        self.cricketroom2.add_obstacles([self.obstacle13, self.obstacle9, self.obstacle14, self.obstacle15, self.obstacle16])
        
        self.cricketroom3 = Biome("cricketroom3", "cricketroom3.png", [(1550, 200, self.cricketroom1, "right", 100, 100), (1550, 600, self.cricketroom1, "right", 100, 100)], [], False)
        self.obstacle17 = Obstacles("test_object1.png", 0, screen_height-150, screen_width, 150)
        self.obstacle18 = Obstacles("test_object1.png", screen_width-600, 305, 600, 195)
        self.cricketroom3.add_obstacles([self.obstacle7, self.obstacle8, self.obstacle17, self.obstacle16, self.obstacle18])
        
        self.cricketroom4 = Biome("cricketroom4", "cricketroom4.png", [(800, 895, self.cricketroom3, "down", 100, 100)], [], False)
        self.cricketroom4.add_obstacles([self.obstacle7, self.obstacle8, self.obstacle9, self.obstacle14, self.obstacle15, self.obstacle16])
        
        self.cricketroom5 = Biome("cricketroom5", "cricketroom2.png", [(800, 895, self.cricketroom4, "down", 100, 100)], [], False)
        self.cricketroom5.add_obstacles([self.obstacle13, self.obstacle9, self.obstacle14, self.obstacle15, self.obstacle16])
        
        self.room1.add_exits([(1550, 380, self.room2, "right", 100, 100)])
        self.room2.add_exits([(1000, 180, self.cricketroom1, "up", 70, 30)])
        self.cricketroom1.add_exits([(800, -95, self.cricketroom2, "up", 100, 100), (-95, 200, self.cricketroom3, "left", 100, 100), (-95, 600, self.cricketroom3, "left", 100, 100)])
        self.cricketroom2.add_exits([(800, -95, self.cricketroom4, "up", 100, 100)])
        self.cricketroom3.add_exits([(800, -95, self.cricketroom2, "up", 100, 100)])
        self.cricketroom4.add_exits([(800, -95, self.cricketroom5, "up", 100, 100)])
        
        
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
    def going_to_dungeon(self, player:Player2, biome:Biome, screen:pygame.display):
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
    def going_to_next_biome(self, player:Player2, biome:Biome, curr_screen_x_pos:int, curr_screen_y_pos:int, screen:pygame.display):    
        curr_biome = biome
        #print(player.player_rectangle.topleft)
        for exit in curr_biome.exits:
            exit_x = exit[0]
            exit_y = exit[1]
            if (player.player_rectangle.topleft[0] < exit_x + exit[4] and player.player_rectangle.topleft[0] > exit_x - exit[4]) and (player.player_rectangle.topleft[1] < exit_y + exit[5] and player.player_rectangle.topleft[1] > exit_y - exit[5]):
                next_biome = exit[2]
                # moving down or up
                if (exit[3] == "down" or exit[3] == "up"):
                    if exit[3] == "down":
                        change = -100
                        y_pos = screen_height
                    else:
                        change = 100
                        y_pos = -1 * screen_height
                    count = screen_height
                    while count > 0:
                        curr_screen_y_pos += change
                        curr_biome.render(curr_screen_x_pos, curr_screen_y_pos, player, screen)
                        y_pos += change
                        next_biome.render(curr_screen_x_pos, y_pos, player, screen)
                        new_y = player.player_rectangle.topleft[1] + change
                        if new_y < 0:
                            new_y = player.player_rectangle[3] + 10
                        if new_y > screen_height:
                            new_y = screen_height - 10
                        player.player_rectangle.topleft = (player.player_rectangle.topleft[0], new_y)
                        player.render(player.player_rectangle.topleft[0], player.player_rectangle.topleft[1], screen)
                        count -= 100
                        pygame.display.update()
                        pygame.time.wait(10)
                    if curr_biome == self.cricketroom1:
                        player.player_rectangle.topleft = (player.player_rectangle.topleft[0], 220)
                        player.render(player.player_rectangle.topleft[0], player.player_rectangle.topleft[1], screen)
                        pygame.display.update()
                # moving left or right
                else:
                    if exit[3] == "right":
                        change = -100
                        x_pos = screen_width
                    else:
                        change = 100
                        x_pos = -1 * screen_width
                    count = screen_width
                    while count > 0:
                        curr_screen_x_pos += change
                        curr_biome.render(curr_screen_x_pos, curr_screen_y_pos, player, screen)
                        x_pos += change
                        next_biome.render(x_pos, curr_screen_y_pos, player, screen)
                        new_x = player.player_rectangle.topleft[0] + change
                        if new_x < 0:
                            new_x = 10
                        if new_x > screen_width - player.player_rectangle[2]:
                            new_x = screen_width - player.player_rectangle[2] - 50
                        player.player_rectangle.topleft = (new_x, player.player_rectangle.topleft[1])
                        player.render(player.player_rectangle.topleft[0], player.player_rectangle.topleft[1], screen)
                        count -= 100
                        pygame.display.update()
                        pygame.time.wait(20)
                next_biome.render(0, 0, player, screen)
                #player.player_rectangle.topleft = (player.player_rectangle.topleft[0], -100)
                return next_biome
        return None
    
    def obstacles_in_biome(self, player:Player2, biome:Biome):
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
    
    def monster_attack(self, curr_biome:Biome, player:Player2, screen:pygame.display):
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
        
    def display_text(self, words_startx_starty:list, curr_biome:Biome, player:Player2, text_index:int, previous_text:list, screen:pygame.display):
        """
        start_y = 100 + text_index * 50
        size = self.font.size(words)
        start_x = (screen_width - size[0]) // 2
        """
        words = words_startx_starty[0]
        print(self.font.size(words)[0])
        start_x = words_startx_starty[1]
        start_y = words_startx_starty[2]
        for i in range(1, len(words) + 1):
            curr_biome.render(0, 0, player, screen)
            for t in previous_text:
                screen.blit(t[0], t[1])
                pygame.display.update()
            text = self.font.render(words[0:i], True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect = (start_x, start_y)
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.wait(80)
        return (text, text_rect)
        
        