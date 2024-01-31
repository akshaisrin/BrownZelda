from Biome import *

class Exit:
    
    def __init__(self, x:int, y:int, next_room:Biome, player_direction:str, width:int, height:int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.next_room = next_room
        self.player_direction = player_direction
        self.rect = (x, y, width, height)