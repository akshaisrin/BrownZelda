import pygame

class Player:

    def __init__(self, username: str, inventory:dict, curr_item:str, curr_level:int, curr_checkpoint, lives_remaining: int, health_bar: int, wealth: int, img:str):
        self.username = username
        self.inventory = inventory
        self.curr_item = curr_item
        self.curr_level = curr_level
        self.curr_checkpoint = curr_checkpoint
        self.lives_remaining = lives_remaining
        self.health_bar = health_bar
        self.wealth = wealth
        self.player_rectangle=self.img.get_rect()
        self.player_rectangle.x=0
        self.player_rectangle.y=0

    directions = {"left":(-1,0), "right":(1,0), "up":(0,1), "down":(0,-1)} #do we want to add diagonals?

    def move(direction:str): #figure out how to use arrow keys to set direction string variable -- right arrow sets direction to "right" and calls move
        self.player_rectangle.x += directions[]