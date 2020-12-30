import pyglet
import players
from constants import constants as c

def make_yammy():       #not a playing character
    yammy = players.Yammy(img=players.Yammy.stand_right, x=30, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH)
    yammy.scale = 2
    yammy.opacity = 0
    return yammy

def make_firelight():
    fire_light = players.FireLight(img=players.FireLight.stand_left, x=c.OFF_SCREEN_R, y=c.FLOAT_H, batch=c.MAIN_BATCH)
    fire_light.scale = 1.5
    return fire_light

def make_dragon():
    dragon = players.Dragon(img=players.Dragon.stand_left, x=c.OFF_SCREEN_R, y=c.WALK_H, batch=c.MAIN_BATCH)
    dragon.scale = 2
    return dragon

def make_big_boo():
    big_boo = players.BigBoo(img=players.BigBoo.stand_left, x=c.OFF_SCREEN_R, y=c.FLOAT_H, batch=c.MAIN_BATCH)
    return big_boo

def make_green_koopa():
    green_koopa = players.GreenKoopa(img=players.GreenKoopa.stand_left, x=c.OFF_SCREEN_R, y=c.WALK_H, batch=c.MAIN_BATCH) 
    green_koopa.scale = 2
    return green_koopa

def make_big_mole():
    big_mole = players.BigMole(img=players.BigMole.stand_left, x=c.OFF_SCREEN_R, y=c.WALK_H, batch=c.MAIN_BATCH)
    big_mole.scale = 1.5 
    return big_mole

def make_mario():
    mario = players.Mario(img=players.Mario.stand_left, x=c.OFF_SCREEN_R, y=c.WALK_H, batch=c.MAIN_BATCH)
    mario.scale = 2
    return mario

def make_luigi():
    luigi = players.Luigi(img=players.Luigi.stand_left, x=c.OFF_SCREEN_R, y=c.WALK_H, batch=c.MAIN_BATCH)
    luigi.scale = 2
    return luigi
