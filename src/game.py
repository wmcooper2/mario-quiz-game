#!/usr/bin/env python3
# from constants import *
# from gameutil import *
# from itemsetup import *
# from playerscores import *
# from problems import *
# from items import *  # must come after players import
from background import Background
# from yammy import Yammy
from floatingplayer import FloatingPlayer
from walkingplayer import WalkingPlayer


# 3rd party
import pyglet

"""Main file for the Mario quiz game."""
clock = pyglet.clock
key = pyglet.window.key
# from pyglet import clock
# from pyglet.window import key
pyglet.resource.path = ["./images"]  # dont move this
pyglet.resource.reindex()  # dont move this


FRAME_SPEED = 1/90
GAME_WINDOW = pyglet.window.Window(1000, 563)
SCREEN_WIDTH = GAME_WINDOW.width
SCREEN_HEIGHT = GAME_WINDOW.height
SCORE_SPRITE_Y = SCREEN_HEIGHT - 36
MAIN = pyglet.graphics.Batch()
key_handler = key.KeyStateHandler()
GAME_WINDOW.push_handlers(key_handler)
background_img = pyglet.resource.image("quiz1.png")
BACKGROUND = Background(img=background_img, batch=MAIN)

YAMMY_PLATFORM_H = 264
YAMMY_X = 30
OFF_SCREEN_RIGHT = 600
OFF_SCREEN_LEFT = -100
FLOAT_HEIGHT = 100
FLOAT_SPEED = 3
GROUND_HEIGHT = 63


@GAME_WINDOW.event
def on_draw():
    """Draw the visual elements. Returns None."""
    GAME_WINDOW.clear()
    MAIN.draw()


# PLAYER SETUP
# sprite image setup
# yammy_img = pyglet.resource.image("yammyfaceright.png")
# yammy_img = pyglet.image.load("yammyfaceright.png").get_texture()
fire_light_img = pyglet.resource.image("firelightgoleft.png")
fire_light_go_right = pyglet.resource.image("firelightgoright.png")
fire_light_go_left = pyglet.resource.image("firelightgoleft.png")

boo_img = pyglet.resource.image("bigboofaceleft.png")
boo_go_right = pyglet.resource.image("bigboogoright.png")
boo_go_left = pyglet.resource.image("bigboogoleft.png")

mole_img = pyglet.resource.image("bigmolefaceleft.png")
mole_go_right = pyglet.resource.image("bigmolegoright.png")
mole_go_left = pyglet.resource.image("bigmolegoleft.png")


dragon_img = pyglet.resource.image("dragonfaceleft.png")
dragon_go_right = pyglet.resource.image("dragongoright.png")
dragon_go_left = pyglet.resource.image("dragongoleft.png")


# yammy = Yammy(yammy_img, x=YAMMY_X, y=YAMMY_PLATFORM_H, batch=MAIN)
# f2 = FireLight()
# print("f2: ", f2)
fire_light = FloatingPlayer(fire_light_img, fire_light_go_right,
                            fire_light_go_left, x=100, y=FLOAT_HEIGHT, batch=MAIN)
boo = FloatingPlayer(boo_img, boo_go_right,
                     boo_go_left, x=200, y=FLOAT_HEIGHT, batch=MAIN)
mole = WalkingPlayer(mole_img, mole_go_right, mole_go_left,
                     x=300, y=GROUND_HEIGHT, batch=MAIN)
dragon = WalkingPlayer(dragon_img, dragon_go_right, dragon_go_left,
                       x=400, y=GROUND_HEIGHT, batch=MAIN)


# this is for shuffling the order and for the update loop
# characters are drawn through the batch=MAIN kwargs
PLAYERS = [fire_light, boo, mole, dragon]
# PLAYER_SPOTS = []

# randomize_players(characters)                 # gameutil.py
# player_positions()                            # gameutil.py
# all_items = setup_items(NUM_ITEMS)            # itemsetup.py
# item_positions(all_items)                     # gameutil.py
# score_positions()                             # gameutil.py
# setup_scores(PLAYERS, SCORE_SPOTS, SCORES)    # playerscores.py
# prob = Problem()                              # problems.py


# def update_x_pos(player, DT):
# """Updates player's x-position. Returns None."""
# player.spot = PLAYER_SPOTS[PLAYERS.index(player)]
# player.update(DT)


# def player_score(player):
# """Updates player's score. Returns None."""
# score_points = SCORES[player.point_index].points
# score_object = SCORES[player.point_index]
# if player.points != score_points:
# score_object.update(score_object, player)


# def player_inventory(player, DT):
# """Updates player's item. Returns None."""
# items = player.inventory
# if items:
# items[0].update(DT)
# items[0].transition()


def update(DT):
    """Game update loop. Returns None."""
    # yammy.update(DT)
    # fire_light.update()
    # big_boo.update()
    # big_mole.update()

    for player in PLAYERS:
        # update_x_pos(player, DT)
        # player_score(player)
        # player_inventory(player, DT)
        player.update()


# pp = PLAYERS
# readyplayer = pp[0]
# pprint(FLAGS)
# if readyplayer.inventory:
# present_problem(readyplayer, prob)

# if FLAGS["bombomb"]:
# print("BANG!")

# update PLAYERS
# update_players(DT)
# [player.float() for player in floaters]
# update_items(all_items, DT)  # items.py
# update_scores()

# DEBUG
#    if key_handler[key.SPACE]:
#    pprint(key_handler.keys())

# player gets one item
# if key_handler[key._1] \
# and not any_movement(all_items, pp, yammy) \
# and not FLAGS["box"]:
# FLAGS["box"] = not FLAGS["box"]
# item = all_items[0]
# yammy.wand()  # wave magic wand
# yammy.take(item)  # takes the item
# all_items.remove(item)  # item taken from platform
# item.spot_y = ITEM_DISAPPEAR_HEIGHT  # raise item
# item.trans = not item.trans
# item.trans_dir = not item.trans_dir

# all_items.append(new_item())  # new item to lineup
# yammy.victim = readyplayer
#        give item and remove from inventory

#   if key_handler[key.LEFT] \
#       and not player_movement(pp) \
#       and not S_BB:
#           rotate_players_left(pp)

#   if key_handler[key.RIGHT] \
#       and not player_movement(pp) \
#       and not S_BB:
#           rotate_players_right(pp)

#   if key_handler[key.UP] \
#       and not player_movement(pp) \
#       and not S_BB:
#           mix_players(pp)

#   if key_handler[key.O] \
#       and readyplayer.has_item() \
#       and S_BB:
#           plus_one(readyplayer)
#           item_clean_up(pp, S_BB)

#   if key_handler[key.X] \
#       and readyplayer.has_item() \
#       and S_BB:
#           minus_one(readyplayer)
#           item_clean_up(pp, S_BB)

# if key_handler[key.A] \
# and not item_movement(all_items, yammy):
# rotate_items_left(all_items)

# if key_handler[key.D] \
# and not item_movement(all_items, yammy):
# rotate_items_right(all_items)


#   if key_handler[key.S] \
#       and not item_movement(all_items, yammy):
#           mix_items(all_items)
#


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, FRAME_SPEED)
    pyglet.app.run()
