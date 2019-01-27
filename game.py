#!/usr/bin/env python3
"""Main file for the Mario quiz game."""

#stand lib
import random
import sys

#3rd party
import pyglet
from pyglet import clock
from pyglet.window import key
#setup resources path, don't move these two lines
pyglet.resource.path = ["./resources", "./src"] 
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

#background
BACKGROUND = Background(img=Background.background_img, batch=MAIN_BATCH)

#PLAYER SETUP
CHARACTERS = []
# the order of elements with pp determines the order
#+ of the players on the screen.
PLAYERS = []
SCORE_DISPLAY = []
WALKING_PLAYERS = []
FLOATING_PLAYERS = []

YAMMY = make_yammy()
FIRE_LIGHT = make_firelight()
DRAGON = make_dragon()
BIG_BOO = make_big_boo()
GREEN_KOOPA = make_green_koopa()
BIG_MOLE = make_big_mole()
MARIO = make_mario()
LUIGI = make_luigi()

CHARACTERS.append(FIRE_LIGHT)
CHARACTERS.append(DRAGON)
CHARACTERS.append(BIG_BOO)
CHARACTERS.append(GREEN_KOOPA)
CHARACTERS.append(BIG_MOLE)
CHARACTERS.append(MARIO)
CHARACTERS.append(LUIGI)

FLOATING_PLAYERS.append(FIRE_LIGHT)
FLOATING_PLAYERS.append(BIG_BOO)

WALKING_PLAYERS.append(DRAGON)
WALKING_PLAYERS.append(GREEN_KOOPA)
WALKING_PLAYERS.append(BIG_MOLE)
WALKING_PLAYERS.append(MARIO)
WALKING_PLAYERS.append(LUIGI)

randomize_players(PLAYERS_RANDOMIZED, CHARACTERS, PLAYERS, NUM_PLAYERS)

#SETUP ITEMS
ALL_ITEMS = []                  
setup_items(NUM_ITEMS, ALL_ITEMS)

#line setups
player_line_up()
item_line_up(ALL_ITEMS)
top_row_line_up()

#SETUP SCORES
score_setup(PLAYERS, SCORE_SPOTS, SCORE_DISPLAY)

#MAIN PROBLEM INSTANCE
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
        prob.black_box.draw()
        S_BB = True     #set flag

        if NEW_QUESTION:
            NEW_QUESTION = False    #reset flag
            #simple vocab
            if isinstance(players_item, RedMushroom):    
                prob.random_english_word()
            #verbs
            if isinstance(players_item, GreenMushroom):  
                prob.random_present_verb()
            #Japanese to English translation
            if isinstance(players_item, PirahnaPlant):   
                prob.random_target_sentence()
            #pronunciation
            if isinstance(players_item, YoshiCoin):      
                prob.random_pronunciation()
            #answer the question
            if isinstance(players_item, SpinyBeetle):    
                prob.random_question()
        prob.guide.draw()
        prob.question.draw()

    #top row scores
    for score in SCORE_DISPLAY:
        if score.points is 0:
            score.zero.draw()
        elif abs(score.points) > 0 and abs(score.points) <= 5:
            for element in score.small_score:
                element.draw()
        elif abs(score.points) > 5:
            for element in score.big_score:
                element.draw()

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

    #all players, minus one point
    if POW_BUTTON_EFFECT:           
        for player in readyplayer:
            player.points -= 1
        POW_BUTTON_EFFECT = False   #reset flag
        item_clean_up()

    #update players
    for player in pp:
        #location
        player.spot = PLAYER_SPOTS[pp.index(player)]
        player.update(DT)

        #scores
        score_points = SCORE_DISPLAY[player.point_index].points
        score_object = SCORE_DISPLAY[player.point_index]
        if player.points != score_points:
            score_object.update(score_object, player) 

    #player floating effect
    for player in FLOATING_PLAYERS:
        player.float()

    #update items
    for item in ALL_ITEMS:
        item.spot_x = ITEM_SPOTS[ALL_ITEMS.index(item)]
        item.update(DT)

    #item transfer controlled by Yammy object
    YAMMY.update()
    if YAMMY.inventory:                     #only if len() > 0
        YAMMY.inventory[0].update(DT)       #update the item
        YAMMY.inventory[0].transition()     #transition the item

    #fade YAMMY in and out
    if KH[key.F] \
        and not player_movement(pp) \
        and not YAMMY.transitioning:
            YAMMY.transitioning = True              #set flag
            YAMMY.toggle_transition_direction()     #toggle flag

    #player gets one item
    if KH[key._1] \
        and not any_movement(ALL_ITEMS, pp, YAMMY) \
        and not S_BB:
            NEW_QUESTION = True     #reset flag
            yi= ALL_ITEMS[0]        #YAMMY acts on first item
            YAMMY.wave_wand()       #wave magic wand
            YAMMY.take_item(yi)     #takes the item
            ALL_ITEMS.remove(yi)    #item taken from platform
            yi.spot_y = ITEM_DISAPPEAR_HEIGHT   #raise item
            yi.transitioning = True             #disappear item 
            ALL_ITEMS.append(new_item())        #new item to lineup
            YAMMY.victim = readyplayer
            #item given to player in YAMMY.update()

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
#            import pdb; pdb.set_trace()
            right_answer(readyplayer)
            item_clean_up(pp, S_BB)

    if KH[key.X] \
        and readyplayer.has_item() \
        and S_BB:
            wrong_answer(readyplayer)
            item_clean_up(pp, S_BB)

    if KH[key.A] \
        and not item_movement(ALL_ITEMS, YAMMY):
            rotate_items_left(ALL_ITEMS)

    if KH[key.D] \
        and not item_movement(ALL_ITEMS, YAMMY):
            rotate_items_right(ALL_ITEMS)

    if KH[key.S] \
        and not item_movement(ALL_ITEMS, YAMMY):
            mix_items(ALL_ITEMS)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, FRAME_SPEED)
    pyglet.app.run()
