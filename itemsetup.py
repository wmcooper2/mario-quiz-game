import pyglet
import random
import items
from constants import *


#item probability
#replace the call to random below and the item assignments with this block function
#for x in range(NUM_ITEMS):
#    choice = random.choice(1, 100)
#    if choice <= 5:                             #  5%
#        item = "pow button"
#    if choice > 5 and choice <= 20:             # 15%
#        item = "yoshi coin"
#    if choice > 20 and choice <= 35:            # 15%
#        item = "bombomb"
#    if choice > 35 and choice <= 55:            # 20%
#        item = "red mushroom"

# 2,3,6,12,27,27,12,6,3,2 == 100



item_choices = [    "green mushroom", 
                    "red mushroom", 
                    "pow button", 
                    "yoshi coin", 
                    "spiny beetle", 
                    "pirahna plant",
                    "bombomb",]

def new_item():
    """Adds new item to all_items. Returns Sprite object."""
    item = random.choice(item_choices)
    if item == "green mushroom": 
        item = (items.GreenMushroom(img = items.GreenMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "red mushroom": 
        item = (items.RedMushroom(img = items.RedMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "pow button": 
        item = (items.PowButton(img = items.PowButton.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "yoshi coin": 
        item = (items.YoshiCoin(img = items.YoshiCoin.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "spiny beetle": 
        item = (items.SpinyBeetle(img = items.SpinyBeetle.walk_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "pirahna plant":
        item = (items.PirahnaPlant(img = items.PirahnaPlant.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "bombomb":
        item = (items.Bombomb(img = items.Bombomb.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    item.scale = 1.5
    return item
