#std lib
import asyncio
from typing import Any

#3rd party

#custom
from constants import Constants as c
import items as i
import util as u


#TODO, give player option to use item

#NOTE
"""
keys assigned so far:
    Digits:     1
    Letters:    ADFOSUX
    Arrows:     Left Right Up
"""

def handle_key_presses(yammy: Any, problem: Any) -> None:
    player = u.player_in_front()
#     if u.key_f():
#         yammy.toggle_disappear()

    if not u.any_movement():
        if u.key_1():
            if not problem.showing:
                problem.random_question()
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
            #toggle problem
            if problem.showing:
                problem.toggle()

        #minus one point
        elif u.key_x():
            u.wrong_answer(player)
            if player.item:
                player.item.poof()
                player.item = None
            u.rotate_players_left()
            #toggle problem
            if problem.showing:
                problem.toggle()

        elif u.key_a():
            u.rotate_items_left()

        elif u.key_d():
            u.rotate_items_right()

        elif u.key_s():
            c.ALL_ITEMS = u.mix(c.ALL_ITEMS)

        elif u.key_u():
            player.use_item()
