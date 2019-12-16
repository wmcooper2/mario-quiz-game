
from constants import *

def update(DT):
    """Game update loop. Returns None."""
    pp          = PLAYERS
    readyplayer = pp[0]

    #need to set effects as globals, maybe because of the game loop
#    global BOMBOMB_EFFECT, POW_BUTTON_EFFECT
#
#    #mix items
#    if BOMBOMB_EFFECT:
#        mix_items()
#        BOMBOMB_EFFECT = False      #reset flag
#        item_clean_up()
#
#    #all players, minus one point
#    if POW_BUTTON_EFFECT:           
#        for player in readyplayer:
#            player.points -= 1
#        POW_BUTTON_EFFECT = False   #reset flag
#        item_clean_up()
#
    #update players
    for player in pp:
        #location
#        player.spot = PLAYER_SPOTS[pp.index(player)]
        player.update(DT)

        #scores
#        score_points = SCORE_DISPLAY[player.point_index].points
#        score_object = SCORE_DISPLAY[player.point_index]
#        if player.points != score_points:
#            score_object.update(score_object, player) 

    #player floating effect
#    for player in floaters:
#        player.float()

    #update items
#    for item in ALL_ITEMS:
#        item.spot_x = ITEM_SPOTS[ALL_ITEMS.index(item)]
#        item.update(DT)

    #item transfer controlled by Yammy object
#    YAMMY.update()
#    if YAMMY.inventory:                     #only if len() > 0
#        YAMMY.inventory[0].update(DT)       #update the item
#        YAMMY.inventory[0].transition()     #transition the item

    #fade YAMMY in and out
#    if KH[key.F] \
#        and not player_movement(pp) \
#        and not YAMMY.transitioning:
#            YAMMY.transitioning = True              #set flag
#            YAMMY.toggle_transition_direction()     #toggle flag
#
#    #player gets one item
#    if KH[key._1] \
#        and not any_movement(ALL_ITEMS, pp, YAMMY) \
#        and not S_BB:
#            NEW_QUESTION = True     #reset flag
#            yi= ALL_ITEMS[0]        #YAMMY acts on first item
#            YAMMY.wave_wand()       #wave magic wand
#            YAMMY.take_item(yi)     #takes the item
#            ALL_ITEMS.remove(yi)    #item taken from platform
#            yi.spot_y = ITEM_DISAPPEAR_HEIGHT   #raise item
#            yi.transitioning = True             #disappear item 
#            ALL_ITEMS.append(new_item())        #new item to lineup
#            YAMMY.victim = readyplayer
#            #item given to player in YAMMY.update()
#
#    if KH[key.LEFT] \
#        and not player_movement(pp) \
#        and not S_BB:
#            rotate_players_left(pp)
#
#    if KH[key.RIGHT] \
#        and not player_movement(pp) \
#        and not S_BB:
#            rotate_players_right(pp)
#
#    if KH[key.UP] \
#        and not player_movement(pp) \
#        and not S_BB:
#            mix_players(pp)
#
#    if KH[key.O] \
#        and readyplayer.has_item() \
#        and S_BB:
##            import pdb; pdb.set_trace()
#            right_answer(readyplayer)
#            item_clean_up(pp, S_BB)
#
#    if KH[key.X] \
#        and readyplayer.has_item() \
#        and S_BB:
#            wrong_answer(readyplayer)
#            item_clean_up(pp, S_BB)
#
#    if KH[key.A] \
#        and not item_movement(ALL_ITEMS, YAMMY):
#            rotate_items_left(ALL_ITEMS)
#
#    if KH[key.D] \
#        and not item_movement(ALL_ITEMS, YAMMY):
#            rotate_items_right(ALL_ITEMS)
#
#    if KH[key.S] \
#        and not item_movement(ALL_ITEMS, YAMMY):
#            mix_items(ALL_ITEMS)
