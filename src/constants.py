# standard lib
from enum import Enum, auto
import math
from pathlib import Path
from typing import Dict, Text

# 3rd party
import pyglet
from pyglet.window import key


# GAME PLAY SETTINGS
class Settings:
    NUM_PLAYERS = 6
    NUM_ITEMS = 6
    # grades that you want to include in the game
    #GRADES          = [1, 2, 3]
    #GRADES          = [1, 2]
    GRADES = [1]


class Difficulty(Enum):
    # DIFFICULTY = "superhard"  # supereasy, easy, medium, hard, superhard
    SUPEREASY = auto()
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()
    SUPERHARD = auto()


class Items(Enum):
    RED_MUSHROOM = auto()
    GREEN_MUSHROOM = auto()
    YOSHI_COIN = auto()
    PIRAHNA_PLANT = auto()
    SPINY_BEETLE = auto()
    POW_BUTTON = auto()
    BOMBOMB = auto()

# ITEMS
# RED_MUSHROOM = "red mushroom"
# green_mushroom = "green mushroom"
# yoshi_coin = "yoshi coin"
# PIRAHNA_PLANT = "pirahna plant"
# SPINY_BEETLE = "spiny beetle"
# POW_BUTTON = "pow button"
# BOMBOMB = "bombomb"


# SCORES
BIG_SCORE_SIZE = 24
COIN_WIDTH = 12
COIN_WIDTH_B = 30
MAXSCORE_S = 5
MAXSCORE_B = 3
SCORES = []
SCORE_FONT = "Comic Sans MS"
SKULL_WIDTH = 16
ZERO_SIZE = 24

# page range only applies to the highest grade in GRADES
#PAGE_RANGE = [0, 500]
#PAGE_RANGE = [0, 200]
#PAGE_RANGE = [0, 100]
PAGE_RANGE = [0, 50]
#PAGE_RANGE = [0, 35]

# DIFFICULTY RANGES
# item indices;
# 1 bombomb
# 2 pow button
# 3 spiny beetle
# 4 pirahna plant
# 5 yoshi coin
# 6 green mushroom
# 7 red mushroom


class DifficultyRange():
    # actual ranges (uncommented)  <-mean items   nice items->
    # probabilities, % of appearance (commented)
    #  1, 1, 1, 5, 10, 37,  45
    SUPER_EASY = [1, 2, 3, 8, 18, 55, 100]
    #  2, 3,  5, 10, 15, 30,  35
    EASY_RANGE = [2, 5, 10, 20, 35, 65, 100]
    #5,  5, 10, 15, 15, 25,  25
    MEDIUM_RANGE = [5, 10, 20, 35, 50, 75, 100]
    #  15, 15, 15, 15, 15, 15,  10
    HARD_RANGE = [15, 30, 45, 60, 75, 90, 100]
    #  10, 10, 20, 20, 20, 10,  10
    SUPER_HARD_RANGE = [10, 20, 40, 60, 80, 90, 100]


# pixel locations relative to screen
TOP_ROW_SPOTS = []
INVENTORY_SPOT = []
ITEM_SPOTS = []
SCORE_SPOTS = []

ITEM_START_LEFT = 216  # be careful changing this value
ITEM_PLATFORM_WIDTH = 300
ITEM_DISAPPEAR_HEIGHT = 300
ITEM_TRANSITION_SPEED = 9
ITEM_FALLING_SPEED = 6
ITEM_X_SPEED = 1.5
ITEM_Y_SPEED = 1

# FLAGS
#QUESTION_BLOCK_EFFECT   = False
#BOMBOMB_EFFECT          = False
#DEBUG                   = False
#GREEN_MUSHROOM_EFFECT   = False
#PIRAHNA_PLANT_EFFECT    = False
#POW_BUTTON_EFFECT       = False
#RED_MUSHROOM_EFFECT     = False
#SPINY_BEETLE_EFFECT     = False
#YOSHI_COIN_EFFECT       = False
#FEATHER_EFFECT          = False
#STAR_EFFECT             = False
# PLAYERS_RANDOMIZED      = False    #delete
# S_BB                    = False     #show black box
#NEW_QUESTION            = True


class Flags:
    beetle = False
    bombomb = False
    box = False
    coin = False
    debug = False
    green_mush = False
    pirahna = False
    pow_block = False
    question = False
    red_mush = False

# FLAGS = {
    # "beetle": False,
    # "bombomb": False,
    # "box": False,
    # "coin": False,
    # "debug": False,
    # "g_mush": False,
    # "pirahna": False,
    # "pow": False,
    # "question": False,
    # "r_mush": False,
# }


MAIN_TIME = 0
ENGLISH_FONT = "Comic Sans MS"
JAPANESE_FONT = "Yu Mincho Regular"
GUIDE = "Translate"
GUIDE_SIZE = 24
QUESTION_SIZE = 36


# doesnt work, use the built in resource thing
#IMGS                = str(Path.cwd())+"/resources/"
#FIRELIGHT_R         = IMGS+"firelightgoright.png"
#FIRELIGHT_L         = IMGS+"firelightgoleft.png"
