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
    #okay
#     if u.player_has_item(c.P1):
    if u.player_has_item(c.P1) and not u.movement(c.P1):
#     if u.player_has_item(c.P1) and not u.movement(c.P1) and c.P1.last_question_answered_correctly:
    #and item has not yet been earned by answering a question correctly

    #and item is on the player
        #QUESTION
        problem.box.draw()
        problem.question.draw()

    

def draw_sprites() -> None:
    """Draw all the visual elements."""
    #update these vars each time through the loop
    c.GAME_WINDOW.clear()
    c.BACKGROUND_BATCH.draw()
    c.YAMMY_BATCH.draw()
    c.PLAYER_BATCH.draw()
    c.SCORE_BATCH.draw()
    c.ITEM_BATCH.draw()
    c.ANIMATION_BATCH.draw()
