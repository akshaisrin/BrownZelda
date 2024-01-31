BrownZelda/DesignDoc

**Overview**
**General Information and Twists**
Our project is a remake of the 1980’s NES game, “The Legend of Zelda”. Our goal in making this project was to keep the general game mechanics of the NES game the same while customizing its storyline, graphics, monster design, and more to add in our own flair and bring a more unique experience to our players.
**Twist 1 - Storyline**
In the original game, the player plays as Link, a knight from the kingdom of Hyrule, and fights their way through monsters and obstacles to collect pieces of the Triforce in order to rescue Princess Zelda from the clutches of Ganon. In our game, the player plays as the iconic Indian TV character, Chotta Bheem, who has failed his math test. His mom forces him to go find Mr. Puri, his teacher (definitely not the same person), in order to convince him to change his grade. To do so, Chotta Bheem travels through three uniquely themed dungeons to collect ingredients to craft the perfect samosa to give to Mr. Puri, in the hopes that it will turn the tides in his favor and save him from the eternal wrath of his mom.
**Twist 2 - Themed Dungeons + Monsters**
In our game, each of our dungeons has a unique theme that ties into our storyline and is based on a different Indian cultural concept. Each dungeon also has unique monsters/bosses that are relevant to that theme. The player starts in a cricket stadium where they face Virat Kohli and the Indian cricket team, before going to an Indian Auntie’s house to face the Auntie herself armed with chappals, and finally ending at the premiere of a Bollywood movie to face the infamous Shah Rukh Khan himself. Once the player has collected all the ingredients, they assemble the samosa and face Mr. Puri in Eastlake as the final boss. Each boss also has a unique set of attacks entirely different from the original game to add some more variety and difficulty to our game. For example, our first dungeon’s boss, Virat Kohli, pelts cricket balls and has a charge attack where they charge towards the player and deal extra damage.
**Twist 3 - Graphics**
We also created unique images for our player, monsters, obstacles, and backgrounds in an 8-bit pixel-art style to keep with the retro theme of our game. A lot of our artwork was created using online AI image creators, including the Bing AI Image Creator.
**Twist 4 - Checkpoints**![drivers license](https://github.com/akshaisrin/BrownZeldaButNotGarbage/assets/90334707/b53371c2-9635-4d4e-850d-722db1aa4bf6)

The original game doesn’t have a checkpoint system, so we created checkpoints after each boss fight and set of mini bosses in our dungeons. That way, if a player loses all their health at any point in the game, they can respawn where they died to get another chance at beating our game. This leaves the player from getting frustrated and rage-quitting if the game gets difficult for them and puts lower stakes on losing health to make the game a more enjoyable experience overall.
**Twist 5 - Text**
We also included text throughout our game to ensure that the player understood how the storyline was progressing as they played through the game.
**Twist 6 - Merged Dungeon + Overworld**
The original game has a separate overworld that the player travels through in order to get to the dungeons. We wanted to make our game quick and easily playable so we merged the overworld and dungeon concepts. The player now starts off at the first dungeon and automatically gets teleported to the next dungeon upon collecting each samosa ingredient.
**Twist 7- Dual Input Functionality**
While our game is a PC-based game, we still wanted to bring the look, feel, and experience of playing using a handheld device and controller to the player. As an alternative, our game also supports XBox 1 controller functionality in addition to basic arrow key controls.

**Design Choices**
**Overall Strategy:**
After choosing our game and twist, it quickly became clear to us one thing stood out as our selling point: the story. We had a story that would briefly be hilarious, and wanted to prioritize that selling point throughout our game.
So, every design choice was made based on one element: speed. We wanted to move the player quickly through the game so that they could keep laughing and being amused. This isn’t the type of game where we wanted the player repeatedly struggling through sections, as eventually the allure of the story would wear off, and the selling point and main twist of our game is voided.
With that in mind, let’s move through the main design choices we made.
Design Choice 1 - Text:
We decided to add text to the game in order to explain the story and game mechanics to the user. We didn’t want the user struggling to understand what was going on, or spending time puzzling over game features. (UX Section dives deeper into this)
Design Choice 2 - Checkpoints:
We added checkpoints to the game so the user would not have to repeat large sections of the story for a single death. After the initial surprise of our story’s plot points, the allure wears off in following run-throughs. So, after completing a floor, we made sure the user would not have to replay the floor by adding checkpoints for them to use. (UX Section dives deeper into this)
Design Choice 3 - Encouraged Randomness
Well aware of our emphasis on the story’s hilarity as our selling point, we heavily encouraged randomness in all aspects of our design, both game and story wise. Chotta Bheem getting a bad grade as the main character? Why not! Burnie Sanders being a main weapon of Shah Ruh Khan, who is also an enemy? Sure! Mr. Puri with a horn as the final boss? Of course! By encouraging this idea throughout our project, we emphasized our main selling point. 
Design Choice 4 - Adding Item Drops from Monsters:
We felt that the initial Legend of Zelda game did not prioritize forcing the player to kill the monsters in his path enough, so we added healing items that drop from monsters to encourage the player to kill monsters efficiently in order to heal up before boss fights. Additionally, we also added a lock and key system (with keys dropping from monsters) to stunt the player’s progress, thereby forcing them to kill all the monsters and further explore the game.

**Conclusion:**
The above design choices support our idea of speed and story focus throughout the project, as well as forcing the user to fight the variety of monsters we created unlike the original game. We accepted and understood that our game was most enjoyable as a first time playthrough, and took that into account throughout our design process.

**Connection to Culture**
An interesting element of our group dynamic is that we are all Indian (shocking in a CS course, I know). While brainstorming our game, we thought it might be a fun idea to connect the game to various elements of our culture. We also took into account that a lot of the members of our ASP class were Indian, and as they were our audience, the game may strike a chord for them specifically as well.
We made the main character a famous Indian TV Show character from our childhoods, Chotta Bheem. Continuing the trend, we made healing items in the game ladoos, a famous Indian sweet and Chotta Bheem’s iconic power-boosting food. We connected to various elements of Indian culture, whether that was through sports with the Indian cricket team as the floor 1 enemy, or through arts and culture with Shah Ruh Khan as the floor 3 enemy. We also connected back to family dynamics in India, playing on inside jokes and having the main story being about Chotta Bheem failing a math test and his mom being mad at him, a common theme in South Asian households.
We felt that creating this connection to our culture made the game far more meaningful to us when we worked on it, and hopefully more meaningful and entertaining to our fellow students when they play it.

Us at ISA Diwali

**Mission Statement**
Design an engaging game that connects to our culture.

**Instructions to Run**
Run Main.py
If not using XBox controller, use the arrow keys to move and the spacebar to attack
If using the XBox controller, connect it to the PC by either connecting it via MicroUSB or using Bluetooth. Once connected, use the left joystick to move and “X” to attack.


**Architecture**
Monsters
We have two different types of monsters, mini bosses and medium bosses. Mini bosses are the “henchmen” of the medium bosses and are the first wave of challenges in each dungeon- the player must first fight their way through all the mini bosses before getting to the medium boss, which is the boss for each dungeon. We have a generic Monster.py file, which contains all the baseline monster functions that all the mini bosses/medium bosses have and use for their behavior, like shooting, patrolling, moving, etc. Each monster also has a projectile attribute, which is a projectile object assigned to it. The monster file also has a realign_projectile function, which sends the projectile back to the monster after it goes off the screen or collides with the player. MiniBoss.py contains more functions specific to mini bosses like predefined close-ranged attacks and long-ranged attacks that we can easily call. MediumBoss.py works in a similar way, containing more generic attacks that all medium bosses are able to use. Finally, we have the specific monster files for each mini boss/medium boss. For our mini bosses files, we have CricketNPC.py, AuntieClone.py, Paparazzi.py, and CSPKid.py. Our medium boss files are Kohli.py, Antieji.py, SRK.py, and Puri.py. In each of our specific monster files we have an attack function that controls all the movement, attacks, and cooldowns (if necessary) for that monster. Each of our mini bosses have a main_attack string assigned to them (since each mini boss only has one type of attack assigned to them). For example, the CricketNPC has a patrol and shoot attack, a follow path and shoot attack, and a hit attack, which is where the monster just constantly travels towards the player. The medium bosses also all have some sort of cooldown, where after they use their main set of attacks, they are in a cooldown where they can’t move or attack. This is the player’s chance to hit the monster before the monster ends its cooldown and returns back to its original set of attacks, thereby making the game a bit easier to beat.

**Overworld:**
The Overworld class is where all the rooms are initialized. Each room is its own Biome object that has an image (given by self.file_path), list of exits that lead to neighboring rooms, text, obstacles, items, and monsters. When you render a room (using the render and render_characters functions), the room image, obstacles, text, and monsters are all rendered together. After each room is initialized in Overworld, the monsters and obstacles for that room are also initialized and added to the room.
The Overworld class also contains methods for transitioning between rooms and levels, preventing player and obstacle collision, allowing monsters to attack players, picking up items, and unlocking blocked exits. When transitioning between rooms and levels, the next room that needs to be rendered is shown in parts rather than changing all at once to provide a feeling of actually traveling to a new location. To do the player and obstacle collision, the colliderect function was used to detect when the player touches any of the obstacles in the room. If the colliderect function returns True, then the player position is adjusted according to what direction the player was traveling to prevent the player from walking through obstacles. Essentially, the Overworld class ties together many of the other classes and allows for all the rooms to be rendered.

**Items:**
The Item class is for all items the player can pick up during the game. The classes it comprises are the Ladoo, Key and Ingredient sub-classes, all which have relatively similar functionality and so were able to inherit most methods from the main item class.
The main method of the Item class is the render method, which just takes in the item image, scales it up to the standard item size, and renders the item. In classes like the key and ladoo class, I override this method with a majority of the same code, but a use case where if the item has already been picked up, it will not be rendered.
Most of the functionality of the items are taken care of in other parts of the code, the Item class is mostly used just for simple consistent rendering across all items we added into the project.	

**Player:**
Player class has to take a spritesheet of the Chotta Bheem character in different positions, and use subsurface() to separate the sprite sheet into a Surface that is added to the list of frames. In the handlemove() function, we check booleans for if the player is attacking, is paralyzed, and direction. When the player presses the right arrow key, for example, the direction variable is changed to “right”. And same for up. At the end, the player rectangle is updated with move_ip().
The render function renders the spritesheet frame that aligns with the current direction, and renders the punching version of the character. There is also a function to render health, which renders a full heart, half heart, and empty heart based on the value of the health_bar. 	
The die_and_begone function checks if the health is completely 0, and if so, it blits the game over screen and respawns if it is turned on, or exits the game if player is playing without respawn.



**User Experience**
Storyline:
We tried to make the storyline both entertaining and funny to keep the user engaged throughout the game. For example, in the third level (the gala rooms), we made the user experience more enjoyable by adding John Cena music and making the medium boss Shah Rukh Khan so that while the player is paralyzed and unable to attack, they are still entertained by these creative and comedic additions. We changed the location and monster images for each level of the game, while still trying to maintain an overall theme and the purpose of the quest, to prevent the user from feeling that the game was boring.
Text Guidance: 
There are text prompts throughout the game to make it easy for the user to understand how to play the game. For example, the starting few screens explain to the user how they can use arrow keys to move and press space to attack. Later in the game, the text slowly explains different aspects of the game such as how the player can pick up items to increase their health. By choosing to give instructions one at a time through the display of text on particular screens instead of giving them all at once in the beginning, we tried to slowly introduce the user to the game’s rules and functions to prevent them from feeling overwhelmed with information and confused at the beginning. Additionally, after testing our code, we decided to make the printing of the text faster so that the user didn’t have to wait for too long for the text to be fully displayed.
Difficulty Levels: 
We planned different attacks for each Medium Boss and lesser impact attacks for the Mini Bosses of each level. This allows that player to engage with different types of combat so the levels don’t get repetitive. Additionally, we changed constants such as projectile speeds and monster speeds of each monster based on our experiences during a play-through. For example, in the Auntieji level, we throw an unexpected curve at the player by cloning in Auntie Mini Bosses when the player has halfway defeated the main Auntie. 
Checkpoints: 
To encourage the player to keep playing the game, even if they suck, we added checkpoints, which allows the player to respawn in the first room of the level they died in. This ensures that the player will not get frustrated with their lack of skill and continue to maintain hope to continue playing the game.
Theatrics: 
We had many animations and theatrical transitions throughout the game to improve the user experience when transitioning between levels and rooms. For example, when the monster in a dungeon is killed, based on a probability they drop a key that the player “picks up”, and when the player enters the room with the locked door, the key reappears and moves toward the door to unlock it. Another example is the transition between levels, where the player moves to pick up an ingredient, and then the next level opens up with animation. Our game also has a variety of sound effects including background music as the player progresses through the dungeons. These details immensely improve the user experience and game experience.
Health/Food: 
Out of the list of things in our backlog, we prioritized creating items that boost the player’s health such as the ladoos. This feature reduced the difficulty of the game to ensure that the user didn’t find it impossible to finish the game and thus felt motivated to continue playing.
Standardize Experience:
After initially developing the game, we noticed that the game ran at far different speeds across different machines, depending on their processing speed. This made it hard for us to balance things like animation and difficulty, as it was vastly different based on the machine the code was run on. To fix this, we set a max frames per second (30) that the game loop would run. We kept this number low enough that most of the machines we tested were able to easily run at that speed. This allowed us to standardize the experience across multiple machines and gave us control back over the user’s gameplay. When you are unsure about what exactly the user’s gameplay looks like due to differences in computing power, it makes it far harder to prioritize their experience while playing.



**Retrospectives**
General Feeling
We feel that overall the process of writing this app was a success. We learned a lot about collaborating with others, both through code in Git and with our overall communication. The process was very rewarding overall, developing a fun game allowed us to have a product of our efforts that we could show to others. Despite some frustrations along the way (mostly fixing the numerous bugs that inevitably showed up during our development), the process was overall very enjoyable.
Communication
Overall, our communication was quite strong. In the early days of the project, we immediately made a team group chat and used it extensively throughout the project. Additionally, we also split up tasks effectively, utilizing smaller groups to speed up discussion times. Later on, we utilized a calendar to plan out tasks and set deadlines in order to effectively finish the project on time. However, we did not use Github Issues very effectively, which I think cost us some efficiency in terms of work. 

Our January Deadline Calendar



**Major Surprises**
We each spent a long time fixing bugs in our code, especially for the collision system. While we expected that there would inevitably be issues with the code after we all put together our individual parts, we didn’t expect that these issues would take several days to debug and that at times it would be very difficult to determine why the issue was happening. Another surprise was when we had lots of merging and git issues when trying to push code. While merging issues were expected since we were working in a larger group, there were times when git raised issues even after we followed the process of add > commit > git pull –rebase > resolve merge conflicts > git rebase –continue > git push.
Improvements for Next Time
We spent the first two weeks of the project trying to learn how to use React and Electron as alternate frameworks to Pygame. However, in the end we decided to just use Pygame due to the steep learning curve it would take to learn an entirely new framework. We decided to prioritize making our game more appealing to our players over choosing a framework that offered more functionality but was difficult to learn. Next time, it would be better if we spent less time determining what platform and programming language we would like to use as this time could have been better spent adding additional features to our game. Next time we would also like to start putting together the individual components of our game earlier on. This would allow us to fix bugs in our code that arose after we put everything together one at a time rather than having to fix all the bugs at once closer to the end of the deadline.
