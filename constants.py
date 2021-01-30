#std lib 
import enum

#3rd party
import pyglet
from pyglet.window import key


#setup image directory
images = "./resources"
music = "./music"
pyglet.resource.path = [images, music]
pyglet.resource.reindex()

class player_speed(enum.Enum):
    walk = 0
    run = 1

class Items(enum.Enum):
    RED_MUSHROOM = 0
    GREEN_MUSHROOM = 1
    YOSHI_COIN = 2
    PIRAHNA_PLANT = 3
    SPINY_BEETLE = 4
    POW_BUTTON = 5
    BOMBOMB = 6
    FEATHER = 7
    STAR = 8
    QUESTION_BLOCK = 9

#DIFFICULTY LEVEL
class Difficulty(enum.Enum):
    SUPER_EASY = 0
    EASY = 1
    MEDIUM = 2
    HARD = 3
    SUPER_HARD = 4

class Effects(enum.Enum):
    QUESTION_BLOCK = 0
    BOMBOMB = 1
    POW_BUTTON = 2
    SPINY_BEETLE = 3
    GREEN_MUSHROOM = 4
    RED_MUSHROOM = 5
    PIRAHNA_PLANT = 6
    YOSHI_COIN = 7
    FEATHER = 8
    STAR = 9
    RANDOMIZE_PLAYERS = 10
    GAME_STARTED = 11
    MIXING_PLAYER = 12

class Screens():
    OPTIONS = False
    PLAYERS = False
    GAME = False
    TITLE = True
#     TITLE = False

class Constants():
#CONVENIENCE VARIABLES
    IMG = pyglet.resource.image
    GRID = pyglet.image.ImageGrid
    ANIM = pyglet.image.Animation.from_image_sequence
    SPRITE = pyglet.sprite.Sprite
    LABEL = pyglet.text.Label

#FLAGS
    #TODO, move the flags into enum classes
    #DEBUG
    DEBUG = False
    ALL_RED_MUSHROOMS = False
    ALL_GREEN_MUSHROOMS = False
    ALL_YOSHI_COINS = False
    ALL_PIRAHNA_PLANTS = False
    ALL_SPINY_BEETLES = False
    ALL_POW_BUTTONS = False
    ALL_BOMBOMBS = False

#IMPORTANT LISTS
    #items
    ALL_ITEMS = []
    ITEM_SPOTS = []
    QUESTION_ITEM = []

    #players
    ALL_PLAYERS = []
    FLOATING_PLAYERS = []
    PLAYERS = []
    PLAYER_SPOTS = []
    WALKING_PLAYERS = []

    #scores
    SCORE_DISPLAY = []
    SCORE_SPOTS = []

#SETTINGS
    NUM_PLAYERS = 6
    NUM_ITEMS = 9
    GRADES = [1, 2, 3]
    PAGE_RANGE = [0, 500]
    MIN_OPACITY = 0
    MAX_OPACITY = 255
    FONT = "Comic Sans MS"
    FONT_SIZE = 24
    DIFFICULTY = Difficulty.SUPER_HARD
    ITEM_SCALE = 1.5
    ITEM_START_LEFT = 216   #be careful changing this value
    ITEM_PLATFORM_H = 264
    ITEM_PLATFORM_W = 300
    ITEM_X_SPEED = 2        #set to 1 or 2 when not in debug mode
    ITEM_Y_SPEED = 1
    PLAYER_X_SPEED = 3
    PLAYER_Y_SPEED = 6

#PROBABILITIES
    #for 7 items, waiting to debug the 3 new ones (star, feather, question block)
    #[bombomb, pow button, spiny beetle, pirahna plant, yoshi coin, green mushroom, red mushroom]
    #actual ranges      <-hard items     easy items->           #probabilities (% of appearance)
    SUPER_EASY_RANGE =  [1, 2, 3, 8, 18, 55, 100]               # 1,  1,  1,  5, 10, 37, 45
    EASY_RANGE =        [2, 5, 10, 20, 35, 65, 100]             # 2,  3,  5, 10, 15, 30, 35
    MEDIUM_RANGE =      [5, 10, 20, 35, 50, 75, 100]            # 5,  5, 10, 15, 15, 25, 25
    HARD_RANGE =        [15, 30, 45, 60, 75, 90, 100]           #15, 15, 15, 15, 15, 15, 10
    SUPER_HARD_RANGE =  [10, 20, 40, 60, 80, 90, 100]           #10, 10, 20, 20, 20, 10, 10

#DRAWING SPRITES
    ANIMATION_BATCH = pyglet.graphics.Batch()
    MAIN_BATCH = pyglet.graphics.Batch()
    BACKGROUND_BATCH = pyglet.graphics.Batch()
    GROUND_BATCH = pyglet.graphics.Batch()
    PLAYER_BATCH = pyglet.graphics.Batch()
    ITEM_BATCH = pyglet.graphics.Batch()
    SCORE_BATCH = pyglet.graphics.Batch()
    YAMMY_BATCH = pyglet.graphics.Batch()
    PROBLEM_BATCH = pyglet.graphics.Batch()
    TITLE_BATCH = pyglet.graphics.Batch()
    TITLE_BACKGROUND_BATCH = pyglet.graphics.Batch()

#GAMEPLAY SETTINGS
    FRAME_SPEED = 1/90
    GAME_WINDOW = pyglet.window.Window(1000, 563)
    KH = key.KeyStateHandler()  # Key Handler
    GAME_WINDOW.push_handlers(KH)
    SCREEN_W = GAME_WINDOW.width
    SCREEN_H = GAME_WINDOW.height
    OFF_SCREEN_R = 1100
    OFF_SCREEN_L = -100
    FLOAT_H = 120
    WALK_H = 63
    MAIN_TIME = 0
    POINT_X_OFFSET = 40
    POINT_Y_OFFSET = 10
    SCORE_SPRITE_Y = 0

#CHANGING POINTS OF FOCUS DURING GAMEPLAY
    P1 = None
    TRANSFER_ITEM = None

#QUESTION SETTINGS 
#     SHOWING_BLACK_BOX = False
    NEW_QUESTION = None
