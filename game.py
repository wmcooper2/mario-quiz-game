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

@GAME_WINDOW.event
def on_draw():
    """Draw the visual elements. Returns None."""
    #GAME_WINDOW.event's module doesnt import my constants, 
    #+ maybe thats why I need globals here?
#    global NEW_QUESTION

    GAME_WINDOW.clear()
    MAIN.draw()
    pp = PLAYERS[0]

    if pp.inventory:
        present_problem(pp, prob)
    update_scores()

def update(DT):
    """Game update loop. Returns None."""
    pp          = PLAYERS
    readyplayer = pp[0]

    #need to set effects as globals, maybe because of the game loop
#    global BOMBOMB_EFFECT, POW_BUTTON_EFFECT

    if BOMBOMB_EFFECT:      bombomb_effect()    #mix items on screen
    elif POW_BUTTON_EFFECT: pow_button_effect() #all players, minus point

    #update PLAYERS
    for player in pp:
        #location
        player.spot = PLAYER_SPOTS[pp.index(player)]
        player.update(DT)

        #scores
        score_points = SCORES[player.point_index].points
        score_object = SCORES[player.point_index]
        if player.points != score_points:
            score_object.update(score_object, player) 

    [player.float() for player in floaters]
    update_item_pos(all_items, DT)          #items.py
    yammy.update(DT)

    #fade yammy in and out
    if KH[key.F] \
        and not player_movement(pp) \
        and not yammy.trans:
#            yammy.trans = True              #set flag
            yammy.trans = not yammy.trans
#            yammy.toggle_transition()     #toggle flag


#DEBUG
    if KH[key.SPACE]:
        pprint(KH.keys())

    #player gets one item
    if KH[key._1] \
        and not any_movement(all_items, pp, yammy) \
        and not S_BB:
            NEW_QUESTION = True     #reset flag
            yi = all_items[0]       #yammy acts on first item
            yammy.wave_wand()       #wave magic wand
            yammy.take_item(yi)     #takes the item
            all_items.remove(yi)    #item taken from platform
            yi.spot_y = ITEM_DISAPPEAR_HEIGHT   #raise item
            yi.transitioning = True             #disappear item 
            all_items.append(new_item())        #new item to lineup
            yammy.victim = readyplayer
            #item given to player in yammy.update()

    if KH[key.LEFT] \
        and not player_movement(pp) \
        and not S_BB:
            rotate_players_left(pp)

    if KH[key.RIGHT] \
        and not player_movement(pp) \
        and not S_BB:
            rotate_players_right(pp)

    if KH[key.UP] \
        and not player_movement(pp) \
        and not S_BB:
            mix_players(pp)

    if KH[key.O] \
        and readyplayer.has_item() \
        and S_BB:
            plus_one(readyplayer)
            item_clean_up(pp, S_BB)

    if KH[key.X] \
        and readyplayer.has_item() \
        and S_BB:
            minus_one(readyplayer)
            item_clean_up(pp, S_BB)

    if KH[key.A] \
        and not item_movement(all_items, yammy):
            rotate_items_left(all_items)

    if KH[key.D] \
        and not item_movement(all_items, yammy):
            rotate_items_right(all_items)

    if KH[key.S] \
        and not item_movement(all_items, yammy):
            mix_items(all_items)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, FRAME_SPEED)
    pyglet.app.run()
