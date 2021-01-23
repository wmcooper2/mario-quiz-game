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
    player = u.player_in_front()
#     c.SHOWING_BLACK_BOX = True
#     if not player.item and not u.movement(player):
    if not u.movement(player):
#         problem.random_question()
    #TODO, question box flashes when a player is rotated out...
        # call custom draw method on problem
        problem.box.draw()
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
    c.ANIMATION_BATCH.draw()
