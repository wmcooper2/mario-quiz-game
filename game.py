#!/usr/bin/env python3
"""Main file for the Mario quiz game."""
#        import pdb; pdb.set_trace()

#stand lib
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

BACKGROUND = Background(img=Background.background_img, batch=MAIN_BATCH)

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
    MAIN_BATCH.draw()
    pp = PLAYERS[0]

    if pp.has_item():
        present_problem(pp, prob)
#    update_scores()

def update(DT):
    """Game update loop. Returns None."""
    pp          = PLAYERS
    readyplayer = pp[0]

    #need to set effects as globals, maybe because of the game loop
    global BOMBOMB_EFFECT, POW_BUTTON_EFFECT

    #mix items
    if BOMBOMB_EFFECT:
        mix_items()
        BOMBOMB_EFFECT = False      #reset flag
        item_clean_up()

    #all PLAYERS, minus one point
    if POW_BUTTON_EFFECT:           
        for player in readyplayer:
            player.points -= 1
        POW_BUTTON_EFFECT = False   #reset flag
        item_clean_up()

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

    #player floating effect
    for player in floaters:
        player.float()

    #update items
    for item in all_items:
        item.spot_x = ITEM_SPOTS[all_items.index(item)]
        item.update(DT)

    #item transfer controlled by Yammy object
    yammy.update()
    if yammy.inventory:                     #only if len() > 0
        yammy.inventory[0].update(DT)       #update the item
        yammy.inventory[0].transition()     #transition the item

    #fade yammy in and out
    if KH[key.F] \
        and not player_movement(pp) \
        and not yammy.transitioning:
            yammy.transitioning = True              #set flag
            yammy.toggle_transition_direction()     #toggle flag

    #player gets one item
    if KH[key._1] \
        and not any_movement(all_items, pp, yammy) \
        and not S_BB:
            NEW_QUESTION = True     #reset flag
            yi= all_items[0]        #yammy acts on first item
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
            right_answer(readyplayer)
            item_clean_up(pp, S_BB)

    if KH[key.X] \
        and readyplayer.has_item() \
        and S_BB:
            wrong_answer(readyplayer)
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
