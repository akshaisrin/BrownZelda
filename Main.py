import os
import sys
import time
import pygame
from XBoxController import XboxController
from screens.loadingScreens.InitialLoadingScreen import InitialLoadingScreen
from screens.loadingScreens.NewLoadingScreen import NewLoadingScreen
from screens.InstructionsScreen import *
from screens.FinalScreen import FinalScreen
from pygame.locals import *
from Constants import *
#from inputs import get_gamepad
#from XBoxController import *
from Player2 import *
from items.Sword import Sword
from Overworld import *

pygame.init()

# Set up screen dimensions
screen_width, screen_height = 1500, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brown Zelda (But Not Garbage)")
pygame.mixer.init()
font = pygame.font.Font('freesansbold.ttf', 32)
current_screen = None


def init_loading_screen():
    #set screen to initial loading screen
    current_screen = InitialLoadingScreen(screen)
    loadingscreenstarttime = time.time()
    #load in title music
    pygame.mixer.music.load(os.path.join("Assets", "originalzeldatitlemusic.mp3"))  
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play()

    #initialize loading screen booleans - when each section of loading screen is complete will turn them to true
    gameLoop = True
    initialLoadingScreenDone = False
    newLoadingScreenDone = False
    instructionsScreenStarted = False
    firstSongSet = False
    secondSongSet = False
    thirdSongSet = False
    fourthSongSet = False
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            #when loading screen animation is complete - user can move onto story with space
            elif newLoadingScreenDone and not instructionsScreenStarted and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.set_volume(0.2)
                    loadingscreenstarttime = time.time()
                    instructionsScreenStarted = True

        #fades out of original zelda loading screen to new brown zelda loading screen - adds music
        if not initialLoadingScreenDone:
            #sets how long it has been since loading screen started
            elapsedTime = time.time() - loadingscreenstarttime
            if elapsedTime > 20:
                initialLoadingScreenDone = True
                current_screen = NewLoadingScreen(screen)
                loadingscreenstarttime = time.time()
                pygame.mixer.music.set_volume(0.7)
            elif elapsedTime > 18 and not thirdSongSet: 
                pygame.mixer.music.set_volume(0.55)
                thirdSongSet = True
            elif elapsedTime > 16 and not secondSongSet:
                #swap to chotta bheem music
                pygame.mixer.music.load(os.path.join("Assets", "chottabheemtitlesong.mp3"))  
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)
                secondSongSet = True
            elif elapsedTime > 13 and not fourthSongSet:
                pygame.mixer.music.set_volume(0.15)
                fourthSongSet = True
            elif elapsedTime > 10 and not firstSongSet:
                pygame.mixer.music.set_volume(0.3)
                firstSongSet = True
            elif elapsedTime > 4:
                current_screen.display(elapsedTime - 4)
            else:
                current_screen.display(0)
        elif not newLoadingScreenDone:
            elapsedTime = time.time() - loadingscreenstarttime
            if elapsedTime > 6:
                newLoadingScreenDone = True
            else:
                current_screen.display(elapsedTime)    
        elif instructionsScreenStarted:
            elapsedTime = time.time() - loadingscreenstarttime
            current_screen.displayfade(elapsedTime)
            if elapsedTime > 2:
                gameLoop = False         
        pygame.display.update()


def init_instructions_screen():
    #sets screen to instructions screen - also tracks time since screen started
    current_screen = InstructionsScreen(screen) 
    instructionsscreenstarttime = time.time()

    gameLoop = True
    while gameLoop:
        elapsedTime = time.time() - instructionsscreenstarttime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
                
            #allows player to skip instructions screen if they wish by hitting space
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    gameLoop = False

        #scrolls down instructions screen - tracking elapsed time to know how far down to scroll
        if elapsedTime > 72:
            pygame.mixer.music.stop()
            gameLoop = False
        elif elapsedTime > 68:
            current_screen.displayfade(elapsedTime - 68)
        elif elapsedTime > 65:
            pygame.mixer.music.set_volume(.1)
        else:
            current_screen.display(elapsedTime)
        pygame.display.update()
        
         
def init_home_screen():
    #creates clock to make fps consistent across machines
    clock = pygame.time.Clock()
    controller_detected=True 
    sword = Sword()
    #loads in player and weapon
    player1 = Player2("bheem", {}, sword, 1, 1.2, 1, 5, 5, "str", 750, 400, 0)
     
    #test mode variable to skip slower parts of gameplay
    test_mode = False
    # create the overworld and starting room
    overworld = Overworld()
    curr_screen = overworld.room1
    if test_mode:
        curr_screen = overworld.cricketroom1
        overworld.cricketroom3.add_key(Key(overworld.cricketroom3, 800, 400, 800, 100))
    if curr_screen == overworld.schoolroom1:
        player1.player_rectangle.topleft = (750, 700)
    
    # create variables for the current screen's x and y position
    curr_screen_x_pos = 0
    curr_screen_y_pos = 0
    
    
    try:
        joystick=XboxController()
    except:
        controller_detected=False
    # Establishing game loop to keep screen running
    

    #adds gameloop variable and direction variable to keep track of player movement
    #also adds in text variables to keep track of text display
    gameLoop = True
    direction = None
    direction_for_collision = None
    framecounter = 0
    firstchange = False
    
    display_text = True # if text should be rendered
    keep_text_displayed = True # if text should continue to be displayed after rendering
    text_index = 0 # what text sentence should be rendered
    texts = [] # the list of all the text that needs to be rendered
    respawn=False
    curr_dir="ahhhhhhh"
    while gameLoop:
        #sets fps to 30 frames
        clock.tick(30)
        #tracks number of frames since game started for animation purposes
        framecounter = framecounter + 1
        # checks if it's time to transition to the next level
        next_screen = overworld.picksupitems(player1, curr_screen, screen)
        if next_screen != None:
            curr_screen = next_screen
            keep_text_displayed = False
            text_index = 0
            texts = []
        #checks if player is in a room with a key and if they have picked it up - also unlocks rooms if player has key
        overworld.pickupkeys(player1, curr_screen)
        overworld.unlockroom(player1, curr_screen, screen)
        
        # prevents player and obstacle collision
        overworld.obstacles_in_biome(player1, curr_screen, direction_for_collision)

        #renders page (items, players, background, monsters)
        curr_screen.render(curr_screen_x_pos, curr_screen_y_pos, player1, screen)
        curr_screen.render_characters(player1, screen)
        
        #if player is off the screen - put them back on the screen
        player1.adjustplayer(curr_screen)

        #renders text if necessary
        if curr_screen.text != None and text_index < len(curr_screen.text) and display_text:
            new_text = overworld.display_text(curr_screen.text[text_index], curr_screen, player1, texts, screen)
            texts.append(new_text)
            keep_text_displayed = True
            display_text = False
        
        # keeps the rendered text on the screen if necessary
        if keep_text_displayed:
            for t in texts:
                screen.blit(t[0], t[1])
            text_index += 1 
            display_text = True
        
        #checks if player is going to next room
        if curr_screen != None:
            new_screen = overworld.going_to_next_biome(player1, curr_screen, curr_screen_x_pos, curr_screen_y_pos, screen)
            if new_screen != None:
                keep_text_displayed = False
                text_index = 0
                texts = []
                curr_screen = new_screen
                curr_screen_x_pos = 0
                curr_screen_y_pos = 0
        
        # checks if the player has died
        if player1.check_checkpoint():
            screen_before_death = curr_screen
            curr_screen = overworld.game_over_screen
            player1.checkpoint = False
            respawn = True
            keep_text_displayed = False
            text_index = 0
            texts = []
            overworld.shah_rukh.paralyzing = False

        # if not overworld.shah_rukh.paralyzing:
        #     pygame.mixer.music.load(os.path.join("Assets", "cut down john cena music.mp3"))  
        #     pygame.mixer.music.set_volume(0.3)
        #     pygame.mixer.music.play(-1)   
                
        monsters_alive = overworld.monster_attack(curr_screen, player1, screen)[1]

        # player controls for x box controller
        axis="x"
        
        if controller_detected:        
            new_state=(joystick.get_x_axis(), joystick.get_y_axis())
            
            # player movement with x box controller
            val=[abs(joystick.get_x_axis()), abs(joystick.get_y_axis())]

            if val[1]>val[0]:
                axis="y"

            if axis=="x":
                if (new_state[0]<-1*Constants.controller_threshold):
                    direction = "left"
                    direction_for_collision = "left"
                    firstchange=True

                elif (new_state[0]>Constants.controller_threshold):
                    direction = "right"
                    direction_for_collision = "right"
                    firstchange=True
            
            elif axis=="y":
                if (new_state[1]<-1*Constants.controller_threshold):
                    direction = "down"
                    direction_for_collision = "down"
                    firstchange=True
                elif (new_state[1]>controller_threshold):
                    direction = "up" 
                    direction_for_collision = "up"
                    firstchange=True
            
            # This code represents a key-up if keyboard controls were used- if the direction is changed, the current frame is changed

            if curr_dir!=direction:
                if direction=="left" or direction=="right":
                    player1.current_frame = 10
                
                if direction=="up":
                    player1.current_frame = 11
                    
                if direction=="down":
                    player1.current_frame = 9
                
                curr_dir=direction
                direction=None
            
            if abs(new_state[0])<Constants.controller_threshold and abs(new_state[1])<Constants.controller_threshold:
                direction=None
                curr_dir=direction

            # This handles the player attack using the controller

            if (joystick.X) and not player1.attacking:
                manage_player_attack(player1, curr_screen)
            
            # This handles the player respawn functionality using the controller

            if joystick.A:
                if respawn:
                    overworld = Overworld()
                    # determine what the current level is
                    if screen_before_death.name[0:4] == "cric":
                        curr_screen = overworld.room1
                        player1.player_rectangle.topleft = (screen_width//2, screen_height//2)
                    elif screen_before_death.name[0:4] == "hous":
                        curr_screen = overworld.houseroom1
                        player1.player_rectangle.topleft = (screen_width//2, 650)
                    elif screen_before_death.name[0:4] == "gala":
                        curr_screen = overworld.galaroom1
                        player1.player_rectangle.topleft = (screen_width//2, 650)
                    else:
                        curr_screen = overworld.schoolroom1
                        player1.player_rectangle.topleft = (screen_width//2, 700)
                    player1.health_bar = 5
                    player1.lives_remaining = 5
                    keep_text_displayed = False
                    text_index = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop=False
                    pygame.quit()
                    sys.exit()     

        else:   
            #controls movement - sets direction variable
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:                   
                    if event.key == pygame.K_LEFT: 
                        direction = "left"
                        direction_for_collision = "left"
                        firstchange = True
                    elif event.key == pygame.K_RIGHT: 
                        direction = "right"
                        direction_for_collision = "right"
                        firstchange = True
                    elif event.key == pygame.K_UP:
                        direction = "up" 
                        direction_for_collision = "up"
                        firstchange = True
                    elif event.key == pygame.K_DOWN: 
                        direction = "down"
                        direction_for_collision = "down"
                        firstchange = True

                    # lets the player respawn to the beginning of the current level
                    elif event.key == pygame.K_k:
                        if respawn:
                            overworld = Overworld()
                            # determine what the current level is
                            if screen_before_death.name[0:4] == "cric":
                                curr_screen = overworld.room1
                                player1.player_rectangle.topleft = (screen_width//2, screen_height//2)
                            elif screen_before_death.name[0:4] == "hous":
                                curr_screen = overworld.houseroom1
                                player1.player_rectangle.topleft = (screen_width//2, 650)
                            elif screen_before_death.name[0:4] == "gala":
                                curr_screen = overworld.galaroom1
                                player1.player_rectangle.topleft = (screen_width//2, 650)
                            else:
                                curr_screen = overworld.schoolroom1
                                player1.player_rectangle.topleft = (screen_width//2, 700)
                            player1.health_bar = 5
                            player1.lives_remaining = 5
                            keep_text_displayed = False
                            text_index = 0
                            respawn = False
                            
                #stops movement if key is released - sets direction to None
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player1.current_frame = 10
                        direction = None
                    elif event.key == pygame.K_UP:
                        player1.current_frame = 11
                        direction = None
                    elif event.key == pygame.K_DOWN:
                        player1.current_frame = 9
                        direction = None
                    elif (event.key == pygame.K_SPACE) and not player1.attacking:
                        manage_player_attack(player1, curr_screen)
                        
                if event.type == pygame.QUIT:
                    gameLoop=False
                    pygame.quit()
                    sys.exit()
        
        #handles monsters dropping keys to unlock dungeons
        overworld.monsterkeydrop(player1, curr_screen)
        overworld.keydrop(player1, curr_screen)
        
        #handles player movement and renders health
        player1.handlemove(direction, framecounter, firstchange)
        player1.renderhealth(10, 10, screen)
        firstchange = False
        
        # check if the player has reached the final boss
        if not overworld.given_samosa:
            sc = overworld.samosa_final_boss(player1, screen)
            if sc != None:
                curr_screen = sc
        
        #if any monsters in schoolroom9 are dead, end the game
        if overworld.nomonstersalive(overworld.schoolroom9):
            init_final_screen()
            gameLoop = False
        
        pygame.display.update()


def manage_player_attack(player1, curr_screen):
    canattack = True
    #check if player 1 is within 100 pixels of any obstacle in the biome
    if player1.current_frame == 10 and player1.flipped: 
        if not curr_screen.is_valid_point(player1.player_rectangle.topleft[0] + 150, player1.player_rectangle.topleft[1]):
            canattack = False
    elif player1.current_frame == 10 and not player1.flipped:
        if not curr_screen.is_valid_point(player1.player_rectangle.topleft[0] - 50, player1.player_rectangle.topleft[1]):
            canattack = False
    elif player1.current_frame == 9:
        if not curr_screen.is_valid_point(player1.player_rectangle.topleft[0], player1.player_rectangle.topleft[1] + 150):
            canattack = False
    elif player1.current_frame == 11:
        if not curr_screen.is_valid_point(player1.player_rectangle.topleft[0], player1.player_rectangle.topleft[1] - 50):
            canattack = False
    else:
        if not curr_screen.is_valid_point(player1.player_rectangle.topleft[0], player1.player_rectangle.topleft[1]):
            canattack = False
    if canattack:
        player1.attacking = True
        player1.attackingtime = time.time()
        player1.attack(curr_screen.monsters)

#final screen method - follows similar logic to instructions sceen
def init_final_screen():
    current_screen = FinalScreen(screen)
    finalscreenstarttime = time.time()

    pygame.mixer.music.load(os.path.join("Assets", "chottabheemtitlesong.mp3"))  
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    gameLoop = True
    while gameLoop:
        elapsedTime = time.time() - finalscreenstarttime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    gameLoop = False

        if elapsedTime > 59:
            pygame.mixer.music.stop()
            gameLoop = False
        elif elapsedTime > 55:
            current_screen.displayfade(elapsedTime - 55)
        else:
            current_screen.display(elapsedTime)
        pygame.display.update()
        
# init_loading_screen()
# init_instructions_screen()
init_home_screen()
init_final_screen()
