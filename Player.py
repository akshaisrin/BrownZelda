import pygame
import Constants

class Player:

    def __init__(self, username: str, inventory:dict, curr_item:str, curr_level:int, curr_checkpoint:tuple(int,int,int), lives_remaining: int, health_bar: int, wealth: int, img:str, start_x, start_y, start_z):
        self.username = username
        self.inventory = inventory
        self.curr_item = curr_item
        self.curr_level = curr_level
        self.curr_checkpoint = curr_checkpoint
        self.lives_remaining = lives_remaining
        self.health_bar = health_bar
        self.wealth = wealth
        self.player_rectangle=self.img.get_rect()
        self.x_pos = start_x
        self.y_pos = start_y
        self.z_pos = start_z


    def move(self,direction:str): #figure out how to use arrow keys to set direction string variable -- right arrow sets direction to "right" and calls move
        self.x_pos += Constants.directions[direction][0]
        self.y_pos += Constants.directions[direction][1]
        
    def select_item(self, item:str):
        if item in self.inventory:
            self.curr_item = item

    def use_item(self):
        self.curr_item.use() #use function will be defined in Item classes

    def get_attacked(self, damage:int):
        self.health_bar -= damage

    def get_healed(self, healing:int):
        self.health_bar += healing
    
    def die_and_begone(self):
        self.lives_remaining -= 1
        if self.lives_remaining == 0:
            OverWorld.game_over()
        else:
            self.respawn() 

    def respawn(self):
        self.x_pos = self.curr_checkpoint[0]
        self.y_pos = self.curr_checkpoint[1]
        self.z_pos = self.curr_checkpoint[2]

