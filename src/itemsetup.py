#stand lib
import random

#3rd party
import pyglet

#custom
from src.constants import *
from src.items import *

item_choices = [  
                    RED_MUSHROOM, 
                    GREEN_MUSHROOM, 
                    YOSHI_COIN,
                    PIRAHNA_PLANT,
                    SPINY_BEETLE,
                    POW_BUTTON,                     # non-question
                    BOMBOMB,                        # non-question
#                    FEATHER,
#                    STAR,
#                    QUESTION_BLOCK,
]

def setup_items(num_items, all_items):
    """Sets up the items on the platform. Returns None."""
    for item in range(num_items):
        all_items.append(new_item())
    
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
        item = (RedMushroom(img=RedMushroom.stand_right_anim, \
                x=OFF_SCREEN_LEFT, y=ITEM_PLATFORM_HEIGHT, \
                batch=MAIN_BATCH))
        item.scale = 1.5
    elif item_choice ==  GREEN_MUSHROOM:
        item = (GreenMushroom(img=GreenMushroom.stand_right_anim, \
                x=OFF_SCREEN_LEFT, y=ITEM_PLATFORM_HEIGHT, \
                batch=MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == YOSHI_COIN: 
        item = (YoshiCoin(img=YoshiCoin.stand_right_anim, \
                x=OFF_SCREEN_LEFT, y=ITEM_PLATFORM_HEIGHT, \
                batch=MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == PIRAHNA_PLANT:
        item = (PirahnaPlant(img=PirahnaPlant.stand_right_anim, \
                x=OFF_SCREEN_LEFT, y=ITEM_PLATFORM_HEIGHT, \
                batch=MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == SPINY_BEETLE: 
        item = (SpinyBeetle(img=SpinyBeetle.walk_right_anim, \
                x=OFF_SCREEN_LEFT, y=ITEM_PLATFORM_HEIGHT, \
                batch=MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == POW_BUTTON:
        item = (PowButton(img=PowButton.stand_right_anim, \
                x=OFF_SCREEN_LEFT, y=ITEM_PLATFORM_HEIGHT, \
                batch=MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == BOMBOMB:
        item = (Bombomb(img=Bombomb.stand_right_anim, \
                x=OFF_SCREEN_LEFT, y=ITEM_PLATFORM_HEIGHT, \
                batch=MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == "feather": 
        item = (Feather(img=Feather.stand_right_anim, \
                x=OFF_SCREEN_LEFT, y=ITEM_PLATFORM_HEIGHT, \
                batch=MAIN_BATCH))
    elif item_choice == "star": 
        item = (Star(img=Star.stand_right_anim, \
                x=OFF_SCREEN_LEFT, y=ITEM_PLATFORM_HEIGHT, \
                batch=MAIN_BATCH))
    elif item_choice == "question block": 
        item = (QuestionBlock(img=QuestionBlock.stand_right_anim, \
                x=OFF_SCREEN_LEFT, y=ITEM_PLATFORM_HEIGHT, \
                batch=MAIN_BATCH))
    return item
