#std lib
import random

#3rd party
import pyglet
# from pyglet import clock
from pyglet.window import key

#custom
from constants import constants as c
from util import (
    add_items,
    mix_items,
    mix_players,
    player_movement,
    randomize_players,
    reverse_rotate_player_list,
    right_answer,
    rotate_items_left,
    rotate_items_right,
    rotate_players_left,
    rotate_players_right,
    Line)
import players as sprites
import problems
import items #must come after sprites (resource mod is defined in sprites... move to main?) #not needed?
import playerscores
from itemsetup import new_item # must stay here... strange error

#SPRITES
background = sprites.Background(img=sprites.Background.background_img, batch=c.MAIN_BATCH)
yammy = sprites.make_yammy()
mario = sprites.make_mario()
luigi = sprites.make_luigi()
fire_light = sprites.make_firelight()
dragon = sprites.make_dragon()
big_boo = sprites.make_big_boo()
green_koopa = sprites.make_green_koopa()
big_mole = sprites.make_big_mole()

c.ALL_PLAYERS = [
    mario,
    luigi,
    fire_light,
    dragon,
    big_boo,
    green_koopa,
    big_mole]

#TODO, make a way to check if player is walking type so that I don't have to waste memory or complicate things by adding another list here for walking vs floating players.
c.WALKING_PLAYERS = [
    dragon,
    green_koopa,
    big_mole,
    mario,
    luigi]

c.FLOATING_PLAYERS = [
    fire_light,
    big_boo]

#local constants
PLAYER_SPOTS = Line.player_spots
ITEM_SPOTS = Line.item_spots
PROB = problems.Problem
VBB = PROB.BLACK_BOX


#TODO, refactor the arg out
add_items(new_item)
randomize_players()



#TODO, there are 2 update functions???
def update_(DT):
    c.GAME_WINDOW.clear()
    c.MAIN_BATCH.draw()
    p1 = c.PLAYERS[0]
    
    #show the problem
    if c.SHOWING_BLACK_BOX: 
        VBB.draw()#mixing the different ways methods from different classes are called... 
        p1.inventory[0].problem.question.draw() #change so that it doesnt go through the item instance, but goes directly to the class attribute

        #question guides
        if p1.has_item() and c.SHOWING_BLACK_BOX: 
            players_item = p1.inventory[0]
            if isinstance(players_item, items.RedMushroom):    #simple vocab
                PROB.english_vocab_guide.draw()
            elif isinstance(players_item, items.GreenMushroom):  #verbs
                PROB.present_verb_guide.draw()
            elif isinstance(players_item, items.PirahnaPlant):   #J -> E translation
                PROB.english_sentence_guide.draw() 
            elif isinstance(players_item, items.YoshiCoin):      #pronunciation
                PROB.pronunciation_guide.draw()
            elif isinstance(players_item, items.SpinyBeetle):    #answer the question
                PROB.answer_my_question_guide.draw()

    #I dont know what this block does
#    for score in c.SCORE_DISPLAY:
#        if len(score.big_score) > 0:
#            for thing in score.big_score:
#                thing.draw()
#        elif score.points == 0:
#            score.zero.draw()

def update(dt):
    """Game update loop. Returns None."""
    #non-question effects go below this comment.
    if c.BOMBOMB_EFFECT:                                        #mix items
        mix_items()
        c.BOMBOMB_EFFECT = False                            #reset flag
        item_clean_up()
    if c.POW_BUTTON_EFFECT:                                 #all, minus one point
        for player in c.PLAYERS:
            player.points -= 1
        c.POW_BUTTON_EFFECT = False                         #reset flag
        item_clean_up()

#    if constants.FEATHER_EFFECT:
#        print("change feather effect to something more interesting.")
#        rotate_players_left()
#        FEATHER_EFFECT = False                                 #reset flag
#        item_clean_up()
#    if constants.STAR_EFFECT:
#        print("change star effect to something more interesting.")
#        STAR_EFFECT = False                                    #reset flag
#        item_clean_up()
#    if constants.QUESTION_BLOCK_EFFECT:
#        print("change star effect to something more interesting.")
#        QUESTION_BLOCK_EFFECT = False                          #reset flag
#        item_clean_up()

#     print(c.PLAYERS)
    p1 = c.PLAYERS[0]

    for player in c.PLAYERS:                              #update players 
        player.spot = PLAYER_SPOTS[c.PLAYERS.index(player)]
        player.update(dt)

        #player automatically uses item
        if player.has_item() and c.SHOWING_BLACK_BOX == False: 
#             breakpoint()
            print("INVENTORY:", p1.inventory)
            players_item = p1.inventory[0]
            player.use_item() 
   
        #update player scores 
        score_points = c.SCORE_DISPLAY[player.point_index].points #the integer value
        score_object = c.SCORE_DISPLAY[player.point_index]        #the score object
        if player.points != score_points: 
            score_object.update(score_object, player)           #player_score is in a different instance than player

    for player in c.FLOATING_PLAYERS:
        player.float()

    for item in c.ALL_ITEMS:                                      #update items 
        item.spot_x = ITEM_SPOTS[c.ALL_ITEMS.index(item)]
        item.update(dt)

    #item transfer is automatically controlled by Yammy
    #TODO, pass player and item to yammy to do the transfer
    yammy.update()

    #disappear Yammy
    if c.KH[key.F]:
        yammy.toggle_disappear()

#     #player gets one item
#     elif c.KH[key._1] and not any_movement() and not c.SHOWING_BLACK_BOX: 
#         yammys_item = c.ALL_ITEMS[0]
#         yammy.wave_wand()
#         yammy.take_item(yammys_item)
#         c.ALL_ITEMS.remove(yammys_item)
#         yammys_item.spot_y = c.ITEM_DISAPPEAR_H                   #make the item rise
#         yammys_item.disappear = True                        #make item disappear
#         c.ALL_ITEMS.append(new_item())                            #add new item to lineup
#         yammy.victim = p1                             #victim player in ready position
    #player gets one item
    elif c.KH[key._1] and not any_movement() and not c.SHOWING_BLACK_BOX: 
        c.QUESTION_ITEM = c.ALL_ITEMS.pop(0)    #take item from list
        yammy.wave_wand()                       #visual action
#         item.disappear()                      #change item's attributes
        item.spot_y = c.ITEM_DISAPPEAR_H            #make the item rise, make method of item
        item.disappear = True                       #make item disappear, make method of item
        c.ALL_ITEMS.append(new_item())          #add new item to list


    elif c.KH[key.LEFT] and not player_movement() and not c.SHOWING_BLACK_BOX:
        rotate_players_left()

    elif c.KH[key.RIGHT] and not player_movement() and not c.SHOWING_BLACK_BOX:
        rotate_players_right()

    elif c.KH[key.UP] and not player_movement() and not c.SHOWING_BLACK_BOX:
        mix_players()

    elif c.KH[key.O] and p1.item and c.SHOWING_BLACK_BOX:
        right_answer(c.PLAYERS[0])                        #plus one point
        item_clean_up()

    elif c.KH[key.X] and p1.item and c.SHOWING_BLACK_BOX:
        wrong_answer(c.PLAYERS[0])                        #minus one point
        item_clean_up()

    elif c.KH[key.A] and not item_movement():
        rotate_items_left()

    elif c.KH[key.D] and not item_movement():
        rotate_items_right()

    elif c.KH[key.S] and not item_movement():
        mix_items()

def item_clean_up():
    """Performs item clean up. Returns None."""
    player = c.PLAYERS[0]
    players_item = player.inventory[0]
    c.SHOWING_BLACK_BOX = False                                 #reset flag, stop showing box
    player.item = False                                         #reset flag
    player.inventory.remove(players_item)                       #remove the item from player's inventory
    players_item.delete()                                       #item's instance is deleted

    #show points in terminal (move to the update/draw blocks)
#     for player in c.PLAYERS:
#         print(player.__class__, " has ", player.points, " points.")
#         print("point_index = ", player.point_index)

def any_movement() -> bool:
    """Checks if anything is moving."""
    #dont change this, creates a weird bug if you do.
    movement = []
    for player in c.PLAYERS: 
        movement.append(player.moving)
    for item in c.ALL_ITEMS: 
        movement.append(item.moving)
    if yammy.inventory:
        movement.append(yammy.inventory[0].moving)
    return any(movement)

def item_movement():
    """Checks if any item is moving. Return Boolean."""
    movement = []
    for item in c.ALL_ITEMS: 
        movement.append(item.moving)
    if yammy.inventory:
        movement.append(yammy.inventory[0].moving)
    return any(movement)

#line setups
lines = Line(screen_w=c.SCREEN_W, num_players=c.NUM_PLAYERS, num_items=c.NUM_ITEMS)
lines.line_up()                                             #player line up
lines.item_line_up(c.ALL_ITEMS)                               #item line up
lines.top_row_line_up()                                     #for scores and item at top of game_window
player_spots = lines.player_spots                           #at players platform
item_spots = lines.item_spots                               #at item platform
score_spots = lines.score_spots                             #at top of game_window
inventory_spot = lines.inventory_spot                       #at top center of game_window

#score setup, relies on playerscores.py
for player in c.PLAYERS:
    score_x = score_spots[c.PLAYERS.index(player)]
    score_sprite = playerscores.make_sprite(player, score_x)
    c.SCORE_DISPLAY.append(score_sprite) 
    player.point_index = c.SCORE_DISPLAY.index(score_sprite) 



@c.GAME_WINDOW.event
def on_draw():
    """Draw the visual elements. Returns None."""
    c.GAME_WINDOW.clear()
    c.MAIN_BATCH.draw()
    main_player = c.PLAYERS[0]

    if main_player.has_item():
        # basic pattern:
            # draw the black box
            # change the guide
            # change the question in the problem
            # draw the guide
            # draw the question        
        players_item = main_player.inventory[0]
        VBB.draw()
        S_BB = True     #set flag

        if c.NEW_QUESTION:
            c.NEW_QUESTION = False    #reset flag
            #simple vocab
            if isinstance(players_item, RedMushroom):    
                PROB.random_english_word()
            #verbs
            elif isinstance(players_item, GreenMushroom):  
                PROB.random_present_verb()
            #Japanese to English translation
            elif isinstance(players_item, PirahnaPlant):   
                PROB.random_target_sentence()
            #pronunciation
            elif isinstance(players_item, YoshiCoin):      
                PROB.random_pronunciation()
            #answer the question
            elif isinstance(players_item, SpinyBeetle):    
                PROB.random_question()
#         PROB.guide.draw()
#         PROB.question.draw()

    #top row scores
    for score in c.SCORE_DISPLAY:
        if score.points == 0:
            score.zero.draw()
        elif abs(score.points) > 0 and abs(score.points) <= 5:
            for element in score.small_score:
                element.draw()
        elif abs(score.points) > 5:
            for element in score.big_score:
                element.draw()


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, c.FRAME_SPEED)
    pyglet.app.run()
