#stand lib

#3rd party
import pyglet

#custom
from src.constants import *
from src.players import *

def make_yammy():       #not a playing character
    yammy = Yammy(img=Yammy.stand_right, x=30, \
            y=ITEM_PLATFORM_HEIGHT, batch=MAIN_BATCH)
    yammy.scale = 2
    yammy.opacity = 0
    return yammy

def make_firelight():
    fire_light = FireLight(img=FireLight.stand_left, \
            x=OFF_SCREEN_RIGHT, y=FLOAT_HEIGHT, batch=MAIN_BATCH)
    fire_light.scale = 1.5
    return fire_light

def make_dragon():
    dragon = Dragon(img=Dragon.stand_left, x=OFF_SCREEN_RIGHT, \
            y=WALK_HEIGHT, batch=MAIN_BATCH)
    dragon.scale = 2
    return dragon

def make_big_boo():
    big_boo = BigBoo(img=BigBoo.stand_left, x=OFF_SCREEN_RIGHT, \
            y=FLOAT_HEIGHT, batch=MAIN_BATCH)
    return big_boo

def make_green_koopa():
    green_koopa = GreenKoopa(img=GreenKoopa.stand_left, \
            x=OFF_SCREEN_RIGHT, y=WALK_HEIGHT, batch=MAIN_BATCH) 
    green_koopa.scale = 2
    return green_koopa

def make_big_mole():
    big_mole = BigMole(img=BigMole.stand_left, \
            x=OFF_SCREEN_RIGHT, y=WALK_HEIGHT, batch=MAIN_BATCH)
    big_mole.scale = 1.5 
    return big_mole

def make_mario():
    mario = Mario(img=Mario.stand_left, x=OFF_SCREEN_RIGHT, \
            y=WALK_HEIGHT, batch=MAIN_BATCH)
    mario.scale = 2
    return mario

def make_luigi():
    luigi = Luigi(img=Luigi.stand_left, x=OFF_SCREEN_RIGHT, \
            y=WALK_HEIGHT, batch=MAIN_BATCH)
    luigi.scale = 2
    return luigi
