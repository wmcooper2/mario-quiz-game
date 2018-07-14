import pyglet
import random
import items
from constants import *

item_choices = [  
                    RED_MUSHROOM, 
                    GREEN_MUSHROOM, 
                    YOSHI_COIN,
                    PIRAHNA_PLANT,
                    SPINY_BEETLE,
                    POW_BUTTON,                     # non-question
                    BOMBOMB,                        # non-question
#                    "feather",                      # non-question
#                    "star",                         # non-question
#                    "question block",               # unknown
]
    
def item_probability(probabilities):
    """returns a choice of item based on the passed in probability list. Returns String."""
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
    
def new_item():
    """Adds new item to all_items. Returns Sprite object."""
    #default item is RedMushroom
    item = (items.RedMushroom(img = items.RedMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    item.scale = 1.5
    item_choice = RED_MUSHROOM

    if SUPER_EASY:
        item_choice = item_probability(SUPER_EASY_RANGE)
    elif EASY:
        item_choice = item_probability(EASY_RANGE)
    elif MEDIUM:
        item_choice = item_probability(MEDIUM_RANGE)
    elif HARD:
        item_choice = item_probability(HARD_RANGE)
    elif SUPER_HARD:
        item_choice = item_probability(SUPER_HARD_RANGE)
    
    if item_choice == RED_MUSHROOM: 
        item = (items.RedMushroom(img = items.RedMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice ==  GREEN_MUSHROOM:
        item = (items.GreenMushroom(img = items.GreenMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice == YOSHI_COIN: 
        item = (items.YoshiCoin(img = items.YoshiCoin.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice == PIRAHNA_PLANT:
        item = (items.PirahnaPlant(img = items.PirahnaPlant.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice == SPINY_BEETLE: 
        item = (items.SpinyBeetle(img = items.SpinyBeetle.walk_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice == POW_BUTTON: 
        item = (items.PowButton(img = items.PowButton.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice == BOMBOMB:
        item = (items.Bombomb(img = items.Bombomb.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
#    elif item_choice == "feather": 
#        item = (items.Feather(img = items.Feather.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
#    elif item_choice == "star": 
#        item = (items.Star(img = items.Star.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
#    elif item_choice == "question block": 
#        item = (items.QuestionBlock(img = items.QuestionBlock.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    return item
