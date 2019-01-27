#!/usr/bin/env python3
"""Main file for the Mario quiz game."""

#stand lib
import random
import sys

#3rd party
import pyglet
from pyglet import clock
from pyglet.window import key

# setup resources
pyglet.resource.path = ["./resources", "./src"] 
pyglet.resource.reindex()

#custom
from src.constants import *
from src.gameutil import *
from src.itemsetup import new_item
from src.players import *           #not needed?
from src.playersetup import *
from src.playerscores import *
from src.problems import *
from src.items import *             #must come after players 

#setup player containers
ALL_PLAYERS = []            #initial player order hard-coded below

# change this order to change the players on the screen
PLAYING_PLAYERS = []        #players added in randomize_players()

SCORE_DISPLAY = []          #score display sprites
WALKING_PLAYERS = []
FLOATING_PLAYERS = []

#background
BACKGROUND = Background(img=Background.background_img, batch=MAIN_BATCH)

#player setup
YAMMY = make_yammy()
FIRE_LIGHT = make_firelight()
DRAGON = make_dragon()
BIG_BOO = make_big_boo()
GREEN_KOOPA = make_green_koopa()
BIG_MOLE = make_big_mole()
MARIO = make_mario()
LUIGI = make_luigi()

ALL_PLAYERS.append(FIRE_LIGHT)
ALL_PLAYERS.append(DRAGON)
ALL_PLAYERS.append(BIG_BOO)
ALL_PLAYERS.append(GREEN_KOOPA)
ALL_PLAYERS.append(BIG_MOLE)
ALL_PLAYERS.append(MARIO)
ALL_PLAYERS.append(LUIGI)

FLOATING_PLAYERS.append(FIRE_LIGHT)
FLOATING_PLAYERS.append(BIG_BOO)

WALKING_PLAYERS.append(DRAGON)
WALKING_PLAYERS.append(GREEN_KOOPA)
WALKING_PLAYERS.append(BIG_MOLE)
WALKING_PLAYERS.append(MARIO)
WALKING_PLAYERS.append(LUIGI)

randomize_players(PLAYERS_RANDOMIZED, ALL_PLAYERS, PLAYING_PLAYERS, NUM_PLAYERS)

#SETUP ITEMS
ALL_ITEMS = []                  
#new items added with new_item() and the for-loop below it.
for item in range(NUM_ITEMS):
    ALL_ITEMS.append(new_item())

#line setups
player_line_up()
item_line_up(ALL_ITEMS)
top_row_line_up()

#score setup, relies on playerscores.py
for element in PLAYING_PLAYERS:
    score_x = SCORE_SPOTS[PLAYING_PLAYERS.index(element)]
    score_sprite = make_sprite(element, score_x)
    SCORE_DISPLAY.append(score_sprite)
    element.point_index = SCORE_DISPLAY.index(score_sprite)

# main problem instance
prob = Problem()

@GAME_WINDOW.event
def on_draw():
    """Draw the visual elements. Returns None."""
    GAME_WINDOW.clear()
    MAIN_BATCH.draw()
    player = PLAYING_PLAYERS[0]

    if player.has_item():
        # basic pattern:
            # draw the black box
            # change the guide
            # change the question in the problem
            # draw the guide
            # draw the question        
        players_item = player.inventory[0]
        prob.black_box.draw()
        S_BB = True     #set flag

        if NEW_QUESTION:
            NEW_QUESTION = False    #reset flag
            #simple vocab
            if isinstance(players_item, items.RedMushroom):    
                prob.random_english_word()
            #verbs
            if isinstance(players_item, items.GreenMushroom):  
                prob.random_present_verb()
            #Japanese to English translation
            if isinstance(players_item, items.PirahnaPlant):   
                prob.random_target_sentence()
            #pronunciation
            if isinstance(players_item, items.YoshiCoin):      
                prob.random_pronunciation()
            #answer the question
            if isinstance(players_item, items.SpinyBeetle):    
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
    #need to set effects as globals, maybe because of the game loop
    global BOMBOMB_EFFECT, POW_BUTTON_EFFECT

    #mix items
    if BOMBOMB_EFFECT:
        mix_items()
        BOMBOMB_EFFECT = False      #reset flag
        item_clean_up()

    #all players, minus one point
    if POW_BUTTON_EFFECT:           
        for player in PLAYING_PLAYERS:
            player.points -= 1
        POW_BUTTON_EFFECT = False   #reset flag
        item_clean_up()

#    if FEATHER_EFFECT:
#        print("change feather effect to something more interesting.")
#        rotate_players_left()
#        FEATHER_EFFECT = False                                 #reset flag
#        item_clean_up()
#    if STAR_EFFECT:
#        print("change star effect to something more interesting.")
#        STAR_EFFECT = False                                    #reset flag
#        item_clean_up()
#    if QUESTION_BLOCK_EFFECT:
#        print("change star effect to something more interesting.")
#        QUESTION_BLOCK_EFFECT = False                          #reset flag
#        item_clean_up()

    #update players
    rp = PLAYING_PLAYERS[0]
    for player in PLAYING_PLAYERS:
        #location
        player.spot = PLAYER_SPOTS[PLAYING_PLAYERS.index(player)]
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
    if KH[key.F] and not player_movement() \
                          and not YAMMY.transitioning:
        YAMMY.transitioning = True              #set flag
        YAMMY.toggle_transition_direction()     #toggle flag

    #player gets one item
    if KH[key._1] and not any_movement() and not S_BB:
        NEW_QUESTION = True     #reset flag
        #yammy's item = yi
        yi= ALL_ITEMS[0]        #YAMMY wants the first item
        YAMMY.wave_wand()       #wave magic wand
        YAMMY.take_item(yi)     #takes the item
        ALL_ITEMS.remove(yi)    #item taken from platform
        yi.spot_y = ITEM_DISAPPEAR_HEIGHT   #make the item rise
        yi.transitioning = True             #make item disappear
        ALL_ITEMS.append(new_item())        #add new item to lineup
        YAMMY.victim = rp                   #PLAYING_PLAYERS[0]
        #item given to player in YAMMY.update()

    if KH[key.LEFT] and not player_movement() and not S_BB:
        rotate_players_left()

    if KH[key.RIGHT] and not player_movement() and not S_BB:
        rotate_players_right()

    if KH[key.UP] and not player_movement() and not S_BB:
        mix_players()

    if KH[key.O] and rp.has_item() and S_BB:
        right_answer()
        item_clean_up()

    if KH[key.X] and rp.has_item() and S_BB:
        wrong_answer()
        item_clean_up()

    if KH[key.A] and not item_movement():
        rotate_items_left()

    if KH[key.D] and not item_movement():
        rotate_items_right()

    if KH[key.S] and not item_movement():
        mix_items()

def item_clean_up():
    """Performs item clean up. Returns None."""
    player = PLAYING_PLAYERS[0]
    players_item = player.inventory[0]
    player.inventory.remove(players_item)   #remove inventory
    players_item.delete()
    player.item = False     #reset flag
    S_BB = False            #reset flag

    #show points in terminal 
    if DEBUG:
        for p in PLAYING_PLAYERS:
            print(p.__class__, " has ", p.points, " points.")
            print("point_index = ", p.point_index)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, FRAME_SPEED)
    pyglet.app.run()
