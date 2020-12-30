#std lib
import random

#3rd party
import pyglet

#custom
import items
from constants import constants as c

item_choices = [  
                    c.RED_MUSHROOM, 
                    c.GREEN_MUSHROOM, 
                    c.YOSHI_COIN,
                    c.PIRAHNA_PLANT,
                    c.SPINY_BEETLE,
                    c.POW_BUTTON,                     # non-question
                    c.BOMBOMB,                        # non-question
#                    "feather",                      # non-question
#                    "star",                         # non-question
#                    "question block",               # unknown
]
    
def item_probability(probabilities):
    """returns a choice of item based on the passed in probability list. Returns String."""
    list_ = probabilities
    choice = random.randrange(1, 100, 1)
    if choice >= list_[5] and choice <= list_[6]:                  
        item = c.RED_MUSHROOM
    elif choice >= list_[4] and choice < list_[5]:               
        item = c.GREEN_MUSHROOM 
    elif choice >= list_[3] and choice < list_[4]:                
        item = c.YOSHI_COIN 
    elif choice >= list_[2] and choice < list_[3]:               
        item = c.PIRAHNA_PLANT 
    elif choice >= list_[1] and choice < list_[2]:              
        item = c.SPINY_BEETLE 
    elif choice >= list_[0] and choice < list_[1]:             
        item = c.POW_BUTTON 
    elif choice > 0 and choice < list_[0]:            
        item = c.BOMBOMB 
    return item
    
def new_item():
    """Adds new item to all_items. Returns Sprite object."""
    #default item is RedMushroom
    item = (items.RedMushroom(img=items.RedMushroom.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH))
    item.scale = 1.5
    item_choice = c.RED_MUSHROOM

    if c.SUPER_EASY:
        item_choice = item_probability(c.SUPER_EASY_RANGE)
    elif c.EASY:
        item_choice = item_probability(c.EASY_RANGE)
    elif c.MEDIUM:
        item_choice = item_probability(c.MEDIUM_RANGE)
    elif c.HARD:
        item_choice = item_probability(c.HARD_RANGE)
    elif c.SUPER_HARD:
        item_choice = item_probability(c.SUPER_HARD_RANGE)
    
    if item_choice == c.RED_MUSHROOM: 
        item = (items.RedMushroom(img=items.RedMushroom.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice ==  c.GREEN_MUSHROOM:
        item = (items.GreenMushroom(img=items.GreenMushroom.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == c.YOSHI_COIN: 
        item = (items.YoshiCoin(img=items.YoshiCoin.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == c.PIRAHNA_PLANT:
        item = (items.PirahnaPlant(img=items.PirahnaPlant.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == c.SPINY_BEETLE: 
        item = (items.SpinyBeetle(img=items.SpinyBeetle.walk_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == c.POW_BUTTON: 
        item = (items.PowButton(img=items.PowButton.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == c.BOMBOMB:
        item = (items.Bombomb(img=items.Bombomb.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH))
        item.scale = 1.5
#    elif item_choice == "feather": 
#        item = (items.Feather(img=items.Feather.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH))
#    elif item_choice == "star": 
#        item = (items.Star(img=items.Star.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH))
#    elif item_choice == "question block": 
#        item = (items.QuestionBlock(img=items.QuestionBlock.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH))
    return item
