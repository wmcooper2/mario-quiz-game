#std lib
from pprint import pprint
import random

#3rd party
import pyglet

#custom
from constants import constants as c
from draw_loop import draw_game_board
from effects import handle_item_effects
import items as i
from key_presses import handle_key_presses
import util as u
import sprites as s

#TODO, if player moves while item in air, then wierd stuff happens
#TODO, items move to bottom of screen
#TODO, game crashes on item transfer
#TODO, make a way to check if player is walking type so that I don't have to waste memory or complicate things by adding another list here for walking vs floating players.

#SPRITES
background = s.Background(img=s.Background.background_img, batch=c.MAIN_BATCH)
yammy = s.Yammy(img=c.IMG("yammystandright.png"))
mario = s.Mario(img=c.IMG("bigmariostandleft.png"))
luigi = s.Luigi(img=c.IMG("bigluigistandleft.png"))
fire_light = s.FireLight(img=c.IMG("firelightwalkleft.png"))
dragon = s.Dragon(img=c.IMG("dragonstandleft.png"))
big_boo = s.BigBoo(img=c.IMG("bigboostandleft.png"))
green_koopa = s.GreenKoopa(img=c.IMG("greenkoopastandleft.png"))
big_mole = s.BigMole(img=c.IMG("bigmolestandleft.png"))

c.ALL_PLAYERS = [
    mario,
    luigi,
    fire_light,
    dragon,
    big_boo,
    green_koopa,
    big_mole]

c.WALKING_PLAYERS = [
    dragon,
    green_koopa,
    big_mole,
    mario,
    luigi]

c.FLOATING_PLAYERS = [
    fire_light,
    big_boo]

# u.setup_positions_on_screen()
u.set_player_spots()
u.set_item_spots()
i.add_items()
u.set_score_spots()
u.add_players(c.RANDOMIZE_PLAYERS)
u.scores_setup(c.SCORE_SPOTS)
c.P1 = c.PLAYERS[0]     #Set Player 1

# ================================================================================
# print("item_spots:", c.ITEM_SPOTS)
# 
# print("all_items:", len(c.ALL_ITEMS))
# for item in c.ALL_ITEMS:
#     print(item, item.x, item.dest_x) #no anchor_x here
# 
# 
# temp = u.remove_item_from_all_items()
# print("temp:", temp, temp.x, temp.dest_x)
# print("c.ITEM:", c.ITEM)
# 
# 
# print("all_items:", len(c.ALL_ITEMS))
# for item in c.ALL_ITEMS:
#     print(item, item.x, item.dest_x) #no anchor_x here
# 
# temp.transfer_item()
# print("temp:", temp, temp.x, temp.dest_x)
# print("c.ITEM:", c.ITEM)
# 
# i.add_item()
# print("all_items:", len(c.ALL_ITEMS))
# for item in c.ALL_ITEMS:
#     print(item, item.x, item.dest_x) #no anchor_x here
# print("temp:", temp, temp.x, temp.dest_x)
# print("c.ITEM:", c.ITEM)
# 
# # temp.delete()
# # c.ITEM.delete()
#  
# quit()
# 
# ================================================================================






def update_players(dt) -> None:
    c.P1 = c.PLAYERS[0]     #reset player 1
    #update player positions
    for player in c.PLAYERS:
        player.spot = c.PLAYER_SPOTS[c.PLAYERS.index(player)]
        player.update(dt)

        #player automatically uses item
#         if player.inventory and c.SHOWING_BLACK_BOX == False: 
#             print("INVENTORY:", c.P1.inventory)
#             main_item = c.P1.inventory[0]
#             player.use_item() 
   
        #update player scores 
#         score_points = c.SCORE_DISPLAY[player.point_index].points #the integer value
#         score_object = c.SCORE_DISPLAY[player.point_index]        #the score object
#         if player.points != score_points: 
#             score_object.update(score_object, player)           #player_score is in a different instance than player

    #FLOATING PLAYERS
    for player in c.FLOATING_PLAYERS:
        player.float()

def update_items(dt) -> None:
    for item in c.ALL_ITEMS:
        item.dest_x = c.ITEM_SPOTS[c.ALL_ITEMS.index(item)]
        item.update(dt)
    if c.ITEM != None:
        c.ITEM.update(dt)



def update(dt) -> None:
    """Game update loop."""
#     handle_item_effects()
    yammy.update()
    update_players(dt)
    update_items(dt)
    handle_key_presses(yammy)   #need to pass yammy

@c.GAME_WINDOW.event
def on_draw() -> None:
    """Draw the visual elements."""
    c.GAME_WINDOW.clear()
    c.MAIN_BATCH.draw()
    draw_game_board()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, c.FRAME_SPEED)
    pyglet.app.run()
