#std lib
from typing import Any

#3rd party
import pyglet

#custom
from constants import Constants as c
import util as u


def draw_menu() -> None:
    print("menu")

def draw_problem(problem: Any) -> None:
    """
        basic pattern:
            draw the black box
            change the guide
            change the question in the problem
            draw the guide
            draw the question        
    """
    pass
    #okay
#     if u.player_has_item(c.P1):
    #TODO, make these functions in util
#     if u.player_stopped_moving(c.P1) and u.player_in_first_spot(c.P1):

    #no good
#     if u.player_has_item(c.P1) and u.is_transfer_item_on_player(c.P1):

    #and item is on the player
        #QUESTION
#         problem.box.draw()
#         problem.question.draw()

    

def draw_sprites() -> None:
    """Draw all the visual elements."""
    #update these vars each time through the loop
    c.GAME_WINDOW.clear()
    c.BACKGROUND_BATCH.draw()
    c.YAMMY_BATCH.draw()
    c.PLAYER_BATCH.draw()
    c.SCORE_BATCH.draw()
    c.ITEM_BATCH.draw()
