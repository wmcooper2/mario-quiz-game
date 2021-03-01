# Mario-Themed English Quiz Game
A turn-based English flashcard review game.  
Up to 6 players.  
Don't forget to install dependencies with `pip install -r requirements.txt` and to start up your virtual environment.  
Tested on python 3.9 and macOS (Big Sur).  

### Basic Gameplay
1. Decide the order of the teams and let them choose their players.
2. Run the game with `./start`
3. Wait for the players and items to come to a stop.
4. Press 1 to give a player an item.
5. Press "o" for a right answer and "x" for a wrong answer.
5. Answer within the time limit.
6. Player with the most points wins.

### Controls
|Key|Description|
|:---|:---|
|1 | give player an item  
|a | rotate items to left  
|s | randomly mix items  
|d | rotate items to right  
|x | current player minus one point  
|o | current player plus one point  
|u | use item (for player in first position only)  
|left arrow|rotate players left  
|right arrow|rotate players right  
|up arrow|randomly mix players  
|esc|quit the game  

#### Options Menu
|Key|Description|
|:---|:---|
|left right|move left and right
|up down|move up and down
|space|enable or disable (items only)  

### Items
|Item|Description|
|:---|:---|
|yoshi coin||
|red mushroom||
|green mushroom||
|pow button||
|spiney beetle||
|pirahna plant||
|bombomb||

_not yet_  
star  
feather  
question block

### Notes
* Still need to add effects for the items.  
* Character and item z-indices are a little wierd and you can notice it when they move across other sprites.  
* Need to add player selection screen.  
* Add difficutly changes. The labels are there but nothing changes yet in the game.  

### Screen Shots
![Title Screen](titleScreen.png)

![Option Screen](optionScreen.png)

![Game Screen](gameScreen.png)

![Game Screen 2](gameScreen2.png)
