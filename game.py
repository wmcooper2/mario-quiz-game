#std lib
from pprint import pprint
import random

#3rd party
import pyglet

#custom
from animations import transfer_item
from constants import Constants as c
from constants import Screens
from draw_loop import draw_menu, draw_problem, draw_sprites, draw_title
import items as i
from key_presses import game_loop_keys, title_loop_keys
import util as u
import sprites as s

#TODO, add the star, feather and question block to the game
#NOTE, the business logic is separated from the drawing of the sprites in the update loops

#Music
# source = pyglet.media.load('explosion.wav')
# source = pyglet.resource.media('overworld.mp3')
source = pyglet.media.load('./music/overworld.mp3')
source.play()

#SPRITES
background = s.Background()
selector = s.Selector()
yammy = s.Yammy()

#floaters
fire_light = s.FireLight()
big_boo = s.BigBoo()

#walkers
dragon = s.Dragon()
green_koopa = s.GreenKoopa()
big_mole = s.BigMole()
mario = s.Mario()
luigi = s.Luigi()

#PLAYERS
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

#SOME SETUP
#Items
u.set_item_spots()
i.add_items()

#Players
u.set_player_spots()
u.add_players()

#Scores
#TODO, move these to their respective classes?
u.set_score_spots()
u.set_score_indices()
u.set_player_score_sprites()
u.assign_x_pos_to_player_score_sprites()
u.set_score_values_x()

question = c.NEW_QUESTION
problem = s.Problem()

def update_items(dt) -> None:
    for item in c.ALL_ITEMS:
        item.dest_x = c.ITEM_SPOTS[c.ALL_ITEMS.index(item)]
        item.update(dt)
    if c.TRANSFER_ITEM is not None:
        c.TRANSFER_ITEM.update(dt)
    
def update_players(dt) -> None:
    #update player positions
    for p in c.PLAYERS:
        p.spot = c.PLAYER_SPOTS[c.PLAYERS.index(p)]
        p.update(dt)

def game_loop(dt) -> None:
    """Handles the business logic for the game loop."""
    yammy.update()
    update_players(dt)
    update_items(dt)
    game_loop_keys(yammy, problem)
    transfer_item()

def title_loop(dt) -> None:
    """Handles the business logic for the Title screen."""
    #key handlers for title buttons
    title_loop_keys(selector)

@c.GAME_WINDOW.event
def on_draw() -> None:
    """Handles the drawing the sprites on screen."""
    if Screens.TITLE:
        c.GAME_WINDOW.clear()
        draw_title()
    else:
        draw_sprites()
        if problem.showing:
            draw_problem(problem)

if __name__ == "__main__":
    if Screens.TITLE:
        pyglet.clock.schedule_interval(title_loop, c.FRAME_SPEED)
    else:
        pyglet.clock.schedule_interval(game_loop, c.FRAME_SPEED)
    pyglet.app.run()
