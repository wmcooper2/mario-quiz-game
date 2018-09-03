import pyglet
from pyglet.window import key
import math

#debugging values
#DEBUG = False
DEBUG = True
ALL_RED_MUSHROOMS = False
ALL_GREEN_MUSHROOMS = False
ALL_YOSHI_COINS = False
ALL_PIRAHNA_PLANTS = False
ALL_SPINY_BEETLES = False
ALL_POW_BUTTONS = False
ALL_BOMBOMBS = False

RED_MUSHROOM = "red mushroom"
GREEN_MUSHROOM = "green mushroom" 
YOSHI_COIN = "yoshi coin"
PIRAHNA_PLANT = "pirahna plant"
SPINY_BEETLE = "spiny beetle"
POW_BUTTON = "pow button"
BOMBOMB = "bombomb"

#settings
NUM_PLAYERS = 6
NUM_ITEMS = 6
#GRADES = [1, 2, 3]              #only put in the grades that you want to include
#GRADES = [1, 2]              
GRADES = [1]              

# the page range only applies to the highest grade in GRADES
#PAGE_RANGE = [0, 500]           
#PAGE_RANGE = [0, 200]
#PAGE_RANGE = [0, 100]           
PAGE_RANGE = [0, 50]           
#PAGE_RANGE = [0, 35]

#difficulty level
SUPER_EASY = False
EASY = False
MEDIUM = False
HARD = False
SUPER_HARD = True

# for 7 items, waiting to debug the 3 new ones (star, feather, question block)
# [bombomb, pow button, spiny beetle, pirahna plant, yoshi coin, green mushroom, red mushroom]
# actual ranges     <-hard items     easy items->           #probabilities (% of appearance)
SUPER_EASY_RANGE =  [1, 2, 3, 8, 18, 55, 100]               # 1,  1,  1,  5, 10, 37, 45
EASY_RANGE =        [2, 5, 10, 20, 35, 65, 100]             # 2,  3,  5, 10, 15, 30, 35
MEDIUM_RANGE =      [5, 10, 20, 35, 50, 75, 100]            # 5,  5, 10, 15, 15, 25, 25
HARD_RANGE =        [15, 30, 45, 60, 75, 90, 100]           #15, 15, 15, 15, 15, 15, 10
SUPER_HARD_RANGE =  [10, 20, 40, 60, 80, 90, 100]           #10, 10, 20, 20, 20, 10, 10

# pixel locations relative to screen
TOP_ROW_SPOTS = []
INVENTORY_SPOT = []
PLAYER_SPOTS = []
ITEM_SPOTS = []
SCORE_SPOTS = []

ITEM_START_LEFT = 216                   #be careful changing this value
ITEM_PLATFORM_HEIGHT = 264
ITEM_PLATFORM_WIDTH = 300
ITEM_DISAPPEAR_HEIGHT = 300
ITEM_TRANSITION_SPEED = 9
ITEM_FALLING_SPEED = 6
ITEM_X_SPEED = 1.5
ITEM_Y_SPEED = 1

# flags
#QUESTION_BLOCK_EFFECT = False
BOMBOMB_EFFECT = False
POW_BUTTON_EFFECT = False
#SPINY_BEETLE_EFFECT = False
#GREEN_MUSHROOM_EFFECT = False
#RED_MUSHROOM_EFFECT = False
#PIRAHNA_PLANT_EFFECT = False
#YOSHI_COIN_EFFECT = False
FEATHER_EFFECT = False
STAR_EFFECT = False
PLAYERS_RANDOMIZED = False
GAME_JUST_STARTED = True
SHOW_BLACK_BOX = False
MIXING_PLAYER_SPOTS = False
NEW_QUESTION = True

FRAME_SPEED = 1/90
GAME_WINDOW = pyglet.window.Window(1000, 563)
MAIN_BATCH = pyglet.graphics.Batch()
KEY_HANDLER = key.KeyStateHandler()
GAME_WINDOW.push_handlers(KEY_HANDLER)
ENGLISH_FONT = "Comic Sans MS"
JAPANESE_FONT = "Yu Mincho Regular"
GUIDE_SIZE = 24
QUESTION_SIZE = 36
GUIDE = "Translate"

SCREEN_WIDTH = GAME_WINDOW.width
SCREEN_HEIGHT = GAME_WINDOW.height
OFF_SCREEN_RIGHT = 1100
OFF_SCREEN_LEFT = -100
FLOAT_HEIGHT = 100
WALK_HEIGHT = 63
SCORE_SPRITE_Y = SCREEN_HEIGHT - 36

def center_image(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def center_floater(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def center_walker(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2

def falling_item(time):
    """Calculates y position of falling object. Returns Integer."""
    #calculates "-(1/2) * g * t^2" where g == 9.8 and time is the accumu    lated time for falling
    #changed gravity to 5 from 9.8
    return math.floor(-(0.5 * 5) * (time ** 2))

def top_row_line_up():
    """Sets the positions of the top row on the screen (scores and item     inventory). Returns None."""
    for spot in range(7):
        TOP_ROW_SPOTS.append((SCREEN_WIDTH // 8) * spot + 125)
    if NUM_PLAYERS >= 4:
        INVENTORY_SPOT.append(TOP_ROW_SPOTS[3])

    #quick patch
    for element in TOP_ROW_SPOTS[0:3]:
        SCORE_SPOTS.append(element)
    for element in TOP_ROW_SPOTS[4:8]:
        SCORE_SPOTS.append(element)

def player_line_up():
    """Sets the available player positions on the screen. Returns None."""
    for place in range(NUM_PLAYERS):
        if len(PLAYER_SPOTS) == 0:
            first_spot = (SCREEN_WIDTH // 2) - 150
            PLAYER_SPOTS.append(first_spot)
        else:
            next_spot = (SCREEN_WIDTH // 2) - 150 + (100 * place)
            PLAYER_SPOTS.append(next_spot)

def item_line_up(items):
    """Sets the available item positions on the screen. Returns None."""
    for item in range(NUM_ITEMS):
        if len(ITEM_SPOTS) == 0:
            first_spot = (SCREEN_WIDTH // 2) - ITEM_START_LEFT
            ITEM_SPOTS.append(first_spot)
        else:
            next_spot = (SCREEN_WIDTH // 2) - ITEM_START_LEFT - (24 * item)
            ITEM_SPOTS.append(next_spot)
