#std lib
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

def handle_key_presses(yammy: Any) -> None:
    #disappear Yammy
    if u.key_f():
        yammy.toggle_disappear()

    #yammy drops item
    elif u.key_1() and not u.any_movement(c.PLAYERS, c.ALL_ITEMS, [c.TRANSFER_ITEM]) and not u.black_box_visible():
        #if player already has item, delete that item first
        if u.player_has_item(c.P1):
#             c.P1.item.delete()
            c.P1.item.poof()
            c.P1.item = None
        yammy.wave_wand()
        c.TRANSFER_ITEM = u.remove_item_from_platform()
        i.add_item()

    elif u.key_left() and not u.movement(c.PLAYERS) and not u.black_box_visible():
        u.rotate_players_left()

    elif u.key_right() and not u.movement(c.PLAYERS) and not u.black_box_visible():
        u.rotate_players_right()

    elif u.key_up() and not u.movement(c.PLAYERS) and not u.black_box_visible():
        c.PLAYERS = u.mix(c.PLAYERS)

    #plus one point
    elif u.key_o() and u.player_has_item(c.P1) and not u.movement(c.PLAYERS):
        u.right_answer(c.P1)
        u.rotate_players_left()

    #minus one point
    elif u.key_x() and u.player_has_item(c.P1) and not u.movement(c.PLAYERS):
        u.wrong_answer(c.P1)
        c.P1.delete_item()
        u.rotate_players_left()
        #set item dest to go off screen left and disappear after it leaves the visible area?

    elif u.key_a() and not u.movement(c.ALL_ITEMS):
        u.rotate_items_left()

    elif u.key_d()  and not u.movement(c.ALL_ITEMS):
        u.rotate_items_right()

    elif u.key_s() and not u.movement(c.ALL_ITEMS):
        c.ALL_ITEMS = u.mix(c.ALL_ITEMS)

    elif u.key_u() and u.player_has_item(c.P1):
        c.P1.use_item()
        #delete item after use
        c.P1.delete_item()
