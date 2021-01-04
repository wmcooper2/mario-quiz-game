#std lib
import random
from typing import Any, List

#3rd party
import pyglet

#custom
import items
from constants import constants as c
from constants import Items as i
from constants import Difficulty as d

def choose_item(difficulty: List[int]) -> Any:
    """Choose an item."""
    if difficulty == d.SUPER_EASY:
        return probability(c.SUPER_EASY_RANGE)
    elif difficulty == d.EASY:
        return probability(c.EASY_RANGE)
    elif difficulty == d.MEDIUM:
        return probability(c.MEDIUM_RANGE)
    elif difficulty == d.HARD:
        return probability(c.HARD_RANGE)
    elif difficulty == d.SUPER_HARD:
        return probability(c.SUPER_HARD_RANGE)

def probability(choices) -> Any:
    """returns a choice of item based on the passed in probability list."""
    choice = random.randrange(1, 100, 1)
    if choice >= choices[5] and choice <= choices[6]:                  
        return i.RED_MUSHROOM
    elif choice >= choices[4] and choice < choices[5]:               
        return i.GREEN_MUSHROOM 
    elif choice >= choices[3] and choice < choices[4]:                
        return i.YOSHI_COIN 
    elif choice >= choices[2] and choice < choices[3]:               
        return i.PIRAHNA_PLANT 
    elif choice >= choices[1] and choice < choices[2]:              
        return i.SPINY_BEETLE 
    elif choice >= choices[0] and choice < choices[1]:             
        return i.POW_BUTTON 
    elif choice > 0 and choice < choices[0]:            
        return i.BOMBOMB 
    
def new_item() -> Any:
    """Adds new item to all_items. Returns Sprite object."""
    difficulty = c.DIFFICULTY
    choice = choose_item(difficulty)

    if choice == i.RED_MUSHROOM: 
        return (items.RedMushroom(img=items.RedMushroom.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE))
    elif choice == i.GREEN_MUSHROOM:
        return (items.GreenMushroom(img=items.GreenMushroom.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE))
    elif choice == i.YOSHI_COIN: 
        return (items.YoshiCoin(img=items.YoshiCoin.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE))
    elif choice == i.PIRAHNA_PLANT:
        return (items.PirahnaPlant(img=items.PirahnaPlant.walk_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE))
    elif choice == i.SPINY_BEETLE: 
        return (items.SpinyBeetle(img=items.SpinyBeetle.walk_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE))
    elif choice == i.POW_BUTTON: 
        return (items.PowButton(img=items.PowButton.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE))
    elif choice == i.BOMBOMB:
        return (items.Bombomb(img=items.Bombomb.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE))
#    elif choice == i.FEATHER: 
#        return (items.Feather(img=items.Feather.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE))
#    elif choice == i.STAR: 
#        return (items.Star(img=items.Star.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE))
#    elif choice == i.QUESTION_BLOCK: 
#        return (items.QuestionBlock(img=items.QuestionBlock.stand_right_anim, x=c.OFF_SCREEN_L, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH, scale=c.ITEM_SCALE))
