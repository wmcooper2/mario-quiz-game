#std lib
import math
import random
from typing import Any, List 

#3rd party
import pyglet
from pyglet.window import key

#custom
from constants import constants as c
from constants import Difficulty as d
from constants import Items as i
from items import (
    RedMushroom,
    GreenMushroom,
    YoshiCoin,
    PirahnaPlant,
    SpinyBeetle,
    PowButton,
    Bombomb,
    QuestionBlock,
    Feather,
    Star)
from scores import mini_sprite

#GAMEPLAY
#TODO, what about the movement of c.ITEM ?
def any_movement(players: List[Any], items: List[Any]) -> bool:
    """Checks if anything is moving."""
    return any([movement(players), movement(items)])

def black_box_visible() -> bool:
    return c.SHOWING_BLACK_BOX

def choose_item(difficulty: List[int]) -> Any:
    """Choose an item."""
    if difficulty == d.SUPER_EASY:
        return probability(c.SUPER_EASY_RANGE)
    elif difficulty == d.EASY:
        return probability(c.EASY_RANGE)
    elif difficulty == d.MEDIUM:
        return probability(c.MEDIUM_RANGE)
    elif difficulty == d.HARD:
        return probability(c.HARD_RANGE)
    elif difficulty == d.SUPER_HARD:
        return probability(c.SUPER_HARD_RANGE)
 
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

def new_item() -> Any:
    """Adds new item to all_items. Returns Sprite object."""
    difficulty = c.DIFFICULTY
    choice = choose_item(difficulty)

    if choice == i.RED_MUSHROOM: 
#         return RedMushroom(img=i.RedMushroom.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE)
        return RedMushroom(img=c.IMG("redmushroom.png"))

    elif choice == i.GREEN_MUSHROOM:
#         return GreenMushroom(img=i.GreenMushroom.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE)
        return GreenMushroom(img=c.IMG("greenmushroom.png"))

    elif choice == i.YOSHI_COIN: 
#         return YoshiCoin(img=i.YoshiCoin.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE)
        return YoshiCoin(img=c.IMG("yoshicoinright.png"))

    elif choice == i.PIRAHNA_PLANT:
#         return PirahnaPlant(img=i.PirahnaPlant.walk_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE)
        return PirahnaPlant(img=c.IMG("pirahnaplantsmall.png"))

    elif choice == i.SPINY_BEETLE: 
#         return SpinyBeetle(img=i.SpinyBeetle.walk_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE)
        return SpinyBeetle(img=c.IMG("spinybeetlestandright.png"))

    elif choice == i.POW_BUTTON: 
#         return PowButton(img=i.PowButton.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE)
        return PowButton(img=c.IMG("powbutton.png"))

    elif choice == i.BOMBOMB:
#         return Bombomb(img=i.Bombomb.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE)
        return Bombomb(img=c.IMG("bombombstandright.png"))

    elif choice == i.FEATHER: 
#        return Feather(img=i.Feather.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE)
       return Feather(img=c.IMG("feather.png"))

    elif choice == i.STAR: 
#        return Star(img=i.Star.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE)
       return Star(img=c.IMG("star.png"))

    elif choice == i.QUESTION_BLOCK: 
#        return QuestionBlock(img=i.QuestionBlock.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE)
       return QuestionBlock(img=c.IMG("questionblock.png"))






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
def add_item() -> None:
    """Adds 1 new item to c.ALL_ITEMS."""
    c.ALL_ITEMS.append(new_item())

# def add_items(new_item) -> None:
def add_items() -> None:
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

# def center_ground_sprite(obj):
#     obj.anchor_x = obj.width // 2
#     obj.anchor_y = 0

def probability(choices) -> Any:
    """returns a choice of item based on the passed in probability list."""
    choice = random.randrange(1, 100, 1)
    if choice >= choices[5] and choice <= choices[6]:                  
        return i.RED_MUSHROOM
    elif choice >= choices[4] and choice < choices[5]:               
        return i.GREEN_MUSHROOM 
    elif choice >= choices[3] and choice < choices[4]:                
        return i.YOSHI_COIN 
    elif choice >= choices[2] and choice < choices[3]:               
        return i.PIRAHNA_PLANT 
    elif choice >= choices[1] and choice < choices[2]:              
        return i.SPINY_BEETLE 
    elif choice >= choices[0] and choice < choices[1]:             
        return i.POW_BUTTON 
    elif choice > 0 and choice < choices[0]:            
        return i.BOMBOMB 

def set_player_spots() -> None:
    """Sets player positions on the screen."""
    for place in range(c.NUM_PLAYERS):
        if len(c.PLAYER_SPOTS) == 0:
            first_spot = (c.SCREEN_W // 2) - 150
            c.PLAYER_SPOTS.append(first_spot)
        else:
            next_spot = (c.SCREEN_W // 2) - 150 + (100 * place)
            c.PLAYER_SPOTS.append(next_spot)

def setup_positions_on_screen():
    """Calculate and assign the positions on screen."""
    set_player_spots()
    set_item_spots(c.ALL_ITEMS)
    set_score_spots()
#     add_items()                       #sets up c.ALL_ITEMS
    add_players(c.RANDOMIZE_PLAYERS)          #sets up c.PLAYERS
#     scores_setup(c.SCORE_SPOTS, mini_sprite)
    scores_setup(c.SCORE_SPOTS)

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

# def scores_setup(spots, mini_sprite) -> None:
def scores_setup(spots) -> None:
    """Assign mini sprites to players."""
    for player in c.PLAYERS:
        score_x = spots[c.PLAYERS.index(player)]
        sprite = mini_sprite(player, score_x)
        c.SCORE_DISPLAY.append(sprite) 
        player.point_index = c.SCORE_DISPLAY.index(sprite) 
