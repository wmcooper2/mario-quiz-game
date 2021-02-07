#std lib
from typing import Any

#3rd party
import pyglet

#custom
from constants import Constants as c
import util as u
import sprites as s

# label = pyglet.text.Label('Hello, world',
#     font_name='Times New Roman',
#     font_size=36,
#     x=100,
#     y=100,
#     color=(255, 0, 0, 255),
#     batch=c.TITLE_BATCH)

# title = s.Title()
# subtitle = s.SubTitle()
# title_background = s.TitleBackground()
# title_ground = s.TitleGround()
# options_button = s.OptionsBtn()
# game_button = s.GameBtn()
 
def draw_menu() -> None:
    print("menu")

def draw_title() -> None:
    """Draw the title screen."""
    c.TITLE_BACKGROUND_BATCH.draw()
    c.GROUND_BATCH.draw()
    c.TITLE_BATCH.draw()

def draw_problem(problem: Any) -> None:
    """Draw the problem."""
    player = u.player_in_front()
    if not u.movement(player):
        problem.box.draw()
        c.PROBLEM_BATCH.draw()

def draw_sprites() -> None:
    """Draw all the visual elements.
        These are drawn each time through the main game loop.
    """
    c.GAME_WINDOW.clear()
    c.BACKGROUND_BATCH.draw()
    c.YAMMY_BATCH.draw()
    c.PLAYER_BATCH.draw()
    if c.SCORES:
        c.SCORE_BATCH.draw()
    c.ITEM_BATCH.draw()
    c.ANIMATION_BATCH.draw()
