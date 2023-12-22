import pygame
import Constants
import os
import sys
import time
from items.Sword import Sword

class Player2:

    def __init__(self, username: str, inventory:dict, curr_item:str, curr_level:int, curr_checkpoint:tuple, lives_remaining: int, health_bar: int, wealth: int, img:str, start_x, start_y, start_z):
        self.spritesheet=pygame.image.load(os.path.join("Assets", "chotta-bheem-spritesheet.png"))
        self.spritesheet=pygame.transform.scale(self.spritesheet, (576, 192))
        self.current_frame = 9
        self.spritesheet_frames = [self.spritesheet.subsurface((i * 64, j * 64, 64, 64)) for j in range(3) for i in range(9)]
        self.player_rectangle=self.spritesheet_frames[self.current_frame].get_rect()
        self.player_rectangle.topleft = (start_x, start_y)
        self.flipped = False
        self.lastup = None
        self.lastleft = None
        self.direction = None
        self.framegap = 10
        self.spritesheet_dframes = []
        for frame in self.spritesheet_frames:
            rect = frame.get_rect()
            dsurface = frame.copy()
            wsurface = pygame.Surface(rect.size, pygame.SRCALPHA)
            wsurface.fill('white')
            dsurface.blit(wsurface, (0, 0), None, pygame.BLEND_RGB_ADD)
            self.spritesheet_dframes.append(dsurface)
        self.attackspritesheet=pygame.image.load(os.path.join("Assets", "chotta-bheem-attackspritesheet.png"))
        self.attackspritesheet=pygame.transform.scale(self.attackspritesheet, (576, 192))
        self.spritesheet_aframes = [self.attackspritesheet.subsurface((i * 64, j * 64, 64, 64)) for j in range(3) for i in range(9)]
        self.spritesheet_adframes = []
        for frame in self.spritesheet_aframes:
            rect = frame.get_rect()
            dsurface = frame.copy()
            wsurface = pygame.Surface(rect.size, pygame.SRCALPHA)
            wsurface.fill('white')
            dsurface.blit(wsurface, (0, 0), None, pygame.BLEND_RGB_ADD)
            self.spritesheet_adframes.append(dsurface)

        self.attacked = False
        self.attacktime = time.time()

        self.currentitem = curr_item
        self.attacking = False
        self.attackingtime = time.time()

        self.full_heart_img = pygame.image.load(os.path.join("Assets", "full_heart.png"))
        self.empty_heart_img = pygame.image.load(os.path.join("Assets", "empty_heart.png"))
        self.full_heart_img = pygame.transform.scale(self.full_heart_img, (32, 32))
        self.empty_heart_img = pygame.transform.scale(self.empty_heart_img, (32, 32))
        self.heart_spacing = 40
    
        self.username = username
        self.inventory = inventory
        self.curr_level = curr_level
        self.curr_checkpoint = curr_checkpoint
        self.lives_remaining = lives_remaining
        self.original_health=health_bar
        self.health_bar = self.original_health
        self.wealth = wealth
    
        
    def select_item(self, item:str):
        if item in self.inventory:
            self.curr_item = item

    def use_item(self):
        self.curr_item.use() #use function will be defined in Item classes

    def get_attacked(self, damage:int, screen):
        self.attacked = True
        self.attacktime = time.time()
        self.health_bar -= damage

        if (self.health_bar<=0):
            print("player just lost all their health")
            self.lives_remaining-=1
            self.die_and_begone(screen)

    def attack(self, monster):
        self.attacking = True
        self.attackingtime = time.time()
        if (self.player_rectangle.colliderect(monster.monster_rectangle)):
            monster.get_hit(self.currentitem.power)

    def get_healed(self, healing:int):
        self.health_bar += healing
    
    
    def die_and_begone(self, screen, overworld=None):
        if self.lives_remaining <= 0:
            print("GAME OVER")
            game_over_img=pygame.image.load(os.path.join("Assets", "game_over_screen.jpg"))
            game_over_img = pygame.transform.scale(game_over_img, (Constants.screen_width, Constants.screen_height))
            screen.blit(game_over_img, (0, 0))

            pygame.display.update()
            time.sleep(3)
            sys.exit()
            #overworld.game_over()
        else:
            self.respawn() 


    def respawn(self):
        self.health_bar=self.original_health
        print("PLAYER RESPAWNED")

        # self.x_pos = self.curr_checkpoint[0]
        # self.y_pos = self.curr_checkpoint[1]
        # self.z_pos = self.curr_checkpoint[2]

    def handlemove(self, direction, framecounter, firstchange): 
        if self.attacking: 
            return
        self.direction = direction
        if self.direction == None:
            return
        elif self.direction == "left":
            if framecounter % self.framegap == 0 or firstchange:
                if self.current_frame != 10:
                    self.current_frame = 10
                else:
                    if self.lastleft == 13:
                        self.current_frame = 16
                        self.lastleft = 16
                    else:
                        self.current_frame = 13
                        self.lastleft = 13
                if self.flipped:
                    self.spritesheet_frames = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_frames]
                    self.spritesheet_dframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_dframes]
                    self.spritesheet_aframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_aframes]
                    self.flipped = False
        elif self.direction == "right":
            if framecounter % self.framegap == 0 or firstchange:
                if self.current_frame != 10:
                    self.current_frame = 10
                else:
                    if self.lastleft == 13:
                        self.current_frame = 16
                        self.lastleft = 16
                    else:
                        self.current_frame = 13
                        self.lastleft = 13
                if not self.flipped:
                    self.spritesheet_frames = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_frames]
                    self.spritesheet_dframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_dframes]
                    self.spritesheet_aframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_aframes]
                    self.flipped = True
        elif self.direction == "up":
            if framecounter % self.framegap == 0 or firstchange:
                if self.lastup == 14:
                    self.current_frame = 17
                    self.lastup = 17
                else:
                    self.current_frame = 14
                    self.lastup = 14
        else:
            if framecounter % self.framegap == 0 or firstchange:
                if self.lastup == 12:
                    self.current_frame = 15
                    self.lastup = 15
                else:
                    self.current_frame = 12
                    self.lastup = 12
        
        self.player_rectangle.move_ip(Constants.directions[self.direction][0], Constants.directions[self.direction][1])
        
    def render(self, x_pos:float, y_pos:float, screen:pygame.display) -> None:
        image = None
        if self.attacking:
            elapsedTime = time.time() - self.attackingtime
            if elapsedTime > 0.3:
                self.attacking = False
            if self.current_frame == 10:
                if self.attacked and elapsedTime % 0.1 > 0.05:
                    image = pygame.transform.scale(self.spritesheet_adframes[13], (64, 64))
                else:
                    image = pygame.transform.scale(self.spritesheet_aframes[13], (64, 64))
            elif self.current_frame == 11:
                if self.attacked and elapsedTime % 0.1 > 0.05:
                    image = pygame.transform.scale(self.spritesheet_adframes[17], (64, 64))
                else:
                    image = pygame.transform.scale(self.spritesheet_aframes[17], (64, 64))
            else:
                if self.attacked and elapsedTime % 0.1 > 0.05:
                    image = pygame.transform.scale(self.spritesheet_adframes[15], (64, 64))
                else:
                    image = pygame.transform.scale(self.spritesheet_aframes[15], (64, 64))
        elif self.attacked:
            elapsedTime = time.time() - self.attacktime
            if elapsedTime > 1:
                self.attacked = False
            if elapsedTime % 0.1 > 0.05:
                image = pygame.transform.scale(self.spritesheet_dframes[self.current_frame], (64, 64))
            else:
                image = pygame.transform.scale(self.spritesheet_frames[self.current_frame], (64, 64))
        else:
            image = pygame.transform.scale(self.spritesheet_frames[self.current_frame], (64, 64))
        self.player_rectangle = image.get_rect()
        self.player_rectangle.topleft = (x_pos, y_pos)
        screen.blit(image, self.player_rectangle)
    
    def renderhealth(self, x_pos, y_pos, screen):
        for i in range(self.original_health):
            heart_image = self.full_heart_img if i < self.health_bar else self.empty_heart_img
            screen.blit(heart_image, (x_pos + i * self.heart_spacing, y_pos))
    
