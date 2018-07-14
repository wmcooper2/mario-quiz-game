import pyglet
import random
import items
from constants import *

#def easy_difficulty2():
#    """Game is set to 'easy' and more simple questions and helpful items are used. Returns String."""
#    choice = random.randrange(1, 100, 1)
#    if choice <= 0 and choice < 2:                    #   2% 
#        item = "question block"
#    elif choice <= 2 and choice < 5:                  #   3%
#        item = "bombomb"
#    elif choice <= 5 and choice < 11:                 #   6%
#        item = "pow button"
#    elif choice <= 11 and choice < 23:                #   12%
#        item = "spiney beetle"
#    elif choice <= 23 and choice < 50:                #   27%
#        item = "green mushroom"
#    elif choice <= 50 and choice < 77:                #   27%
#        item = "red mushroom"
#    elif choice <= 77 and choice < 89:                #   12%
#        item = "pirahna plant"
#    elif choice <= 89 and choice < 95:                #   6%
#        item = "yoshi coin"
#    elif choice <= 95 and choice < 98:                #   3%
#        item = "feather"
#    elif choice <= 98 and choice < 100:               #   2%
#        item = "star"
#    return item
    


def super_easy_difficulty(): #intro version
    """Game is set to 'easy' and more simple questions and helpful items are used. Returns String."""
    choice = random.randrange(1, 100, 1)
    if choice >= EASY[5] and choice <= EASY[6]:                  
        item = "red mushroom"
    elif choice >= EASY[4] and choice < EASY[5]:               
        item = "green mushroom"
    elif choice >= EASY[3] and choice < EASY[4]:                
        item = "yoshi coin"
    elif choice >= EASY[2] and choice < EASY[3]:               
        item = "pirahna plant"
    elif choice >= EASY[1] and choice < EASY[2]:              
        item = "spiney beetle"
    elif choice >= EASY[0] and choice < EASY[1]:             
        item = "pow button"
    elif choice > 0 and choice < EASY[0]:            
        item = "bombomb"
    print("random choice integer = ", str(choice))
    print("easy_difficulty(), item choice = ", item)
    return item
    
#
##    medium probability distribution
##    2,3,6,12,27,27,12,6,3,2 == 100
#def medium_difficulty():
##    replace the call to random below and the item assignments with this block function
##    for x in range(NUM_ITEMS):
#    choice = random.randrange(1, 100, 1)
#    if choice <= 0 and choice < 2:                    #   2% 
#        item = "question block"
#    elif choice <= 2 and choice < 5:                  #   3%
#        item = "bombomb"
#    elif choice <= 5 and choice < 11:                 #   6%
#        item = "pow button"
#    elif choice <= 11 and choice < 23:                #   12%
#        item = "spiney beetle"
#    elif choice <= 23 and choice < 50:                #   27%
#        item = "green mushroom"
#    elif choice <= 50 and choice < 77:                #   27%
#        item = "red mushroom"
#    elif choice <= 77 and choice < 89:                #   12%
#        item = "pirahna plant"
#    elif choice <= 89 and choice < 95:                #   6%
#        item = "yoshi coin"
#    elif choice <= 95 and choice < 98:                #   3%
#        item = "feather"
#    elif choice <= 98 and choice < 100:               #   2%
#        item = "star"
#    return item

item_choices = [  
#                    "question block",               # unknown
                    "bombomb",                      # non-question
                    "pow button",                   # non-question
                    "spiny beetle", 
                    "green mushroom", 
                    "red mushroom", 
                    "pirahna plant",
                    "yoshi coin", 
#                    "feather",                      # non-question
#                    "star",                         # non-question
]

def item_probability(probabilities):
    """returns a choice of item based on the passed in probability list. Returns String."""
    list_ = probabilities
    choice = random.randrange(1, 100, 1)
    if choice >= list_[5] and choice <= list_[6]:                  
        item = "red mushroom"
    elif choice >= list_[4] and choice < list_[5]:               
        item = "green mushroom"
    elif choice >= list_[3] and choice < list_[4]:                
        item = "yoshi coin"
    elif choice >= list_[2] and choice < list_[3]:               
        item = "pirahna plant"
    elif choice >= list_[1] and choice < list_[2]:              
        item = "spiney beetle"
    elif choice >= list_[0] and choice < list_[1]:             
        item = "pow button"
    elif choice > 0 and choice < list_[0]:            
        item = "bombomb"
    print("random choice integer = ", str(choice))
    print("easy_difficulty(), item choice = ", item)
    return item
    
def new_item():
    """Adds new item to all_items. Returns Sprite object."""
    #default item is RedMushroom
    item = (items.RedMushroom(img = items.RedMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    item.scale = 1.5
    item_choice = "red mushroom"

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
    
    if item_choice == "bombomb":
        item = (items.Bombomb(img = items.Bombomb.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice == "pow button": 
        item = (items.PowButton(img = items.PowButton.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice == "spiny beetle": 
        item = (items.SpinyBeetle(img = items.SpinyBeetle.walk_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice == "green mushroom": 
        item = (items.GreenMushroom(img = items.GreenMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice == "red mushroom": 
        item = (items.RedMushroom(img = items.RedMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice == "pirahna plant":
        item = (items.PirahnaPlant(img = items.PirahnaPlant.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
    elif item_choice == "yoshi coin": 
        item = (items.YoshiCoin(img = items.YoshiCoin.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
        item.scale = 1.5
#    elif item_choice == "question block": 
#        item = (items.QuestionBlock(img = items.QuestionBlock.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
#    elif item_choice == "feather": 
#        item = (items.Feather(img = items.Feather.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
#    elif item_choice == "star": 
#        item = (items.Star(img = items.Star.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
#    else:
#        new_item()
#    item.scale = 1.5
    return item
