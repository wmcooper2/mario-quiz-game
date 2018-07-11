import pyglet
from pyglet.window import key

DEBUG = False


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
