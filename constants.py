import pyglet
from pyglet.window import key

FRAME_SPEED = 1/90

DEBUG = False
#DEBUG = True

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

SUPER_EASY = False
EASY = False
MEDIUM = False
HARD = True
SUPER_HARD = False

#for 7 items, waiting to debug the 3 new ones (star, feather, question block)
#[bombomb, pow button, spiny beetle, pirahna plant, yoshi coin, green mushroom, red mushroom]
#actual ranges      <-hard items     easy items->           #probabilities (% of appearance)
SUPER_EASY_RANGE =  [1, 2, 3, 8, 18, 55, 100]               # 1,  1,  1,  5, 10, 37, 45
EASY_RANGE =        [2, 5, 10, 20, 35, 65, 100]             # 2,  3,  5, 10, 15, 30, 35
MEDIUM_RANGE =      [5, 10, 20, 35, 50, 75, 100]            # 5,  5, 10, 15, 15, 25, 25
HARD_RANGE =        [15, 30, 45, 60, 75, 90, 100]           #15, 15, 15, 15, 15, 15, 10
SUPER_HARD_RANGE =  []

game_window = pyglet.window.Window(1000, 563)
main_batch = pyglet.graphics.Batch()
key_handler = key.KeyStateHandler()
game_window.push_handlers(key_handler)

SCREEN_W = game_window.width
SCREEN_H = game_window.height
OFF_SCREEN_R = 1100
OFF_SCREEN_L = -100
FLOAT_H = 100
WALK_H = 63
NUM_PLAYERS = 6
NUM_ITEMS = 6
SCORE_SPRITE_Y = SCREEN_H - 36

ITEM_START_LEFT = 216                   #be careful changing this value
ITEM_PLATFORM_H = 264
ITEM_PLATFORM_W = 300
ITEM_DISAPPEAR_H = 300
ITEM_X_SPEED = 1.5                      #set to 1 or 2 when not in debug mode
ITEM_Y_SPEED = 1


#QUESTION_BLOCK_EFFECT = False
#BOMBOMB_EFFECT = False
#POW_BUTTON_EFFECT = False
#SPINY_BEETLE_EFFECT = False
#GREEN_MUSHROOM_EFFECT = False
#RED_MUSHROOM_EFFECT = False
#PIRAHNA_PLANT_EFFECT = False
#YOSHI_COIN_EFFECT = False
FEATHER_EFFECT = False
STAR_EFFECT = False
