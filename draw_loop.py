#std lib
from typing import Any

#3rd party
import pyglet

#custom
from constants import Constants as c


def draw_menu() -> None:
    print("menu")

def draw_problem(problem: Any) -> None:
    if c.P1.item:
        #QUESTION
        # basic pattern:
            # draw the black box
            # change the guide
            # change the question in the problem
            # draw the guide
            # draw the question        
        problem.box.draw()

    

def draw_sprites() -> None:
    """Draw all the visual elements."""
    #update these vars each time through the loop
    c.GAME_WINDOW.clear()
    c.BACKGROUND_BATCH.draw()
    c.YAMMY_BATCH.draw()
    c.PLAYER_BATCH.draw()
    c.SCORE_BATCH.draw()
    c.ITEM_BATCH.draw()
