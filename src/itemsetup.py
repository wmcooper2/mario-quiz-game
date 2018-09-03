import pyglet
import random
import items
import constants

item_choices = [  
                    constants.RED_MUSHROOM, 
                    constants.GREEN_MUSHROOM, 
                    constants.YOSHI_COIN,
                    constants.PIRAHNA_PLANT,
                    constants.SPINY_BEETLE,
                    constants.POW_BUTTON,                     # non-question
                    constants.BOMBOMB,                        # non-question
#                    constants.FEATHER,
#                    constants.STAR,
#                    constants.QUESTION_BLOCK,
]
    
def item_probability(probabilities):
    """returns a choice of item based on the passed in probability list. Returns String."""
    list_ = probabilities
    choice = random.randrange(1, 100, 1)
    if choice >= list_[5] and choice <= list_[6]:                  
        item = constants.RED_MUSHROOM
    elif choice >= list_[4] and choice < list_[5]:               
        item = constants.GREEN_MUSHROOM 
    elif choice >= list_[3] and choice < list_[4]:                
        item = constants.YOSHI_COIN 
    elif choice >= list_[2] and choice < list_[3]:               
        item = constants.PIRAHNA_PLANT 
    elif choice >= list_[1] and choice < list_[2]:              
        item = constants.SPINY_BEETLE 
    elif choice >= list_[0] and choice < list_[1]:             
        item = constants.POW_BUTTON 
    elif choice > 0 and choice < list_[0]:            
        item = constants.BOMBOMB 
    return item
    
def new_item():
    """Adds new item to all_items. Returns Sprite object."""

    if constants.SUPER_EASY:
        item_choice = item_probability(constants.SUPER_EASY_RANGE)
    elif constants.EASY:
        item_choice = item_probability(constants.EASY_RANGE)
    elif constants.MEDIUM:
        item_choice = item_probability(constants.MEDIUM_RANGE)
    elif constants.HARD:
        item_choice = item_probability(constants.HARD_RANGE)
    elif constants.SUPER_HARD:
        item_choice = item_probability(constants.SUPER_HARD_RANGE)
    
    if item_choice == constants.RED_MUSHROOM: 
        item = (items.RedMushroom(img=items.RedMushroom.stand_right_anim, x=constants.OFF_SCREEN_LEFT, y=constants.ITEM_PLATFORM_HEIGHT, batch=constants.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice ==  constants.GREEN_MUSHROOM:
        item = (items.GreenMushroom(img=items.GreenMushroom.stand_right_anim, x=constants.OFF_SCREEN_LEFT, y=constants.ITEM_PLATFORM_HEIGHT, batch=constants.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == constants.YOSHI_COIN: 
        item = (items.YoshiCoin(img=items.YoshiCoin.stand_right_anim, x=constants.OFF_SCREEN_LEFT, y=constants.ITEM_PLATFORM_HEIGHT, batch=constants.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == constants.PIRAHNA_PLANT:
        item = (items.PirahnaPlant(img=items.PirahnaPlant.stand_right_anim, x=constants.OFF_SCREEN_LEFT, y=constants.ITEM_PLATFORM_HEIGHT, batch=constants.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == constants.SPINY_BEETLE: 
        item = (items.SpinyBeetle(img=items.SpinyBeetle.walk_right_anim, x=constants.OFF_SCREEN_LEFT, y=constants.ITEM_PLATFORM_HEIGHT, batch=constants.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == constants.POW_BUTTON: 
        item = (items.PowButton(img=items.PowButton.stand_right_anim, x=constants.OFF_SCREEN_LEFT, y=constants.ITEM_PLATFORM_HEIGHT, batch=constants.MAIN_BATCH))
        item.scale = 1.5
    elif item_choice == constants.BOMBOMB:
        item = (items.Bombomb(img=items.Bombomb.stand_right_anim, x=constants.OFF_SCREEN_LEFT, y=constants.ITEM_PLATFORM_HEIGHT, batch=constants.MAIN_BATCH))
        item.scale = 1.5
#    elif item_choice == "feather": 
#        item = (items.Feather(img=items.Feather.stand_right_anim, x=constants.OFF_SCREEN_LEFT, y=constants.ITEM_PLATFORM_HEIGHT, batch=constants.MAIN_BATCH))
#    elif item_choice == "star": 
#        item = (items.Star(img=items.Star.stand_right_anim, x=constants.OFF_SCREEN_LEFT, y=constants.ITEM_PLATFORM_HEIGHT, batch=constants.MAIN_BATCH))
#    elif item_choice == "question block": 
#        item = (items.QuestionBlock(img=items.QuestionBlock.stand_right_anim, x=constants.OFF_SCREEN_LEFT, y=constants.ITEM_PLATFORM_HEIGHT, batch=constants.MAIN_BATCH))
    return item
