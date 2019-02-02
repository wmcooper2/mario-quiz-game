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
#setup resources path, don't move these two lines
pyglet.resource.path = ["./resources"] 
pyglet.resource.reindex()

#custom
from src.constants import *
from src.gameutil import *
from src.itemsetup import *
from src.players import *           #not needed?
from src.playersetup import *
from src.playerscores import *
from src.problems import *
from src.items import *             #must come after players 

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
randomize_players(PLAYERS_RANDOMIZED, characters, PLAYERS, NUM_PLAYERS)

#SETUP ITEMS
all_items = setup_items(NUM_ITEMS)

#POSITIONS ON SCREEN, gameutil.py
player_positions()
item_positions(all_items)
score_positions()

#SETUP SCORES, playerscores.py
setup_scores(PLAYERS, SCORE_SPOTS, SCORES)

#PROBLEM, problems.py
prob = Problem()

@GAME_WINDOW.event
def on_draw():
    """Draw the visual elements. Returns None."""
    global NEW_QUESTION

    GAME_WINDOW.clear()
    MAIN_BATCH.draw()
    pp = PLAYERS[0]

    if pp.has_item():
        # basic pattern:
            # draw the black box
            # change the guide
            # change the question in the problem
            # draw the guide
            # draw the question        
        players_item = pp.inventory[0]
        prob.box.draw()
        S_BB = True     #set flag

        if NEW_QUESTION:
            NEW_QUESTION = False    #reset flag
            #simple vocab
            if isinstance(players_item, RedMushroom):    
                prob.random_english_word()
            #verbs
            if isinstance(players_item, GreenMushroom):  
                prob.present_tense()
            #Japanese to English translation
            if isinstance(players_item, PirahnaPlant):   
                prob.target_sentence()
            #pronunciation
            if isinstance(players_item, YoshiCoin):      
                prob.pronunciation()
            #answer the question
            if isinstance(players_item, SpinyBeetle):    
                prob.question()
        prob.guide.draw()
        prob.question.draw()

    #top row scores
    for score in SCORES:
        if score.points is 0: score.zero.draw()
        elif abs(score.points) > 0 and abs(score.points) <= 5:
            for element in score.small_score: element.draw()
        elif abs(score.points) > 5:
            for element in score.big_score: element.draw()

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
