#stand lib
import random

#3rd party
import pyglet

#custom
from src.constants import *
from src.items import *

def setup_items(num):
    """Sets up 'num' items on the platform. Returns None."""
    items = []
    [items.append(new_item()) for item in range(num)]
    return items

def make_item(class_):
    """Generic item constructor. Returns Sprite object."""
    item = (class_(img=class_.facer, x=OFF_SCREEN_LEFT, \
            y=ITEM_PLATFORM_HEIGHT, batch=MAIN))
    item.scale = 1.5
    return item
    
def decision(probabilities):
    """Decides which item. Returns String."""
    list_ = probabilities
    choice = random.randrange(1, 100, 1)
    if choice >= list_[5] and choice <= list_[6]:                  
        item = RED_MUSHROOM
    elif choice >= list_[4] and choice < list_[5]:               
        item = GREEN_MUSHROOM 
    elif choice >= list_[3] and choice < list_[4]:                
        item = YOSHI_COIN 
    elif choice >= list_[2] and choice < list_[3]:               
        item = PIRAHNA_PLANT 
    elif choice >= list_[1] and choice < list_[2]:              
        item = SPINY_BEETLE 
    elif choice >= list_[0] and choice < list_[1]:             
        item = POW_BUTTON 
    elif choice > 0 and choice < list_[0]:            
        item = BOMBOMB 
    return item

def probability(string):
    """Decides which probability range. Returns String."""
    return {
        "supereasy"     : SUPER_EASY_RANGE,
        "easy"          : EASY_RANGE,
        "medium"        : MEDIUM_RANGE,
        "hard"          : HARD_RANGE,
        "superhard"     : SUPER_HARD_RANGE}.get(string)

def new_item():
    """Gets a new item. Returns Sprite object."""
    choice = decision(probability(DIFFICULTY))
    return {RED_MUSHROOM    : make_item(RedMushroom),
            GREEN_MUSHROOM  : make_item(GreenMushroom),
            YOSHI_COIN      : make_item(YoshiCoin),
            PIRAHNA_PLANT   : make_item(PirahnaPlant),
            SPINY_BEETLE    : make_item(SpinyBeetle),
            POW_BUTTON      : make_item(PowButton),
            BOMBOMB         : make_item(Bombomb)
            }.get(choice)

