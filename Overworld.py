from pygame import *
import os
from Room import *
from Constants import *
from Biome import *
from Player2 import *
from Obstacles import *
from Monster import *
from Kohli import *
from CricketNPC import *
from Auntieji import *
from Exit import *
from items.Ladoo import *
from items.Key import *
from Puri import *
from Bugle import *
from Auntieji import *
from CSPKid import *

from SRK import *
from Paparazzi import *
class Overworld(Room):
    
    def __init__(self):
        super().__init__(0, 0, 0)
        global auntie_clone1
        global auntie_clone2
        global auntie_clone3
        
        # set font
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        
        # game over screen
        self.game_over_screen = Biome("game_over", "game_over_screen.png", [], [], False)
        
        # create exit constants
        self.left_width = 10
        self.right_width = 85
        self.H_height = 150
        self.V_width = 150
        self.up_height = 10
        self.down_height = 35        
        
        # initialize the first level
        
        # create the rooms with obstacles
        self.room1 = Biome("room1", "floor1/room1.png", [], [("USE ARROW KEYS TO MOVE AROUND.", (screen_width - 612) // 2, 235), ("PRESS SPACE TO ATTACK.", (screen_width - 421) // 2, 535)], False)
        self.obstacle1 = Obstacles("test_object1.png", 0, 0, screen_width, 290)
        self.obstacle2 = Obstacles("test_object1.png", 0, 500, screen_width, 300)
        self.obstacle3 = Obstacles("test_object1.png", 0, 0, 50, screen_height)
        self.room1.add_obstacles([self.obstacle1, self.obstacle2, self.obstacle3])
        
        self.room2 = Biome("room2", "floor1/room2.png", [Exit(0, 380, self.room1, "left", self.left_width, self.H_height)], [("THE FIRST INGREDIENT IS IN THE EDEN GARDENS.", 15, 235), ("UNFORTUNATELY, THE INDIAN CRICKET TEAM IS VALIANTLY DEFENDING IT.", 15, 535)], False)
        self.obstacle4 = Obstacles("test_object1.png", 0, 0, 925, 290)
        self.obstacle5 = Obstacles("test_object1.png", 1200, 0, 400, screen_height)
        self.obstacle6 = Obstacles("test_object1.png", 0, 0, screen_width, 200)
        self.room2.add_obstacles([self.obstacle2, self.obstacle4, self.obstacle5, self.obstacle6])
        
        self.cricketroom1 = Biome("cricketroom1", "floor1/cricketroom1.png", [Exit(1000, screen_height, self.room2, "down", self.V_width, self.down_height)], [], False)
        self.obstacle7 = Obstacles("test_object1.png", 0, 0, 705, 150)
        self.obstacle8 = Obstacles("test_object1.png", 935, 0, screen_width-935, 150)
        self.obstacle9 = Obstacles("test_object1.png", screen_width-150, 0, 150, screen_height)
        self.obstacle10 = Obstacles("test_object1.png", screen_width-340, screen_height-155, 340, 155)
        self.obstacle11 = Obstacles("test_object1.png", 0, 290, 600, 200)
        self.obstacle12 = Obstacles("test_object1.png", 0, screen_height-155, 905, 155)
        self.cricketroom1.add_obstacles([self.obstacle7, self.obstacle8, self.obstacle9, self.obstacle10, self.obstacle11, self.obstacle12])
        self.cricketroom1.add_items(1)

        self.cricketroom2 = Biome("cricketroom2", "floor1/cricketroom2.png", [Exit(800, screen_height, self.cricketroom1, "down", self.V_width, self.down_height)], [], False)
        self.obstacle13 = Obstacles("test_object1.png", 0, 0, screen_width, 150)
        self.obstacle14 = Obstacles("test_object1.png", 935, screen_height-150, screen_width-935, 150)
        self.obstacle15 = Obstacles("test_object1.png", 0, screen_height-160, 705, 160)
        self.obstacle16 = Obstacles("test_object1.png", 0, 0, 150, screen_height)
        self.cricketroom2.add_obstacles([self.obstacle13, self.obstacle9, self.obstacle14, self.obstacle15, self.obstacle16])
        self.cricketroom2.add_items(1)

        self.cricketroom3 = Biome("cricketroom3", "floor1/cricketroom3.png", [Exit(screen_width, 200, self.cricketroom1, "right", self.right_width, self.H_height), Exit(screen_width, 600, self.cricketroom1, "right", self.right_width, self.H_height)], [], False)
        self.obstacle17 = Obstacles("test_object1.png", 0, screen_height-155, screen_width, 155)
        self.obstacle18 = Obstacles("test_object1.png", screen_width-600, 290, 600, 200)
        self.block_key1 = Obstacles("test_object1.png", 0, 0, screen_width, 150)
        self.cricketroom3.add_obstacles([self.obstacle7, self.obstacle8, self.obstacle17, self.obstacle16, self.obstacle18, self.block_key1])

        self.cricketroom4 = Biome("cricketroom4", "floor1/cricketroom4.png", [Exit(800, screen_height, self.cricketroom3, "down", self.V_width, self.down_height)], [], False)
        self.cricketroom4.add_obstacles([self.obstacle7, self.obstacle8, self.obstacle9, self.obstacle14, self.obstacle15, self.obstacle16, self.block_key1])
        
        self.cricketroom5 = Biome("cricketroom5", "floor1/cricketroom2.png", [Exit(800, screen_height, self.cricketroom4, "down", self.V_width, self.down_height)], [("YOU HAVE COLLECTED THE FIRST SPECIAL INGREDIENT, THE CHUTNEY!", 180, 200)], True, screen_width//2, 650)
        self.cricketroom5.add_obstacles([self.obstacle13, self.obstacle9, self.obstacle14, self.obstacle15, self.obstacle16])
        self.cricketroom5.add_ingredient(Ingredient("chutney.png", 800, 400))
        
        self.room1.add_exits([Exit(screen_width, 380, self.room2, "right", self.right_width, self.H_height)])
        self.room2.add_exits([Exit(1000, 185, self.cricketroom1, "up", self.V_width, self.down_height)])
        self.cricketroom1.add_exits([Exit(800, 0, self.cricketroom2, "up", self.V_width, self.up_height), Exit(0, 200, self.cricketroom3, "left", self.left_width, self.H_height), Exit(0, 600, self.cricketroom3, "left", self.left_width, self.H_height)])
        self.cricketroom3.add_exits([Exit(800, 0, self.cricketroom4, "up", self.V_width, self.up_height)])
        self.cricketroom4.add_exits([Exit(800, 0, self.cricketroom5, "up", self.V_width, self.up_height)])
        
        # create a monster
        self.monster1=Kohli(1.0,"Kohli", 800, 100)
        self.cricketroom4.add_monsters([self.monster1])

        npc_cricker_player_1=CricketNPC(10.0, 1, "NPC Cricket Player 1", 935, 150, "shoot and follow path")
        npc_cricker_player_1.path_coords=[(npc_cricker_player_1.start_pos_x, npc_cricker_player_1.start_pos_y), 
                                          (npc_cricker_player_1.start_pos_x+450, npc_cricker_player_1.start_pos_y), 
                                          (npc_cricker_player_1.start_pos_x+450, npc_cricker_player_1.start_pos_y+450), 
                                          (npc_cricker_player_1.start_pos_x, npc_cricker_player_1.start_pos_y+450)]
        self.cricketroom1.add_monsters([npc_cricker_player_1])


        npc_cricker_player_2=CricketNPC(1, 1, "NPC Cricket Player 2", 700, 500, "hit")
        self.cricketroom1.add_monsters([npc_cricker_player_2])

        npc_cricker_player_3=CricketNPC(1.0, 1, "NPC Cricket Player 3", 180, 150, "shoot and patrol")
        npc_cricker_player_3.patrol_direction="x"
        npc_cricker_player_3.patrol_distance=1220
        self.cricketroom2.add_monsters([npc_cricker_player_3])

        npc_cricker_player_4=CricketNPC(1.0, 1, "NPC Cricket Player 4", 700, 150, "hit")
        self.cricketroom2.add_monsters([npc_cricker_player_4])

        npc_cricker_player_5=CricketNPC(1.0, 1, "NPC Cricket Player 5", 250, 150, "shoot and patrol")
        npc_cricker_player_5.patrol_direction="y"
        npc_cricker_player_5.patrol_distance=520
        self.cricketroom2.add_monsters([npc_cricker_player_5])

        npc_cricker_player_6=CricketNPC(1.0, 1, "NPC Cricket Player 6", 690, 150, "shoot and follow path")
        npc_cricker_player_6.path_coords=[(npc_cricker_player_6.start_pos_x, npc_cricker_player_6.start_pos_y), 
                                          (npc_cricker_player_6.start_pos_x-520, npc_cricker_player_6.start_pos_y), 
                                          (npc_cricker_player_6.start_pos_x-520, npc_cricker_player_6.start_pos_y+470), 
                                          (npc_cricker_player_6.start_pos_x, npc_cricker_player_6.start_pos_y+470)]
        self.cricketroom3.add_monsters([npc_cricker_player_6])

        npc_cricker_player_7=CricketNPC(1.0, 1, "NPC Cricket Player 7", 190, 600, "hit")
        self.cricketroom3.add_monsters([npc_cricker_player_7])
        
        
        self.floor1rooms = [self.room1, self.room2, self.cricketroom1, self.cricketroom2, self.cricketroom3, self.cricketroom4, self.cricketroom5]
        
    
        # initialize the second level
        
        # create the rooms with obstacles
        self.houseroom1 = Biome("houseroom1", "floor2/houseroom1.png", [], [("THE SECOND INGREDIENT IS INSIDE", 110, 400), ("THE LADOO-CART AUNTIE'S HOUSE.", 110, 450), ("IT IS VERY VALUABLE, AND SHE", 900, 400), ("HAS GATHERED HER FRIENDS", 900, 450), ("TO PROTECT IT.", 900, 500)], False)
        self._21 = Obstacles("test_object1.png", 0, 0, screen_width//2 - 50, screen_height)
        self._22 = Obstacles("test_object1.png", screen_width//2 + 100, 0, screen_width//2 - 100, screen_height)
        self._23 = Obstacles("test_object1.png", 0, 700, screen_width, screen_height-700)
        self.houseroom1.add_obstacles([self._21, self._22, self._23])
        
        self.houseroom2 = Biome("houseroom2", "floor2/houseroom2.png", [Exit(screen_width//2, screen_height, self.houseroom1, "down", self.V_width, self.down_height)], [("REMEMBER, YOU CAN PICK UP THE LADOOS ON THE FLOOR TO HEAL YOURSELF!", 110, 45)], False)
        self._24 = Obstacles("test_object1.png", 0, 0, screen_width, 75) # H top band
        self._25 = Obstacles("test_object1.png", 0, screen_height-75, screen_width//2-140, 75) # H bottom left band
        self._26 = Obstacles("test_object1.png", 0, 0, 75, 290) # V left top band
        self._27 = Obstacles("test_object1.png", 0, screen_height-325, 75, 325) # V left bottom band
        self._28 = Obstacles("test_object1.png", screen_width-75, 0, 75, 290) # V right top band
        self._29 = Obstacles("test_object1.png", screen_width-75, screen_height-325, 75, 325) # V right bottom band
        self._210 = Obstacles("test_object1.png", screen_width//2 - 230, 100, 470, 330) # dining table
        self._211 = Obstacles("test_object1.png", screen_width//2+150, screen_height-75, screen_width//2-150, 75) # H bottom right band
        self.houseroom2.add_obstacles([self._24, self._25, self._26, self._27, self._28, self._29, self._210, self._211])
        
        self.houseroom3 = Biome("houseroom3", "floor2/houseroom3.png", [Exit(screen_width, screen_height//2, self.houseroom2, "right", self.right_width, self.H_height)], [], False)
        self._212 = Obstacles("test_object1.png", 0, screen_height-75, screen_width, 75) # H bottom band
        self._213 = Obstacles("test_object1.png", 0, 0, 75, screen_height) # V left band
        self._214 = Obstacles("test_object1.png", 0, 0, screen_width//2-50, screen_height//2-100) # machinery 1
        self._215 = Obstacles("test_object1.png", screen_width//2-40, 0, 125, screen_height//2-15) # machinery 2
        self._216 = Obstacles("test_object1.png", screen_width-470, screen_height-350, 470, 350) # machinery 3
        self.houseroom3.add_obstacles([self._24, self._212, self._213, self._28, self._29, self._214, self._215, self._216])
        
        self.houseroom4 = Biome("houseroom4", "floor2/houseroom4.png", [Exit(0, screen_height//2, self.houseroom2, "left", self.left_width, self.H_height)], [], False)
        self._217 = Obstacles("test_object1.png", 0, 0, screen_width//2-140, 75) # H top left band
        self._218 = Obstacles("test_object1.png", screen_width//2+150, 0, screen_width//2-150, 75) # H top right band
        self._219 = Obstacles("test_object1.png", screen_width-75, 0, 75, screen_height) # V right band
        self._220 = Obstacles("test_object1.png", 550, 280, 430, 520) # TV + couch
        self.block_key2_1 = Obstacles("test_object1.png", 0, 0, screen_width, 75)
        self.houseroom4.add_obstacles([self._212, self._217, self._218, self._219, self._26, self._27, self._220, self.block_key2_1])
        
        self.houseroom5 = Biome("houseroom5", "floor2/houseroom5.png", [Exit(770, screen_height, self.houseroom4, "down", self.V_width, self.down_height)], [], False)
        self._221 = Obstacles("test_object1.png", 520, 160, 320, 330) # bed
        self._222 = Obstacles("test_object1.png", 880, 90, 180, 260) # table
        self.houseroom5.add_obstacles([self._24, self._219, self._26, self._27, self._25, self._211, self._221, self._222])
        
        self.houseroom6 = Biome("houseroom6", "floor2/houseroom6.png", [Exit(screen_width, 380, self.houseroom5, "right", self.right_width, self.H_height)], [], False)
        self.block_key2_2 = Obstacles("test_object1.png", 0, 0, 75, screen_height)
        self.houseroom6.add_obstacles([self._24, self._212, self._26, self._27, self._28, self._29, self.block_key2_2])
        
        self.houseroom7 = Biome("houseroom7", "floor2/houseroom7.png", [Exit(screen_width, 380, self.houseroom6, "right", self.right_width, self.H_height)], [("YOU HAVE COLLECTED THE SECOND SPECIAL INGREDIENT, THE BATTER!", 180, 45)], True, screen_width//2, 650)
        self.houseroom7.add_obstacles([self._24, self._212, self._28, self._29, self._213])
        
        self.houseroom1.add_exits([Exit(screen_width//2, 380, self.houseroom2, "up", self.V_width, self.up_height)])
        self.houseroom2.add_exits([Exit(0, screen_height//2, self.houseroom3, "left", self.left_width, self.H_height), Exit(screen_width, screen_height//2, self.houseroom4, "right", self.right_width, self.H_height)])
        self.houseroom4.add_exits([Exit(770, 0, self.houseroom5, "up", self.V_width, self.up_height)])
        self.houseroom5.add_exits([Exit(0, 380, self.houseroom6, "left", self.left_width, self.H_height)])
        self.houseroom6.add_exits([Exit(0, 380, self.houseroom7, "left", self.left_width, self.H_height)])
        self.houseroom6.add_ingredient(Ingredient("flour.png", 800, 400))
        
        #auntie monsters
        auntie1 = Auntieji(1.0, 10.0, "OG Auntie", 200, 100, 0, 0)
        self.houseroom6.add_monsters([auntie1])
        self.floor2rooms = [self.houseroom1, self.houseroom2, self.houseroom3, self.houseroom4, self.houseroom5, self.houseroom6, self.houseroom7]
        
        # initialize the third level
        
        # create the rooms with obstacles
        self.galaroom1 = Biome("galaroom1", "floor3/galaroom1.png", [], [("THE THIRD INGREDIENT IS HELD BY A FAMOUS ACTOR WHO COLLECTED IT DURING", 60, 695), ("HIS TRAVELS. HE DOES NOT SEEM TOO KEEN TO GIVE IT UP HOWEVER.", 160, 740)], False)
        self.left_crowd3 = Obstacles("test_object1.png", 0, 0, 415, screen_height)
        self.right_crowd3 = Obstacles("test_object1.png", 1120, 0, screen_width-1120, screen_height)
        self.bottom3 = Obstacles("test_object1.png", 0, 680, screen_width, screen_height-680)
        self.galaroom1.add_obstacles([self.left_crowd3, self.right_crowd3, self.bottom3])
        
        self.galaroom2 = Biome("galaroom2", "floor3/galaroom2.png", [Exit(screen_width//2, screen_height, self.galaroom1, "down", 500, self.down_height)], [], False)    
        self.top3 = Obstacles("test_object1.png", 0, 0, screen_width, 280)
        self.bottom_right_corner3 = Obstacles("test_object1.png", 1120, 520, screen_width-1120, screen_height-520)
        self.galaroom2.add_obstacles([self.left_crowd3, self.top3, self.bottom_right_corner3])
        
        self.galaroom3 = Biome("galaroom3", "floor3/galaroom3.png", [Exit(0, screen_height//2, self.galaroom2, "left", self.left_width, self.H_height)], [], False)    
        self.H_left_top_band3 = Obstacles("test_object1.png", 0, 0, 675, 110)
        self.H_right_top_band3 = Obstacles("test_object1.png", 1010, 0, screen_width-1010, 110)
        self.bar3 = Obstacles("test_object1.png", 1210, 0, screen_width-1170, screen_height)
        self.H_bottom_band3 = Obstacles("test_object1.png", 0, screen_height-110, screen_width, 110)
        self.V_top_left_band3 = Obstacles("test_object1.png", 0, 0, 105, 280)
        self.V_bottom_left_band3 = Obstacles("test_object1.png", 0, 520, 105, screen_height-520)
        self.galaroom3.add_obstacles([self.H_left_top_band3, self.H_right_top_band3, self.bar3, self.H_bottom_band3, self.V_top_left_band3, self.V_bottom_left_band3])
        
        self.galaroom4 = Biome("galaroom4", "floor3/galaroom4.png", [Exit(820, screen_height, self.galaroom3, "down", self.V_width, self.down_height)], [], False)    
        self.H_top_band3 = Obstacles("test_object1.png", 0, 0, screen_width, 110)
        self.V_top_right_band3 = Obstacles("test_object1.png", screen_width-105, 0, 105, 280)
        self.V_bottom_right_band3 = Obstacles("test_object1.png", screen_width-105, 520, 105, screen_height-520)
        self.H_left_bottom_band3 = Obstacles("test_object1.png", 0, screen_height-110, 675, 110)
        self.H_right_bottom_band3 = Obstacles("test_object1.png", 1010, screen_height-110, screen_width-1010, 110)
        self.left_table3 = Obstacles("test_object1.png", 230, 180, 215, 190)
        self.right_table3 = Obstacles("test_object1.png", 1040, 390, 215, 190)
        self.block_key3_1 = Obstacles("test_object1.png", screen_width-105, 0, 105, screen_height)
        self.galaroom4.add_obstacles([self.H_top_band3, self.V_top_right_band3, self.V_bottom_right_band3, self.H_right_bottom_band3, self.H_left_bottom_band3, self.V_bottom_left_band3, self.V_top_left_band3, self.left_table3, self.right_table3, self.block_key3_1])
        
        self.galaroom5 = Biome("galaroom5", "floor3/galaroom5.png", [Exit(screen_width, screen_height//2, self.galaroom4, "right", self.right_width, self.H_height)], [], False)    
        self.V_left_band3 = Obstacles("test_object1.png", 0, 0, 105, screen_height)
        self.disco_ball3 = Obstacles("test_object1.png", 770, 110, 140, 150)
        self.dj3 = Obstacles("test_object1.png", 0, 420, 540, screen_height-420)
        self.galaroom5.add_obstacles([self.H_top_band3, self.V_top_right_band3, self.V_bottom_right_band3, self.H_bottom_band3, self.V_left_band3, self.disco_ball3, self.dj3])
        
        self.galaroom6 = Biome("galaroom6", "floor3/galaroom6.png", [Exit(0, screen_height//2, self.galaroom4, "left", self.left_width, self.H_height)], [("THE FAMOUS ACTOR IS SHAH RUKH KHAN!", 420, 40)], False)    
        self.galaroom6.add_obstacles([self.H_top_band3, self.V_top_right_band3, self.V_bottom_right_band3, self.H_bottom_band3, self.V_bottom_left_band3, self.V_top_left_band3, self.block_key3_1])
        
        self.galaroom7 = Biome("galaroom7", "floor3/galaroom7.png", [Exit(0, screen_height//2, self.galaroom6, "left", self.left_width, self.H_height)], [("YOU HAVE COLLECTED THE THIRD SPECIAL INGREDIENT, THE FILLING!", 200, 60)], True, screen_width//2, 700)    
        self.V_right_band3 = Obstacles("test_object1.png", screen_width-105, 0, 105, screen_height)
        self.galaroom7.add_obstacles([self.H_top_band3, self.V_right_band3, self.H_bottom_band3, self.V_bottom_left_band3, self.V_top_left_band3])
        self.galaroom7.add_ingredient(Ingredient("potato.png", 800, 400))
        
        self.galaroom1.add_exits([Exit(screen_width//2, 0, self.galaroom2, "up", 500, self.up_height)])
        self.galaroom2.add_exits([Exit(1231, screen_height//2, self.galaroom3, "right", self.right_width, self.H_height)])
        self.galaroom3.add_exits([Exit(820, 0, self.galaroom4, "up", self.V_width, self.up_height)])
        self.galaroom4.add_exits([Exit(0, screen_height//2, self.galaroom5, "left", self.left_width, self.H_height), Exit(screen_width, screen_height//2, self.galaroom6, "right", self.right_width, self.H_height)])
        self.galaroom6.add_exits([Exit(screen_width, screen_height//2, self.galaroom7, "right", self.right_width, self.H_height)])
        
        self.floor3rooms = [self.galaroom1, self.galaroom2, self.galaroom3, self.galaroom4, self.galaroom5, self.galaroom6, self.galaroom7]#add SRK monster
        shah_rukh = SRK(1.0, 30.0, pygame.image.load(os.path.join("Assets", "SRK_sprite.png")), "SRK", 400, 300, 100, 50, ["paralyze"], "flappybird.png", 10, 10)
        self.galaroom6.add_monsters([shah_rukh])

        #add paparazzi minibosses to all other rooms
        pap1 = Paparazzi(1.0, 1.0, pygame.image.load(os.path.join("Assets", "paparazzi1.png")), "pap1", 100, 50, 100, 50)
        pap2 = Paparazzi(1.0, 1.0, pygame.image.load(os.path.join("Assets", "paparazzi2.png")), "pap1", 100, 50, 300, 100)
        self.galaroom3.add_monsters([pap1,pap2])
        pap3 = Paparazzi(1.0, 1.0, pygame.image.load(os.path.join("Assets", "paparazzi1.png")), "pap1", 100, 50, 100, 50)
        pap4 = Paparazzi(1.0, 1.0, pygame.image.load(os.path.join("Assets", "paparazzi2.png")), "pap1", 100, 50, 300, 100)
        self.galaroom4.add_monsters([pap3, pap4])
        pap5 = Paparazzi(1.0, 1.0, pygame.image.load(os.path.join("Assets", "paparazzi1.png")), "pap1", 100, 50, 100, 50)
        pap6 = Paparazzi(1.0, 1.0, pygame.image.load(os.path.join("Assets", "paparazzi2.png")), "pap1", 100, 50, 100, 600)
        self.galaroom5.add_monsters([pap5, pap6])

        # initialize the fourth level
        
        # create the rooms with obstacles
        self.schoolroom1 = Biome("schoolroom1", "floor4/schoolroom1.png", [], [("NOW, HAVING ASSEBMLED THE", 10, 505), ("RECIPE, IT IS TIME TO DELIVER THE", 10, 555), ("SAMOSAS TO MR. PURI AT EASTLAKE.", 10, 605), ("HOPEFULLY, THE LEGENDS HOLD", 945, 505), ("TRUE AND HE CHANGES", 945, 555), ("YOUR GRADE.", 945, 605)], False)
        self.left_side4 = Obstacles("test_object1.png", 0, 0, 630, screen_height)
        self.right_side4 = Obstacles("test_object1.png", 925, 0, screen_width-925, screen_height)
        self.bottom4 = Obstacles("test_object1.png", 660, 790, 950-660, 10)
        self.left_school_side4 = Obstacles("test_object1.png", 0, 0, 660, 430)
        self.right_school_side4 = Obstacles("test_object1.png", 880, 0, screen_width-880, 430)
        self.schoolroom1.add_obstacles([self.left_side4, self.right_side4, self.bottom4, self.left_school_side4, self.right_school_side4])

        
        self.schoolroom2 = Biome("schoolroom2", "floor4/schoolroom2.png", [Exit(screen_width//2, screen_height, self.schoolroom1, "down", self.V_width, self.down_height)], [], False)
        self.H_top_band4 = Obstacles("test_object1.png", 0, 0, screen_width, 100)
        self.V_right_band4 = Obstacles("test_object1.png", screen_width-100, 0, 100, screen_height)
        self.H_left_bottom_band4 = Obstacles("test_object1.png", 0, 700, 660, 100)
        self.H_right_bottom_band4 = Obstacles("test_object1.png", 880, 700, screen_width-880, 100)
        self.V_top_left_band4 = Obstacles("test_object1.png", 0, 0, 100, 290)
        self.V_bottom_left_band4 = Obstacles("test_object1.png", 0, 490, 100, screen_height-490)
        self.stairs4 = Obstacles("test_object1.png", 950, 190, screen_width-950, 530-190)
        self.schoolroom2.add_obstacles([self.H_top_band4, self.V_right_band4, self.H_left_bottom_band4, self.H_right_bottom_band4, self.V_top_left_band4, self.V_bottom_left_band4, self.stairs4])
        
        csp_kid_1=CSP_Kid(1, 1, 200, 120, "shoot and patrol")
        csp_kid_1.patrol_direction="x"
        csp_kid_1.patrol_distance=700
        self.schoolroom2.add_monsters([csp_kid_1])

        csp_kid_2=CSP_Kid(1, 1, 900, 120, "shoot and patrol")
        csp_kid_2.patrol_direction="x"
        csp_kid_2.patrol_distance=-700
        self.schoolroom2.add_monsters([csp_kid_2])


        self.schoolroom3 = Biome("schoolroom3", "floor4/schoolroom3.png", [Exit(screen_width, screen_height//2, self.schoolroom2, "right", self.right_width, self.H_height)], [], False)
        self.H_left_top_band4 = Obstacles("test_object1.png", 0, 0, 660, 100)
        self.H_right_top_band4 = Obstacles("test_object1.png", 880, 0, screen_width-880, 100)
        self.V_top_right_band4 = Obstacles("test_object1.png", screen_width-100, 0, 100, 290)
        self.V_bottom_right_band4 = Obstacles("test_object1.png", screen_width-100, 490, 100, screen_height-490)
        self.top_crowd4 = Obstacles("test_object1.png", 230, 130, 240, 230)
        self.bottom_crowd4 = Obstacles("test_object1.png", 910, 370, 340, 250)
        self.block_key4_1 = Obstacles("test_object1.png", 0, 0, 100, screen_height)
        self.schoolroom3.add_obstacles([self.H_left_top_band4, self.H_right_top_band4, self.V_top_right_band4, self.V_bottom_right_band4, self.H_left_bottom_band4, self.H_right_bottom_band4, self.V_top_left_band4, self.V_bottom_left_band4, self.top_crowd4, self.bottom_crowd4, self.block_key4_1])
        
        csp_kid_3=CSP_Kid(1, 1, 200, 120, "hit")
        self.schoolroom3.add_monsters([csp_kid_3])


        csp_kid_4=CSP_Kid(1, 1, 800, 120, "hit")
        self.schoolroom3.add_monsters([csp_kid_4])

        csp_kid_5=CSP_Kid(1, 1, 200, 500, "hit")
        self.schoolroom3.add_monsters([csp_kid_5])

        # csp_kid_3=CSP_Kid(1, 1, 900, 120, "shoot and patrol")
        # csp_kid_3.patrol_direction="x"
        # csp_kid_3.patrol_distance=-700
        # self.schoolroom3.add_monsters([csp_kid_3])




        self.schoolroom4 = Biome("schoolroom4", "floor4/schoolroom4.png", [Exit(screen_width//2, screen_height, self.schoolroom3, "down", self.V_width, self.down_height)], [], False)
        self.crowd4 = Obstacles("test_object1.png", 940, 150, 310, 360)
        self.schoolroom4.add_obstacles([self.H_top_band4, self.V_right_band4, self.H_left_bottom_band4, self.H_right_bottom_band4, self.V_top_left_band4, self.V_bottom_left_band4, self.crowd4])
        
        csp_kid_6=CSP_Kid(1, 1, 200, 120, "shoot and patrol")
        csp_kid_6.patrol_direction="y"
        csp_kid_6.patrol_distance=550
        self.schoolroom4.add_monsters([csp_kid_6])

        csp_kid_7=CSP_Kid(1, 1, 200, 120, "shoot and patrol")
        csp_kid_7.patrol_direction="x"
        csp_kid_7.patrol_distance=700
        self.schoolroom4.add_monsters([csp_kid_7])

        
        self.schoolroom5 = Biome("schoolroom5", "floor4/schoolroom5.png", [Exit(screen_width, screen_height//2, self.schoolroom4, "right", self.right_width, self.H_height)], [], False)
        self.H_bottom_band4 = Obstacles("test_object1.png", 0, screen_height-100, screen_width, 100)
        self.V_left_band4 = Obstacles("test_object1.png", 0, 0, 100, screen_height)
        self.left_bookcase4 = Obstacles("test_object1.png", 360, 290, 140, 200)
        self.middle_bookcase4 = Obstacles("test_object1.png", 710, 290, 140, 200)
        self.right_bookcase4 = Obstacles("test_object1.png", 1060, 290, 140, 200)
        self.schoolroom5.add_obstacles([self.H_top_band4, self.V_top_right_band4, self.V_bottom_right_band4, self.H_bottom_band4, self.V_left_band4, self.left_bookcase4, self.middle_bookcase4, self.right_bookcase4])
        

        csp_kid_8=CSP_Kid(1, 1, 200, 120, "shoot and follow path")
        csp_kid_8.path_coords=[(csp_kid_8.start_pos_x, csp_kid_8.start_pos_y), 
                                          (csp_kid_8.start_pos_x+400, csp_kid_8.start_pos_y), 
                                          (csp_kid_8.start_pos_x+400, csp_kid_8.start_pos_y+550), 
                                          (csp_kid_8.start_pos_x, csp_kid_8.start_pos_y+550),
                                          (csp_kid_8.start_pos_x, csp_kid_8.start_pos_y)]
        self.schoolroom5.add_monsters([csp_kid_8])

        csp_kid_9=CSP_Kid(1, 1, 570, 120, "shoot and follow path")
        csp_kid_9.path_coords=[(csp_kid_9.start_pos_x, csp_kid_9.start_pos_y), 
                                          (csp_kid_9.start_pos_x+400, csp_kid_9.start_pos_y), 
                                          (csp_kid_9.start_pos_x+400, csp_kid_9.start_pos_y+550), 
                                          (csp_kid_9.start_pos_x, csp_kid_9.start_pos_y+550),
                                          (csp_kid_9.start_pos_x, csp_kid_9.start_pos_y)]
        self.schoolroom5.add_monsters([csp_kid_9])

        self.schoolroom6 = Biome("schoolroom6", "floor4/schoolroom6.png", [Exit(screen_width, screen_height//2, self.schoolroom3, "right", self.right_width, self.H_height)], [], False)
        self.bookcases4 = Obstacles("test_object1.png", 0, 350, 710, 90)
        self.top_bookcase4 = Obstacles("test_object1.png", 1000, 150, 300, 80)
        self.bottom_bookcase4 = Obstacles("test_object1.png", 1000, 560, 300, 80)
        self.schoolroom6.add_obstacles([self.H_top_band4, self.V_top_right_band4, self.V_bottom_right_band4, self.H_bottom_band4, self.V_left_band4, self.bookcases4, self.top_bookcase4, self.bottom_bookcase4])
        
        csp_kid_10=CSP_Kid(1, 1, 200, 120, "shoot and patrol")
        csp_kid_10.patrol_direction="x"
        csp_kid_10.patrol_distance=700
        self.schoolroom6.add_monsters([csp_kid_10])

        csp_kid_11=CSP_Kid(1, 1, 200, 550, "shoot and patrol")
        csp_kid_11.patrol_direction="x"
        csp_kid_11.patrol_distance=700
        self.schoolroom6.add_monsters([csp_kid_11])


        self.schoolroom7 = Biome("schoolroom7", "floor4/schoolroom7.png", [Exit(screen_width//2, 0, self.schoolroom3, "up", self.V_width, self.up_height)], [], False)
        self.left_crowd4 = Obstacles("test_object1.png", 220, 210, 310, 240)
        self.right_crowd4 = Obstacles("test_object1.png", 860, 370, 190, 240)
        self.block_key4_2 = Obstacles("test_object1.png", screen_width-100, 0, 100, screen_height)
        self.schoolroom7.add_obstacles([self.H_left_top_band4, self.H_right_top_band4, self.V_top_right_band4, self.V_bottom_right_band4, self.H_bottom_band4, self.V_left_band4, self.left_crowd4, self.right_crowd4, self.block_key4_2])
        
        csp_kid_12=CSP_Kid(1, 1, 1300, 120, "shoot and patrol")
        csp_kid_12.patrol_direction="y"
        csp_kid_12.patrol_distance=500
        self.schoolroom7.add_monsters([csp_kid_12])

        csp_kid_13=CSP_Kid(1, 1, 900, 600, "hit")
        self.schoolroom7.add_monsters([csp_kid_13])

        csp_kid_14=CSP_Kid(1, 1, 1300, 600, "hit")
        self.schoolroom7.add_monsters([csp_kid_14])


        self.schoolroom8 = Biome("schoolroom8", "floor4/schoolroom8.png", [Exit(0, screen_height//2, self.schoolroom7, "left", self.left_width, self.H_height)], [("FINALLY, YOU ARE IN MR. PURI'S ROOM. TIME TO DELIVER THE SAMOSA.", 190, 45)], False)
        self.top_computers4 = Obstacles("test_object1.png", 220, 120, 900, 180)
        self.bottom_computers4 = Obstacles("test_object1.png", 220, 470, 900, 180)
        self.teacher4 = Obstacles("test_object1.png", 1240, 170, screen_width-1240, 370)
        self.schoolroom8.add_obstacles([self.H_top_band4, self.V_right_band4, self.H_bottom_band4, self.V_top_left_band4, self.V_bottom_left_band4, self.top_computers4, self.bottom_computers4, self.teacher4])
        

        csp_kid_15=CSP_Kid(1, 1, 1000, 300, "walk")
        self.schoolroom8.add_monsters([csp_kid_15])

        self.schoolroom9 = Biome("schoolroom9", "floor4/schoolroom9.png", [], [], False)
        self.schoolroom9.add_obstacles([self.H_top_band4, self.V_right_band4, self.H_bottom_band4, self.V_left_band4])
        
        self.schoolroom1.add_exits([Exit(740, 410, self.schoolroom2, "up", 90, self.up_height)])
        self.schoolroom2.add_exits([Exit(0, screen_height//2, self.schoolroom3, "left", self.left_width, self.H_height)])
        self.schoolroom3.add_exits([Exit(screen_width//2, 0, self.schoolroom4, "up", self.V_width, self.up_height), Exit(0, screen_height//2, self.schoolroom6, "left", self.left_width, self.H_height), Exit(screen_width//2, screen_height, self.schoolroom7, "down", self.V_width, self.down_height)])
        self.schoolroom4.add_exits([Exit(0, screen_height//2, self.schoolroom5, "left", self.left_width, self.H_height)])
        self.schoolroom7.add_exits([Exit(screen_width, screen_height//2, self.schoolroom8, "right", self.right_width, self.H_height)])

        puri=Puri(10.0,"Puri", 800, 100)
        self.schoolroom9.add_monsters([puri])

        self.floor4rooms = [self.schoolroom1, self.schoolroom2, self.schoolroom3, self.schoolroom4, self.schoolroom5, self.schoolroom6, self.schoolroom7, self.schoolroom8, self.schoolroom9]
        
        
        

    auntie_clone1 = AuntieClone(3.0, 6.0, pygame.image.load(os.path.join("Assets", "auntieclone1.png")), "auntie_clone 1", 100, 50, 0, 0)
    auntie_clone2 = AuntieClone(3.0, 6.0, pygame.image.load(os.path.join("Assets", "auntieclone2.png")), "auntie_clone 1", 100, 50, 0, 0)
    auntie_clone3 = AuntieClone(3.0, 6.0, pygame.image.load(os.path.join("Assets", "auntieclone3.png")), "auntie_clone 1", 100, 50, 0, 0)
    #add clones when auntie is at half health
    def add_clones(self, player, clones = [auntie_clone1, auntie_clone2, auntie_clone3]):
        self.set_auntie_clone_coords(player, clones)
        self.houseroom6.add_monsters(clones)
    #set auntie coordinates based on player
    def set_auntie_coordinates(self, player: Player2, auntie: Auntieji):
        auntie.start_pos_x, auntie.start_pos_y = player.player_rectangle.x + 450, player.player_rectangle.y
    
    def set_auntie_clone_coords(self, player:Player2, clones:list):
        coord_modifiers = [(0,-450), (450,0), (-450,0)]
        i = 0
        for clone in clones:
            clone.monster_rectangle.x, clone.monster_rectangle.y = player.player_rectangle.x + coord_modifiers[i][0], player.player_rectangle.y + coord_modifiers[i][1]
            i+=1
    
    # add burnie obstacles
    burnie1 = Obstacles("burnie_sanders.png", 100, 200, 100, 100)
    burnie2 = Obstacles("burnie_sanders.png", 300, 300, 100, 100)
    burnie3 = Obstacles("burnie_sanders.png", 100, 500, 100, 100)
        
    def add_burnie_sanders(self, screen, burnies:list = [burnie1, burnie2, burnie3]):
        self.galaroom3.add_obstacles_with_img(burnies, screen)
    
    
    def game_over(self, screen:pygame.display):
        img = pygame.image.load(os.path.join("Assets", "game_over_screen.png"))
        image = pygame.transform.scale(img, (screen_width, screen_height))
        screen.blit(image, (0, 0))
        pygame.display.update()
        
    def transition_next_level(self, player:Player2, curr_screen:Biome, screen:pygame.display):
        if curr_screen.last_room:
            monster = None
            if curr_screen == self.cricketroom5:
                monster = self.monster1
                next_screen = self.houseroom1
            elif curr_screen == self.houseroom1:
                next_screen = self.galaroom1
            else:
                next_screen = self.schoolroom1
            image = next_screen.get_image()
            screen.fill((0, 0, 0))
            pygame.display.update()
            pygame.time.wait(500)
            """
            for i in range(30, 1, -2):
                screen.blit(image, ((screen_width - screen_width/i)//2, 0), ((screen_width - screen_width/i)//2, 0, screen_width//i, screen_height))
                pygame.display.update()
                pygame.time.wait(150)
            """
            for i in range(1, 11):
                screen.blit(image, ((screen_width - screen_width//10*i)//2, 0), ((screen_width - screen_width//10*i)//2, 0, screen_width//10*i, screen_height))
                pygame.display.update()
                pygame.time.wait(300)
            player.player_rectangle.topleft = (curr_screen.new_level_x, curr_screen.new_level_y)
            player.health_bar = 5
            return next_screen
        return None
    
    def going_to_next_biome(self, player:Player2, biome:Biome, curr_screen_x_pos:int, curr_screen_y_pos:int, screen:pygame.display):    
        curr_biome = biome
        for exit in curr_biome.exits:
            if (player.player_rectangle.topleft[0] < exit.x + exit.width and player.player_rectangle.topleft[0] > exit.x - exit.width) and (player.player_rectangle.topleft[1] < exit.y + exit.height and player.player_rectangle.topleft[1] > exit.y - exit.height):
                curr_health = player.health_bar
                # moving down or up
                if (exit.player_direction == "down" or exit.player_direction == "up"):
                    if exit.player_direction == "down":
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
                        exit.next_room.render(curr_screen_x_pos, y_pos, player, screen)
                        new_y = player.player_rectangle.topleft[1] + change
                        player.player_rectangle.topleft = (player.player_rectangle.topleft[0], new_y)
                        player.render(player.player_rectangle.topleft[0], player.player_rectangle.topleft[1], screen)
                        count -= 100
                        pygame.display.update()
                        pygame.time.wait(10)
                    if exit.player_direction == "down":
                        new_y = 11
                    else:
                        new_y = screen_height - player.player_rectangle[3]
                    player.player_rectangle.topleft = (player.player_rectangle.topleft[0], new_y)
                    player.render(player.player_rectangle.topleft[0], player.player_rectangle.topleft[1], screen)
                    pygame.display.update()
                    if curr_biome == self.cricketroom1 and exit.player_direction == "down":
                        player.player_rectangle.topleft = (player.player_rectangle.topleft[0], 220)
                    if curr_biome == self.houseroom2 and exit.player_direction == "down":
                        player.player_rectangle.topleft = (750, 400)
                    if curr_biome == self.schoolroom2 and exit.player_direction == "down":
                        player.player_rectangle.topleft = (player.player_rectangle.topleft[0], 421)
                # moving left or right
                else:
                    if exit.player_direction == "right":
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
                        exit.next_room.render(x_pos, curr_screen_y_pos, player, screen)
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
                    if curr_biome == self.galaroom3 and exit.player_direction == "left":
                        player.player_rectangle.topleft = (1140, player.player_rectangle.topleft[1])
                exit.next_room.render(0, 0, player, screen)
                player.health_bar = curr_health
                return exit.next_room
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
                
                mon_alive+=1

                #find auntie
                if isinstance(m, Auntieji):
                    if m.are_clones:
                        self.add_clones(player)
                        m.are_clones = False

                # #find SRK
                if isinstance(m, SRK):
                    if m.add_burnie:
                        self.add_burnie_sanders(screen)
                        print("burnies have been added")
                        m.add_burnie = False

                # check if paralyzing to spam SRK shirtless image
                    if m.paralyzing:
                        srk_img = pygame.image.load(os.path.join("Assets/", "funny_SRK_img.png"))
                        image = pygame.transform.scale(srk_img, (100, 100))
                        screen.blit(image, (0,0))
                        screen.blit(image, (0, 400))
                        screen.blit(image, (600, 0))
                        screen.blit(image, (0,400))

                #if player kills srk while in paralyze, unparalyze
                    if not m.alive:
                        m.paralyzing = False

                # If the player isn't attacking and they touch monster, they should take damage

                if player.player_rectangle.colliderect(m.monster_rectangle) and not player.attacking:

                    # Kohli has more cooldowns, so the player cannot take damage if the Kohli is in a cooldown

                    if isinstance(m, Kohli):
                        if not m.in_initial_cooldown or not m.in_post_attack_cooldown:
                            
                            # Calculating the time between attacks again as a cooldown

                            now = pygame.time.get_ticks()
                            if now - m.last_damage >= Constants.monster_attack_cooldown_count or m.first_time_attacking:
                                if not m.in_hit_cooldown:
                                    m.last_damage = now
                                    
                                    player.get_attacked(m.current_attack_damage, screen)
                                    m.first_time_attacking=False
                    
                    if isinstance(m, Puri):
                        if not m.in_normal_cooldown:
                            
                            # Calculating the time between attacks again as a cooldown

                            now = pygame.time.get_ticks()
                            if now - m.last_damage >= Constants.monster_attack_cooldown_count or m.first_time_attacking:
                                if not m.in_hit_cooldown:
                                    m.last_damage = now
                                    
                                    player.get_attacked(m.current_attack_damage, screen)
                                    m.first_time_attacking=False

                    else:

                        # Same cooldown logic if not Kohli

                        now = pygame.time.get_ticks()
                        if now -m.last_damage >= Constants.monster_attack_cooldown_count or m.first_time_attacking:
                            if not m.in_hit_cooldown:
                                m.last_damage = now
                                player.get_attacked(m.current_attack_damage, screen)
                                m.first_time_attacking=False
                    
                # Projectile is realigned and player takes damage if player gets hit by projectile

                if player.player_rectangle.colliderect(m.projectile.projectile_rectangle):
                    if isinstance(m, Puri) or m.stop_moving:
                        now = pygame.time.get_ticks()
                        if now -m.last_damage >= Constants.monster_attack_cooldown_count or m.first_time_attacking:
                            if not m.in_hit_cooldown:
                                m.last_damage = now
                                m.realign_projectile()
                                m.current_attack_damage=m.projectile.damage
                                player.get_attacked(m.current_attack_damage, screen)
                                m.stop_moving=False
                                m.first_time_attacking=False    
                
                
            return False, monsters
        else:
            return True, monsters
        
    def display_text(self, words_startx_starty:list, curr_biome:Biome, player:Player2, text_index:int, previous_text:list, screen:pygame.display):
        """
        start_y = 100 + text_index * 50
        size = self.font.size(words)
        start_x = (screen_width - size[0]) // 2
        """
        words = words_startx_starty[0]
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
            pygame.time.wait(1)
            pygame.time.wait(1)
        return (text, text_rect)     

    def picksupitems(self, player:Player2, biome:Biome, screen:pygame.display):
        for item in biome.items:
            if item.used == False and item.item_type == "ingredient" and player.player_rectangle.colliderect(item.item_rectangle):
                item.used = True
                next_screen = self.transition_next_level(player, biome, screen)
                return next_screen
            else: 
                player.get_healed(item)

    def pickupkeys(self, player:Player2, biome:Biome):
        for key in biome.keys:
            player.get_key(key)

    def notunlocked(self, biome):
        if biome.file_path[-12:-4] != "unlocked":
            return True
        return False

    def unlockroom(self, player, biome, screen):
        for key in player.key_inventory:            
            if not key.used and key.biomeunlock == biome and self.notunlocked(biome):
                #reset biome.file_path to unlocked version (should be initial file path + unlocked)
                player.key_inventory.remove(key)
                key.used = True
                key.pickedup = False
                key.x_pos = player.player_rectangle.topleft[0]
                key.y_pos = player.player_rectangle.topleft[1]
                for i in range(10):
                    self.flykey(biome,  player,key, screen, i)
                key.pickedup = True
                biome.file_path = biome.file_path[:-4] + "unlocked.png"
                del biome.obstacles[-1]
                del biome.obstacles_rect[-1]
                break

    def flykey(self, biome, player, key, screen, i):
        if key.k_x_pos > key.x_pos:
            key.x_pos = key.x_pos + (key.k_x_pos - key.x_pos) * i/10
        else: key.x_pos = key.x_pos - (key.x_pos - key.k_x_pos) * i/10
        if key.k_y_pos > key.y_pos:
            key.y_pos = key.y_pos + (key.k_y_pos - key.y_pos) * i/10
        else: key.y_pos = key.y_pos - (key.y_pos - key.k_y_pos) * i/10
        biome.render(0, 0, player, screen)
        key.render(screen)
        pygame.display.update()
        pygame.time.wait(200)
    
    def nomonstersalive(self, biome):
        for m in biome.monsters:
            if m.alive:
                return False
        return True

    def monsterkeydrop(self, player, biome):
        for m in biome.monsters:
            if m.alive:
                return
            if m.monster_type == "Mini Boss":
                if len(player.key_inventory) == 0 and biome.name.startswith("cricket"):
                    if random.randint(0, 9) > 7:
                        biome.add_key(Key(self.cricketroom3, m.monster_rectangle.x, m.monster_rectangle.y, 800, 100))
                elif len(player.key_inventory) == 0 and biome.name.startswith("house") and self.notunlocked(self.cricketroom3):
                    if random.randint(0, 9) > 7:
                        biome.add_key(Key(self.houseroom4, m.monster_rectangle.x, m.monster_rectangle.y, 800, 100))
                elif len(player.key_inventory) == 0 and biome.name.startswith("gala") and self.notunlocked(self.galaroom4):
                    if random.randint(0, 9) > 7:
                        biome.add_key(Key(self.galaroom4, m.monster_rectangle.x, m.monster_rectangle.y, 1400, 400))
                elif len(player.key_inventory) == 0 and biome.name.startswith("schoolroom6") and self.notunlocked(self.schoolroom6):
                    if random.randint(0, 9) > 7:
                        biome.add_key(Key(self.schoolroom7, m.monster_rectangle.x, m.monster_rectangle.y, 1400, 400))
                elif len(player.key_inventory) == 0 and biome.name.startswith("school") and self.notunlocked(self.schoolroom3):
                    if random.randint(0, 9) > 7:
                        biome.add_key(Key(self.schoolroom3, m.monster_rectangle.x, m.monster_rectangle.y, 100, 400))
            else:
                if biome.name.startswith("cricket"):
                    biome.add_key(Key(self.cricketroom4, m.monster_rectangle.x, m.monster_rectangle.y, 800, 100))
                elif biome.name.startswith("house"):
                    biome.add_key(Key(self.houseroom6, m.monster_rectangle.x, m.monster_rectangle.y, 100, 400))
                elif biome.name.startswith("gala"):
                    biome.add_key(Key(self.galaroom6, m.monster_rectangle.x, m.monster_rectangle.y, 1400, 400))


    def keydrop(self, player, biome):
        if biome in self.floor1rooms:
            if biome.name == "cricketroom1" or biome.name == "cricketroom2" or biome.name == "cricketroom3":
                if self.nomonstersalive(self.cricketroom1) and self.nomonstersalive(self.cricketroom2) and self.nomonstersalive(self.cricketroom3) and self.notunlocked(self.cricketroom3):
                    biome.add_key(Key(self.cricketroom3, player.player_rectangle.x, player.player_rectangle.y, 800, 100))
            elif biome.name == "houseroom1" or biome.name == "houseroom2" or biome.name == "houseroom3" or biome.name == "houseroom4":
                if self.nomonstersalive(self.houseroom1) and self.nomonstersalive(self.houseroom2) and self.nomonstersalive(self.houseroom3) and self.nomonstersalive(self.houseroom4) and self.notunlocked(self.houseroom4):
                    biome.add_key(Key(self.houseroom4, player.player_rectangle.x, player.player_rectangle.y, 800, 100))
            elif biome.name == "galaroom1" or biome.name == "galaroom2" or biome.name == "galaroom3" or biome.name == "galaroom4":
                if self.nomonstersalive(self.galaroom1) and self.nomonstersalive(self.galaroom2) and self.nomonstersalive(self.galaroom3) and self.nomonstersalive(self.galaroom4) and self.notunlocked(self.galaroom4):
                    biome.add_key(Key(self.galaroom4, player.player_rectangle.x, player.player_rectangle.y, 1400, 400))
            elif biome.name == "schoolroom1" or biome.name == "schoolroom2" or biome.name == "schoolroom3" or biome.name == "schoolroom4" or biome.name == "schoolroom5" or biome.name == "schoolroom7":
                if self.nomonstersalive(self.schoolroom1) and self.nomonstersalive(self.schoolroom2) and self.nomonstersalive(self.schoolroom3) and self.nomonstersalive(self.schoolroom4) and self.nomonstersalive(self.schoolroom5) and self.nomonstersalive(self.schoolroom7) and self.notunlocked(self.schoolroom3):
                    biome.add_key(Key(self.schoolroom3, player.player_rectangle.x, player.player_rectangle.y, 100, 400))
            elif biome.name == "schoolroom6":
                if self.nomonstersalive(self.schoolroom6) and self.notunlocked(self.schoolroom7):
                    biome.add_key(Key(self.schoolroom7, player.player_rectangle.x, player.player_rectangle.y, 1400, 400))


        
