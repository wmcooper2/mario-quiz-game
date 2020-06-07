#!/usr/bin/env python3
"""Main file for the Mario quiz game."""
#        import pdb; pdb.set_trace()

#stand lib
from pprint import pprint
import random
import sys

#3rd party
import pyglet
from pyglet import clock
from pyglet.window import key
pyglet.resource.path = ["./resources"]  #dont move this
pyglet.resource.reindex()               #dont move this

#custom
from src.constants import *
from src.gameutil import *
from src.itemsetup import *
from src.players import *
from src.playersetup import *
from src.playerscores import *
from src.problems import *
from src.items import *     #must come after players import

BACKGROUND = Background(img=Background.background_img, batch=MAIN)

#PLAYER SETUP
yammy = make_yammy()
floaters = [
        fireLight(),
        bigBoo()]
walkers = [
        dragon(),
        greenKoopa(),
        bigMole(),
        mario(),
        luigi()]
characters = floaters + walkers
randomize_players(characters)               #gameutil.py
player_positions()                          #gameutil.py
all_items = setup_items(NUM_ITEMS)          #itemsetup.py
item_positions(all_items)                   #gameutil.py
score_positions()                           #gameutil.py
setup_scores(PLAYERS, SCORE_SPOTS, SCORES)  #playerscores.py
prob = Problem()                            #problems.py

# make sure that everything loaded properly at this point, before entering the game loop

@GAME_WINDOW.event
def on_draw():
    """Draw the visual elements. Returns None."""
    #GAME_WINDOW.event's module doesnt import my constants, 
    #+ maybe thats why I need globals here?
#    global NEW_QUESTION

    GAME_WINDOW.clear()
    MAIN.draw()

def update(DT):
    """Game update loop. Returns None."""
    pp          = PLAYERS
    readyplayer = pp[0]
    pprint(FLAGS)
    if readyplayer.inventory:
        present_problem(readyplayer, prob)

    if FLAGS["bombomb"]:      print("BANG!")

    #update PLAYERS
    update_players(DT)
    [player.float() for player in floaters]
    update_items(all_items, DT)          #items.py
    update_scores()
    yammy.update(DT)

    #fade yammy in and out
    if KH[key.F] \
        and not yammy.trans:
            yammy.trans = not yammy.trans
            yammy.trans_dir = not yammy.trans_dir


#DEBUG
#    if KH[key.SPACE]:
#        pprint(KH.keys())

    #player gets one item
    if KH[key._1] \
        and not any_movement(all_items, pp, yammy) \
        and not FLAGS["box"]:
            FLAGS["box"]    = not FLAGS["box"]
            item            = all_items[0]
            yammy.wand()                #wave magic wand
            yammy.take(item)            #takes the item
            all_items.remove(item)      #item taken from platform
            item.spot_y     = ITEM_DISAPPEAR_HEIGHT #raise item
            item.trans      = not item.trans
            item.trans_dir  = not item.trans_dir

            all_items.append(new_item())            #new item to lineup
            yammy.victim    = readyplayer
            #give item and remove from inventory

#    if KH[key.LEFT] \
#        and not player_movement(pp) \
#        and not S_BB:
#            rotate_players_left(pp)

#    if KH[key.RIGHT] \
#        and not player_movement(pp) \
#        and not S_BB:
#            rotate_players_right(pp)

#    if KH[key.UP] \
#        and not player_movement(pp) \
#        and not S_BB:
#            mix_players(pp)

#    if KH[key.O] \
#        and readyplayer.has_item() \
#        and S_BB:
#            plus_one(readyplayer)
#            item_clean_up(pp, S_BB)

#    if KH[key.X] \
#        and readyplayer.has_item() \
#        and S_BB:
#            minus_one(readyplayer)
#            item_clean_up(pp, S_BB)

    if KH[key.A] \
        and not item_movement(all_items, yammy):
            rotate_items_left(all_items)

    if KH[key.D] \
        and not item_movement(all_items, yammy):
            rotate_items_right(all_items)
#
#    if KH[key.S] \
#        and not item_movement(all_items, yammy):
#            mix_items(all_items)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, FRAME_SPEED)
    pyglet.app.run()
