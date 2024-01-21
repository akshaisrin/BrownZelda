import pygame
import os
import Constants
from Monster import *
from Player2 import *

class Bugle:

    def __init__(self, start_pos_x, start_pos_y, width, height):
        self.height=height
        self.width=width
        self.img=pygame.image.load(os.path.join("Assets", "bugle.png"))
        self.img=pygame.transform.scale(self.img, (self.width, self.height))
        self.bugle_rectangle=self.img.get_rect()
        self.bugle_rectangle.center = (start_pos_x, start_pos_y)
        self.rot_img = pygame.transform.rotate(self.img,0)
    
    def render(self, boss_rectangle:pygame.rect, screen:pygame.display):
      
        self.bugle_rectangle.centerx = boss_rectangle.centerx+30
        self.bugle_rectangle.centery = boss_rectangle.centery+30
        #pygame.draw.rect(screen, (0, 255, 0), self.projectile_rectangle)
        screen.blit(self.rot_img, self.bugle_rectangle)
    
    def rotate_towards_player_and_render(self, player:Player2, boss_rectangle:pygame.rect, screen:pygame.display):
        angle = 360-math.atan2(player.player_rectangle.y-300,player.player_rectangle.x-400)*180/math.pi
        self.rot_img = pygame.transform.rotate(self.img,angle)
        self.bugle_rectangle=self.rot_img.get_rect(center=(boss_rectangle.centerx+30, boss_rectangle.centery+30))
        #screen.blit(rotimage, self.bugle_rectangle)
    
        #self.render(boss_rectangle, screen)