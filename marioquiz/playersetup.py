#3rd party
import pyglet

#custom
from src.constants import *
from src.players import *

def floating(char):
    """Generic floating character constructor. Returns Player object."""
    return char(img=char.animl, x=OFF_SCREEN_RIGHT, y=FLOAT_HEIGHT, \
            batch=MAIN)
    
def walking(char):
    """Generic walking character constructor. Returns Player object."""
    return char(img=char.animl, x=OFF_SCREEN_RIGHT, y=WALK_HEIGHT, \
            batch=MAIN)

#SPECIAL
def make_yammy():
    yammy = Yammy(img=Yammy.faceright, x=30, y=ITEM_PLATFORM_HEIGHT, \
            batch=MAIN)
    yammy.scale = 2
    yammy.opacity = 0
    return yammy

#FLOATING
def bigBoo():
    return floating(BigBoo)

def fireLight():
    char = floating(FireLight)
    char.scale = 1.5
    return char

#WALKING
def dragon():
    char = walking(Dragon)
    char.scale = 2
    return char

def greenKoopa():
    char = walking(GreenKoopa)
    char.scale = 2
    return char

def bigMole():
    char = walking(BigMole)
    char.scale = 1.5 
    return char

def mario():
    char = walking(Mario)
    char.scale = 2
    return char

def luigi():
    char = walking(Luigi)
    char.scale = 2
    return char
