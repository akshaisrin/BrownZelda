import pygame
import Constants
import os
import sys
import time
import random

class Player2:

    def __init__(self, username: str, inventory:dict, curr_item:str, curr_level:int, curr_checkpoint:tuple, lives_remaining: int, health_bar: int, wealth: int, img:str, start_x, start_y, start_z):
        #loads standard spritesheet
        self.spritesheet=pygame.image.load(os.path.join("Assets", "chotta-bheem-spritesheet.png"))
        self.spritesheet=pygame.transform.scale(self.spritesheet, (576, 192))
        #frame of spritesheet player is currently using
        self.current_frame = 9
        #splits standard spritesheet
        self.spritesheet_frames = [self.spritesheet.subsurface((i * 64, j * 64, 64, 64)) for j in range(3) for i in range(9)]
        self.player_rectangle=self.spritesheet_frames[self.current_frame].get_rect()
        self.player_rectangle.topleft = (start_x, start_y)
        #defines variables for animation
        self.flipped = False
        self.lastup = None
        self.lastleft = None
        self.direction = None
        self.framegap = 10
        #defines spritesheet for being attacked
        self.spritesheet_dframes = []
        for frame in self.spritesheet_frames:
            rect = frame.get_rect()
            dsurface = frame.copy()
            wsurface = pygame.Surface(rect.size, pygame.SRCALPHA)
            #wsurface.fill('white')
            dsurface.blit(wsurface, (0, 0), None, pygame.BLEND_RGB_ADD)
            self.spritesheet_dframes.append(dsurface)
        #defines spritesheet for attacking
        self.attackspritesheet=pygame.image.load(os.path.join("Assets", "chotta-bheem-attackspritesheet.png"))
        self.attackspritesheet=pygame.transform.scale(self.attackspritesheet, (576, 192))
        self.spritesheet_aframes = [self.attackspritesheet.subsurface((i * 64, j * 64, 64, 64)) for j in range(3) for i in range(9)]
        self.attackspritesheet2=pygame.image.load(os.path.join("Assets", "chotta-bheem-attackspritesheet3.png"))
        self.attackspritesheet2=pygame.transform.scale(self.attackspritesheet2, (576, 192))
        self.spritesheet_aframes[13] = (self.attackspritesheet2.subsurface((0, 30, 104, 64)))
        self.spritesheet_aframes[15] = (self.attackspritesheet2.subsurface((144, 30, 64, 104)))
        self.spritesheet_aframes[17] = (self.attackspritesheet2.subsurface((208, 0, 64, 104)))
        self.spritesheet_adframes = []
        #defines spritesheet for being attacked and attacking at the same time
        for frame in self.spritesheet_aframes:
            rect = frame.get_rect()
            dsurface = frame.copy()
            wsurface = pygame.Surface(rect.size, pygame.SRCALPHA)
            #wsurface.fill('white')
            dsurface.blit(wsurface, (0, 0), None, pygame.BLEND_RGB_ADD)
            self.spritesheet_adframes.append(dsurface)

        #variables needed to animate being attacked and attacking
        self.attacked = False
        self.attacktime = time.time()
        self.currentitem = curr_item
        self.attacking = False
        self.attackingtime = time.time()

        #images for rendering health
        self.full_heart_img = pygame.image.load(os.path.join("Assets", "full_heart.png"))
        self.empty_heart_img = pygame.image.load(os.path.join("Assets", "empty_heart.png"))
        self.half_heart_img = pygame.image.load(os.path.join("Assets", "half_heart.png"))
        self.full_heart_img = pygame.transform.scale(self.full_heart_img, (32, 32))
        self.empty_heart_img = pygame.transform.scale(self.empty_heart_img, (32, 32))
        self.half_heart_img = pygame.transform.scale(self.half_heart_img, (32, 32))
        self.heart_spacing = 40

        #tracks keys held by player, health of player and checkpoint player is at
        self.key_inventory = []
        self.inventory = inventory
        self.curr_level = curr_level
        self.curr_checkpoint = curr_checkpoint
        self.lives_remaining = lives_remaining
        self.original_health=health_bar
        self.health_bar = self.original_health
        self.is_paralyzed = False
        self.checkpoint = False
    
    # not currently in use, feature scrapped due to time
    def select_item(self, item:str):
        if item in self.inventory:
            self.curr_item = item

    # not currently in use, feature scrapped due to time
    def use_item(self):
        self.curr_item.use() #use function will be defined in Item classes

    # gets attacked by monster - sets render settings and decreases health bar
    def get_attacked(self, damage:int, screen):
        self.attacked = True
        self.attacktime = time.time()
        self.health_bar -= damage

        if (self.health_bar<=0):
            self.lives_remaining-=1
            self.die_and_begone(screen)

    # runs when player attacks - checks if monster is in range and calls get_hit function
    def attack(self, monsters):  
        for monster in monsters:
            if (self.player_rectangle.colliderect(monster.monster_rectangle)):
                
                monster.get_hit(self.currentitem.power)                    
                if not monster.in_hit_cooldown:
                    monster.in_hit_cooldown=True
                    monster.last_hit=pygame.time.get_ticks()

                    
    # checks if player is close to healing items and heals player if it is
    def get_healed(self, item):
        if (self.player_rectangle.colliderect(item.item_rectangle)) and not item.used:
            self.health_bar+=item.power
            if (self.health_bar>self.original_health):
                self.health_bar=self.original_health
            item.used=True
    
    # picks up key off ground and adds it to inventory if player is in range
    def get_key(self, key):
        if (self.player_rectangle.colliderect(key.key_rectangle)):
            self.key_inventory.append(key)
            key.pickedup = True
    

    def die_and_begone(self, screen):
        if self.lives_remaining <= 0:
            game_over_img=pygame.image.load(os.path.join("Assets", "game_over_screen.png"))
            game_over_img = pygame.transform.scale(game_over_img, (Constants.screen_width, Constants.screen_height))
            screen.blit(game_over_img, (0, 0))
            
            self.checkpoint = True

            pygame.display.update()
            
            if not self.checkpoint:
                time.sleep(3)
                sys.exit()
        else:
            self.respawn() 
            
    
    def check_checkpoint(self):
        if self.checkpoint:
            return True
        return False

    # when player respawns resets health bar
    def respawn(self):
        self.health_bar=self.original_health

    # handles player movement - changes player rectangle position and changes current frame
    def handlemove(self, direction, framecounter, firstchange): 
        if self.is_paralyzed:
            return
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
                    self.spritesheet_adframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_adframes]
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
                    self.spritesheet_adframes = [pygame.transform.flip(frame, True, False) for frame in self.spritesheet_adframes]
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
        
    # renders player on screen - handles attacking and getting attacked animation (damage and extension)
    def render(self, x_pos:float, y_pos:float, screen:pygame.display) -> None:
        image = None
        adjustx = 0
        adjusty = 0
        if self.attacking:
            elapsedTime = time.time() - self.attackingtime
            if elapsedTime > 0.5:
                self.attacking = False
                image = pygame.transform.scale(self.spritesheet_frames[self.current_frame], (64, 64))
            elif elapsedTime > 0.3:
                image = pygame.transform.scale(self.spritesheet_frames[self.current_frame], (64, 64))
            else:
                if self.current_frame == 10:
                    if not self.flipped:
                        adjustx = 64
                    if self.attacked and elapsedTime % 0.1 > 0.05:
                        image = pygame.transform.scale(self.spritesheet_adframes[13], (104, 64))
                    else:
                        image = pygame.transform.scale(self.spritesheet_aframes[13], (104, 64))
                elif self.current_frame == 11:
                    adjusty = 40
                    if self.attacked and elapsedTime % 0.1 > 0.05:
                        image = pygame.transform.scale(self.spritesheet_adframes[17], (64, 104))
                    else:
                        image = pygame.transform.scale(self.spritesheet_aframes[17], (64, 104))
                else:
                    if self.attacked and elapsedTime % 0.1 > 0.05:
                        image = pygame.transform.scale(self.spritesheet_adframes[15], (64, 104))
                    else:
                        image = pygame.transform.scale(self.spritesheet_aframes[15], (64, 104))
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
        self.player_rectangle.topleft = (x_pos - adjustx, y_pos - adjusty)
        #pygame.draw.rect(screen, (255,0,0), self.player_rectangle)
        screen.blit(image, self.player_rectangle)
        
        self.player_rectangle.topleft = (x_pos, y_pos)

        
    #if player is out of bounds, randomly teleport player to new location
    def adjustplayer(self, biome):
        if not biome.is_valid_point(self.player_rectangle.topleft[0], self.player_rectangle.topleft[1]) or self.player_rectangle.topleft[0] < -10 or self.player_rectangle.topleft[0] > Constants.screen_width + 10 or self.player_rectangle.topleft[1] < -10 or self.player_rectangle.topleft[1] > Constants.screen_height + 10:
            self.player_rectangle.topleft = (random.randint(0, Constants.screen_width), random.randint(0, Constants.screen_height))
            while not biome.is_valid_spawn(self.player_rectangle.topleft[0], self.player_rectangle.topleft[1]):
                self.player_rectangle.topleft = (random.randint(0, Constants.screen_width), random.randint(0, Constants.screen_height))
        
    
    # renders health bar on screen
    def renderhealth(self, x_pos, y_pos, screen):
        #render health bar with half hearts for .5 health
        for i in range(self.original_health):
            heart_image = None
            if i <= (self.health_bar - 1):
                heart_image = self.full_heart_img
            elif i == (self.health_bar - 0.5):
                heart_image = self.half_heart_img 
            else:
                heart_image = self.empty_heart_img
            
            screen.blit(heart_image, (x_pos + i * self.heart_spacing, y_pos))
