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
    if u.player_has_item(c.P1) and not u.movement(c.P1):
    #TODO, make the user decide to use the item or throw it away before they get the question to earn a new item.

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
