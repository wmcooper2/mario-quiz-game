#std lib
import math
import random
from typing import Any

#3rd party
import pyglet
from pyglet.window import key

#custom
from constants import constants as c


#GAMEPLAY
def any_movement() -> bool:
    """Checks if anything is moving."""
    return any([player_movement(), item_movement()])

def item_clean_up() -> None:
    """Removes item from c.P1 inventory and deletes it from the game."""
    pass
#     item = c.P1.inventory[0]
#     c.SHOWING_BLACK_BOX = False     #reset flag, stop showing box

    #empty list returns false...
#     c.P1.item = False               #reset flag

#     c.P1.inventory.remove(item)     #remove the item from c.P1's inventory
#     item.delete()                   #item's instance is deleted

    #show points in terminal (move to the update/draw blocks)
#     for player in c.PLAYERS:
#         print(player.__class__, " has ", player.points, " points.")
#         print("point_index = ", player.point_index)


#TODO, what about the movement of c.ITEM ?
def item_movement() -> bool:
    """Checks if any item is moving."""
    return any([item.dx or item.dy for item in c.ALL_ITEMS])

def mix_items() -> None:
    """Randomly mixes the items in the line."""
    mixed_items = []
    copy = c.ALL_ITEMS[:]
    for x in c.ALL_ITEMS:
        item_choice = random.choice(copy)
        mixed_items.append(item_choice)
        copy.remove(item_choice)
    c.ALL_ITEMS = mixed_items[:]

def mix_players() -> None:
    """Randomly mixes the players in the line."""
    mixed_players = []
    copy = c.PLAYERS[:]
    for x in c.PLAYERS:
        player_choice = random.choice(copy)
        mixed_players.append(player_choice)
        copy.remove(player_choice)
    c.PLAYERS = mixed_players[:]

def player_movement() -> bool:
    """Checks if any player is moving."""
    return any([player.moving for player in c.PLAYERS])

def player1_has_item() -> bool:
    """Does player1 have an item?"""
    return bool(c.P1.inventory)

def remove_item_from_all_items() -> Any:
    """Removes item from c.ALL_ITEMS and places it in c.ITEMS."""
    item = c.ALL_ITEMS.pop(0)
    c.ITEM = item
    return item

def reverse_rotate_player_list():
    """Rotates contents of players list to the right by one. Returns None."""
    player = c.PLAYERS.pop()
    c.PLAYERS.insert(0, player)

def right_answer(player) -> None:
    """Gives a point to the player in the ready position."""
    player.points += 1

def rotate_items_left() -> None:
    """Rotates contents of items list to the right by one."""         
    item = c.ALL_ITEMS.pop()
    c.ALL_ITEMS.insert(0, item)

def rotate_items_right() -> None:
    """Rotates contents of the items list to left the by one."""      
    item = c.ALL_ITEMS.pop(0)
    c.ALL_ITEMS.append(item) 

def rotate_players_left() -> None: 
    """Rotates contents of players list to the left by one."""
    player = c.PLAYERS.pop(0)
    c.PLAYERS.append(player)

def rotate_players_right() -> None:
    """Rotates contents of players list to the right by one."""
    player = c.PLAYERS.pop()
    c.PLAYERS.insert(0, player)

def wrong_answer(player) -> None:
    """Takes away a point from the player in the ready position."""
    player.points -= 1






#KEY HANDLER CONVENIENCE FUNCTIONS
def key_f() -> bool:
    return c.KH[key.F]

def key_1() -> bool:
    return c.KH[key._1] 

def key_left() -> bool:
    return c.KH[key.LEFT] 

def key_right() -> bool:
    return c.KH[key.RIGHT] 

def key_up() -> bool:
    return c.KH[key.UP]

def key_o() -> bool:
    return c.KH[key.O]

def key_x() -> bool:
    return c.KH[key.X]

def key_a() -> bool:
    return c.KH[key.A]

def key_d() -> bool:
    return c.KH[key.D]

def key_s() -> bool:
    return c.KH[key.S]






#SETUP
def add_item(new_item) -> None:
    """Adds 1 new item to c.ALL_ITEMS."""
    c.ALL_ITEMS.append(new_item())

def add_items(new_item) -> None:
    """Populates c.ALL_ITEMS."""
    for item in range(c.NUM_ITEMS):
        c.ALL_ITEMS.append(new_item())

def add_players(random_=False) -> None:
    """Populates c.PLAYERS."""
    #TODO, Random is the default here... change this to allow a non-random option
    if random_ == False:
        players = []
        copy = c.ALL_PLAYERS[:]
        for x in range(c.NUM_PLAYERS):
            choice_ = random.choice(copy)
            players.append(choice_)
            copy.remove(choice_)
        for player in players:
            c.PLAYERS.append(player) 

def center_image(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def center_floating_player(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def center_walking_player(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2

def center_ground_sprite(obj):
    obj.anchor_x = obj.width // 2
    obj.anchor_y = 0

class Line():
    """Line setup for items, players, scores, etc."""
    top_row_spots = []          #all positions at top of game_window
    inventory_spot = []         #center top of game_window
    player_spots = []           #filled by Line.line_up() 
    item_spots = []             #filled by Line.item_line_up()
    score_spots = []            #the xpos of the players' score sprites 
#     mixing_player_spots = False

    def __init__(self, num_players=0, screen_w=0, num_items=0, *args, **kwargs):
        self.num_players = num_players
        self.screen_w = screen_w
        self.num_items = num_items
        self.columns = []

    def top_row_line_up(self):
        """Sets the positions of the top row on the screen (scores and item inventory). Returns None."""
        for spot in range(7):
            self.top_row_spots.append((self.screen_w // 8) * spot + 125) 
        if self.num_players >= 4:
            self.inventory_spot.append(self.top_row_spots[3])
        self.score_spots = self.top_row_spots[0:3] + self.top_row_spots[4:8] 

    def line_up(self):
        """Sets the available player positions on the screen. Returns None."""
        for place in range(self.num_players):
            if len(self.player_spots) == 0:
                first_spot = (self.screen_w // 2) - 150
                self.player_spots.append(first_spot)
            else:
                next_spot = (self.screen_w // 2) - 150 + (100 * place)
                self.player_spots.append(next_spot)

    def item_line_up(self, items):
        """Sets the available item positions on the screen. Returns None."""
        for item in range(self.num_items):
            if len(self.item_spots) == 0:
                first_spot = (self.screen_w // 2) - c.ITEM_START_LEFT
                self.item_spots.append(first_spot)
            else:
                next_spot = (self.screen_w // 2) - c.ITEM_START_LEFT - (24 * item) 
                self.item_spots.append(next_spot)
