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
# from scores import mini_sprite

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

def set_player_spots() -> None:
    """Sets player positions on the screen."""
    for place in range(c.NUM_PLAYERS):
        if len(c.PLAYER_SPOTS) == 0:
            first_spot = (c.SCREEN_W // 2) - 150
            c.PLAYER_SPOTS.append(first_spot)
        else:
            next_spot = (c.SCREEN_W // 2) - 150 + (100 * place)
            c.PLAYER_SPOTS.append(next_spot)

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
    """Sets score positions evenly along the width of the screen."""
    for num in enumerate(c.PLAYERS):
        space = c.SCREEN_W // len(c.PLAYERS)
        c.SCORE_SPOTS.append((num[0] * space) + (space // 2))

def set_score_indices() -> None:
    """Set player index."""
    for player in c.PLAYERS:
        player.player_index()

def set_player_score_sprites() -> None:
    """Create a mini sprite of the player. Used in the score display."""
    for player in c.PLAYERS:
        player.mini_sprite()

def assign_x_pos_to_player_score_sprites() -> None:
    """Set the x pos of the player's score sprite."""
    for player in c.PLAYERS:
        player.set_score_x()

def set_score_values_x() -> None:
    """Set the x pos of the number in the score display."""
    for player in c.PLAYERS:
        player.set_value_x()

def set_score_number() -> None:
    """Set the player's score to a number. """
    for player in c.PLAYERS:
        player.set_score_number()

