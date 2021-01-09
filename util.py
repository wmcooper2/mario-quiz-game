#std lib
import math
import random
from typing import Any, List 

#3rd party
import pyglet
from pyglet.window import key

#custom
from constants import constants as c
# from constants import Difficulty as d
from constants import Items as i
from scores import mini_sprite

#GAMEPLAY
#TODO, what about the movement of c.ITEM ?
def any_movement(players: List[Any], items: List[Any]) -> bool:
    """Checks if anything is moving."""
    return any([movement(players), movement(items)])

def black_box_visible() -> bool:
    return c.SHOWING_BLACK_BOX
 
def mix(list_: List[Any]) -> List[Any]:
    """Mix elements of 'list_'."""
    mixed = []
    copy = list_[:]
    for x in list_:
        choice = random.choice(copy)
        mixed.append(choice)
        copy.remove(choice)
    return mixed[:]

def movement(list_: List[Any]) -> bool:
    """Checks if any player is moving."""
    return any([thing.dx or thing.dy for thing in list_])

def player1_has_item() -> bool:
    """Does player1 have an item?"""
    return bool(c.P1.inventory)

def remove_item_from_all_items() -> Any:
    """Removes item from c.ALL_ITEMS."""
#     item = c.ALL_ITEMS.pop(0)
#     c.ITEM = item
    return c.ALL_ITEMS.pop(0)

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

# def line_up(self):
#     """Sets the available player positions on the screen. Returns None."""                
#     for place in range(self.num_players):                                                 
#         if len(self.player_spots) == 1:                                                   
#             first_spot = (self.screen_w // 3) - 150                                       
#             self.player_spots.append(first_spot)
#         else:
#             next_spot = (self.screen_w // 3) - 150 + (100 * place)
#             self.player_spots.append(next_spot)                                           
# 
# def item_line_up(self, items):
#     """Sets the available item positions on the screen. Returns None."""                  
#     for item in range(c.NUM_ITEMS):                                                    
#         if len(c.ITEM_SPOTS) == 1:                                                     
#             first_spot = (c.SCREEN_W // 3) - c.ITEM_START_LEFT                         
#             c.ITEM_SPOTS.append(first_spot)
#         else:
#             next_spot = (c.SCREEN_W // 3) - c.ITEM_START_LEFT - (24 * item)            
#             c.ITEM_SPOTS.append(next_spot)     

def set_player_spots() -> None:
    """Sets player positions on the screen."""
    for place in range(c.NUM_PLAYERS):
        if len(c.PLAYER_SPOTS) == 0:
            first_spot = (c.SCREEN_W // 2) - 150
            c.PLAYER_SPOTS.append(first_spot)
        else:
            next_spot = (c.SCREEN_W // 2) - 150 + (100 * place)
            c.PLAYER_SPOTS.append(next_spot)

# def setup_positions_on_screen():
#     """Calculate and assign the positions on screen."""

def set_item_spots() -> None:
    """Sets item positions on the screen."""
    for item in range(c.NUM_ITEMS):
        if len(c.ITEM_SPOTS) == 0:
            first_spot = (c.SCREEN_W // 2) - c.ITEM_START_LEFT
            c.ITEM_SPOTS.append(first_spot)
        else:
            next_spot = (c.SCREEN_W // 2) - c.ITEM_START_LEFT - (24 * item) 
            c.ITEM_SPOTS.append(next_spot)

def set_score_spots() -> None:
    """Sets score positions on the screen."""
    for spot in range(7):
        c.TOP_ROW_SPOTS.append((c.SCREEN_W // 8) * spot + 125) 
    if c.NUM_PLAYERS >= 4:
        c.INVENTORY_SPOT.append(c.TOP_ROW_SPOTS[3])
    c.SCORE_SPOTS = c.TOP_ROW_SPOTS[0:3] + c.TOP_ROW_SPOTS[4:8] 

def scores_setup(spots) -> None:
    """Assign mini sprites to players."""
    for player in c.PLAYERS:
        score_x = spots[c.PLAYERS.index(player)]
        mini = mini_sprite(player)
        mini.x = score_x
        c.SCORE_DISPLAY.append(mini) 
        player.point_index = c.SCORE_DISPLAY.index(mini) 
