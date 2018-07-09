import pyglet
import players
from constants import *
from playerscores import Score

def make_yammy():       #not a playing character
    yammy = players.Yammy(img = players.Yammy.stand_right, x = 30, y = ITEM_PLATFORM_H, batch = main_batch)
    yammy.scale = 2
    yammy.opacity = 0
    return yammy

def make_firelight():
    fire_light = players.FireLight(img = players.FireLight.stand_left, x = OFF_SCREEN_R, y = FLOAT_H, batch = main_batch)
    fire_light.scale = 1.5
    return fire_light

def make_dragon():
    dragon = players.Dragon(img = players.Dragon.stand_left, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
    dragon.scale = 2
    return dragon

def make_big_boo():
    big_boo = players.BigBoo(img = players.BigBoo.stand_left, x = OFF_SCREEN_R, y = FLOAT_H, batch = main_batch)
    return big_boo

def make_green_koopa():
    green_koopa = players.GreenKoopa(img = players.GreenKoopa.stand_left, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch) 
    green_koopa.scale = 2
    return green_koopa

def make_big_mole():
    big_mole = players.BigMole(img = players.BigMole.stand_left, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
    big_mole.scale = 1.5 
    return big_mole

def make_mario():
    mario = players.Mario(img = players.Mario.stand_left, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
    mario.scale = 2
    return mario

def make_luigi():
    luigi = players.Luigi(img = players.Luigi.stand_left, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
    luigi.scale = 2
    return luigi

def make_score_sprite(player, score_x, score_y):
    
    if isinstance(player, players.FireLight):
        score_sprite = players.FireLight(img = players.FireLight.stand_left_seq[0], x = score_x, y = score_y, batch = main_batch)
        score_sprite.y -= 5                             #readjusted for score_display only
#        score_sprite.score = Score(img = Score.coin_img, score_sprite = score_sprite)
    elif isinstance(player, players.Dragon):
        score_sprite = players.Dragon(img = players.Dragon.stand_left, x = score_x, y = score_y, batch = main_batch)
#        score_sprite.score = Score(img = Score.coin_img, score_sprite = score_sprite)
    elif isinstance(player, players.BigBoo):
        score_sprite = players.BigBoo(img = players.BigBoo.stand_left, x = score_x, y = score_y, batch = main_batch)
        score_sprite.y += 15                            #readjusted for score_display only
        score_sprite.scale = 0.5
#        score_sprite.score = Score(img = Score.coin_img, score_sprite = score_sprite)
    elif isinstance(player, players.GreenKoopa):
        score_sprite = players.GreenKoopa(img = players.GreenKoopa.stand_left, x = score_x, y = score_y, batch = main_batch)
#        score_sprite.score = Score(img = Score.coin_img, score_sprite = score_sprite)
    elif isinstance(player, players.BigMole):
        score_sprite = players.BigMole(img = players.BigMole.stand_left, x = score_x, y = score_y, batch = main_batch)
#        score_sprite.score = Score(img = Score.coin_img, score_sprite = score_sprite)
    elif isinstance(player, players.Mario):
        score_sprite = players.Mario(img = players.Mario.stand_left, x = score_x, y = score_y, batch = main_batch)
#        score_sprite.score = Score(img = Score.coin_img, score_sprite = score_sprite)
    elif isinstance(player, players.Luigi):
        score_sprite = players.Luigi(img = players.Luigi.stand_left, x = score_x, y = score_y, batch = main_batch)
#        score_sprite.score = Score(img = Score.coin_img, score_sprite = score_sprite)
    return score_sprite
