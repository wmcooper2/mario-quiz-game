#std lib
from typing import Any

#3rd party

#custom
from constants import constants as c
import util as u

def handle_key_presses(yammy: Any) -> None:

    #disappear Yammy
    if u.key_f():
        yammy.toggle_disappear()

    #Transfer item to player 1
    elif u.key_1() and not u.any_movement(c.PLAYERS, c.ALL_ITEMS) and not u.black_box_visible():
        yammy.wave_wand()
        temp = u.remove_item_from_all_items()
        temp.transfer_item()
        #TODO, remove parameter
#         u.add_item(u.new_item)
        u.add_item()
        temp.delete()

    elif u.key_left() and not u.movement(c.PLAYERS) and not u.black_box_visible():
        u.rotate_players_left()

    elif u.key_right() and not u.movement(c.PLAYERS) and not u.black_box_visible():
        u.rotate_players_right()

    elif u.key_up() and not u.movement(c.PLAYERS) and not u.black_box_visible():
        c.PLAYERS = u.mix(c.PLAYERS)

    #plus one point
    elif u.key_o() and u.player1_has_item():
        u.right_answer(c.P1)

    #minus one point
    elif u.key_x() and u.player1_has_item():
        u.wrong_answer(c.P1)

    elif u.key_a() and not u.movement(c.ALL_ITEMS):
        u.rotate_items_left()

    elif u.key_d()  and not u.movement(c.ALL_ITEMS):
        u.rotate_items_right()

    elif u.key_s() and not u.movement(c.ALL_ITEMS):
        c.ALL_ITEMS = u.mix(c.ALL_ITEMS)

