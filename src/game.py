# 3rd party
from sharedconstants import main_batch
from setup import players
from gameutil import randomize_players, calculate_player_starting_pos
import pyglet
from tabulate import tabulate
"""Main file for the Mario quiz game."""
clock = pyglet.clock
key = pyglet.window.key

# for image setup
# read, https://pyglet.readthedocs.io/en/latest/modules/resource.html#pyglet.resource.reindex
pyglet.resource.reindex()

# from constants import *
# from itemsetup import *
# from playerscores import *
# from problems import *
# from items import *  # must come after players import
# from background import Background


FRAME_SPEED: float = 1/90
GAME_WINDOW = pyglet.window.Window(1000, 563)
SCREEN_WIDTH: int = GAME_WINDOW.width
SCREEN_HEIGHT: int = GAME_WINDOW.height
SCORE_SPRITE_Y: int = SCREEN_HEIGHT - 36
key_handler = key.KeyStateHandler()
GAME_WINDOW.push_handlers(key_handler)
DEBUG = True


@GAME_WINDOW.event
def on_draw():
    """Draw the visual elements. Returns None."""
    GAME_WINDOW.clear()
    main_batch.draw()

# this is for shuffling the order and for the update loop
# characters are drawn through the batch=main_batch kwargs
# players = [fire_light, boo, mole, dragon, koopa, luigi, mario]
# PLAYER_SPOTS = []


# initial random order
# gameutil.py
starting_orders = randomize_players(players)
if DEBUG:
    orders = []
    for player in starting_orders:
        orders.append([starting_orders.index(player), player.name, id(player), player])
    print(tabulate(orders, ["random starting order", "name", "object id", "object"]))
    print()

# replace original player order from loading instances with randomized starting order
players = starting_orders

# gameutil.py
player_screen_positions = calculate_player_starting_pos(
    players, SCREEN_WIDTH)
# print("player_screen_positions: ", player_screen_positions)
# assign players to screen positions
for player in players:
    index = players.index(player)
    new_position = player_screen_positions[index]
    player.spot_in_line = new_position

if DEBUG:
    orders = []
    for player in players:
        orders.append(
            [players.index(player), player.spot_in_line, player.name, id(player), player])
    print(tabulate(orders, ["current order",
                            "x-pixels", "name", "object id", "object"]))
    print()


# all_items = setup_items(NUM_ITEMS)            # itemsetup.py
# item_positions(all_items)                     # gameutil.py
# score_positions()                             # gameutil.py
# setup_scores(players, SCORE_SPOTS, SCORES)    # playerscores.py
# prob = Problem()                              # problems.py


# def update_x_pos(player, DT):
# """Updates player's x-position. Returns None."""
# player.spot_in_line = PLAYER_SPOTS[players.index(player)]
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

    for player in players:
        # update_x_pos(player, DT)
        # player_score(player)
        # player_inventory(player, DT)
        player.update()


# pp = players
# readyplayer = pp[0]
# pprint(FLAGS)
# if readyplayer.inventory:
# present_problem(readyplayer, prob)

# if FLAGS["bombomb"]:
# print("BANG!")

# update players
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
