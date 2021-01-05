#std lib
import random

#3rd party
import pyglet

#custom
from constants import constants as c
from draw_loop import draw_game_board
from key_presses import handle_key_presses
import util as u
import sprites as s
import items #must come after sprites (resource mod is defined in sprites... move to main?) #not needed?

#TODO, remove this somehow
# from itemsetup import new_item # must stay here... strange error

#TODO, refactor new_item function out of this module
#TODO, if player moves while item in air, then wierd stuff happens
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

#line setups
u.setup_positions_on_screen()
# u.set_player_spots()
# u.set_item_spots(c.ALL_ITEMS)
# u.set_score_spots()
# u.add_items(new_item)                     #sets up c.ALL_ITEMS
u.add_items()                               #sets up c.ALL_ITEMS
# u.add_players(c.RANDOMIZE_PLAYERS)        #sets up c.PLAYERS
# u.scores_setup(c.SCORE_SPOTS, mini_sprite)

#Set Player 1, the player closest to the items
c.P1 = c.PLAYERS[0]

def update(dt) -> None:
    """Game update loop.
        Updates occur in this order;
            Item effects
            Yammy
            All players' x_pos
            Floating players y_pos
            c.ALL_ITEMS x_pos and y_pos
            c.ITEM x_pos and y_pos
    """

    #EFFECTS
#     if c.BOMBOMB_EFFECT:                                        #mix items
#         u.mix(c.ALL_ITEMS)
#         c.BOMBOMB_EFFECT = False                            #reset flag
#     if c.POW_BUTTON_EFFECT:                                 #all, minus one point
#         for player in c.PLAYERS:
#             player.points -= 1
#         c.POW_BUTTON_EFFECT = False                         #reset flag
#    if c.FEATHER_EFFECT:
#        print("change feather effect to something more interesting.")
#        u.rotate_players_left()
#        FEATHER_EFFECT = False                                 #reset flag
#    if c.STAR_EFFECT:
#        print("change star effect to something more interesting.")
#        STAR_EFFECT = False                                    #reset flag
#    if c.QUESTION_BLOCK_EFFECT:
#        print("change star effect to something more interesting.")
#        QUESTION_BLOCK_EFFECT = False                          #reset flag

    #YAMMY
    yammy.update()

    #ALL PLAYERS
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
    #update floating players y_pos
    for player in c.FLOATING_PLAYERS:
        player.float()

    #ITEMS
    #update items x_pos and y_pos
    for item in c.ALL_ITEMS:
        if item is not None:
            item.dest_x = c.ITEM_SPOTS[c.ALL_ITEMS.index(item)]
            item.update(dt)

    if c.ITEM is not None:
        c.ITEM.update(dt)

    #KEY HANDLERS
    #need to pass yammy
    handle_key_presses(yammy)

@c.GAME_WINDOW.event
def on_draw() -> None:
    """Draw the visual elements."""
    c.GAME_WINDOW.clear()
    c.MAIN_BATCH.draw()
    draw_game_board()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, c.FRAME_SPEED)
    pyglet.app.run()
