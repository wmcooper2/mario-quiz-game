#custom
from src.constants import *
from src.gameutil import item_clean_up

def bombomb_effect():
    mix_items()
    BOMBOMB_EFFECT = False      #reset flag
    item_clean_up()

def pow_button_effect():
    for player in PLAYERS:
        player.points -= 1
    POW_BUTTON_EFFECT = False   #reset flag
    item_clean_up()

def feather_effect(self):
    """Player skips turn. Returns None."""
    FEATHER_EFFECT = True

def pow_button_effect(self):
    """Pow Button takes one point away from everyone. Returns None"""
    POW_BUTTON_EFFECT = True 

def spiny_beetle_effect(self):
    """Sentence translation (English to Japanese). Returns None"""
    SHOW_BLACK_BOX = True
    self.problem.random_target_sentence()
    problems.Problem.random_target_sentence()

#    def green_mushroom_effect(self):
#        """Presents a pronunciation problem. Returns None"""
#        SHOW_BLACK_BOX = True

#    def red_mushroom_effect(self):
#        """Presents a random English word. Returns None"""
#        SHOW_BLACK_BOX = True

#    def yoshi_coin_effect(self):
#        """Presents a qa 100 question. Returns None"""
#        SHOW_BLACK_BOX = True

#    def question_block_effect(self):
#        """Choose random effect. Returns None."""
#        print("question block effect")

#    def star_effect(self):
#        """Allows player to avoid negative affects. Returns None."""
#        print("star effect")
