import pyglet
from pyglet.window import key

#DEBUG = False
DEBUG = True

EASY_DIFFICULTY = True
MEDIUM_DIFFICULTY = False
HARD_DIFFICULTY = False

#for 7 items, waiting to debug the 3 new ones
#EASY = [35, 30, 15, 10, 5, 3, 2]
EASY = [2, 5, 10, 20, 35, 65, 100]

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
ITEM_PLATFORM_H = 264
ITEM_PLATFORM_W = 300
ITEM_DISAPPEAR_H = 300
NUM_PLAYERS = 6
NUM_ITEMS = 6
SCORE_SPRITE_Y = SCREEN_H - 36

ITEM_X_SPEED = 3

#QUESTION_BLOCK_EFFECT = False
#BOMBOMB_EFFECT = False
#POW_BUTTON_EFFECT = False
#SPINY_BEETLE_EFFECT = False
#GREEN_MUSHROOM_EFFECT = False
#RED_MUSHROOM_EFFECT = False
#PIRAHNA_PLANT_EFFECT = False
#YOSHI_COIN_EFFECT = False
FEATHER_EFFECT = False
#STAR_EFFECT = False
