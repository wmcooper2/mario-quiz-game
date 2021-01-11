#std lib

#3rd party
import pyglet

#custom
from constants import Constants as c
import util as u

def handle_item_effects() -> None:
    #TODO, finish this
    pass
    if c.BOMBOMB_EFFECT:                                        #mix items
        u.mix(c.ALL_ITEMS)
        c.BOMBOMB_EFFECT = False                            #reset flag
    if c.POW_BUTTON_EFFECT:                                 #all, minus one point
        for player in c.PLAYERS:
            player.points -= 1
        c.POW_BUTTON_EFFECT = False                         #reset flag
    if c.FEATHER_EFFECT:
#         print("change feather effect to something more interesting.")
        u.rotate_players_left()
        FEATHER_EFFECT = False                                 #reset flag
    if c.STAR_EFFECT:
#         print("change star effect to something more interesting.")
        STAR_EFFECT = False                                    #reset flag
    if c.QUESTION_BLOCK_EFFECT:
#         print("change star effect to something more interesting.")
        QUESTION_BLOCK_EFFECT = False                          #reset flag

