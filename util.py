#std lib
import math
import random
from typing import Any, List 

#3rd party
import pyglet
from pyglet.window import key

#custom
from constants import Constants as c
from constants import Screens
from constants import Items as i


#SCREENS
def is_title_screen() -> bool:
    return c.SCREEN == Screens.TITLE

def is_options_screen() -> bool:
    return c.SCREEN == Screens.OPTIONS

def is_game_screen() -> bool:
    return c.SCREEN == Screens.GAME

#GAMEPLAY
def any_movement() -> bool:
    """Checks if anything is moving."""
    if c.TRANSFER_ITEM != None:
        return any([movement(c.PLAYERS), movement(c.ALL_ITEMS), movement(c.TRANSFER_ITEM)])
    return any([movement(c.PLAYERS), movement(c.ALL_ITEMS)])

def mix(list_: List[Any]) -> List[Any]:
    """Mix elements of 'list_'."""
    mixed = []
    copy = list_[:]
    for x in list_:
        choice = random.choice(copy)
        mixed.append(choice)
        copy.remove(choice)
    return mixed[:]

def movement(obj: Any) -> bool:
    """Checks if anything is moving."""
    if type(obj) == list:
        return any([thing.dx or thing.dy for thing in obj])
    else:
        return obj.dx != 0 or obj.dy != 0

def player_has_item(player: Any) -> bool:
    """Does player have an item?"""
    return bool(player.item)

def player_in_front() -> Any:
    """Player in the front of the line."""
    return c.PLAYERS[0]

def remove_item_from_platform() -> Any:
    """Removes item from c.ALL_ITEMS."""
    return c.ALL_ITEMS.pop(0)

def reverse_rotate_player_list() -> None:
    """Rotates contents of players list to the right by one."""
    c.PLAYERS.insert(0, c.PLAYERS.pop())

def right_answer(player) -> None:
    """Gives a point to the player in the ready position."""
    player.points += 1

def rotate_items_left() -> None:
    """Rotates contents of items list to the right by one."""         
    c.ALL_ITEMS.insert(0, c.ALL_ITEMS.pop())

def rotate_items_right() -> None:
    """Rotates contents of the items list to left the by one."""      
    c.ALL_ITEMS.append(c.ALL_ITEMS.pop(0))

def rotate_players_left() -> None: 
    """Rotates contents of players list to the left by one."""
    c.PLAYERS.append(c.PLAYERS.pop(0))

def rotate_players_right() -> None:
    """Rotates contents of players list to the right by one."""
    c.PLAYERS.insert(0, c.PLAYERS.pop())

def wrong_answer(player) -> None:
    """Takes away a point from the player in the ready position."""
    player.points -= 1





#KEY HANDLER CONVENIENCE FUNCTIONS
def key_1() -> bool:
    return c.KH[key._1] 

def key_a() -> bool:
    return c.KH[key.A]

def key_b() -> bool:
    return c.KH[key.B]

def key_d() -> bool:
    return c.KH[key.D]

def key_f() -> bool:
    return c.KH[key.F]

def key_o() -> bool:
    return c.KH[key.O]

def key_q() -> bool:
    return c.KH[key.Q]

def key_s() -> bool:
    return c.KH[key.S]

def key_u() -> bool:
    return c.KH[key.U]

def key_x() -> bool:
    return c.KH[key.X]

def key_left() -> bool:
    return c.KH[key.LEFT] 

def key_right() -> bool:
    return c.KH[key.RIGHT] 

def key_up() -> bool:
    return c.KH[key.UP]

def key_down() -> bool:
    return c.KH[key.DOWN]

def key_enter() -> bool:
    return c.KH[key.ENTER]






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
