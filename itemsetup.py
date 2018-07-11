import pyglet
import random
import items
from constants import *


def item_probability():
#     2,3,6,12,27,27,12,6,3,2 == 100
#    replace the call to random below and the item assignments with this block function
#    for x in range(NUM_ITEMS):
    choice = random.randrange(1, 100, 1)
    if choice <= 0 and choice < 2:                    #   2% 
        item = "question block"
    elif choice <= 2 and choice < 5:                  #   3%
        item = "bombomb"
    elif choice <= 5 and choice < 11:                 #   6%
        item = "pow button"
    elif choice <= 11 and choice < 23:                #   12%
        item = "spiney beetle"
    elif choice <= 23 and choice < 50:                #   27%
        item = "green mushroom"
    elif choice <= 50 and choice < 77:                #   27%
        item = "red mushroom"
    elif choice <= 77 and choice < 89:                #   12%
        item = "pirahna plant"
    elif choice <= 89 and choice < 95:                #   6%
        item = "yoshi coin"
    elif choice <= 95 and choice < 98:                #   3%
        item = "feather"
    elif choice <= 98 and choice < 100:               #   2%
        item = "star"
    return item

item_choices = [    "question block",
                    "bombomb",
                    "pow button", 
                    "spiny beetle", 
                    "green mushroom", 
                    "red mushroom", 
                    "pirahna plant",
                    "yoshi coin", 
                    "feather",
                    "star",
]

def new_item():
    """Adds new item to all_items. Returns Sprite object."""
    item = item_probability()
#    item = random.choice(item_choices)
    if item == "question block":
        item = (items.QuestionBlock(img = items.QuestionBlock.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "bombomb":
        item = (items.Bombomb(img = items.Bombomb.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "pow button": 
        item = (items.PowButton(img = items.PowButton.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "spiny beetle": 
        item = (items.SpinyBeetle(img = items.SpinyBeetle.walk_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "green mushroom": 
        item = (items.GreenMushroom(img = items.GreenMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "red mushroom": 
        item = (items.RedMushroom(img = items.RedMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "pirahna plant":
        item = (items.PirahnaPlant(img = items.PirahnaPlant.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "yoshi coin": 
        item = (items.YoshiCoin(img = items.YoshiCoin.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "feather": 
        item = (items.Feather(img = items.Feather.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "star": 
        item = (items.Star(img = items.Star.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    item.scale = 1.5
    return item
