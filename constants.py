#std lib 
import enum

#3rd party
import pyglet
from pyglet.window import key


#setup image directory
resource_dir = "./resources"
pyglet.resource.path = [resource_dir]
pyglet.resource.reindex()

class constants():


#CONVENIENCE VARIABLES
    IMG = pyglet.resource.image
    GRID = pyglet.image.ImageGrid
    ANIM = pyglet.image.Animation.from_image_sequence
    SPRITE = pyglet.sprite.Sprite

#FLAGS
    #DEBUG
    DEBUG = False
    ALL_RED_MUSHROOMS = False
    ALL_GREEN_MUSHROOMS = False
    ALL_YOSHI_COINS = False
    ALL_PIRAHNA_PLANTS = False
    ALL_SPINY_BEETLES = False
    ALL_POW_BUTTONS = False
    ALL_BOMBOMBS = False

    #EFFECTS
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
    RANDOMIZE_PLAYERS = False
    GAME_JUST_STARTED = True 
    MIXING_PLAYER_SPOTS = False
    BOMBOMB_EFFECT = False
    POW_BUTTON_EFFECT = False

    RED_MUSHROOM = "red mushroom"
    GREEN_MUSHROOM = "green mushroom" 
    YOSHI_COIN = "yoshi coin"
    PIRAHNA_PLANT = "pirahna plant"
    SPINY_BEETLE = "spiny beetle"
    POW_BUTTON = "pow button"
    BOMBOMB = "bombomb"

#IMPORTANT LISTS
    ALL_ITEMS = []
    PLAYERS = []
    ALL_PLAYERS = []
    SCORE_DISPLAY = []
    WALKING_PLAYERS = []
    FLOATING_PLAYERS = []
    QUESTION_ITEM = []

#SETTINGS
    NUM_PLAYERS = 6
    NUM_ITEMS = 9
    GRADES = [1, 2, 3]
    PAGE_RANGE = [0, 500]
    MIN_OPACITY = 0
    MAX_OPACITY = 255

#DIFFICULTY LEVEL
    SUPER_EASY = False
    EASY = False
    MEDIUM = False
    HARD = False
    SUPER_HARD = True

#PROBABILITIES
    #for 7 items, waiting to debug the 3 new ones (star, feather, question block)
    #[bombomb, pow button, spiny beetle, pirahna plant, yoshi coin, green mushroom, red mushroom]
    #actual ranges      <-hard items     easy items->           #probabilities (% of appearance)
    SUPER_EASY_RANGE =  [1, 2, 3, 8, 18, 55, 100]               # 1,  1,  1,  5, 10, 37, 45
    EASY_RANGE =        [2, 5, 10, 20, 35, 65, 100]             # 2,  3,  5, 10, 15, 30, 35
    MEDIUM_RANGE =      [5, 10, 20, 35, 50, 75, 100]            # 5,  5, 10, 15, 15, 25, 25
    HARD_RANGE =        [15, 30, 45, 60, 75, 90, 100]           #15, 15, 15, 15, 15, 15, 10
    SUPER_HARD_RANGE =  [10, 20, 40, 60, 80, 90, 100]           #10, 10, 20, 20, 20, 10, 10

    ITEM_START_LEFT = 216   #be careful changing this value
    ITEM_PLATFORM_H = 264
    ITEM_PLATFORM_W = 300
    ITEM_X_SPEED = 2        #set to 1 or 2 when not in debug mode
    ITEM_Y_SPEED = 1

#GAMEPLAY SETTINGS
    FRAME_SPEED = 1/90
    GAME_WINDOW = pyglet.window.Window(1000, 563)
    MAIN_BATCH = pyglet.graphics.Batch()
    KH = key.KeyStateHandler()  # Key Handler
    GAME_WINDOW.push_handlers(KH)

    SCREEN_W = GAME_WINDOW.width
    SCREEN_H = GAME_WINDOW.height
    OFF_SCREEN_R = 1100
    OFF_SCREEN_L = -100
    FLOAT_H = 100
    WALK_H = 63
    SCORE_SPRITE_Y = SCREEN_H - 36
    MAIN_TIME = 0

#CHANGING POINTS OF FOCUS DURING GAMEPLAY
    P1 = None
    ITEM = None

#QUESTION SETTINGS 
    SHOWING_BLACK_BOX = False
    NEW_QUESTION = None

#DEBUG TOOLS
    SPRITE_DATA = ["opacity", "x", "y", "dx", "dy", "dest_x", "dest_y"]

class player_speed(enum.Enum):
    walk = 0
    run = 1

