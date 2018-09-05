#!/usr/bin/env python3
"""Main file for the Mario quiz game."""
import pyglet
from pyglet import clock
from pyglet.window import key
import sys
sys.path.append("src/")
sys.path.append("gamedata/")
from pprint import pprint
pprint(sys.path)
# setup resources
pyglet.resource.path = ["./resources"] 
pyglet.resource.reindex()

import random
import players #not needed?
import playersetup
import playerscores
import problems
import items #must come after players
from itemsetup import new_item
import constants

#setup player containers
ALL_PLAYERS = []            #initial player order hard-coded below

# change this order to change the players on the screen
PLAYING_PLAYERS = []        #players added in randomize_players()

SCORE_DISPLAY = []          #score display sprites
WALKING_PLAYERS = []
FLOATING_PLAYERS = []

#background
BACKGROUND = players.Background(img=players.Background.background_img, batch=constants.MAIN_BATCH)
#background_img = pyglet.resource.image("quiz1.png")
#BACKGROUND = pyglet.sprite.Sprite(background_img, batch=constants.MAIN_BATCH)
#class Background(pyglet.sprite.Sprite):

#    background_img = pyglet.resource.image("quiz1.png")

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#player setup
YAMMY = playersetup.make_yammy()
FIRE_LIGHT = playersetup.make_firelight()
DRAGON = playersetup.make_dragon()
BIG_BOO = playersetup.make_big_boo()
GREEN_KOOPA = playersetup.make_green_koopa()
BIG_MOLE = playersetup.make_big_mole()
MARIO = playersetup.make_mario()
LUIGI = playersetup.make_luigi()

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

#this random player selection assumes that the players dont want to choose their characters.
def randomize_players():
    """Randomizes the starting order of the player line up. Returns None."""
    if constants.PLAYERS_RANDOMIZED is False:
        constants.PLAYERS_RANDOMIZED = True     #set flag
        random_players = []
        copy = ALL_PLAYERS[:]
        for x in range(constants.NUM_PLAYERS):
            player_choice = random.choice(copy)
            random_players.append(player_choice)
            copy.remove(player_choice)
        for player in random_players:
            PLAYING_PLAYERS.append(player)
        del random_players                      #clean up
        del copy                                #clean up
randomize_players()

#setup items
ALL_ITEMS = []                  #new items added with new_item() and the for-loop below it.
for item in range(constants.NUM_ITEMS):
    ALL_ITEMS.append(new_item())

#line setups
constants.player_line_up()                                      #player line up
constants.item_line_up(ALL_ITEMS)                               #item line up
constants.top_row_line_up()                                     #at top of screen

#score setup, relies on playerscores.py
for element in PLAYING_PLAYERS:
    score_x = constants.SCORE_SPOTS[PLAYING_PLAYERS.index(element)]
    score_sprite = playerscores.make_sprite(element, score_x)
    SCORE_DISPLAY.append(score_sprite)
    element.point_index = SCORE_DISPLAY.index(score_sprite)

# main problem instance
problem = problems.Problem()

@constants.GAME_WINDOW.event
def on_draw():
    """Draw MAIN_BATCH which is all the visual elements. Returns None."""
    constants.GAME_WINDOW.clear()
    constants.MAIN_BATCH.draw()
    player = PLAYING_PLAYERS[0]

    if player.has_item():
        # basic pattern:
            # draw the black box
            # change the guide
            # change the question in the problem
            # draw the guide
            # draw the question        
        players_item = player.inventory[0]
        problem.black_box.draw()
        constants.SHOW_BLACK_BOX = True                        #set flag

        if constants.NEW_QUESTION:
            constants.NEW_QUESTION = False                     #reset flag
            if isinstance(players_item, items.RedMushroom):    #simple vocab
                problem.random_english_word()
            if isinstance(players_item, items.GreenMushroom):  #verbs
                problem.random_present_verb()
            if isinstance(players_item, items.PirahnaPlant):   #J -> E translation
                problem.random_target_sentence()
            if isinstance(players_item, items.YoshiCoin):      #pronunciation
                problem.random_pronunciation()
            if isinstance(players_item, items.SpinyBeetle):    #answer the question
                problem.random_question()
        problem.guide.draw()
        problem.question.draw()

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
    #non-question effects go below this comment.
    if constants.BOMBOMB_EFFECT:                          #mix items
        mix_items()
        constants.BOMBOMB_EFFECT = False                  #reset flag
        item_clean_up()
    if constants.POW_BUTTON_EFFECT:                       #all, minus one point
        for player in PLAYING_PLAYERS:
            player.points -= 1
        constants.POW_BUTTON_EFFECT = False               #reset flag
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

    ready_player = PLAYING_PLAYERS[0]
    for player in PLAYING_PLAYERS:                              #update players
        player.spot = constants.PLAYER_SPOTS[PLAYING_PLAYERS.index(player)]
        player.update(DT)

        #update player scores
        score_points = SCORE_DISPLAY[player.point_index].points #the integer value
        score_object = SCORE_DISPLAY[player.point_index]        #the score object
        if player.points != score_points:
            score_object.update(score_object, player)           #player_score != player

    for player in FLOATING_PLAYERS:
        player.float()

    for item in ALL_ITEMS:                                      #update items
        item.spot_x = constants.ITEM_SPOTS[ALL_ITEMS.index(item)]
        item.update(DT)

    #item transfer is automatically controlled by Yammy
    YAMMY.update()
    if YAMMY.inventory:                                         #only if len() > 0
        YAMMY.inventory[0].update(DT)                           #update the item
        YAMMY.inventory[0].transition()                         #transition the item

    #fade YAMMY in and out
    if constants.KEY_HANDLER[key.F] and not player_movement() and not YAMMY.transitioning:
        YAMMY.transitioning = True                              #set flag
        YAMMY.toggle_transition_direction()                     #toggle flag

    #player gets one item
    if constants.KEY_HANDLER[key._1] and not any_movement() and not constants.SHOW_BLACK_BOX:
        constants.NEW_QUESTION = True                           #reset flag
        yammys_item = ALL_ITEMS[0]                              #YAMMY wants the first item
        YAMMY.wave_wand()                                       #wave magic wand
        YAMMY.take_item(yammys_item)                            #takes the item
        ALL_ITEMS.remove(yammys_item)                           #item taken from platform
        yammys_item.spot_y = constants.ITEM_DISAPPEAR_HEIGHT    #make the item rise
        yammys_item.transitioning = True                        #make item disappear
        ALL_ITEMS.append(new_item())                            #add new item to lineup
        YAMMY.victim = ready_player                             #PLAYING_PLAYERS[0]
                                                                #given in YAMMY.update()

    if constants.KEY_HANDLER[key.LEFT] and not player_movement() and not constants.SHOW_BLACK_BOX:
        rotate_players_left()

    if constants.KEY_HANDLER[key.RIGHT] and not player_movement() and not constants.SHOW_BLACK_BOX:
        rotate_players_right()

    if constants.KEY_HANDLER[key.UP] and not player_movement() and not constants.SHOW_BLACK_BOX:
        mix_players()

    if constants.KEY_HANDLER[key.O] and ready_player.has_item() and constants.SHOW_BLACK_BOX:
        right_answer()                                          #plus one point
        item_clean_up()

    if constants.KEY_HANDLER[key.X] and ready_player.has_item() and constants.SHOW_BLACK_BOX:
        wrong_answer()                                          #minus one point
        item_clean_up()

    if constants.KEY_HANDLER[key.A] and not item_movement():
        rotate_items_left()

    if constants.KEY_HANDLER[key.D] and not item_movement():
        rotate_items_right()

    if constants.KEY_HANDLER[key.S] and not item_movement():
        mix_items()

def item_clean_up():
    """Performs item clean up. Returns None."""
    player = PLAYING_PLAYERS[0]
    players_item = player.inventory[0]
    player.inventory.remove(players_item)           #remove the item from player's inventory
    players_item.delete()                           #item's instance is deleted
    player.item = False                             #reset flag
    constants.SHOW_BLACK_BOX = False                #reset flag

    #show points in terminal (move to the update/draw blocks)
    for player in PLAYING_PLAYERS:
        print(player.__class__, " has ", player.points, " points.")
        print("point_index = ", player.point_index)

def right_answer():
    """Gives a point to the player in the ready position. Returns None."""
    PLAYING_PLAYERS[0].points += 1

def wrong_answer():
    """Takes away a point from the player in the ready position. Returns None."""
    PLAYING_PLAYERS[0].points -= 1

def any_movement(): #dont change this, creates a weird bug if you do.
    """Checks if anything is moving. Returns Boolean."""
    movement = []
    for player in PLAYING_PLAYERS:
        movement.append(player.moving)
    for item in ALL_ITEMS:
        movement.append(item.moving)
    if YAMMY.inventory:
        movement.append(YAMMY.inventory[0].moving)
    return any(movement)

def player_movement():
    """Checks if any player is moving. Returns Boolean."""
    movement = []
    for player in PLAYING_PLAYERS:
        movement.append(player.moving)
    return any(movement)

def item_movement():
    """Checks if any item is moving. Return Boolean."""
    movement = []
    for item in ALL_ITEMS:
        movement.append(item.moving)
    if YAMMY.inventory:
        movement.append(YAMMY.inventory[0].moving)
    return any(movement)

def rotate_items_left():
    """Rotates contents of items list to the right by one. Returns None."""
    #reverse order from what appears on screen
    temp_item = ALL_ITEMS[-1]
    ALL_ITEMS.remove(temp_item)
    ALL_ITEMS.insert(0, temp_item)

def rotate_items_right():
    """Rotates contents of the items list to left the by one. Returns None."""
    #reverse order from what appears on screen
    temp_item = ALL_ITEMS[0]
    ALL_ITEMS.remove(temp_item)
    ALL_ITEMS.append(temp_item)

def mix_items():
    """Randomly mixes the items in the line. Returns None."""
    global ALL_ITEMS
    mixed_items = []
    copy = ALL_ITEMS[:]
    for x in ALL_ITEMS:
        item_choice = random.choice(copy)
        mixed_items.append(item_choice)
        copy.remove(item_choice)
    ALL_ITEMS = mixed_items[:]

def rotate_players_left():
    """Rotates contents of players list to the left by one. Returns None."""
    temp_player = PLAYING_PLAYERS[0]
    PLAYING_PLAYERS.remove(temp_player)
    PLAYING_PLAYERS.append(temp_player)

def rotate_players_right():
    """Rotates contents of players list to the right by one. Returns None."""
    temp_player = PLAYING_PLAYERS[-1]
    PLAYING_PLAYERS.remove(temp_player)
    PLAYING_PLAYERS.insert(0, temp_player)

def reverse_rotate_player_list():
    """Rotates contents of players list to the right by one. Returns None."""
    temp_player = PLAYING_PLAYERS[-1]
    PLAYING_PLAYERS.remove(temp_player)
    PLAYING_PLAYERS.insert(0, temp_player)

def mix_players():
    """Randomly mixes the players in the line. Returns None."""
    global PLAYING_PLAYERS
    mixed_players = []
    copy = PLAYING_PLAYERS[:]
    for x in PLAYING_PLAYERS:
        player_choice = random.choice(copy)
        mixed_players.append(player_choice)
        copy.remove(player_choice)
    PLAYING_PLAYERS = mixed_players[:]

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, constants.FRAME_SPEED)
    pyglet.app.run()
