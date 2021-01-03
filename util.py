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
    return any([player.dx for player in c.PLAYERS])

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

def set_player_spots() -> None:
    """Sets player positions on the screen."""
    for place in range(c.NUM_PLAYERS):
        if len(c.PLAYER_SPOTS) == 0:
            first_spot = (c.SCREEN_W // 2) - 150
            c.PLAYER_SPOTS.append(first_spot)
        else:
            next_spot = (c.SCREEN_W // 2) - 150 + (100 * place)
            c.PLAYER_SPOTS.append(next_spot)

def set_item_spots(items) -> None:
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

def scores_setup(spots, make_sprite) -> None:
    """Setup the score sprites at the top of the screen."""
    for player in c.PLAYERS:
        score_x = spots[c.PLAYERS.index(player)]
        sprite = make_sprite(player, score_x)
        c.SCORE_DISPLAY.append(sprite) 
        player.point_index = c.SCORE_DISPLAY.index(sprite) 
