#std lib
import asyncio
from typing import Any

#3rd party
from pyglet import window
from pyglet.window import key

#custom
from constants import Constants as c
from constants import Screens
import items as i
import util as u



def title_loop_keys(title: Any) -> None:
    """"""
    if u.key_up():
        title.selector_up()
    elif u.key_down():
        title.selector_down()
    elif u.key_enter():
        if title.is_game_selected():
            c.SCREEN = Screens.GAME
        elif title.is_options_selected():
            c.SCREEN = Screens.OPTIONS

# @window.event
# def on_key_release(symbol, modifiers):
#     if symbol in pressed_keys:
#         pressed_keys.remove(symbol)
def options_loop_keys(options: Any) -> None:
    """"""
    if u.key_b():
        c.SCREEN = Screens.TITLE
    elif u.key_up():
        options.selector_up()
    elif u.key_down():
        options.selector_down()


def options_loop_keys2(options: Any) -> None:
    """"""

#     def on_key_release(key: Any, func: Any):
#         func()
    if u.key_b():
        c.SCREEN = Screens.TITLE
    elif u.key_up():
        window.on_key_release(key.UP)
#         options.selector_up()
    elif u.key_down():
#         options.selector_down()
        on_key_release(key.DOWN, options.selector_down)

def game_loop_keys(yammy: Any, problem: Any) -> None:
    """
        Digits:     1
        Letters:    ADFOSUX
        Arrows:     Left Right Up
    """
    player = u.player_in_front()
    if not u.any_movement():
        if u.key_1():
            if not problem.showing:
#                 problem.new_question()
                problem.question.draw()
                problem.toggle()
            player.use_item()
            yammy.wave_wand()
            c.TRANSFER_ITEM = u.remove_item_from_platform()
            i.add_item()

        elif u.key_left():
            u.rotate_players_left()

        elif u.key_right():
            u.rotate_players_right()

        elif u.key_up():
            c.PLAYERS = u.mix(c.PLAYERS)

        #plus one point
        elif u.key_o():
            u.right_answer(player)
            u.rotate_players_left()

            if problem.showing:
                problem.toggle()

            #delete prior problem letter sprites

        #minus one point
        elif u.key_x():
            u.wrong_answer(player)
            if player.item:
                player.item.poof()
                player.item = None
            u.rotate_players_left()

            if problem.showing:
                problem.toggle()

            #delete prior problem letter sprites

        elif u.key_a():
            u.rotate_items_left()

        elif u.key_d():
            u.rotate_items_right()

        elif u.key_s():
            c.ALL_ITEMS = u.mix(c.ALL_ITEMS)

        elif u.key_u():
            player.use_item()
