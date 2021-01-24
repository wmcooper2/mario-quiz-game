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
    """Draw the problem."""
    player = u.player_in_front()
    if not u.movement(player):
#         problem.random_question()
        problem.box.draw()
        c.PROBLEM_BATCH.draw()

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
